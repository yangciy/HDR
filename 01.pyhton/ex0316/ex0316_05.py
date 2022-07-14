import operator

tdic,tlist={},[]
tdic={'love':'사랑','chair':'의자','game':'게임','car':'자동차'}


# tlist =sorted(tdic.items(),key=operator.itemgetter(0))

print(list(tdic.items()))
#key와 value를 튜플형태로 출력 - list 형태로 출력
tlist2= list(tdic.items())
tlist2.sort(reverse=1)
print(tlist2)


# sorted= 기존리스트는 변하지 않고 새로운 리스트에 복사
# tlist=[4,6,1,8,9,11,2]                   
# tlist2= sorted(tlist)
# print(tlist2)
# tlist.sort(reverse=True)
# # print(tlist)
# tlist.reverse()
# print(tlist)