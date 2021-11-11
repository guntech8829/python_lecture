select=int(int("1.입력한 수식계산 2.두수사이의 합계:"))
if select == 1:
    numStr=input("***수식을 입력하세요")
    answer=eval(numStr)
    print("%S 결과는 %5.1f입니다."%(numStr,answer))
elif select==2:
    num1=int(input("***첫번째 숫자를 입력하세요"))
    num2=int(input("***두번째 숫자를 입력하세요"))
    for i in range (num1,num2+1):
        answer=i+1
        print("%d+...+%d는 %d입니다."%(num1,num2,answer))
    else:
        print("1또는 2만 입력해야합니다.")