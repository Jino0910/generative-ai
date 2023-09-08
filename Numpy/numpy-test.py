import numpy as np

print('1) np.array()')
print('\n')

# 1차원 배열
vec = np.array([1, 2, 3, 4, 5])
print(vec)
print("\n")

# 2차원 배열
mat = np.array([[10, 20, 30], [ 60, 70, 80]]) 
print(mat)
print("\n")

print('vec의 타입 :',type(vec))
print('mat의 타입 :',type(mat))
print("\n")

print('vec의 축의 개수 :',vec.ndim) # 축의 개수 출력
print('vec의 크기(shape) :',vec.shape) # 크기 출력
print("\n")

print('mat의 축의 개수 :',mat.ndim) # 축의 개수 출력
print('mat의 크기(shape) :',mat.shape) # 크기 출력
print("\n")

print('2) ndarray의 초기화')
print('\n')

# 모든 값이 0인 2x3 배열 생성.
zero_mat = np.zeros((2,3))
print(zero_mat)
print('\n')

# 모든 값이 1인 2x3 배열 생성.
one_mat = np.ones((2,3))
print(one_mat)
print('\n')

# 모든 값이 특정 상수인 배열 생성. 이 경우 7.
same_value_mat = np.full((2,2), 7)
print(same_value_mat)
print('\n')

# 대각선 값이 1이고 나머지 값이 0인 2차원 배열을 생성.
eye_mat = np.eye(3)
print(eye_mat)
print('\n')

# 임의의 값으로 채워진 배열 생성
random_mat = np.random.random((2,2)) # 임의의 값으로 채워진 배열 생성
print(random_mat)
print('\n')


print('3) np.arange()')
print('\n')

# 0부터 9까지
range_vec = np.arange(10)
print(range_vec)
print('\n')

# 1부터 9까지 +2씩 적용되는 범위
n = 2
range_n_step_vec = np.arange(1, 10, n)
print(range_n_step_vec)
print('\n')


print('4) np.reshape()')
print('\n')

reshape_mat = np.array(np.arange(30)).reshape((5,6))
print(reshape_mat)


print('5) Numpy 슬라이싱')
print('\n')

mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat)
print('\n')

# 첫번째 행 출력
slicing_mat = mat[0, :]
print(slicing_mat)
print('\n')

# 두번째 열 출력
slicing_mat = mat[:, 1]
print(slicing_mat)
print('\n')


print('6) Numpy 정수 인덱싱(integer indexing)')
print('\n')

mat = np.array([[1, 2], [4, 5], [7, 8]])
print(mat)
print('\n')

# 1행 0열의 원소
# => 0부터 카운트하므로 두번째 행 첫번째 열의 원소.
print(mat[1, 0])
print('\n')

# mat[[2행, 1행],[0열, 1열]]
# 각 행과 열의 쌍을 매칭하면 2행 0열, 1행 1열의 두 개의 원소.
indexing_mat = mat[[2, 1],[0, 1]]
print(indexing_mat)
print('\n')


print('7) Numpy 연산')
print('\n')

x = np.array([1,2,3])
y = np.array([4,5,6])

# result = np.add(x, y)와 동일.
result = x + y
print(result)
print('\n')

# result = np.subtract(x, y)와 동일.
result = x - y
print(result)
print('\n')

# result = np.multiply(result, x)와 동일.
result = result * x
print(result)
print('\n')

# result = np.divide(result, x)와 동일.
result = result / x
print(result)
print('\n')

mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
mat3 = np.dot(mat1, mat2)
print(mat3)
print('\n')