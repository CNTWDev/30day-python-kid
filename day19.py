"""
Day 19: 函数参数进阶：默认值与关键字

课程定位：
  - 在函数基础上加入默认参数和关键字参数，让函数更灵活易用。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 默认参数：def func(name="值")。
# 2. 关键字参数调用：func(name=value)。
# 3. 参数顺序：先位置参数再关键字参数。
# 4. 避免使用可变对象作为默认值（简单说明）。
# 5. 在函数中添加输入验证，保护参数。
# 6. return 多个值时返回元组。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 复习函数定义与调用。
# 2. 演示默认参数的好处。
# 3. 展示关键字参数提高可读性。
# 4. 设计函数返回多个信息。
# 5. 练习编写带默认值的问候函数。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例：默认参数与关键字
def greet(name: str, time_of_day: str = "早上") -> None:
    print(f"{time_of_day}好, {name}！")

greet("小青")
greet("小夏", time_of_day="下午")

# 返回多个值
def divide_and_remainder(total: int, group: int) -> tuple[int, int]:
    return total // group, total % group

quotient, remainder = divide_and_remainder(10, 3)
print("商:", quotient, "余数:", remainder)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 greet 改成在句末加入感叹号。
# 练习 2：编写函数，默认问候语为“你好”，也允许自定义。
# 练习 3：创建函数返回两个数字的平均值和差值。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟练使用默认参数和关键字参数。
  # - 练习函数返回多个结果。
# 作业要求：
  # 1. 定义函数，计算每日计划完成情况，参数包含任务总数和已完成数量，未提供时默认总数为 5。
  # 2. 返回完成率（0~1）和未完成数量。
  # 3. 输出提示语，鼓励继续完成任务。
  # 4. 输入验证：任务数与完成数必须为非负整数，且完成数不超过总数。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(total_tasks: int = 5, finished_tasks: int = 0) -> tuple[float, int]:
    """计算完成率并输出鼓励信息。"""
    for value, name in ((total_tasks, "total_tasks"), (finished_tasks, "finished_tasks")):
        if not isinstance(value, int):
            raise TypeError(f"{name} 需要是整数。")
        if value < 0:
            raise ValueError(f"{name} 不能为负数。")
    if finished_tasks > total_tasks:
        raise ValueError("完成任务数量不能超过总任务数。")
    remaining = total_tasks - finished_tasks
    rate = finished_tasks / total_tasks if total_tasks else 0.0
    print(f"完成 {finished_tasks} / {total_tasks} 项任务，剩余 {remaining} 项。")
    if remaining == 0:
        print("全部完成！棒极了！")
    else:
        print("继续加油，马上就完成啦！")
    return rate, remaining

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(total_tasks=6, finished_tasks=4)
