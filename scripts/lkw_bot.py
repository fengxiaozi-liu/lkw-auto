#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
洛克王国自动脚本
功能：自动完成日常任务、领取福利等
"""

import pyautogui
import time
import random
from config.game_config import BUTTONS, TASKS, CONFIG

# pyautogui 安全设置
pyautogui.FAILSAFE = True  # 移动鼠标到角落自动停止
pyautogui.PAUSE = 0.5     # 每次点击后暂停

class LKWBot:
    def __init__(self):
        self.running = False
        
    def click(self, button_name, delay=None):
        """点击按钮"""
        if button_name not in BUTTONS:
            print(f"❌ 未知按钮: {button_name}")
            return False
            
        x, y = BUTTONS[button_name]
        # 添加随机偏移，防止被检测
        offset_x = random.randint(-5, 5)
        offset_y = random.randint(-5, 5)
        
        pyautogui.click(x + offset_x, y + offset_y)
        print(f"✅ 点击: {button_name} ({x}, {y})")
        
        # 等待
        wait_time = delay or random.uniform(*CONFIG["click_interval"])
        time.sleep(wait_time)
        return True
    
    def wait(self, seconds):
        """等待"""
        print(f"⏳ 等待 {seconds} 秒...")
        time.sleep(seconds)
    
    def screenshot(self, name="screenshot"):
        """截图"""
        filename = f"./screenshots/{name}_{int(time.time())}.png"
        pyautogui.screenshot(filename)
        print(f"📸 截图: {filename}")
        return filename
    
    def run_task(self, task_name):
        """执行任务"""
        if task_name not in TASKS:
            print(f"❌ 未知任务: {task_name}")
            return False
            
        task = TASKS[task_name]
        print(f"\n🚀 开始任务: {task['name']}")
        
        for i, step in enumerate(task["steps"]):
            action = step["action"]
            
            if action == "click":
                self.click(step["target"])
            elif action == "wait":
                self.wait(step.get("seconds", 2))
            elif action == "screenshot":
                self.screenshot(step.get("name", f"step_{i}"))
            elif action == "find_and_click":
                # 图像识别点击（高级功能）
                self.find_and_click(step["target"])
                
        print(f"✅ 任务完成: {task['name']}")
        return True
    
    def find_and_click(self, image_path):
        """查找图片并点击（需要预先准备模板图）"""
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                center = pyautogui.center(location)
                pyautogui.click(center)
                print(f"✅ 找到并点击: {image_path}")
                return True
            else:
                print(f"❌ 未找到: {image_path}")
                return False
        except Exception as e:
            print(f"❌ 查找失败: {e}")
            return False
    
    def daily_routine(self):
        """每日 Routine"""
        print("\n" + "="*50)
        print("🎮 开始每日任务")
        print("="*50)
        
        # 1. 做任务
        self.run_task("daily")
        
        # 2. 领福利
        self.run_task("welfare")
        
        print("\n" + "="*50)
        print("✅ 每日任务完成！")
        print("="*50)

def main():
    print("""
╔══════════════════════════════════════╗
║   洛克王国自动脚本 v1.0           ║
║   - 自动完成日常任务               ║
║   - 一键领取福利                   ║
╚══════════════════════════════════════╝
    """)
    
    bot = LKWBot()
    
    # 等待用户准备
    print("10秒后开始，请切换到游戏界面...")
    time.sleep(10)
    
    # 运行每日任务
    bot.daily_routine()
    
    # 或者循环运行
    # while True:
    #     bot.daily_routine()
    #     time.sleep(3600)  # 每小时执行一次

if __name__ == "__main__":
    main()
