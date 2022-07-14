students=[
    [1,'a',100,100,100,100,0,0],
    [2,'b',100,100,100,100,0,0],
    [3,'c',100,100,100,100,0,0],
    [4,'d',100,100,100,100,0,0],
    [5,'e',100,100,100,100,0,0]
]


while 1:
    search=input('사람이름을 입력하세요..>  ')
    for idx, stu in enumerate(students):
        if search in stu:
            del(students[idx])
        
            # for s in stu:
            #     print(s,end= ' ')
            # print()
            # break
    print(students)
            
