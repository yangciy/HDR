money,c500,c100,c50,c10=0,0,0,0,0

money= int(input('교환할 돈을 입력하세요.>>>'))

c500=money//500
money= money-c500*500
c100=money//100
money= money-c100*100
c50=money//50
c10=int(money%50/10)

print('500원: ',c500,'100원: ',c100,'50원: ',c50,'10원: ',c10)

money= int(input('교환할 돈을 입력하세요.>>>'))
c500=money//500
c100=money%500//100
c50=money%500%100//50
c10=int(money%500%100%50/10)

print('500원: ',c500,'100원: ',c100,'50원: ',c50,'10원: ',c10)