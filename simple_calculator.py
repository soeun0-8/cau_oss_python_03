# Homework #2
#20213168 박소은

# 사용자에게 연산방법을 문자열로 입력을 받은 후
# 정수 2개를 입력받아 연산을 수행하는 프로그램

# 연산방법은 "+", "-", "*", "/", "%", "end" 6가지이며,
# "+"일 경우 덧셈(add) "-"일 경우 뺄셈(sub)
# "*"일 경우 곱셈(mul) "/"일 경우 나눗셈(div)
# "%"일 경우 나머지(mod)를 수행하며
# "end"일 경우 반복을 종료하고 "Exit program"을 출력하고 종료한다.
# 그 외 입력의 경우 "Invalid operator"을 출력한다.

# arithmetic_ops: 연산 수행(정수 2개 입력받은 후 매개함수로 전달)
def arithmetic_ops(op):
    num1 = int(input("input 1st number:"))
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

# +와 -는 함수로 정의 (def 이용 - add, sub)
# *, /, %는 익명함수(lambda) 사용

#+, - 함수 정의
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

while True:
    op = input("input operation:")
    if op == "end":
        break   # "반복을 종료"
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add) # 정의된 함수 사용
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda x,y:x*y) # 익명함수(lambda) 사용

    elif op == "-":
        num1, num2, ret = arithmetic_ops(sub)
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda x,y:x/y)
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda x,y:x%y)
    else:
        print("Invalid operation")
        continue # Invalid operation이므로 연산결과를 출력하지 않고 "넘어간다".
    print(f"{num1}{op}{num2} = {ret}")  # 연산 결과를 출력

print("Exit program")