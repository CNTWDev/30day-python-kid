"""
Day 17: 组合数据：列表里的字典

课程定位：
  - 学习将字典放入列表，管理多条信息，理解嵌套数据的结构化思维。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 嵌套结构：列表中包含多个字典。
# 2. 通过 for 循环遍历每个字典。
# 3. 访问字典的键获取具体信息。
# 4. 使用 append 添加新记录。
# 5. 复制数据时使用 copy 深浅复制概念（简单说明）。
# 6. 保持数据结构清晰，便于阅读。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾字典存储一条信息的方式。
# 2. 演示把多个学生字典放入列表。
# 3. 遍历列表打印每位学生信息。
# 4. 通过 append 添加新学生。
# 5. 小组活动：设计自己的班级名册。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例：学生信息列表
students = [
    {"name": "小晨", "age": 8, "hobby": "画画"},
    {"name": "小诺", "age": 7, "hobby": "踢球"},
]
for student in students:
    print(f"{student['name']} 喜欢 {student['hobby']}")

new_student = {"name": "小丽", "age": 8, "hobby": "跳舞"}
students.append(new_student)
print("更新后的学生列表:", students)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：修改其中一个学生的爱好并打印。
# 练习 2：加入一位新学生，包含名字和喜欢的颜色。
# 练习 3：遍历列表时输出‘你好，名字！’的问候。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 理解嵌套数据结构。
  # - 练习遍历列表并访问字典键。
# 作业要求：
  # 1. 创建一个包含三本书信息（书名、作者、页数）的列表。
  # 2. 遍历打印每本书的介绍。
  # 3. 额外挑战：统计总页数。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(books: list[dict[str, object]]) -> None:
    """输出书籍信息并统计总页数。"""
    if not isinstance(books, list):
        raise TypeError("books 需要是列表。")
    if not books:
        raise ValueError("至少提供一本书的信息。")
    total_pages = 0
    for index, book in enumerate(books, start=1):
        if not isinstance(book, dict):
            raise TypeError("每本书需要使用字典表示。")
        required = {"title", "author", "pages"}
        if not required.issubset(book.keys()):
            raise ValueError("书籍字典需要包含 title、author、pages。")
        title = book["title"]
        author = book["author"]
        pages = book["pages"]
        if not isinstance(title, str) or not isinstance(author, str):
            raise TypeError("title 和 author 需要是字符串。")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("pages 需要是正整数。")
        total_pages += pages
        print(f"{index}. 《{title}》 作者：{author}，共 {pages} 页。")
    print("总页数:", total_pages)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution([
    {"title": "森林奇遇", "author": "王老师", "pages": 60},
    {"title": "海洋探险", "author": "李老师", "pages": 48},
    {"title": "天空之城", "author": "赵老师", "pages": 72},
])
