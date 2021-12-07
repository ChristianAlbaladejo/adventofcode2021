import numpy as np
with open('input.txt','r') as f:
    rawData=f.read()
data=rawData.strip()
data=np.array(data.split(','),dtype=np.int)

def reproduce(initial,days):
    fishes=np.zeros(9,dtype=np.int)
    for i in range(fishes.shape[0]):
        fishes[i]=len(np.where(initial==i)[0])
    for d in range(days):
        zeroTo6=fishes[:7]
        seven8=fishes[7:]
        newFish=zeroTo6[0]
        zeroTo6=np.roll(zeroTo6,-1)
        zeroTo6[-1]+=seven8[0]
        seven8=np.roll(seven8,-1)
        seven8[-1]=newFish
        fishes=np.concatenate((zeroTo6,seven8))
    return fishes

# Part 1
print("Part 1 result {}".format(np.sum(reproduce(data, 80))))

# Part 2
print("Part 2 result {}".format(np.sum(reproduce(data, 256))))