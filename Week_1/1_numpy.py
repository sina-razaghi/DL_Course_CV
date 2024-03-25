################################## Work with Numpy Library ##################################

import numpy as np

# # dtype = np.bool / np.float / np.int / np.complex 
# a = np.array([1,2,3], dtype=np.float64)
# print("\nA (simple array) =>\n")
# print(a)
# print("\n=================\n")


# b = np.array([[[1, 1, 1], [2, 2, 2], [3, 3, 3]],
#               [[4, 4, 4], [5, 5, 5], [6, 6, 6]]])
# print("B (simple 3D array) =>\n")
# print(b.shape)
# print(b)
# print(b[1])
# print(b[1][1])
# print("\n=================\n")


# c = np.zeros((3, 2))
# print("C (zero & one array) =>\n")
# print(c)


# c = np.ones((3, 2))
# print("\nC =>")
# print(c)
# print("\n=================\n")


# d = np.arange(10)
# print("D (range array) =>\n")
# print(d)
# d = np.arange(2, 12, 3)
# print(d)
# print("\n=================\n")


# e = np.linspace(10, 20, 5)
# print("E (float range array) =>\n")
# print(e)
# print("\n=================\n")


# f = np.full((3, 5), 7)
# print("F (simple exact number array) =>\n")
# print(f)
# print("\n=================\n")


# g = np.eye(4)
# print("G (I matrix) =>\n")
# print(g)
# print("\n=================\n")


# h = np.random.random((2,3))
# print("H (random 0:1 array) =>\n")
# print(h)
# print("\n=================\n")



# ################################## Work with Files in Numpy ##################################



# # # Save npy File Single Array
# # np.save("my_array.npy", b)

# # # Load npy File Single Array
# # output = np.load("my_array.npy")
# # print(output)


# # # Save npz File Multi Array
# # np.savez("multi_array.npz", a, c)

# # # Load npz File Multi Array
# # output = np.load("multi_array.npz" )
# # print(output["arr_0"])
# # print(output["arr_1"])


# # # Save txt File
# # np.savetxt("my_array.txt", b)

# # Load txt File
# # output = np.loadtxt("my_array.txt")
# # print(output)


# # print(f"\nshape b => {b.shape}")
# # print(f"lengh b => {len(b)}")
# # print(f"ndim b => {b.ndim}")
# # print(f"size b => {b.size}")
# # print(f"dtype b => {b.dtype}")
# # print(f"dtype c => {c.dtype}")
# # c_int = c.astype(int)
# # print(f"astype c => {c_int.dtype}")


# i = np.array([[1, 2],
#               [3, 4]])

# j = np.array([[-1, -2],
#               [3, 4]])

# print(f"i+j =\n{i+j}\n")
# print(f"i-j =\n{i-j}\n")
# print(f"i*j =\n{i*j}\n")
# print(f"i/j =\n{i/j}\n")

# # np.add
# # np.subtract
# # np.divide
# # np.multiply (eleman dar eleman)

# # np.exp (e^...)
# # np.sqrt (Radical)
# # np.sin
# # np.cos
# # np.log


# # martix multiply :

# i = np.array([[1, 2, 3],
#               [4, 5, 6]])

# j = np.array([[1, 2],
#               [3, 4],
#               [5, 6]])

# print(f"matmul i,j = \n{np.matmul(i, j)}\n")
# print(f"martix multiply (@) i,j = \n{i@j}\n")

# print(f"Are these a & b equal :\n{a==b}")
# print(f"Are these a bigger than b  :\n{a>b}")

# print("Maximum of matrix a:")
# print(a.max())
# print(np.max(a))

# # np.sum() / np.min() / np.max(axis=0) / np.median() / np.std(b) (enheraf meyar)

# print("\nSUM axis=0 => ")
# print(np.sum(b, axis=0))
# print("\nSUM axis=1 => ")
# print(np.sum(b, axis=1))
# #    axis  |   [  [ [1, 1, 1], [2, 2, 2], [3, 3, 3] ],
# #     = 0  v      [ [4, 4, 4], [5, 5, 5], [6, 6, 6] ]  ]
# #                        --------->
# #                         axis = 1 



###############################################################################

a = np.array([1, 2, 3, 4, 5, 6])
b = np.copy(a)

b[0] = 10

print("\nnew a =>")
print(a)
print("\ncopy of a =>")
print(b)

print("\nsorted a =>")
print(np.sort(a))
print("\nunsorted a =>")
print(a)

c = np.array([[20, 1, 6], [0, 4, 5]])
print("\nc =>")
print(c)

c.sort(axis=0)
print("\nsorted c axis=0 =>")
print(c)

c.sort(axis=1)
print("\nsorted c axis=1 =>")
print(c)

print("\n======================")

print("\nreshape a =>")
print(np.reshape(a, (3, -1)))

print("\nconcatenate a,b =>")
print(np.concatenate((a, b)))


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.copy(a)

b[0][0] = 10

print("\nconcatenate(2D) a,b axis=0 =>")
print(np.concatenate((a, b), axis=0))

print("\nconcatenate(2D) a,b axis=1 =>")
print(np.concatenate((a, b), axis=1))

print("\nhstack a,b =>")
print(np.hstack((a, b)))

print("\nhstack a,b =>")
print(np.vstack((a, b)))
