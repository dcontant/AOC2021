with open('aoc2021_3.txt') as e:
    f = e.read().splitlines()[:-1]
half = len(f)//2
def isbitset(n,i):
#check if the ith bit on n is set, index start at 1
    return bool(n & (1<<i-1))

gamma_dict = dict((n,0) for n in range(1,13))
for x in f:
    for i in range(12,0,-1):
        gamma_dict[i] += isbitset(int(x,2),i)
gamma = ''
for k,v in gamma_dict.items():
    if v>half:
        gamma += '1'
    else:
        gamma += '0'
gamma = int(gamma[::-1],2)
epsilon = 4095 - gamma
print(gamma,bin(gamma),epsilon,bin(epsilon),gamma*epsilon)
