"""
Day 3: 学会和计算机对话：input

课程定位：
  - 教学生从键盘获取信息，理解 input 返回字符串，并学会基本类型转换。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. input 函数：提示用户输入内容。
# 2. input 返回字符串，需要用 int() 转成整数。
# 3. 变量保存用户的回答，让程序更灵活。
# 4. strip 简单说明：去掉前后的空格（演示用）。
# 5. 基本输入验证：判断字符串是否为数字。
# 6. 友好的提示语，指导用户正确输入。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 展示电脑如何询问名字并打招呼。
# 2. 解释 input 返回的是字符串。
# 3. 演示把输入的数字转换成整数进行加法。
# 4. 讨论如果输入不是数字会发生什么。
# 5. 让学生尝试不同的输入内容。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：和计算机打招呼
name = input("你好呀，你叫什么名字? ")
name = name.strip()
print("很高兴认识你,", name, "!")

# 示例 2：把输入转换成数字
age_text = input("你今年几岁啦? ")
if age_text.isdigit():
    age = int(age_text)
    print("明年你就", age + 1, "岁啦！")
else:
    print("请输入正确的数字哦！")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：修改提示语句，让它更有趣，比如询问最喜欢的颜色。
# 练习 2：尝试对输入的数字进行乘法或减法。
# 练习 3：加入一个新的输入问题，例如最喜欢的动物。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟悉 input 的用法。
  # - 练习字符串拼接与数字转换。
# 作业要求：
  # 1. 询问用户的名字，并打印欢迎语。
  # 2. 询问喜欢的数字，转换成整数后计算它乘以 2 的结果。
  # 3. 输出一句总结的话，包含名字和计算后的数字。
  # 4. 额外挑战：如果输入不是数字，要给出提醒。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(get_name: str, favorite_number_text: str) -> None:
    """模拟 input 结果，输出欢迎语并计算数字的两倍。"""
    if not isinstance(get_name, str):
        raise TypeError("名字需要是字符串。")
    if not isinstance(favorite_number_text, str):
        raise TypeError("数字输入需要是字符串。")
    name = get_name.strip()
    number_text = favorite_number_text.strip()
    print("欢迎你,", name, "!")
    if number_text.isdigit():
        number = int(number_text)
        print("你喜欢的数字乘以 2 是", number * 2)
        print(name, "今天学会了让计算机做数学！")
    else:
        print("提醒：需要输入数字才能计算哦！")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(get_name='小芳', favorite_number_text='6')
