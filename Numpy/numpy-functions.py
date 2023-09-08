import numpy as np

# shape      방크기
# ndim       차원
# dtype      데이터형식
# itemsize   메모리 바이트수
# size       자료 갯수

## number types 
# np.array([10, 20, 30], 'float64')

# array      리스트
# maxrix     2차원 행렬

# insert     넣기
# delete     빼기 


### Generation Functions

## array()    
# np.array([10, 20, 30])

## arange()
# np.arange(3)
# 0에서 숫자 3개를 채운다

## zeros()
# np.zeros((2, 3))
# 2 x 3 행렬을 0으로 채운다

## ones()
# np.ones((2, 3))
# 2 x 3 행렬을 1으로 채운다

## linspace()
# np.linspace(0, 5, 6)
# 0에서 5까지 6개로 나눈다

## logspace()
# np.logspace(0, 5, 11)


### Math

# a = np.array([10, 20, 30])
# b = np.array([1, 2, 3])

## + 
# c = a + b
# [11, 22, 33]

## - 
# c = a - b
# [9, 18, 27]

## ** 
# c = b**2 
# [1, 4, 9]

## *
# c = 2*a
# [20, 40, 60]

## <
# idx = b < 20
# [true, false, false]


### Math Statistical Functsions

# a = np.array([10, 20, 30])

## mean()
# 값들의 평균

## average()
# np. average(a, weights=[1, 1, 0])
# 가중치를 줄 수 있음

## median()
# 중간값

## cumsum()
# 앞의 값들을 계속 더한다

### Math Useful Functsions

# a = np.array([10, 20, 30])

## sum()
# 값들의 합

## min()
# 최소값

## argmin()
# 최소값의 index

## max()
# 최대값

## argmax()
# 최대값의 index

## ptp()
# 최대값과 최소값의 차이


### Array Manupulation

# a = np.array([1, 2, 3, 4, 5, 6])

## reshape()
# a.reshape(2, 3)
# array([[1, 2, 3], 
#        [4, 5, 6]])

# np.linspace(1, 10, 10).reshape(2, 5)
# array([[1, 2, 3, 4, 5], 
#        6, 7, 8, 9, 10]])


# a = np.array([[1, 2], [3, 4]])

## repeat()
# a.repeat(a, 2)
# array([1, 1, 2, 2, 3, 3, 4, 5])

# a.repeat(a, 2, axis=0)
# array([[1, 2], 
#        [1, 2],
#        [3, 4],
#        [3, 4]])

# a.repeat(a, 2, axis=1)
# array([[1, 1, 2, 2],
#        [3, 3, 4, 4]])

# a.repeat(a, [1, 2], axis=0)
# array([[1, 2], 
#        [3, 4],
#        [3, 4]])

# a.repeat(a, [3, 1], axis=0)
# array([[1, 2], 
#        [1, 2],
#        [1, 2],
#        [3, 4]])

# a.repeat(a, [1, 2], axis=1)
# array([[1, 2, 2],
#        [3, 4, 4]])


# a.repeat(a, [3, 1], axis=1)
# array([[1, 1, 1, 2],
#        [3, 3, 3, 4]])

# a = np.array([[1], [2], [3]])
# b = np.array([[4], [5], [6]])

## concatenate()
# np.concatenate((a, b), axis=0)
# array([[1],
#         [2],
#         [3],
#         [4],
#         [5],
#         [6]])

# np.concatenate((a, b), axis=1)
# array([[1, 4], 
#        [2, 5],
#        [3, 6]])


# a = np.array([10, 20, 30])
# b = np.array([40, 50, 60])

## hstack()
# np.hstack((a, b))
# array([10, 20, 30, 40, 50, 60])

## vstact()
# np.vstack((a, b))
# array([10, 20, 30],
#       [40, 50, 60]])

# a = np.array([10, 20, 30],
#              [40, 50, 60])

## hsplit()
# np.hsplit(a, 3)
# array([[10, 40],
#        [20, 50],
#        [30, 60]])

## vsplit()
# np.vsplit(a, 2)
# array([10, 20, 30],
#       [40, 50, 60])


## transpose()
# a.transpose()
# array([[10, 40],
#        [20, 50],
#        [30, 60]])

## ravel()
# a.ravel()
# a.reshape(-1)
# array([10, 20, 30, 40, 50, 60])

# a.ravel(order='C') 가로 방향 중심
# array([10, 20, 30, 40, 50, 60])

# a.ravel(order='F') 세로 방향 중심
# array([10, 40, 20, 50, 30, 60])

## flatten()
# a.flatten()
# array([10, 20, 30, 40, 50, 60])

# a = np.array([[10, 20, 30]])
## squeeze() 
# a.squeeze()
# array([10, 20, 30])
# 차원이 하나 빠짐

## newaxis()
# 차원이 하나 생성

## view()
# shallow copy 얕은 복사
# 메모리상 데이터는 공유해서 같으나 shape은 변경되도 문제 없음

## copy()
# deep copy 깊은 복사

## all()
# 모든 값이 참인지

## any()
# 하나라도 참인지

## nonzero()
# 0이 아닌 곳의 index들을 반환

## where()
# 조건절에 true의 index들을 반환

### Indexing & Slicing

# a = np.array([100., 101., 102., 103., 104.])

## a[x]

# a[0]
# a[4]
# a[-1]
# a[[0, 4]]

## a[::]
# a[0:3]
# a[0:3:1]
# a[0:3:2]
# a[2:5]
# a[:]
# a[::1]
# a[::2]
# a[::-1]
# a[::-2]
# a[-2::-2]

# a = np.array([[100., 101., 102.],
#              [200., 202., 203.]])

# a[0][0]
# a[0, 0]
# a[:,:]
# a[0,:]
# a[1,:]
# a[:,0]
# a[:,2][:, np.newaxis]
# a[:,[0, 2]]
# a[:, -1]
# a[:, ::-1]


### Linear Algebra

## *
## @
## dot()
## trace()
## inv()
## solve()
## eig()
## svd()
## fill_diagonal()


# exam

# a = np.array([[10, 20, 30],
#               [40, 50, 60],
#               [70, 80, 90]])
# b = np.linspace(1, 3, 3)[np.newaxis].repeat(3, axis=0).transpose()
# print(a * b)

## 브로드캐스팅
# b = np.linspace(1, 3, 3)[np.newaxis].transpose()
# print(a * b)  

## fromfunction 함수 이용 행렬생성
## setdiff1d 교집합제거
## random.randint
## random.rand
