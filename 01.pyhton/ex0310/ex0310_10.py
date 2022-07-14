pi=3.14195
r= float(input('반지름을 입력하시오.>>>'))
print('원주율 = {}'.format(pi))
print('반지름 = {}'.format(r))
print('넓이 = {} * {} * {} = {:.2f}'.format(r,r,pi,r*r*pi))
print('원의 둘레 = {} * 2 * {} = {:.2f}'.format(r,pi,2*r*pi))