import scipy.misc as sp

arr = sp.imread("./allblack.png")
print(arr)

newArr = []

for row in arr:
    for pixel in row:
        newArr.append(pixel[0]/255)
