


#numpy 的对象是ndarray（多维数组），由实际的数据和数据的元数据组成
import numpy as np
a = np.array([np.arange(2), np.arange(2)])
a.shape      #矩阵A的形状，几行几列
a.dtype      #矩阵的数据类型
a[0.0]       #矩阵元素下标从0开始，这代表获取矩阵A第一行第一列元素
a.dtype.itemsize       #矩阵A中元素所占用字符
sctypeDict.keys()      #查询所有的数据类型


t = dtype([('name', str_40), ('numitems', int32),('price', float32)]) 
#define a combination data type, include three sorts name ,quantity and price
demo1 = array([('Milk', 42, 3.14), dtype = t])



a[:7:2]
a[::-1] #index and slice


b = arange(24).reshape(2,3,4)       #reshape ,change the matrix shape 
b [0,...]                           #equal to b[0,:,:,:]
b[0,1,::2]                          #choose the element by step 2
b[0,::-1,-1]                        #choose the element by reverse


b.ravel()                           #change matrix shape to one dimension
b.flatten                           #equal to b.ravel()
b.transpose                         #transpose matrix
b.resize                            #function equal reshape, but it's change the matrix forever


vstack(a,b)               #== concatenate((a,b), axis= 0) vertical combination
hstack(a,b)               #== concatenate((a,b), axis= 1) horizon combination 
dstack(a,b)               #deep combination 
concatenate(a,b)


hsplit(a,3)               #== split(a,3,axis=1)
vsplit(a,3)               #== split(a,3,axis=0)
dsplit(a,3)               #deep split

b.ndim                    #dimension number
b.size                    #matrix element quantity
b.nbytes                  #all matrix bytes
b.T                       #equal to b.transpose
b.real                    #
b.imag                    #
b.flat
#1, f = b.flat, for item in f: print(item)
#2, b.flat(2)   choose the element
#3, b.flat[[1,3]]
#4, b.flat = 7
#5, b.flat[[1,3]] = 1


b.tolist                  #change the matrix to list