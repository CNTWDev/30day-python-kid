"""
Day 29: 期末项目筹备：文本冒险设计

课程定位：
  - 规划期末项目，设计简单文本冒险游戏的结构，强调数据驱动与函数协作。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 确定游戏场景、角色和选择分支。
# 2. 使用字典或列表存储场景信息。
# 3. 编写函数处理玩家选择。
# 4. 输入验证确保选择合法。
# 5. 使用循环控制游戏流程。
# 6. 记录玩家得分或物品状态。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 介绍文本冒险游戏的基本元素。
# 2. 展示场景数据结构设计方法。
# 3. 编写函数显示场景和选项。
# 4. 演示根据玩家选择跳转场景。
# 5. 小组讨论：添加奖励或结局。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

scenes = {
    "start": {
        "description": "你站在神秘森林的入口。",
        "options": {"A": "left_path", "B": "right_path"}
    },
    "left_path": {
        "description": "你遇到了一只友善的小鹿。",
        "options": {}
    },
    "right_path": {
        "description": "一条小河挡住了去路。",
        "options": {}
    }
}

def show_scene(scene_id: str) -> None:
    scene = scenes.get(scene_id)
    if not scene:
        print("未知场景。")
        return
    print(scene["description"])
    for key, next_scene in scene["options"].items():
        print(f"选择 {key} -> 前往 {next_scene}")

show_scene("start")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：为 left_path 和 right_path 添加新的描述或选项。
# 练习 2：设计一个新的场景并加入 scenes 字典。
# 练习 3：考虑如何记录玩家收集的物品。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 准备文本冒险项目的数据结构。
  # - 规划函数之间的合作方式。
# 作业要求：
  # 1. 定义至少三个场景，每个场景包含描述和选项。
  # 2. 编写函数展示场景并返回玩家选择。
  # 3. 编写控制函数，根据选择跳转下一个场景。
  # 4. 额外挑战：加入简单的分数或物品系统。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(scenes: dict[str, dict[str, object]], start_scene: str = "start") -> None:
    """运行简单的文本冒险流程，直到场景没有更多选项。"""
    if not isinstance(scenes, dict):
        raise TypeError("scenes 需要是字典。")
    if start_scene not in scenes:
        raise ValueError("起始场景不存在。")
    current = start_scene
    score = 0
    while True:
        scene = scenes.get(current)
        if not scene:
            print("遇到未知场景，游戏结束。")
            break
        description = scene.get("description")
        options = scene.get("options", {})
        reward = scene.get("reward", 0)
        if not isinstance(description, str):
            raise TypeError("场景描述需要是字符串。")
        if not isinstance(options, dict):
            raise TypeError("选项需要是字典。")
        score += reward if isinstance(reward, int) else 0
        print("场景:", description)
        if not options:
            print("没有更多选择，游戏到此结束。")
            break
        choice_key = next(iter(options))
        next_scene = options[choice_key]
        if not isinstance(next_scene, str):
            raise TypeError("场景名称需要是字符串。")
        print(f"自动选择 {choice_key} -> {next_scene}")
        current = next_scene
    print("最终得分:", score)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    adventure_scenes = {
        'start': {'description': '你看到两条路。', 'options': {'A': 'river'}, 'reward': 1},
        'river': {'description': '你找到一朵神秘之花。', 'options': {}, 'reward': 3},
    }
    homework_solution(adventure_scenes)
