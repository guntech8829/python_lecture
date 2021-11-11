ch=""
a,b=0,0

while True:
    a=int(input("A:"))
    b=int(input("B:"))
    ch=input("연산자")

    if (ch=="+"):
        print(f"{a}+{b}={a+b}")
    elif (ch=="-"):
        print(f"{a}-{b}={a-b}")
    elif (ch=="*"):
        print(f"{a}*{b}={a*b}")
    elif (ch=="/"):
        print(f"{a}/{b}={a/b}")    
    elif (ch=="%"):
        print(f"{a}%{b}={a%b}")   
    elif (ch=="//"):
        print(f"{a}//{b}={a//b}")   
    elif (ch=="**"):
        print(f"{a}**{b}={a**b}")   
    else:
        print(f"연산자를 잘못 입력했습니다.")
    d = input("종료하시려면 'q'를 입력해주세요.")
    if(d == "q"):
        break