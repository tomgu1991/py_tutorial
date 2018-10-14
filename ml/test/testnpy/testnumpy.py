#!/usr/bin/env python3
# Author Zuxing Gu

'''
x = np.array([[1,2,3], [4,5,6]])
print("x:\n{}".format(x))
print(x.ndim)
print(x.shape)

print("========\n")
a = np.arange(10)
print(a)
print(len(a))
print(a.ndim)
b = np.arange(1, 9, 2)
print(b)
c = np.linspace(0, 1, 6)
print(c)
d = np.linspace(0, 1, 6, endpoint=False)
print(d)
'''

'''
print("========\n")
a = np.ones((3, 3))
print(a)
b = np.zeros((2, 2, 2))
print(b)
c = np.eye(3)
print(c)
d = np.diag(np.array([1, 2, 3, 4]))
print(d)
e = np.random.rand(4)
print(e)
f = np.random.randn(100)
print(f)
g = sorted(f)
print(g)
print(np.average(g))
x = np.linspace(-10, 10, 100)
# plt.plot(x, g, marker="x")
# plt.show()
'''

'''
print("========\n")
x = np.linspace(0, 3, 20)
y = np.linspace(0, 6, 20)
# plt.plot(x, y, 'o')
# plt.show()

image = np.random.rand(30, 30)
# plt.imshow(image, cmap=plt.cm.hot)
# plt.colorbar()
# plt.savefig('fig.png')
# plt.show()
'''

'''
print("========\n")
a = np.arange(10)
print(a)
print(a[0], a[2], a[-1])
print(a[::-1])
print(a[2:9:3])
print(a[:4])
print(a[1:3])
print(a[::2])
print(a[3:])
'''

'''
print("========\n")
a = np.arange(10)
b = a[::2]
print(b)
b[0] = 12
print(a, b)
print(np.may_share_memory(a, b))
c = a.copy()
c[0] = 24
print(a, c, np.may_share_memory(a, c))
'''

'''
print("========\n")
np.random.seed(5)
a = np.random.randint(0, 21, 15)
print(a)
print(a % 3)
mask = (a % 3 == 0)
extract = a[mask]
print(extract)
'''
