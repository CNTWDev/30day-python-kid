"""
Day 13: 循环遍历列表

课程定位：
  - 结合 for 循环遍历列表，练习累计求和和条件筛选，深化数据处理能力。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. for item in list 遍历列表元素。
# 2. 使用 enumerate 获取索引和元素。
# 3. 在循环中统计总和或计数。
# 4. 条件判断筛选列表元素。
# 5. 构建新的列表存储符合条件的结果。
# 6. 保持变量命名清晰易懂。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾列表和 for 循环基础。
# 2. 演示遍历朋友姓名列表并打印。
# 3. 结合 enumerate 输出序号。
# 4. 演示累加数字列表求和。
# 5. 练习筛选大于某个数的元素。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：遍历姓名列表
classmates = ["小美", "小东", "小南"]
for index, name in enumerate(classmates, start=1):
    print(f"第 {index} 位同学是 {name}")

# 示例 2：求总和与筛选
scores = [95, 82, 76, 88]
total = 0
high_scores = []
for score in scores:
    total += score
    if score >= 90:
        high_scores.append(score)
average = total / len(scores)
print("总分:", total)
print("平均分:", average)
print("高分列表:", high_scores)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 classmates 列表改成自己的朋友，并输出问候语。
# 练习 2：新建一个数字列表，计算它们的合计。
# 练习 3：筛选出列表中大于 50 的数字。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 巩固遍历列表的技巧。
  # - 练习条件筛选与累加。"
# 作业要求：
  # 1. 创建包含多个书本页数的列表。
  # 2. 计算总页数和平均页数。
  # 3. 筛选出页数超过 50 页的书。
  # 4. 额外挑战：把筛选结果打印成带序号的列表。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(page_counts: list[int]) -> None:
    """统计书本页数，计算平均值并筛选长书。"""
    if not isinstance(page_counts, list):
        raise TypeError("page_counts 需要是列表。")
    if not page_counts:
        raise ValueError("列表不能为空。")
    for count in page_counts:
        if not isinstance(count, int):
            raise TypeError("页数需要是整数。")
        if count <= 0:
            raise ValueError("页数需要是正整数。")
    total = sum(page_counts)
    average = total / len(page_counts)
    long_books = [count for count in page_counts if count > 50]
    print("总页数:", total)
    print("平均页数:", average)
    if long_books:
        print("页数超过 50 页的书有：")
        for index, count in enumerate(long_books, start=1):
            print(f"{index}. {count} 页")
    else:
        print("没有超过 50 页的书。")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution([30, 55, 48, 90])
