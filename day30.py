"""
Day 30: 庆祝与提升：期末回顾与展望

课程定位：
  - 总结 30 天学习，完善文本冒险项目，规划未来扩展，鼓励持续探索。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 回顾所有核心概念：变量、条件、循环、函数、数据结构。
# 2. 针对项目进行代码审查，寻找改进点。
# 3. 编写简单测试确保功能正常。
# 4. 记录改进想法与待办事项。
# 5. 编写 README 或说明文档概述项目。
# 6. 庆祝成果，设置新学习目标。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 复习关键知识点并答疑。
# 2. 演示完善的文本冒险项目。
# 3. 一起编写简单测试用例。
# 4. 讨论未来可以添加的功能。
# 5. 写下感谢语和学习心得。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

def adventure_scene(scene_id: str) -> str:
    mapping = {
        "start": "冒险开始啦！",
        "river": "你来到河边，水声潺潺。",
        "cave": "黑暗的山洞需要勇气。",
    }
    return mapping.get(scene_id, "未知场景")

# 简单测试
assert adventure_scene("start") == "冒险开始啦！"
assert adventure_scene("forest") == "未知场景"
print("所有测试通过，冒险故事准备就绪！")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：为 adventure_scene 增加新的场景和测试。
# 练习 2：写下三条今天想要感谢的人或事。
# 练习 3：规划下一个要学习的 Python 技能。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 回顾本课程所有内容。
  # - 完成期末项目并留下扩展计划。
# 作业要求：
  # 1. 在文本冒险项目中加入至少两个新场景或功能。
  # 2. 编写测试函数验证关键逻辑。
  # 3. 撰写简短的项目说明和未来计划清单。
  # 4. 额外挑战：邀请家人一起试玩并记录反馈。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(project_notes: dict[str, object]) -> None:
    """整理项目成果、运行测试并输出未来计划。"""
    if not isinstance(project_notes, dict):
        raise TypeError("project_notes 需要是字典。")
    required = {"scenes", "tests", "plan"}
    if not required.issubset(project_notes.keys()):
        raise ValueError("需要提供 scenes、tests、plan 三个键。")
    scenes = project_notes["scenes"]
    tests = project_notes["tests"]
    plan = project_notes["plan"]
    if not isinstance(scenes, dict):
        raise TypeError("scenes 需要是字典。")
    if not isinstance(tests, list):
        raise TypeError("tests 需要是列表。")
    if not isinstance(plan, list):
        raise TypeError("plan 需要是列表。")
    print("=== 项目场景一览 ===")
    for name, info in scenes.items():
        print(f"场景 {name}: {info}")
    print("=== 运行测试 ===")
    for index, test_result in enumerate(tests, start=1):
        if not isinstance(test_result, bool):
            raise TypeError("测试结果需要是布尔值。")
        print(f"测试 {index}: {'通过' if test_result else '需要改进'}")
    print("=== 未来计划 ===")
    for todo in plan:
        if not isinstance(todo, str):
            raise TypeError("计划内容需要是字符串。")
        print("-", todo)
    print("感谢自己的坚持，未来继续加油！")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    notes_example = {
        'scenes': {'start': '新的起点', 'forest': '神秘的森林'},
        'tests': [True, True, False],
        'plan': ['加入音效', '绘制地图'],
    }
    homework_solution(notes_example)
