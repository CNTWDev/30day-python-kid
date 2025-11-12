"""
Day 12: 列表操作再升级

课程定位：
  - 在列表基础上，学习 insert、pop、remove 等方法，并理解复制与清空。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. insert(index, value) 在指定位置插入元素。
# 2. pop() 删除并返回最后一个元素。
# 3. remove(value) 删除第一次出现的元素。
# 4. copy() 创建列表副本，避免修改原数据。
# 5. clear() 清空列表。
# 6. 在操作前检查列表是否为空。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 复习列表创建与 append。
# 2. 演示 insert 在中间插入新元素。
# 3. 展示 pop 取出元素的过程。
# 4. 探讨什么时候需要复制列表。
# 5. 小组练习：设计自己的任务列表。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：插入与删除
tasks = ["写作业", "练琴", "阅读"]
tasks.insert(1, "画画")
print("插入后的任务列表:", tasks)
finished = tasks.pop()  # 默认删除最后一个
print("完成任务:", finished)
print("剩余任务:", tasks)

# 示例 2：复制列表
tasks_copy = tasks.copy()
tasks.remove("写作业")
print("原列表修改后:", tasks)
print("复制列表保持原样:", tasks_copy)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：使用 insert 把一个新朋友加入名单的第二个位置。
# 练习 2：用 pop 删除列表最后一项，并打印被删除的内容。
# 练习 3：创建列表副本，比较修改前后的差异。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟练掌握常用列表方法。
  # - 理解复制与原地修改的区别。
# 作业要求：
  # 1. 创建一个待办任务列表，至少包含三项。
  # 2. 在列表开头插入“热身运动”。
  # 3. 删除最后一项任务并显示它。
  # 4. 创建副本并清空原列表，比较两者。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(todo_list: list[str]) -> None:
    """操作任务列表，展示插入、删除、复制与清空的效果。"""
    if not isinstance(todo_list, list):
        raise TypeError("todo_list 需要是列表。")
    for item in todo_list:
        if not isinstance(item, str):
            raise TypeError("任务名称需要是字符串。")
    if len(todo_list) < 3:
        raise ValueError("任务列表至少包含三项。")
    tasks = todo_list.copy()
    tasks.insert(0, "热身运动")
    print("添加热身后的任务列表:", tasks)
    removed_task = tasks.pop()
    print("删除的最后一项任务:", removed_task)
    snapshot = tasks.copy()
    tasks.clear()
    print("清空后的原列表:", tasks)
    print("副本中的任务仍然存在:", snapshot)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(['写作业', '整理书包', '阅读故事'])
