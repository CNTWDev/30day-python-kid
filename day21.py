"""
Day 21: 猜数字小游戏

课程定位：
  - 综合运用循环、条件、随机数，制作一个简单的猜数字游戏，提升综合能力。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. while 循环结合条件控制游戏流程。
# 2. 随机数作为秘密数字。
# 3. 每轮提示玩家猜测结果。
# 4. 统计尝试次数并给出反馈。
# 5. 当输入无效时给出提醒并跳过。
# 6. 使用布尔变量控制游戏继续。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 展示游戏目标：猜中 1~20 的数字。
# 2. 分解游戏步骤：生成数字、循环猜测、比较大小。
# 3. 现场演示游戏玩法。
# 4. 学生分组实现自己的版本。
# 5. 分享增加的创意提示。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

import random

secret = random.randint(1, 20)
attempts = 0
guessed = False

while not guessed:
    guess_text = input("猜一个 1~20 的数字：")
    if not guess_text.isdigit():
        print("请输入数字哦！")
        continue
    guess = int(guess_text)
    attempts += 1
    if guess == secret:
        print("恭喜猜对啦！用了", attempts, "次。")
        guessed = True
    elif guess < secret:
        print("有点小了，再试试！")
    else:
        print("有点大了，继续加油！")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把范围改成 1~10，测试游戏难度。
# 练习 2：添加提示：当猜测过多次时鼓励玩家。
# 练习 3：记录每次猜测的数字，结束时打印全部尝试。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 综合运用所学语法完成小游戏。
  # - 练习输入验证和循环控制。
# 作业要求：
  # 1. 编写函数模拟猜数字过程，参数为待猜数字列表（可用于测试）。
  # 2. 按顺序使用列表中的数字作为猜测，直到猜中或耗尽数字。
  # 3. 输出每次猜测结果与最终情况。
  # 4. 额外挑战：记录猜中所用次数，未猜中时给出鼓励。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(secret: int, guesses: list[int]) -> None:
    """模拟猜数字过程并输出反馈。"""
    if not isinstance(secret, int):
        raise TypeError("secret 需要是整数。")
    if secret < 1 or secret > 20:
        raise ValueError("secret 需要在 1 到 20 之间。")
    if not isinstance(guesses, list):
        raise TypeError("guesses 需要是列表。")
    attempts = 0
    for guess in guesses:
        if not isinstance(guess, int):
            raise TypeError("猜测需要是整数。")
        attempts += 1
        if guess == secret:
            print(f"第 {attempts} 次猜中！数字就是 {secret}。")
            return
        if guess < secret:
            print(f"第 {attempts} 次猜 {guess}，有点小。")
        else:
            print(f"第 {attempts} 次猜 {guess}，有点大。")
    print("用完所有数字也没有猜中，下次继续努力！")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(secret=7, guesses=[3, 9, 7])
