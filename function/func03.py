## 함수 선언 부분 ##
def calc(v1, v2, op) :
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    return result

## 전역 변수 선언 부분 ##
res = 0
var, var2, oper = 0, 0, ""

## 메인 코드 부분 ##
oper = input("계산을 입력(+,-,*,/) : ")
var1 = int(input("첫 번째 수를 입력 : "))
var2 = int(input("두 번째 수를 입력 : "))

res = calc(var1, var2, oper)
print(f"## 계산기 : {var1} {oper} {var2} = {res}")