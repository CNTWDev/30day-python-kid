"""
Day 28: 模块化设计：分解大问题

课程定位：
  - 学习把大任务拆成多个函数或模块，规划执行顺序，理解主程序与辅助函数的协作。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 模块化思维：一个函数负责一件事。
# 2. 主函数 main() 作为程序入口。
# 3. 辅助函数提供数据准备、计算、展示。
# 4. 函数之间通过参数和返回值通信。
# 5. 保持函数短小，便于测试。
# 6. 为每个函数写注释说明职责。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾之前的故事生成器结构。
# 2. 演示将任务拆分为准备、计算、展示三个函数。
# 3. 编写 main 函数协调执行顺序。
# 4. 课堂练习：拆分自己的小任务。
# 5. 讨论拆分带来的好处。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

def prepare_numbers() -> list[int]:
    return [2, 4, 6, 8]

def compute_average(values: list[int]) -> float:
    assert values, "values 不能为空"
    return sum(values) / len(values)

def show_result(average_value: float) -> None:
    print(f"这些数字的平均值是 {average_value}")

def main() -> None:
    numbers = prepare_numbers()
    avg = compute_average(numbers)
    show_result(avg)

if __name__ == "__main__":
    main()

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 prepare_numbers 改成从 input 获取数字。
# 练习 2：在 compute_average 中加入调试信息。
# 练习 3：创建新的 main 函数用于故事生成器。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 学会将任务拆分为多个函数。
  # - 设计清晰的主程序流程。
# 作业要求：
  # 1. 编写小型“每日计划”程序：准备任务列表、计算完成率、展示报告。
  # 2. 分别实现 prepare_tasks、calculate_progress、display_report、main 四个函数。
  # 3. 每个函数需要有输入验证。
  # 4. 额外挑战：在 main 中增加异常处理，保证程序稳定。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def prepare_tasks(raw_tasks: list[dict[str, object]]) -> list[dict[str, object]]:
    """验证任务数据并返回副本。"""
    if not isinstance(raw_tasks, list):
        raise TypeError("raw_tasks 需要是列表。")
    tasks: list[dict[str, object]] = []
    for task in raw_tasks:
        if not isinstance(task, dict):
            raise TypeError("每个任务需要是字典。")
        if "name" not in task or "done" not in task:
            raise ValueError("任务字典需要包含 name 和 done。")
        name = task["name"]
        done = task["done"]
        if not isinstance(name, str):
            raise TypeError("任务名称需要是字符串。")
        if not isinstance(done, bool):
            raise TypeError("done 需要是布尔值。")
        tasks.append({"name": name.strip(), "done": done})
    return tasks


def calculate_progress(tasks: list[dict[str, object]]) -> tuple[int, int, float]:
    """统计已完成与总任务，返回完成数量、总数和完成率。"""
    if not tasks:
        raise ValueError("任务列表不能为空。")
    completed = sum(1 for task in tasks if task["done"])
    total = len(tasks)
    rate = completed / total
    return completed, total, rate


def display_report(completed: int, total: int, rate: float) -> None:
    """打印任务进度报告。"""
    print(f"今日任务完成 {completed} / {total}")
    print(f"完成率：{rate * 100:.0f}%")
    if rate == 1.0:
        print("全部完成，棒极了！")
    elif rate >= 0.5:
        print("进度过半，继续保持！")
    else:
        print("加油，只要坚持就能完成！")


def homework_solution(raw_tasks: list[dict[str, object]]) -> None:
    """综合调用各函数，展示模块化设计流程。"""
    try:
        tasks = prepare_tasks(raw_tasks)
        completed, total, rate = calculate_progress(tasks)
        display_report(completed, total, rate)
    except (TypeError, ValueError) as error:
        print("数据有问题：", error)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    example_tasks = [
        {'name': '朗读课文', 'done': True},
        {'name': '数学练习', 'done': False},
        {'name': '钢琴练习', 'done': True},
    ]
    homework_solution(example_tasks)
