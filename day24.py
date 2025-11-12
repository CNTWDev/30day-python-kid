"""
Day 24: 集合 set 的神奇能力

课程定位：
  - 认识集合用于存储不重复的元素，学习集合运算帮助统计和筛选。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 集合 set 使用花括号 { } 创建。
# 2. 集合自动去重，没有顺序概念。
# 3. 添加元素使用 add，删除使用 remove/discard。
# 4. in 关键字判断元素是否存在。
# 5. 集合运算：并集 union、交集 intersection。
# 6. 在转换前，可将列表转为集合以去重。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 讨论重复元素的问题，引出集合概念。
# 2. 演示列表转换成集合后去重。
# 3. 展示添加和删除元素的方法。
# 4. 演示两个集合求交集和并集。
# 5. 课堂练习：统计同学喜欢的水果。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：集合去重
fruits = ["苹果", "香蕉", "苹果", "梨子"]
unique_fruits = set(fruits)
print("去重后的水果集合:", unique_fruits)

# 示例 2：集合运算
class_a = {"小明", "小红", "小刚"}
class_b = {"小红", "小丽", "小刚"}
print("两个班共同喜欢的同学:", class_a.intersection(class_b))
print("两个班所有的同学:", class_a.union(class_b))

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 fruits 列表换成自己的清单，观察集合去重效果。
# 练习 2：往集合中添加一个新元素，再删除一个元素。
# 练习 3：创建两个集合，求它们的差集。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 学会使用集合去重和检测元素存在。
  # - 了解基本集合运算。
# 作业要求：
  # 1. 输入两个兴趣列表，把它们转换成集合。
  # 2. 输出共同兴趣和所有兴趣集合。
  # 3. 判断某个兴趣是否在集合中。
  # 4. 额外挑战：计算共有兴趣的数量。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(interests_a: list[str], interests_b: list[str], check_item: str) -> None:
    """展示两个兴趣集合的并集、交集及成员检测。"""
    if not isinstance(interests_a, list) or not isinstance(interests_b, list):
        raise TypeError("两个兴趣列表都需要是 list。")
    for collection in (interests_a, interests_b):
        for item in collection:
            if not isinstance(item, str):
                raise TypeError("兴趣名称需要是字符串。")
    if not isinstance(check_item, str):
        raise TypeError("check_item 需要是字符串。")
    set_a = {item.strip() for item in interests_a if item.strip()}
    set_b = {item.strip() for item in interests_b if item.strip()}
    common = set_a.intersection(set_b)
    total = set_a.union(set_b)
    print("集合 A:", set_a)
    print("集合 B:", set_b)
    print("共同兴趣:", common)
    print("所有兴趣:", total)
    print(f"{check_item} 是否在共同兴趣中:", check_item in common)
    print("共同兴趣数量:", len(common))

# 供教师演示或学生验证使用
if __name__ == "__main__":
    example_a = ['绘画', '跳舞', '绘画']
    example_b = ['跳舞', '编程']
    homework_solution(example_a, example_b, '跳舞')
