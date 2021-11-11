a=int(input("점수를 입력해보십시오"))
res=''
if a >=60:
    res='합격'
else:
    res='불합격'
print(res)

res='합격' if a>=60 else'불합격'
print(res)
