"""
Day 27: 调试小帮手：print 与 assert

课程定位：
  - 学习用 print 调试和 assert 断言验证假设，增强问题排查能力。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. print 调试：输出关键变量的值。
# 2. 断言 assert 条件：条件不满足时抛出 AssertionError。
# 3. 断言用于检查永远应该成立的事实。
# 4. 在函数开头使用断言验证参数。
# 5. 调试时及时移除或注释多余输出。
# 6. 编写简单的自测函数检查结果。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 展示一个带 bug 的例子。
# 2. 通过 print 输出中间值定位问题。
# 3. 介绍 assert 如何快速发现错误。
# 4. 让学生为之前写的函数添加断言。
# 5. 总结调试时保持耐心和有序记录。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

def average(numbers: list[int]) -> float:
    assert numbers, "numbers 列表不能为空"
    total = 0
    for num in numbers:
        total += num
        print("当前总和:", total)  # 调试输出
    return total / len(numbers)

print("平均值:", average([2, 4, 6]))

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：给 average 函数添加更多 assert，如检查元素是整数。
# 练习 2：尝试计算空列表平均数，观察断言信息。
# 练习 3：在调试完成后删除多余的 print。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 学会使用断言验证假设。
  # - 体验 print 帮助观察程序运行。
# 作业要求：
  # 1. 编写函数，计算列表最大值，使用 assert 检查输入。
  # 2. 在循环中使用 print 显示当前比较的值。
  # 3. 最终返回最大值，并在测试后可以注释掉 print。
  # 4. 额外挑战：提供一个可选参数控制是否打印调试信息。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(numbers: list[int], debug: bool = True) -> int:
    """返回列表最大值，可选打印调试信息。"""
    assert isinstance(numbers, list), "numbers 必须是列表"
    assert numbers, "numbers 列表不能为空"
    for value in numbers:
        assert isinstance(value, int), "列表元素必须是整数"
    current_max = numbers[0]
    for value in numbers[1:]:
        if debug:
            print(f"比较 {current_max} 和 {value}")
        if value > current_max:
            current_max = value
            if debug:
                print("更新最大值为", current_max)
    if debug:
        print("最终最大值:", current_max)
    return current_max

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution([3, 9, 1, 7], debug=False)
