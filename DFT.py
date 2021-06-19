import numpy as np
import PIL.Image as image
import matplotlib.pyplot as plt
F=image.open('test.png')
F = np.array(F)
N=F.shape[-1]
y=np.arange(N)
fft=1j*np.zeros((N,N))
for i in range(N):
    for j in range(N):
        P = np.exp(-1j * y / N * i * 2 * np.pi)
        Q = np.exp(-1j * y / N * j * 2 * np.pi)
        fft[i,j]=P@F@Q.T
plt.imshow(fft.__abs__(),cmap='gray')
plt.show()