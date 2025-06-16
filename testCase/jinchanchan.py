import re
import time
from datetime import datetime
import adbutils
from rich.console import Console
from rich.table import Table
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
import threading
from typing import Dict, List, Optional


class AndroidResourceMonitor:
    def __init__(self, device_serial: Optional[str] = None):
        """初始化ADB连接"""
        self.adb = adbutils.AdbClient(host="10.85.77.129", port=5555)
        self.device = self.adb.device()
        self._stop_event = threading.Event()

        # 监控配置
        self.config = {
            'cpu_warning': 90,
            'mem_warning': 85,
            'temp_warning': 45,
            'interval': 1
        }

    # -------------------- 核心监控方法 --------------------
    def get_cpu_usage(self) -> List[Dict]:
        """获取CPU使用率前10的进程"""
        result = self.device.shell("top -n 1 -o %CPU")
        cpu_data = []
        for line in result.splitlines()[5:15]:
            parts = re.split(r'\s+', line.strip())
            if len(parts) >= 9:
                cpu_data.append({
                    "pid": parts[0],
                    "user": parts[1],
                    "cpu%": float(parts[8]),
                    "name": parts[-1]
                })
        return cpu_data

    def get_memory_info(self) -> Dict:
        """获取内存使用情况"""
        result = self.device.shell("dumpsys meminfo")
        total = re.search(r"Total RAM:\s+(\d+)", result)
        free = re.search(r"Free RAM:\s+(\d+)", result)
        if total and free:
            total = int(total.group(1))
            free = int(free.group(1))
            return {
                "total_MB": total / 1024,
                "used_MB": (total - free) / 1024,
                "usage%": (total - free) / total * 100
            }
        return {}

    def get_network_stats(self, interval: float = 1) -> Dict:
        """获取网络流量统计"""

        def parse_net_dev():
            result = self.device.shell("cat /proc/net/dev")
            return {
                "wlan0": int(result.split("wlan0:")[1].split()[0]),
                "rmnet0": int(result.split("rmnet0:")[1].split()[8])
            }

        start = parse_net_dev()
        time.sleep(interval)
        end = parse_net_dev()
        return {
            "download_KBps": (end["wlan0"] - start["wlan0"]) / interval / 1024,
            "upload_KBps": (end["rmnet0"] - start["rmnet0"]) / interval / 1024
        }

    def get_battery_temp(self) -> float:
        """获取电池温度(摄氏度)"""
        temp = self.device.shell("dumpsys battery | grep temperature").split(":")[1].strip()
        return float(temp) / 10

    # -------------------- 监控模式 --------------------
    def console_monitor(self, duration: int = 60):
        """控制台实时监控"""
        console = Console()
        start_time = time.time()

        while not self._stop_event.is_set() and (time.time() - start_time < duration):
            cpu = self.get_cpu_usage()
            mem = self.get_memory_info()
            net = self.get_network_stats(self.config['interval'])

            table = Table(title=f"Android资源监控 [设备: {self.device.serial}]")
            table.add_column("指标", justify="right")
            table.add_column("值", justify="left")

            table.add_row("CPU使用率", f"{sum(p['cpu%'] for p in cpu):.1f}%")
            table.add_row("内存占用", f"{mem.get('used_MB', 0):.1f}MB/{mem.get('total_MB', 0):.1f}MB")
            table.add_row("网络流量", f"↑{net.get('upload_KBps', 0):.1f}KB/s ↓{net.get('download_KBps', 0):.1f}KB/s")
            table.add_row("电池温度", f"{self.get_battery_temp():.1f}°C")

            console.clear()
            console.print(table)
            self._check_alerts(cpu, mem)
            time.sleep(self.config['interval'])

    def plot_monitor(self, duration: int = 60):
        """Matplotlib动态图表监控"""
        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        timestamps = []
        cpu_data, mem_data, net_up, net_down = [], [], [], []

        def update(frame):
            if self._stop_event.is_set():
                plt.close()
                return

            cpu = sum(p['cpu%'] for p in self.get_cpu_usage())
            mem = self.get_memory_info()
            net = self.get_network_stats(self.config['interval'])

            timestamps.append(time.strftime("%H:%M:%S"))
            cpu_data.append(cpu)
            mem_data.append(mem.get('usage%', 0))
            net_up.append(net.get('upload_KBps', 0))
            net_down.append(net.get('download_KBps', 0))

            axs[0, 0].clear()
            axs[0, 0].plot(timestamps, cpu_data, 'r-')
            axs[0, 0].set_title('CPU使用率 (%)')

            axs[0, 1].clear()
            axs[0, 1].plot(timestamps, mem_data, 'b-')
            axs[0, 1].set_title('内存占用率 (%)')

            axs[1, 0].clear()
            axs[1, 0].plot(timestamps, net_up, 'g-', label='上传')
            axs[1, 0].plot(timestamps, net_down, 'y-', label='下载')
            axs[1, 0].set_title('网络流量 (KB/s)')
            axs[1, 0].legend()

            plt.tight_layout()

        ani = FuncAnimation(fig, update, interval=self.config['interval'] * 1000,
                            save_count=duration // self.config['interval'])
        plt.show()

    def log_to_csv(self, filename: str = 'metrics.csv', duration: int = 300):
        """记录监控数据到CSV"""
        data = []
        start = time.time()

        while not self._stop_event.is_set() and (time.time() - start < duration):
            entry = {
                "timestamp": datetime.now().isoformat(),
                "cpu_usage": sum(p['cpu%'] for p in self.get_cpu_usage()),
                **self.get_memory_info(),
                **self.get_network_stats(self.config['interval']),
                "temperature": self.get_battery_temp()
            }
            data.append(entry)
            time.sleep(self.config['interval'])

        pd.DataFrame(data).to_csv(filename, index=False)

    # -------------------- 辅助功能 --------------------
    def _check_alerts(self, cpu_data: List, mem_data: Dict):
        """检查阈值告警"""
        total_cpu = sum(p['cpu%'] for p in cpu_data)
        if total_cpu > self.config['cpu_warning']:
            print(f"[警告] CPU使用率过高: {total_cpu:.1f}%")

        if mem_data.get('usage%', 0) > self.config['mem_warning']:
            print(f"[警告] 内存占用过高: {mem_data['usage%']:.1f}%")

        temp = self.get_battery_temp()
        if temp > self.config['temp_warning']:
            print(f"[警告] 电池温度过高: {temp:.1f}°C")

    def stop(self):
        """停止监控"""
        self._stop_event.set()

    # -------------------- 主控方法 --------------------
    def run(self, mode: str = 'console', **kwargs):
        """
        启动监控
        :param mode: console/plot/log
        :param kwargs: 各模式专用参数
        """
        self._stop_event.clear()

        if mode == 'console':
            self.console_monitor(**kwargs)
        elif mode == 'plot':
            self.plot_monitor(**kwargs)
        elif mode == 'log':
            self.log_to_csv(**kwargs)
        else:
            raise ValueError("不支持的监控模式")


if __name__ == "__main__":
    # 使用示例
    monitor = AndroidResourceMonitor()

    try:
        # 启动控制台监控60秒
        monitor.run(mode='console', duration=1200)

        # 或者在另一个线程启动图表监控
        # threading.Thread(target=monitor.run, kwargs={'mode':'plot'}).start()

    except KeyboardInterrupt:
        monitor.stop()
        print("监控已停止")