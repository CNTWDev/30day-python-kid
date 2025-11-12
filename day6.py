"""
Day 6: 更多条件：elif 和逻辑运算

课程定位：
  - 扩展 if 语句，加入 elif 和逻辑运算符 and/or，处理多种情况。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. elif 用于检查多个条件。
# 2. 逻辑运算符 and 与 or 的含义。
# 3. not 用于取反，理解 True 变 False。
# 4. 编写条件时从最可能的情况开始检查。
# 5. 保持条件简洁易读。
# 6. 组合 input 与条件，做简单小测验。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 复习 if/else 结构。
# 2. 介绍 elif，展示多重条件。
# 3. 讲解 and/or 的生活例子（同时完成作业和练琴）。
# 4. 黑板演示条件组合，学生判断结果。
# 5. 课堂练习设计小测验问题。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：elif 使用
score = 85
if score >= 90:
    print("A级优秀！")
elif score >= 80:
    print("B级良好，继续加油！")
else:
    print("努力就会进步！")

# 示例 2：and 与 or
finished_homework = True
practiced_piano = False
if finished_homework and practiced_piano:
    print("双重任务完成，奖励十分钟休息！")
elif finished_homework or practiced_piano:
    print("完成了一项任务，再努力完成另一项！")
else:
    print("今天要努力完成学习任务哦！")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：调整 score 的值，观察输出信息。
# 练习 2：新增一个条件：如果 score 小于 60，提示需要额外辅导。
# 练习 3：练习使用 not，判断学生是否没有完成作业。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟练编写多条件判断。
  # - 学会使用 and、or、not 组合条件。
# 作业要求：
  # 1. 输入天气状况 (sunny/rainy/snowy)。
  # 2. 根据天气给出不同的外出建议。
  # 3. 如果天气不是以上三种，提示无法识别。
  # 4. 额外挑战：加入温度条件（比如温度大于 30 度时提醒做好防暑）。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(weather: str, temperature: int | float) -> None:
    """根据天气和温度给出建议。"""
    if not isinstance(weather, str):
        raise TypeError("weather 需要是字符串。")
    if not isinstance(temperature, (int, float)):
        raise TypeError("temperature 需要是数字。")
    weather_clean = weather.strip().lower()
    if weather_clean == "sunny":
        print("阳光明媚，记得戴帽子出门！")
    elif weather_clean == "rainy":
        print("下雨天，雨伞别忘了！")
    elif weather_clean == "snowy":
        print("飘雪啦，注意保暖。")
    else:
        print("暂时不知道这种天气，查查天气预报吧！")

    if temperature > 30:
        print("今天有点热，记得多喝水！")
    elif temperature < 0:
        print("非常冷，要穿厚衣服！")
    else:
        print("气温适中，适合户外活动。")

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(weather='sunny', temperature=28)
