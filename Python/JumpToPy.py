# JumpToPtyhon 66p. 리스트 자료형 
"""
a=[1,2,3,4,5]
b=a[:2]
c=a[2:]

#print(b)
#print(c)

a=[1,2,3]
a.append(4)
print(a)

dic={'name':'pey','phone':'0101111111','birth':'1111'}
a={1:'hi'}
a[2]='b'

treeHit=0
while treeHit<10:
    treeHit+=1
    print("나무를 %d 번 찍었습니다."%treeHit)
    if treeHit==10:
        print("나무 넘어갑니다. ")


coffee=10
while True:
    money=int(input("돈을 넣어주세요:"))
    if money==300:
        coffee=coffee-1
    elif money>300:
        print("거스름돈 %d를 주고 커피를 줍니다."%(money-300))
        coffee=coffee-1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d 개입니다. "%coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


a=0
while a<10:
    a=a+1
    if a%2==0:continue
    print(a)

test_list=['one','two','three']
for i in test_list:
    print(i)

a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)

marks=[90,25,67,45,80]
number=0
for mark in marks:
    if mark >=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격입니다."%number)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60:continue
    print("%d번 학생 축하합니다. 합격입니다."%(number+1))

a=[1,2,3,4]
result=[num*3 for num in a]
print(result)
result2=[num*3 for num in a if num %2==0]

for i,name in enumerate(['body','foo','bar']):
    print(i,name)

def positive(numberList):
    result=[]
    for num in numberList:
        if num>0:
            result.append(num)
    return result

print(positive([1,-3,2,0,-5,6]))

def positive2(x):
    return x>0

print(filter(positive2,[1,-3,2,0,-5,6]))
print(list(filter(lambda x:x>0,[1,-3,2,0,-5,6]))

#print(list("python"))
#print(list((1,2,3)))

def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result

result=two_times([1,2,3,4])
print(result)

print(list(zip([1,2,3],[4,5,6])))

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1 & s2)
print(s1|s2)
print(s1-s2)
"""











