"""
Day 23: 小算法：最值与排序

课程定位：
  - 介绍查找最小值、最大值以及排序函数，让学生感受算法思维。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. min()/max() 获取列表最小最大值。
# 2. sorted() 返回排序后的新列表。
# 3. list.sort() 原地排序，会修改原列表。
# 4. reverse=True 进行降序排列。
# 5. 在排序前复制列表，保护原数据。
# 6. 空列表处理：先检查长度。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 复习列表操作。
# 2. 演示 min、max 查找。
# 3. 展示 sorted 与 sort 区别。
# 4. 实际例子：成绩排序。
# 5. 练习给数字贴顺序名次。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

scores = [88, 92, 75, 90, 85]
print("最高分:", max(scores))
print("最低分:", min(scores))

sorted_scores = sorted(scores)
print("从低到高排序:", sorted_scores)
print("原列表保持不变:", scores)

scores_copy = scores.copy()
scores_copy.sort(reverse=True)
print("从高到低排序:", scores_copy)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 scores 改成自己的分数列表。
# 练习 2：尝试将 sorted 结果保存后，用于打印前三名。
# 练习 3：观察 sort 与 sorted 的区别，并写下发现。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 掌握常用最值与排序函数。
  # - 学会在排序前复制以保护原数据。
# 作业要求：
  # 1. 接收一个整数列表，输出最大值、最小值。
  # 2. 打印从小到大排序的列表。
  # 3. 打印从大到小排序的列表。
  # 4. 额外挑战：输出原列表，确认未被修改。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(numbers: list[int]) -> None:
    """展示列表的最值与不同排序结果。"""
    if not isinstance(numbers, list):
        raise TypeError("numbers 需要是列表。")
    if not numbers:
        raise ValueError("列表不能为空。")
    for value in numbers:
        if not isinstance(value, int):
            raise TypeError("列表元素需要是整数。")
    print("最大值:", max(numbers))
    print("最小值:", min(numbers))
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)
    print("从小到大:", ascending)
    print("从大到小:", descending)
    print("原列表保持不变:", numbers)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution([12, 5, 33, 21, 18])
