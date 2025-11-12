"""
Day 4: 认识比较运算和布尔值

课程定位：
  - 介绍 >、<、== 等比较运算，并理解 True/False 的意义，为条件语句做准备。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 比较运算符：>, <, ==, >=, <=, !=。
# 2. 布尔值 (Boolean)：只有 True 和 False。
# 3. 比较表达式的结果可以存入变量。
# 4. 使用 print 查看布尔结果，理解真假。
# 5. 组合比较与算术运算 (如 age + 1 > 8)。
# 6. 布尔值在日常生活中的例子。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 通过现实场景（身高比较）引入真假概念。
# 2. 演示不同的比较表达式。
# 3. 展示布尔值如何随变量变化而改变。
# 4. 让学生猜测表达式的结果，再运行验证。
# 5. 总结布尔值在程序控制中的作用。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例 1：基本比较
my_age = 8
friend_age = 7
print("我比朋友大吗?", my_age > friend_age)
print("我们同岁吗?", my_age == friend_age)

# 示例 2：把比较结果保存下来
is_taller = True  # 假设我更高
print("我是不是更高?", is_taller)

# 示例 3：组合算术和比较
candies = 5
will_have = candies + 2
print("吃完糖后糖果会超过 6 个吗?", will_have > 6)

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：修改 my_age 和 friend_age 的值，观察比较结果变化。
# 练习 2：新增一个比较，判断 candies 是否等于 7。
# 练习 3：思考并打印：10 - 3 是否大于 4。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 练习比较运算符的使用。
  # - 理解布尔值在判断中的作用。
# 作业要求：
  # 1. 创建两个变量，表示两个同学的作业本数量。
  # 2. 输出比较结果：谁的作业本更多，是否一样多。
  # 3. 计算他们作业本总数是否大于 10。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(count_a: int, count_b: int) -> None:
    """比较两个作业本数量，输出结果。"""
    for value, name in ((count_a, "count_a"), (count_b, "count_b")):
        if not isinstance(value, int):
            raise TypeError(f"{name} 需要是整数。")
        if value < 0:
            raise ValueError(f"{name} 不能为负数。")
    print("同学 A 的作业本数量:", count_a)
    print("同学 B 的作业本数量:", count_b)
    print("A 的作业本更多吗?", count_a > count_b)
    print("他们一样多吗?", count_a == count_b)
    print("总数量是否大于 10?", (count_a + count_b) > 10)

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution(count_a=6, count_b=5)
