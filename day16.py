"""
Day 16: 字典开启信息库

课程定位：
  - 学习字典存储键值对，掌握增删改查，为管理结构化数据打基础。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 字典 (dict)：使用键 (key) 找到值 (value)。
# 2. 使用 {} 定义字典，键值对用冒号分隔。
# 3. 访问方式：dict[key] 或 get(key)。
# 4. 添加/修改：直接赋值给新键或旧键。
# 5. 删除键：del 或 pop。
# 6. keys()/values()/items() 遍历内容。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 讲述需要快速查找信息的场景。
# 2. 演示创建学生信息字典。
# 3. 展示添加电话或地址信息。
# 4. 遍历 items 打印所有键值对。
# 5. 小组任务：设计自己的字典。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：创建与访问
student = {
    "name": "小麦",
    "age": 8,
    "grade": 2
}
print("学生的名字:", student["name"])

# 示例 2：添加与遍历
student["favorite_subject"] = "科学"
student["age"] = 9  # 更新年龄
for key, value in student.items():
    print(f"{key} -> {value}")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：创建一个字典保存自己喜欢的书的信息。
# 练习 2：修改字典中的一项，然后打印全部内容。
# 练习 3：尝试使用 get 方法获取不存在的键，观察返回值。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟悉字典的基本操作。",
  # - 练习增删改查键值对。
# 作业要求：
  # 1. 创建一个包含姓名、年龄、最喜欢运动的字典。
  # 2. 添加一个键“dream”，记录梦想。
  # 3. 修改年龄加 1。
  # 4. 删除运动信息。
  # 5. 额外挑战：循环打印剩余键值对。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(profile: dict[str, object]) -> None:
    """对个人信息字典进行增删改查并打印结果。"""
    if not isinstance(profile, dict):
        raise TypeError("profile 需要是字典。")
    required_keys = {"name", "age", "favorite_sport"}
    if not required_keys.issubset(profile.keys()):
        raise ValueError("字典需要包含 name、age、favorite_sport 三个键。")
    if not isinstance(profile["name"], str) or not isinstance(profile["favorite_sport"], str):
        raise TypeError("name 和 favorite_sport 需要是字符串。")
    if not isinstance(profile["age"], int):
        raise TypeError("age 需要是整数。")
    data = profile.copy()
    data["dream"] = "成为小小科学家"
    data["age"] += 1
    data.pop("favorite_sport", None)
    print("更新后的个人信息：")
    for key, value in data.items():
        print(f"- {key}: {value}")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution({'name': '小麦', 'age': 8, 'favorite_sport': '跳绳'})
