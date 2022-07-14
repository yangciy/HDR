def cal(v1):
    temp1=v1[0]
    temp2=v1[1]
    v1[0]=temp1+temp2
    v1[1]=temp1-temp2
    

    
myList=[100,200]
print('더하기, 빼기 값 :',myList[0],myList[1])
hap,sub=0,0

cal(myList)
hap=myList[0]
sub=myList[1]



# def cal(v1,v2):
#     global hap,sub
#     hap =v1+v2
#     sub =v1-v2
# myList=[]
# hap,sub=0,0

# myList=cal(100,200)
# print('더하기, 빼기 값 :',hap,sub)




# def cal(v1,v2):
#     calList=[]
#     res1=v1+v2
#     res2=v1-v2
#     calList.append(res1)
#     calList.append(res2)
#     return calList

    
# myList=[]
# hap,sub=0,0

# myList=cal(100,200)
# hap=myList[0]
# sub=myList[1]
# print('더하기, 빼기 값 :',hap,sub)





# # def cal1():
# #     global a 
# #     a= 10
    
    
# # a=20

# # cal1()
# # print(a)