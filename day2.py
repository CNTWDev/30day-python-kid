"""
Day 2: 玩转数字和变量

课程定位：
  - 巩固 print 的使用，重点理解数字运算和变量命名，让学生能用变量存储信息。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 注释 (Comment)：用 # 开头的说明文字，帮助理解代码。
# 2. 变量命名规则：只能用字母、数字、下划线，不能以数字开头。
# 3. 整数 (int) 与加减乘除运算。
# 4. 赋值运算符 = ：把右侧的值放进左侧的变量。
# 5. 使用 print 输出多个内容时，用逗号分隔。
# 6. 变量更新：同一个变量可以被重新赋值。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 复习 Day 1，回顾 print 的作用。
# 2. 通过生活例子讲解“变量”像储物盒。
# 3. 演示如何创建变量、修改变量。
# 4. 一起做加法、减法的小游戏。
# 5. 课堂练习，让学生亲自修改数字并观察结果。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：变量的创建与打印
apples = 3
oranges = 2
print("苹果的数量:", apples)
print("橘子的数量:", oranges)
print("水果总数:", apples + oranges)

# 示例 2：变量重新赋值
apples = apples + 1  # 增加一个苹果
print("我又多了一个苹果，现在有", apples, "个！")

# 示例 3：把字符串和数字一起输出
days_of_study = 2
print("我们已经学习了", days_of_study, "天的 Python。")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 apples 的初始值改成 5，再运行观察输出。
# 练习 2：创建一个新变量 bananas 储存香蕉数量，并与苹果一起打印出来。
# 练习 3：计算 10 - 3 的结果，把答案存进变量 result，并用 print 展示。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 巩固变量和算术的使用。
  # - 练习在一条语句中输出多种信息。
# 作业要求：
  # 1. 创建两个变量，分别表示今天读的故事书数量和做的数学题数量。
  # 2. 使用 print 打印一句话，描述今天的学习成果。
  # 3. 计算今天共完成的学习任务总数并输出。
  # 4. 额外挑战：把总数乘以 2，想象明天完成双倍任务是什么样。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(stories: int, math_problems: int) -> None:
    """输出当天学习成果，并计算总任务量与双倍任务量。"""
    if not isinstance(stories, int) or not isinstance(math_problems, int):
        raise TypeError("stories 和 math_problems 需要是整数。")
    if stories < 0 or math_problems < 0:
        raise ValueError("学习数量不能为负数。")
    total = stories + math_problems
    print("我今天读了", stories, "本故事书。")
    print("我今天做了", math_problems, "道数学题。")
    print("今天一共完成", total, "项学习任务！")
    print("如果明天完成双倍任务，那就是", total * 2, "项！")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(stories=2, math_problems=5)
