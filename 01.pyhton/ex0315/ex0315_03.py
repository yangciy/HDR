# aa = [10,20,30]

# aa.append(40)

# print(aa)

# aa[3]=500
# print(aa)


# aa[0:2]=[200,300]

# print(aa)


# aa[1] =[1,2]
# print(aa)
# del(aa[1])
# print(aa)
  
students=[
    [1,'a',100,100,100,100,0,0],
    [2,'b',100,100,100,100,0,0],
    [3,'c',100,100,100,100,0,0],
    [4,'d',100,100,100,100,0,0],
    [5,'e',100,100,100,100,0,0]
]

cnt=0
search=input('검색할 이름을 작성하세요.')
for stu in students:
    if search in stu:
        print("[찾는 학생의 성적]")
        for s in stu:
            print(s,end=' ')
        print()
        cnt=1
        break       
    else:
        continue
if cnt==0:        
    print('찾는 학생이 없습니다.')    
            
        
    

# if serach in students:
#     print()
