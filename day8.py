"""
Day 8: for 循环与 range

课程定位：
  - 介绍 for 循环和 range，学习遍历固定次数与数字序列的技巧。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. for 循环语法：for 变量 in 序列。
# 2. range(n) 生成 0 到 n-1 的数字。
# 3. range(start, end, step) 的三参数形式。
# 4. for 循环与 while 的区别。
# 5. 在循环中使用累加器统计总数。
# 6. 结合字符串输出更整齐的结果。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾 while 循环，比较差异。
# 2. 演示 for + range 打印 1~5。
# 3. 解释步长 step 的作用。
# 4. 在循环中计算总和。
# 5. 让学生自己设计循环输出模式。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：从 1 数到 5
for number in range(1, 6):
    print("现在的数字是", number)

# 示例 2：步长为 2
print("偶数：")
for even in range(0, 11, 2):
    print(even)

# 示例 3：计算总和
total = 0
for num in range(1, 6):
    total += num
print("1 到 5 的总和是", total)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 range(1, 6) 改成 range(2, 7)，看看输出。
# 练习 2：使用步长 3 生成序列。
# 练习 3：在循环中打印乘法表的一行，如 3 * 1 到 3 * 5。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟练掌握 for 循环语法。
  # - 练习使用 range 生成数字序列。
# 作业要求：
  # 1. 用 for 循环打印 1 到 10 中的偶数。
  # 2. 计算这些偶数的总和并输出。
  # 3. 额外挑战：打印一个简单的星号阶梯，每行星号数量递增。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(start: int = 1, end: int = 10) -> None:
    """打印给定范围内的偶数及其总和，并绘制星号阶梯。"""
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start 和 end 需要是整数。")
    if start > end:
        raise ValueError("start 不能大于 end。")
    even_numbers = []
    for number in range(start, end + 1):
        if number % 2 == 0:
            even_numbers.append(number)
    print("偶数列表:", even_numbers)
    print("偶数总和:", sum(even_numbers))
    print("星号阶梯：")
    for index in range(1, len(even_numbers) + 1):
        print("*" * index)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(1, 10)
