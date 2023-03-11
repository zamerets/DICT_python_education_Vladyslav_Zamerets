import copy

global rows_1, rows_2, columns_1, columns_2, end_program
end_program = False

matrix_1 = []
matrix_2 = []


# создание и заполнение 2х матриц данными
def mat_create(a, b, matrix):
    matrix = []
    for i in range(a):
        matrix.append([0] * b)
    for i in range(0, a):
        row = input().split()[:b]
        for j in range(0, b):
            matrix[i][j] = float(row[j])
    return matrix


# вывод матрицы
def mat_print(matrix):
    lengthI = len(matrix)
    count = 0
    for element in matrix:
        count += len(element)
    lengthJ = count / lengthI
    for i in range(lengthI):
        for j in range(int(lengthJ)):
            isInt = float(matrix[i][j]).is_integer()
            if isInt:
                matrix[i][j] = int(matrix[i][j])
            else:
                matrix[i][j] = round(matrix[i][j], 3)
    for i in matrix:
        print(*i)


def create_matrix(matrix_1):
    global rows_1, columns_1
    enter_rows = input().split(' ')
    if len(enter_rows) < 2:
        print("impossible")
        menu()
    rows_1, columns_1 = int(enter_rows[0]), int(enter_rows[1])
    matrix_1 = mat_create(rows_1, columns_1, matrix_1)
    return matrix_1


# вторая матрица является элементом прибавления и умножения
def second_matrix_create(matrix_2):
    global rows_2, columns_2
    enter_rows = input().split(' ')
    if len(enter_rows) < 2:
        print("impossible")
        menu()
    rows_2, columns_2 = int(enter_rows[0]), int(enter_rows[1])
    matrix_2 = mat_create(rows_2, columns_2, matrix_2)
    return matrix_2


# функция вызывает последовательность функций связанных с прибавлением матриц
def matrix_add(matrix_1, matrix_2):
    if rows_1 == rows_2 and columns_1 == columns_2:
        matrix_sum = []
        for i in range(rows_1):
            matrix_sum.append([0] * columns_1)
        for i in range(rows_1):
            for j in range(columns_1):
                matrix_1[i][j] = matrix_1[i][j] + matrix_2[i][j]
        print("Sum: ")
        mat_print(matrix_1)
    else:
        print("This operation is impossible!")
    return matrix_1, matrix_2


# умножить на константу
def const_multiply(matrix_1, multiply_constant):
    matrix_multi_by_const = []
    for i in range(rows_1):
        matrix_multi_by_const.append([0] * columns_1)
    for i in range(rows_1):
        for j in range(columns_1):
            matrix_multi_by_const[i][j] = matrix_1[i][j] * multiply_constant
    return matrix_multi_by_const


def multi_matrix(matrix_1, matrix_2):
    if rows_2 == columns_1:
        length = len(matrix_1)
        result_matrix = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    result_matrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
    print("Multiplied: ")
    mat_print(result_matrix)

def transpose_main(matrix_1):
    length = len(matrix_1)
    result_matrix = [[0 for i in range(length)] for i in range(length)]  # пустая матрица
    for i in range(length):
        for j in range(length):
            result_matrix[i][j] = matrix_1[j][i]
    return result_matrix


def matrix_transpose(matrix_1):
    key = input('''
    1. Main diagonal 
    2. Side diagonal 
    3. Vertical line 
    4. Horizontal line \n''')
    match key:
        case "1":
            matrix_1 = create_matrix(matrix_1)
            mat_print(transpose_main(matrix_1))
        case "2":
            matrix_1 = create_matrix(matrix_1)
            length = len(matrix_1)
            result_matrix = [[0 for i in range(length)] for i in range(length)]  # пустая матрица
            for i in range(length):
                for j in range(length):
                    result_matrix[i][j] = matrix_1[-j - 1][-i - 1]
            mat_print(result_matrix)
        case "3":
            matrix_1 = create_matrix(matrix_1)
            length = len(matrix_1)
            result_matrix = [[0 for i in range(length)] for i in range(length)]  # пустая матрица
            for i in range(length):
                for j in range(length):
                    result_matrix[i][j] = matrix_1[i][-j - 1]
            mat_print(result_matrix)
        case "4":
            matrix_1 = create_matrix(matrix_1)
            length = len(matrix_1)
            result_matrix = [[0 for i in range(length)] for i in range(length)]  # пустая матрица
            for i in range(length):
                for j in range(length):
                    result_matrix[i][j] = matrix_1[-i - 1][j]
            mat_print(result_matrix)


def det_counter(matrix_1):
    def minor(matrix_1, i, j):
        M = copy.deepcopy(matrix_1)  # копирование!
        del M[i]
        for i in range(len(matrix_1[0]) - 1):
            del M[i][j]
        return M

    def det(matrix_1):
        m = len(matrix_1)
        n = len(matrix_1[0])
        if m != n:
            return None
        if n == 1:
            return matrix_1[0][0]
        signum = 1
        determinant = 0
        # разложение по первой строке
        for j in range(n):
            if det(minor(matrix_1, 0, j)) is None:
                determinant += 0
                signum *= -1
            else:
                determinant += matrix_1[0][j] * signum * det(minor(matrix_1, 0, j))
                signum *= -1
        return determinant

    return det(matrix_1)


def reverse_matrix(matrix_1):
    if len(matrix_1) != len(matrix_1[0]):
        print('Non-square matrix!!!')
        return None
    det = det_counter(matrix_1)
    if det == 0:
        print('Reverse matrix for matrix with zero determinant doesn`t exist')
        return None
    transpose_matrix = transpose_main(matrix_1)
    reverse_matrix = [[0 for j in range(len(transpose_matrix))] for i in range(len(transpose_matrix[0]))]
    for i in range(len(transpose_matrix)):
        for j in range(len(transpose_matrix[0])):
            minor = [[0 for j in range(len(transpose_matrix) - 1)] for i in range(len(transpose_matrix[0]) - 1)]
            row_shift = 0
            for k in range(len(transpose_matrix)):
                if k == i:
                    row_shift = 1
                    continue
                column_shift = 0
                for p in range(len(transpose_matrix[0])):
                    if p == j:
                        column_shift = 1
                        continue
                    minor[(k - row_shift)][(p - column_shift)] = transpose_matrix[k][p]
            reverse_matrix[i][j] = ((-1) ** (i + j)) * det_counter(minor)
    return const_multiply(reverse_matrix, 1/det)



def menu():
    print('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrix
4. Transpose matix
5. Determinant 
6. Reverse
0. Exit \n''')
    key = input("Your choice: ")
    match key:
        case "1":
            matrix_1 = []
            matrix_1 = create_matrix(matrix_1)
            matrix_2 = []
            matrix_2 = second_matrix_create(matrix_2)
            matrix_add(matrix_1, matrix_2)
        case "2":
            matrix_1 = []
            matrix_1 = create_matrix(matrix_1)
            multiply_constant = float(input())
            mat_print(const_multiply(matrix_1, multiply_constant))
        case "3":
            matrix_1 = []
            matrix_1 = create_matrix(matrix_1)
            matrix_2 = []
            matrix_2 = second_matrix_create(matrix_2)
            multi_matrix(matrix_1, matrix_2)
        case "4":
            matrix_1 = []
            matrix_transpose(matrix_1)
        case "5":
            matrix_1 = []
            matrix_1 = create_matrix(matrix_1)
            print("Determinant is:", det_counter(matrix_1))
        case "6":
            matrix_1 = []
            matrix_1 = create_matrix(matrix_1)
            mat_print(reverse_matrix(matrix_1))
        case "0":
            global end_program
            end_program = True
            return


while not end_program:
    menu()
