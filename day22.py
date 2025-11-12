"""
Day 22: 守护程序：输入与异常处理

课程定位：
  - 强调防御性编程，学习 try/except 捕获错误，确保程序稳健运行。
"""

# ================================
# 知识点总览 (Knowledge Points)
# ================================

# 1. 常见错误类型：ValueError、ZeroDivisionError。
# 2. 使用 try/except 捕获异常并给出提示。
# 3. finally 块用于清理或结束提醒。
# 4. 自定义错误信息帮助用户理解。
# 5. 输入验证优先，尽量避免异常。
# 6. 记录错误情况用于排查（简单打印）。

# ================================
# 课堂活动设计 (Lesson Flow)
# ================================

# 1. 讨论程序出错的真实案例。
# 2. 演示没有处理异常会崩溃。
# 3. 展示 try/except 包裹敏感代码。
# 4. 设计安全的除法函数。
# 5. 课堂练习：给之前的代码添加异常处理。

# ================================
# 教学示例代码 (Teaching Demos)
# ================================

# 示例：安全除法
def safe_divide(a: str, b: str) -> None:
    try:
        numerator = float(a)
        denominator = float(b)
        result = numerator / denominator
    except ValueError:
        print("请输入正确的数字！")
    except ZeroDivisionError:
        print("除数不能为 0！")
    else:
        print("结果是", result)
    finally:
        print("计算结束，感谢使用！")

safe_divide("6", "2")
safe_divide("六", "2")

# ================================
# 课堂练习 (In-Class Practice)
# ================================

# 练习 1：尝试用 safe_divide 处理不同输入情况。
# 练习 2：修改函数，在成功时打印“计算成功”。
# 练习 3：思考还可以捕获哪些异常，写在注释里。

# ================================
# 课后作业 (Homework Assignment)
# ================================

# 作业目标：
  # - 强化输入验证与异常处理观念。
  # - 设计健壮的函数，避免程序崩溃。
# 作业要求：
  # 1. 编写函数，接收两个字符串形式的数字并求和。
  # 2. 若输入不是数字，提示重新输入。
  # 3. 额外挑战：限制结果不能超过 100，超过则给出提醒。

# ================================
# 作业参考答案 (Reference Solution)
# ================================

def homework_solution(number_a: str, number_b: str) -> float | None:
    """将字符串数字相加，包含异常处理和结果限制。"""
    if not isinstance(number_a, str) or not isinstance(number_b, str):
        raise TypeError("两个参数都需要是字符串。")
    try:
        a = float(number_a.strip())
        b = float(number_b.strip())
    except ValueError:
        print("至少有一个输入不是数字，请检查后再试。")
        return None
    total = a + b
    if total > 100:
        print("结果超过 100，请使用更小的数字。")
        return None
    print(f"{a} + {b} = {total}")
    return total

# 供教师演示或学生验证使用
if __name__ == "__main__":
    homework_solution('45', '50')
