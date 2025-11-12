"""
Day 15: 不可变伙伴：元组

课程定位：
  - 介绍元组与列表的区别，强调不可变特性，并展示解包操作。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 元组 (tuple)：用圆括号创建，不可修改。
# 2. 访问方式与列表类似，通过索引。
# 3. 元组可以存储不同类型的数据。
# 4. 解包 (unpack)：一次取出多个值。
# 5. 为什么需要不可变数据：保证安全。
# 6. len() 同样适用于元组。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 比较列表和元组的不同。
# 2. 演示创建坐标元组。
# 3. 展示尝试修改元组会报错。
# 4. 讲解解包，同时赋值多个变量。
# 5. 设计活动：描述动物的信息。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：创建与访问
coordinates = (3, 5)
print("X 坐标:", coordinates[0])
print("Y 坐标:", coordinates[1])

# 示例 2：解包
pet = ("Lucky", "狗狗", 2)
name, species, age = pet
print(f"宠物 {name} 是一只 {species}，今年 {age} 岁。")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：创建一个包含三种文具的元组，打印第二项。
# 练习 2：尝试解包元组，把数据赋给三个变量。
# 练习 3：讨论为什么不应该修改元组。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 认识元组的特性与用途。
  # - 练习元组解包和访问。
# 作业要求：
  # 1. 创建一个包含城市名称、天气、温度的元组。
  # 2. 使用解包一次性获取三个值并打印描述。
  # 3. 额外挑战：把温度转换成字符串，组合成完整句子。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(city_weather: tuple[str, str, int | float]) -> None:
    """解包城市天气信息并输出描述。"""
    if not isinstance(city_weather, tuple):
        raise TypeError("city_weather 需要是元组。")
    if len(city_weather) != 3:
        raise ValueError("元组需要包含三个元素：城市、天气、温度。")
    city, condition, temperature = city_weather
    if not isinstance(city, str) or not isinstance(condition, str):
        raise TypeError("城市和天气描述需要是字符串。")
    if not isinstance(temperature, (int, float)):
        raise TypeError("温度需要是数字。")
    print(f"今天在{city}，天气是{condition}，气温{temperature}度。")
    print("保持好心情，享受美好的一天！")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(('上海', '晴朗', 26))
