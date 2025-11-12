"""
Day 14: 字符串与列表的转换

课程定位：
  - 学习 split 和 join，把字符串拆成列表、再组合回字符串，理解数据结构之间的转换。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. split() 按分隔符切分字符串。
# 2. join() 用分隔符把列表合成字符串。
# 3. 拆分文本时需确保分隔符正确。
# 4. strip() 清理每个词的两端空格。
# 5. 使用列表推导式顺便处理数据。
# 6. 转换前后检查长度避免空数据。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 回顾字符串和列表的特性。
# 2. 演示 split 把句子拆成单词列表。
# 3. 演示 join 把单词拼成句子。
# 4. 组合 strip 清理空格。
# 5. 小练习：拆分兴趣列表再重组。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：split 拆分
sentence = "苹果, 香蕉, 草莓"
parts = sentence.split(",")
clean_parts = [item.strip() for item in parts]
print("拆分后的列表:", clean_parts)

# 示例 2：join 拼接
joined = " 和 ".join(clean_parts)
print("重新组合后的句子:", joined)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：把 sentence 改成自己的兴趣，用 split 拆分。
# 练习 2：尝试使用不同的分隔符，例如分号。
# 练习 3：用 join 把列表组合成“我喜欢A，也喜欢B”的句子。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 熟练掌握 split 和 join 的使用。
  # - 练习数据清理与重组。
# 作业要求：
  # 1. 输入一个用逗号分隔的物品清单。
  # 2. 拆分成列表并去掉空格。
  # 3. 输出列表长度以及每个物品。
  # 4. 使用 join 把它们组合成一句话。
  # 5. 额外挑战：如果清单为空，给出提示。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(raw_items: str) -> None:
    """拆分物品清单并重新组合输出。"""
    if not isinstance(raw_items, str):
        raise TypeError("raw_items 需要是字符串。")
    text = raw_items.strip()
    if not text:
        print("清单为空，请写上一些物品。")
        return
    parts = [item.strip() for item in text.split(",") if item.strip()]
    if not parts:
        print("没有识别出有效的物品，请检查输入。")
        return
    print("共有", len(parts), "样物品：")
    for index, item in enumerate(parts, start=1):
        print(f"{index}. {item}")
    sentence = "、".join(parts)
    print("我准备带这些：", sentence)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution('铅笔, 橡皮, 彩笔')
