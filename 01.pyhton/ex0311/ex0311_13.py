#구구단
for i in range(2,100):
    if i%2==0:
        for j in range(1,10):
            if j%2==1:
                print('{} * {} = {}'.format(i,j,i*j))
        
        