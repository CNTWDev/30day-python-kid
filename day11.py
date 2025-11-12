"""
Day 11: 列表初体验

课程定位：
  - 认识列表存储多个元素，学习创建、访问以及修改，建立集合思维。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 列表 (list)：用方括号 [] 包围。
# 2. 通过索引访问列表元素，索引从 0 开始。
# 3. len() 获取列表长度。
# 4. 列表元素可修改。
# 5. append() 在末尾添加新元素。
# 6. 清晰列出列表内容，便于阅读。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 讨论为什么需要一次存储多个数据。
# 2. 演示创建喜爱水果的列表。
# 3. 展示如何访问第一个、最后一个元素。
# 4. 演示 append 添加新元素。
# 5. 引导学生动手修改列表。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：创建列表并访问
favorite_fruits = ["苹果", "香蕉", "草莓"]
print("我喜欢的第一个水果是", favorite_fruits[0])
print("共有", len(favorite_fruits), "种水果")

# 示例 2：修改与添加
favorite_fruits[1] = "芒果"
favorite_fruits.append("桃子")
print("更新后的列表:", favorite_fruits)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：创建一个包含三个玩具的列表，打印第二个玩具。
# 练习 2：把列表中的一个元素改成其他内容。
# 练习 3：使用 append 添加一个新玩具并输出。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 理解列表的基本操作。
  # - 练习访问和修改列表。
# 作业要求：
  # 1. 创建一个包含三门课程的列表。
  # 2. 输出第一门和最后一门课程名称。
  # 3. 添加一门新的兴趣课程。
  # 4. 额外挑战：打印列表长度并逐个打印课程。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(courses: list[str], new_course: str) -> None:
    """展示课程列表、添加课程并逐项打印。"""
    if not isinstance(courses, list):
        raise TypeError("courses 需要是列表。")
    for item in courses:
        if not isinstance(item, str):
            raise TypeError("课程名称需要是字符串。")
    if not isinstance(new_course, str):
        raise TypeError("new_course 需要是字符串。")
    course_list = courses.copy()
    if not course_list:
        raise ValueError("课程列表至少包含一门课程。")
    print("第一门课程:", course_list[0])
    print("最后一门课程:", course_list[-1])
    course_list.append(new_course)
    print("更新后的课程列表:", course_list)
    print("共有", len(course_list), "门课程，分别是：")
    for subject in course_list:
        print("-", subject)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(['语文', '数学', '美术'], '科学实验')
