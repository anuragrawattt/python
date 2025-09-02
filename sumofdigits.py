# def func():
#     n=int(input())
#     c=[]
#     b=str(n)
#     c=c.insert(0,any) 
#     print(c)
# #     sum=0
# #     for i in len(b):
# #         a=b.split()
# #         sum=sum+i
# #         i=i+1
# # func(12345)
# func()      
# n=int(input())
# c=[]
# b=str(n)
# c=b.split()
# print(c,type(c))
# num = 1234
# str_num = str(num)  # "1234"
# print(str_num.split())  # ['1234']  — split without a separator just returns the whole string in a list
num = 1234
str_num = str(num)
digits = [int(d) for d in str_num]  # convert each character to int
print(digits)  # Output: [1, 2, 3, 4]
sum=0
for i in digits:
    sum=sum+i
    i+=1
print(f"sum of digits is: {sum}")    