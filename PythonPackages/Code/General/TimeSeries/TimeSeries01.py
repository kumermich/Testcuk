import scipy.stats

ndat = 100
rng = np.random.default_rng(42)
rng2 = np.random.default_rng(43)

def my_lin(x, m=4, b=20, e=0):
    return m * x + b + e

x = rng.random(ndat)*50
e = rng2.normal(0,10,len(x))
y = my_lin(x, e=e)

a = scipy.stats.linregress(x,y)
print(f'y = {a.slope:.2g}x + {a.intercept:.3g}')