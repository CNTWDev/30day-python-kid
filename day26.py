"""
Day 26: 故事生成小项目

课程定位：
  - 综合运用列表、随机模块与函数，制作一个简单故事生成器，激发创意。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 组合多个列表生成不同片段。
# 2. 使用 random.choice 从列表中随机选取元素。
# 3. 函数分层设计：准备数据、生成句子、输出故事。
# 4. 保证数据结构清晰易扩展。
# 5. 加入输入验证确保列表非空。
# 6. 通过参数控制故事长度或模式。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾 random 模块用法。
# 2. 设计故事的三个部分：主角、地点、事件。
# 3. 编写函数随机组合故事片段。
# 4. 扩展示例：生成多句故事。
# 5. 课堂分享最有趣的故事。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

import random

characters = ["小兔", "小鹿", "小马"]
places = ["森林", "湖边", "花园"]
events = ["发现宝藏", "帮助朋友", "学习编程"]

def create_story() -> str:
    hero = random.choice(characters)
    place = random.choice(places)
    event = random.choice(events)
    return f"今天，{hero} 在 {place} {event}！"

print(create_story())

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：增加新的角色和地点，再运行多次。
# 练习 2：修改函数，让它生成两句话的故事。
# 练习 3：尝试让用户输入角色名字，加入故事。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 通过小项目综合应用所学知识。
  # - 学会拆分功能到多个函数中。
# 作业要求：
  # 1. 编写故事生成器，传入角色、地点、事件列表。
  # 2. 检查列表非空后再随机取值。
  # 3. 支持生成多句故事。
  # 4. 额外挑战：允许传入主角名字列表，循环使用每个主角。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

import random


def homework_solution(characters: list[str], places: list[str], events: list[str], sentences: int = 1) -> list[str]:
    """生成指定句数的随机故事，返回故事列表。"""
    for name, collection in (("characters", characters), ("places", places), ("events", events)):
        if not isinstance(collection, list):
            raise TypeError(f"{name} 需要是列表。")
        if not collection:
            raise ValueError(f"{name} 列表不能为空。")
        for item in collection:
            if not isinstance(item, str):
                raise TypeError(f"{name} 中的元素需要是字符串。")
    if not isinstance(sentences, int) or sentences <= 0:
        raise ValueError("sentences 需要是正整数。")
    stories: list[str] = []
    for _ in range(sentences):
        hero = random.choice(characters)
        place = random.choice(places)
        event = random.choice(events)
        story = f"今天，{hero} 在 {place} {event}。"
        stories.append(story)
        print(story)
    return stories

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(['小猫', '小狗'], ['海边', '山顶'], ['找到宝藏', '结识朋友'], sentences=3)
