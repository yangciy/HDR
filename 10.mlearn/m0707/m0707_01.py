from scipy.stats import uniform, randint
rgen=randint(0,10)
print(rgen.rvs(5))


ugen=uniform(0,1)
print(ugen.rvs(10))