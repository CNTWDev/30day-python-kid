"""
Day 25: 列表推导与快速构建

课程定位：
  - 学习列表推导式，快速创建和转换列表，提升代码表达力。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 列表推导式语法：[表达式 for 元素 in 可迭代对象]。
# 2. 可加入条件过滤，如 if 条件。
# 3. 推导式适合表达简单转换。
# 4. 保持推导式简短易读。
# 5. 与传统 for 循环对比，理解优势。
# 6. 推导式也可用于集合和字典（简单提及）。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾传统 for 循环构建列表方式。
# 2. 展示推导式等价写法。
# 3. 演示加入过滤条件的推导式。
# 4. 练习将字符串长度存入新列表。
# 5. 课堂讨论：什么时候不用推导式。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：平方列表
numbers = [1, 2, 3, 4]
squares = [num * num for num in numbers]
print("平方列表:", squares)

# 示例 2：过滤偶数
even_squares = [num * num for num in numbers if num % 2 == 0]
print("偶数的平方:", even_squares)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：用推导式创建一个包含 1~10 的偶数列表。
# 练习 2：把一组单词转换为它们的长度。
# 练习 3：练习写出传统 for 循环与推导式的对比。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟练使用列表推导式。
  # - 将推导式与传统循环对照理解。
# 作业要求：
  # 1. 输入一个整数列表，返回其中大于 5 的数字的平方列表。
  # 2. 同时输出使用 for 循环得到的结果，验证一致性。
  # 3. 额外挑战：构建一个列表，包含原数字与平方组成的元组。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(numbers: list[int]) -> None:
    """比较推导式与传统循环的结果，并构建额外元组列表。"""
    if not isinstance(numbers, list):
        raise TypeError("numbers 需要是列表。")
    for num in numbers:
        if not isinstance(num, int):
            raise TypeError("列表元素需要是整数。")
    filtered_comprehension = [num * num for num in numbers if num > 5]
    filtered_loop: list[int] = []
    for num in numbers:
        if num > 5:
            filtered_loop.append(num * num)
    print("推导式结果:", filtered_comprehension)
    print("循环结果:", filtered_loop)
    if filtered_comprehension == filtered_loop:
        print("两种方法结果一致！")
    pairs = [(num, num * num) for num in numbers]
    print("数字与平方组成的元组列表:", pairs)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution([2, 5, 6, 9])
