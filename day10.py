"""
Day 10: 字符串小工坊：格式化与方法

课程定位：
  - 在理解字符串基础上，学习常见方法 upper、lower、title 以及 f-string 格式化，让输出更美观。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 字符串方法 upper/lower/title 改变大小写。
# 2. strip 去掉开头结尾空格。
# 3. f-string 使用 {变量} 嵌入信息。
# 4. 安全处理用户输入，避免多余空格。
# 5. 组合多种方法制作整洁的句子。
# 6. 善用注释说明格式化目的。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾字符串的基本操作。
# 2. 展示 upper/lower 效果。
# 3. 演示 f-string 的写法。
# 4. 实践活动：设计“欢迎牌”。
# 5. 分享每个人的格式化句子。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：字符串方法
hobby = "  playing Chess  "
clean_hobby = hobby.strip()
print("原始信息:", hobby)
print("大写:", clean_hobby.upper())
print("小写:", clean_hobby.lower())
print("标题格式:", clean_hobby.title())

# 示例 2：f-string 格式化
name = "小宇"
activity = "绘画"
message = f"欢迎 {name}! 今天我们要练习 {activity}!"
print(message)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 hobby 换成你喜欢的活动，观察不同格式。
# 练习 2：使用 f-string 输出一句鼓励话，比如“加油，小明！”
# 练习 3：创建一个句子，把名字和喜欢的动物组合在一起。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 掌握字符串方法与格式化写法。
  # - 输出整洁友好的句子。
# 作业要求：
  # 1. 输入姓名和最喜欢的运动。
  # 2. 去除多余空格，把运动名转换成标题格式。
  # 3. 使用 f-string 输出一句邀请一起运动的话。
  # 4. 额外挑战：再输出一句运动口号（全部大写）。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(name: str, sport: str) -> None:
    """格式化输出关于运动的邀请语和口号。"""
    if not isinstance(name, str) or not isinstance(sport, str):
        raise TypeError("name 和 sport 需要是字符串。")
    clean_name = name.strip()
    clean_sport = sport.strip()
    if not clean_name:
        raise ValueError("名字不能为空。")
    if not clean_sport:
        raise ValueError("运动名称不能为空。")
    sport_title = clean_sport.title()
    print(f"嗨 {clean_name}，我们一起练习 {sport_title} 吧！")
    print((f"{sport_title} 最棒！").upper())

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution('小宇', '  badminton ')
