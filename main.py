num1=[1,2,3]
num2=[5,2,9]
result=map(lambda x,y: x+y, num1,num2)
print(list(result))
nums=[2,9,6,4,8,6]
def square(n):
    return n*n
res=list(map(square,nums))
print(res)