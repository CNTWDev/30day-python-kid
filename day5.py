"""
Day 5: 初识 if 判断语句

课程定位：
  - 结合布尔值学习 if 语句，根据条件决定是否执行代码。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. if 语句结构：if 条件: -> 缩进代码块。
# 2. 缩进的重要性：表示属于 if 内部的指令。
# 3. 条件为 True 才会执行 if 内的代码。
# 4. 使用 else 处理条件为 False 的情况。
# 5. 使用 input + if 做简单互动。
# 6. 保持代码整洁，缩进一致。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾比较运算和布尔值。
# 2. 展示 if 的语法结构。
# 3. 演示 if 判断天气是否带伞。
# 4. 增加 else 分支，处理不同情况。
# 5. 让学生尝试修改条件，编写新的判断。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：简单判断
raining = True
if raining:
    print("下雨了，记得带伞！")

# 示例 2：if + else
homework_done = False
if homework_done:
    print("可以去玩啦！")
else:
    print("先完成作业再玩哦！")

# 示例 3：结合 input
answer = input("你喜欢冰淇淋吗? (yes/no) ")
if answer.strip().lower() == "yes":
    print("我也喜欢冰淇淋！")
else:
    print("那我们改天聊聊别的美食！")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 homework_done 改成 True，看看输出什么。
# 练习 2：新增一个变量 favorite_color，如果是 'blue' 就打印特别信息。
# 练习 3：使用 input 判断用户是否喜欢运动，并给出回应。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟练使用 if/else 语句。
  # - 练习根据不同输入输出不同结果。
# 作业要求：
  # 1. 询问今天是否完成阅读任务 (yes/no)。
  # 2. 如果完成，输出鼓励语；否则提醒继续努力。
  # 3. 额外挑战：判断回答是否既不是 yes 也不是 no，给出提示。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(response: str) -> None:
    """根据响应输出不同的提示信息。"""
    if not isinstance(response, str):
        raise TypeError("response 需要是字符串。")
    reply = response.strip().lower()
    if reply == "yes":
        print("太棒了，坚持阅读让你更聪明！")
    elif reply == "no":
        print("加油！读完今天的小故事再休息。")
    else:
        print("请输入 yes 或 no，让我知道你的答案。")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(response='yes')
