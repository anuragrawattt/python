# import random
# computer=random.choice([-1,0,1])
n=int(input("enter 1 to encoding enter 2 for decoding"))
if n==1:
    msg=input("enter msg for encoding")
    b=msg.split()   
    rand=str(input("enter random characters 6 only"))
    if len(msg)<3:
        print(msg[::-1])
    else:
        encoding=msg[1:]
        c=rand[:3]+ encoding + msg[:1] + rand[3:]
        print(c)
        
elif n==2:
    msg=input("enter msg for decoding")
    b=msg.split()
    if len(msg)<3:
        print(msg[::-1])
    else:
        decoding=msg[-4]+msg[3:-4]
        print(decoding)
else:
    print("Invalid")     




# msg=input("enter the msg u want to decode")
# b=msg.split()
# for i in b:
#     if len(b)<3:
#         print(b[::-1])
#     else:
#         rand=input("enter random 6 words")
#         c=b[1:]
#         print(rand[:3]+c+b[:1]+rand[3:]) 
           
