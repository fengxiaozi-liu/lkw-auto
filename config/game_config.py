# 洛克王国自动脚本 - 配置文件

## 游戏截图路径
IMAGE_PATH = "./images/"
MAIN_MENU = IMAGE_PATH + "main_menu.webp"
QUEST_PAGE = IMAGE_PATH + "quest_page.webp"

## 按钮位置配置 (基于 2400x1080 分辨率)
## 坐标格式: (x, y)

BUTTONS = {
    # 主界面按钮
    "task": (2200, 500),      # 任务按钮
    "welfare": (2250, 350),    # 福利按钮
    "背包": (2200, 650),       # 背包按钮
    "pet": (2100, 750),       # 宠物按钮
    "events": (1200, 650),     # 精彩活动
    
    # 任务界面按钮
    "one_key_collect": (2050, 950),   # 一键领取
    "one_key_complete": (1750, 950),   # 一键完成
    "quest_list": (600, 300),         # 任务一览
    
    # 通用按钮
    "back": (100, 100),               # 返回
    "confirm": (1200, 700),           # 确认
    "start": (1200, 800),            # 开始
}

## 任务配置
TASKS = {
    "daily": {
        "name": "每日任务",
        "steps": [
            {"action": "click", "target": "task"},
            {"action": "wait", "seconds": 2},
            {"action": "click", "target": "one_key_complete"},
            {"action": "wait", "seconds": 5},
            {"action": "click", "target": "one_key_collect"},
            {"action": "wait", "seconds": 2},
            {"action": "click", "target": "back"},
        ]
    },
    "welfare": {
        "name": "福利领取",
        "steps": [
            {"action": "click", "target": "welfare"},
            {"action": "wait", "seconds": 2},
            {"action": "click", "target": "one_key_collect"},
            {"action": "wait", "seconds": 2},
            {"action": "click", "target": "back"},
        ]
    }
}

## 脚本配置
CONFIG = {
    "screenshot_interval": 1,        # 截图间隔(秒)
    "click_interval": (1, 3),        # 点击间隔范围(秒)
    "max_retries": 3,                # 最大重试次数
    "debug_mode": True,               # 调试模式
}
