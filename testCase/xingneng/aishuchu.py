import subprocess
import os


# 1. 使用 ADB 导出耗电数据
def export_battery_data():
    try:
        # 运行 ADB 命令获取电池耗电数据
        adb_command = "adb shell dumpsys batteryhistory"
        result = subprocess.run(adb_command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout)
            return result.stdout
        else:
            print(f"ADB 命令执行失败: {result.stderr}")
            return None
    except Exception as e:
        print(f"执行 ADB 命令时发生错误: {e}")
        return None

    # 2. 读取并解析耗电数据


def parse_battery_data(data):
    lines = data.strip().split('\n')
    # 这里简单示例，直接将每行数据作为一条记录
    records = []
    for line in lines:
        records.append(line)
    return records


# 3. 将解析后的数据转换为 HTML 格式
def convert_to_html(records):
    html_head = """ 
<!DOCTYPE html> 
<html lang="en"> 
<head> 
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>电池耗电数据</title> 
    <style> 
        table { 
            width: 100%; 
            border-collapse: collapse; 
        } 
        th, td { 
            border: 1px solid #ddd; 
            padding: 8px; 
            text-align: left; 
        } 
        th { 
            background-color: #f2f2f2; 
        } 
    </style> 
</head> 
<body> 
    <h1>电池耗电数据</h1> 
    <table> 
        <thead> 
            <tr> 
                <th>序号</th> 
                <th>数据记录</th> 
            </tr> 
        </thead> 
        <tbody> 
    """
    html_body = ""
    for i, record in enumerate(records, start=1):
        html_body += f""" 
            <tr> 
                <td>{i}</td> 
                <td>{record}</td> 
            </tr> 
        """
    html_tail = """ 
        </tbody> 
    </table> 
</body> 
</html> 
    """
    html_content = html_head + html_body + html_tail
    return html_content


# 4. 保存 HTML 文件
def save_html(html_content, filename="battery_data.html"):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML 文件已保存为 {filename}")
    except Exception as e:
        print(f"保存 HTML 文件时发生错误: {e}")

    # 主函数


def maind():
    # 导出耗电数据
    battery_data = export_battery_data()
    if battery_data:
        # 解析耗电数据
        records = parse_battery_data(battery_data)
        # 转换为 HTML 格式
        html_content = convert_to_html(records)
        # 保存 HTML 文件
        save_html(html_content)


if __name__ == '__main__':
    maind()