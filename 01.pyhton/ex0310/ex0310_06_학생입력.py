id='admin'
pw='1111'
student=[]
students=[]
# 무한
# u_id=input('아이디를 입력하세요.>>')
# u_pw=input('비밀번호를 입력하세요.>>')
# print('로그인 성공')
stu_no=1
while(1):
    
    # if(id==u_id and pw==u_pw):
    print('학생번호 ',stu_no)
 
    stu_name= input('학생이름을 입력하시오.>>')
    kor =int(input("국어성적을 입력하시오.>>"))
    eng =int(input("영어성적을 입력하시오.>>"))
    math=int(input("수학성적을 입력하시오.>>"))
    total=kor+eng+math
    avg=total/3
    rank=0
    student=[stu_no, stu_name, kor, eng, math, total, avg, rank]
    students.append(student)
    print(students)
    if stu_no ==5:
        break
        # print('학생번호 : '+stu_no)
        # print('학생이름 : ' + stu_name)
        # print('국어 :',kor)
        # print('영어 :',eng)
        # print('수학 :',math)
      
    stu_no+=1
        # print('총점 :',total)
        # print('평균 : %5.2f' %avg)

        # break
    # else:
    #     print('아이디 또는 비밀번호를 확인하세요.')






    # a= float(input("숫자를 입력해봐라"))
    # print(a)