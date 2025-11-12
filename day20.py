"""
Day 20: 善用模块：import 初体验

课程定位：
  - 介绍标准库模块的概念，学习 import 使用 math、random 等工具函数。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 模块 (module)：包含一组函数与常量。
# 2. import module 与 from module import func 的差别。
# 3. 使用 math.sqrt 等函数进行计算。
# 4. random.randint 生成随机整数。
# 5. 命名空间：模块名作为前缀。
# 6. 合理引用模块，避免重复造轮子。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 讨论为什么需要模块（更多工具）。
# 2. 演示 math 模块的常用函数。
# 3. 展示 random 生成随机数。
# 4. 设计掷骰子的小游戏。
# 5. 小组分享可以组合模块做的事。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

import math
import random

# 示例 1：使用 math
number = 16
print("16 的平方根是", math.sqrt(number))
print("圆周率 π 约等于", math.pi)

# 示例 2：random 生成随机数
dice = random.randint(1, 6)
print("掷骰子结果:", dice)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：使用 math.pow 计算 2 的 3 次方。
# 练习 2：生成 1~10 的随机整数，重复三次。
# 练习 3：思考还想探索哪些模块，并写在注释里。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟悉 import 语法与模块使用。
  # - 结合模块解决小问题。
# 作业要求：
  # 1. 使用 random 模块生成 1~100 的随机数。
  # 2. 使用 math.sqrt 计算该随机数的平方根（保留两位小数）。
  # 3. 输出结果并提示学生再次尝试。
  # 4. 额外挑战：统计重复运行 5 次的平均随机值。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

import math
import random


def homework_solution(rounds: int = 1) -> None:
    """多次生成随机数并输出平方根及平均值。"""
    if not isinstance(rounds, int):
        raise TypeError("rounds 需要是整数。")
    if rounds <= 0:
        raise ValueError("rounds 需要是正整数。")
    results: list[int] = []
    for _ in range(rounds):
        number = random.randint(1, 100)
        results.append(number)
        root = round(math.sqrt(number), 2)
        print(f"随机数 {number} 的平方根约等于 {root}")
    if rounds > 1:
        average = sum(results) / rounds
        print(f"这些随机数的平均值约为 {average:.2f}")
    print("欢迎再次运行，看看会得到哪些数字！")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(rounds=5)
