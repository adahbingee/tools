import cv2 as cv
import numpy as np

# solve B(bigo) to K(Kwai) CCM

color_k = [
[142.0, 224.0, 206.0],
[176.0, 175.0, 208.0],
[108.0, 133.0, 77.0],
[126.0, 163.0, 189.0],
[219.0, 170.0, 145.0],
[136.0, 102.0, 73.0],
[233.0, 185.0, 61.0],
[186.0, 223.0, 91.0],
[108.0, 78.0, 104.0],
[222.0, 109.0, 103.0],
[97.0, 126.0, 199.0],
[224.0, 142.0, 51.0],
[94.0, 185.0, 217.0],
[223.0, 120.0, 158.0],
[236.0, 215.0, 70.0],
[217.0, 82.0, 72.0],
[112.0, 192.0, 115.0],
[59.0, 91.0, 172.0],
[45.0, 54.0, 44.0],
[98.0, 107.0, 93.0],
[164.0, 171.0, 156.0],
[201.0, 209.0, 192.0],
[219.0, 227.0, 209.0],
[239.0, 243.0, 222.0],
]

color_b = [
[144.0, 221.0, 202.0],
[178.0, 173.0, 204.0],
[109.0, 130.0, 74.0],
[128.0, 161.0, 183.0],
[218.0, 166.0, 139.0],
[138.0, 101.0, 70.0],
[231.0, 179.0, 59.0],
[188.0, 221.0, 87.0],
[108.0, 76.0, 99.0],
[222.0, 107.0, 100.0],
[98.0, 125.0, 194.0],
[224.0, 138.0, 49.0],
[96.0, 184.0, 214.0],
[222.0, 116.0, 152.0],
[235.0, 210.0, 68.0],
[216.0, 80.0, 70.0],
[114.0, 191.0, 111.0],
[60.0, 90.0, 166.0],
[45.0, 52.0, 40.0],
[96.0, 104.0, 89.0],
[162.0, 167.0, 149.0],
[201.0, 204.0, 185.0],
[219.0, 222.0, 201.0],
[240.0, 241.0, 217.0],
]

matK = np.array(color_k)
matB = np.array(color_b)

# solve B(bigo) to K(Kwai) CCM
pointNum = matK.shape[0]

# Ax   = b
# A'Ax = A'b
# Mx   = y
# x    = M^-1 y
A = np.zeros([pointNum*3, 9]) # 72, 9
b = np.zeros([pointNum*3, 1]) # 72, 1
n = 0
for r in range(0, A.shape[0], 3):
    A[r+0][0] = matB[n][0]
    A[r+0][1] = matB[n][1]
    A[r+0][2] = matB[n][2]
    A[r+1][3] = matB[n][0]
    A[r+1][4] = matB[n][1]
    A[r+1][5] = matB[n][2]
    A[r+2][6] = matB[n][0]
    A[r+2][7] = matB[n][1]
    A[r+2][8] = matB[n][2]
    b[r+0][0] = matK[n][0]
    b[r+1][0] = matK[n][1]
    b[r+2][0] = matK[n][2]
    n = n + 1

At = np.transpose(A)
M  = np.matmul(At, A)
y  = np.matmul(At, b)

iM  = np.linalg.inv(M)
ccm = np.matmul(iM, y)
ccm = np.reshape(ccm, [3, 3])
print(ccm)

# use ccm
img = cv.imread('bigo.PNG')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        vec0 = img[y][x]
        vec1 = np.matmul(ccm, vec0)
        vec1 = np.round(vec1)
        vec1 = np.clip(vec1, 0, 255)
        img[y][x] = vec1

img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
cv.imwrite('out.png', img)