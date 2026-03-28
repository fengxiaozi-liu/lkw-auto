# 洛克王国自动脚本 - 配置文件

## 游戏截图路径
IMAGE_PATH = "./images/"
MAIN_MENU = IMAGE_PATH + "main_menu.webp"
QUEST_PAGE = IMAGE_PATH + "quest_page.webp"

## 按钮位置配置 (基于 2400x1080 分辨率)
## 坐标格式: (x, y)

BUTTONS = {
    # 主界面按钮 (右侧菜单，从上到下)
    "events": (2000, 320),      # 精彩活动
    "welfare": (2050, 450),     # 福利
    "task": (2050, 580),         # 任务
    "bag": (2000, 710),         # 背包
    "pet": (1950, 840),         # 宠物
    
    # 任务界面按钮
    "one_key_collect": (2050, 950),   # 一键领取
    "one_key_complete": (1750, 950),   # 一键完成
    "quest_list": (600, 300),          # 任务一览
    
    # 通用按钮
    "back": (80, 80),                  # 返回 (左上角)
    "confirm": (1200, 700),             # 确认
    "start": (1200, 800),               # 开始
    
    # 底部功能
    "exp_pet": (500, 1000),           # 经验宠物
    "fold": (2200, 1000),             # 收起
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
    },
    "events": {
        "name": "精彩活动",
        "steps": [
            {"action": "click", "target": "events"},
            {"action": "wait", "seconds": 2},
            # 精彩活动页面需要截图确认具体按钮
            {"action": "click", "target": "back"},
        ]
    }
}

## 脚本配置
CONFIG = {
    "screenshot_interval": 1,        # 截图间隔(秒)
    "click_interval": (1, 3),      # 点击间隔范围(秒)
    "max_retries": 3,               # 最大重试次数
    "debug_mode": True,              # 调试模式
}
