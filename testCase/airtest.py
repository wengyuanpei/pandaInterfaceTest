# -*- encoding=utf8 -*-


from airtest.core import *
from airtest.cli.parser import cli_setup
from airtest.core.api import auto_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/S1DEV005?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


# script content
print("start...")




# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
while True:

    touch(Template(r"tpl1685341804356.png", record_pos=(-0.38, -0.734), resolution=(640, 1136)))

    touch(Template(r"tpl1685341602781.png", record_pos=(0.306, -0.433), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341611069.png", record_pos=(0.323, -0.425), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341619966.png", record_pos=(-0.402, -0.731), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341625998.png", record_pos=(-0.183, 0.302), resolution=(640, 1136)))
    touch(Template(r"tpl1685341631727.png", record_pos=(0.353, 0.028), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341638103.png", record_pos=(-0.395, -0.739), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341646716.png", record_pos=(-0.161, -0.745), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341655318.png", record_pos=(-0.341, 0.463), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341662072.png", record_pos=(0.061, -0.534), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341669561.png", record_pos=(-0.278, -0.056), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341673710.png", record_pos=(-0.248, 0.342), resolution=(640, 1136)))
    sleep(60.0)
    touch(Template(r"tpl1685341688895.png", record_pos=(-0.38, -0.688), resolution=(640, 1136)))
    touch(Template(r"tpl1685341692815.png", record_pos=(-0.431, -0.713), resolution=(640, 1136)))
    sleep(1.0)
    touch(Template(r"tpl1685341702438.png", record_pos=(-0.412, -0.709), resolution=(640, 1136)))
    sleep(1.0)

    touch(Template(r"tpl1685341707512.png", record_pos=(-0.409, -0.723), resolution=(640, 1136)))
