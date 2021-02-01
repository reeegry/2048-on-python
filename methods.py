import random


# Create random number in grid
def random_number(GridClass):
    random_column = random.randint(0, 3)
    random_row = random.randint(0, 3)
    random_position = GridClass.massive[random_row][random_column]
    while random_position != 0:
        if random_position == 0:
            break
        else:
            random_column = random.randint(0, 3)
            random_row = random.randint(0, 3)
            random_position = GridClass.massive[random_row][random_column]

    if random.random() <= 0.75:
        number_to_insert = 2
    else:
        number_to_insert = 4

    GridClass.massive[random_row][random_column] = number_to_insert


# a special function to sort the list when moving down
def sort_row_for_move_down_and_right(row_to_sort):
    len_row_to_sort = len(row_to_sort)
    row_sorted = []
    for element in range(len_row_to_sort):
        if row_to_sort[element] == 0:
            row_sorted.insert(0, 0)
        else:
            row_sorted.append(row_to_sort[element])
    return row_sorted


# a special function to sort the list when moving down
def sort_row_for_move_up_and_left(row_to_sort):
    row_sorted = []
    zero_count = row_to_sort.count(0)
    if zero_count != 0:
        while zero_count != 0:
            for j in reversed(row_to_sort):
                if j == 0:
                    row_sorted.append(0)
                    del j
                    zero_count -= 1
                else:
                    row_sorted.insert(0, j)
        return row_sorted
    else:
        return row_to_sort


# I had to divide the 2 methods below because in the situation [x, x, x, x] it is not clear how to proceed
# If you can help me improve this part of the code, please commit
def multiplication_by_2_left(sorted_massive):
    for number in range(1, len(sorted_massive)):
        if sorted_massive[number - 1] == sorted_massive[number] and sorted_massive[number] != 0:
            sorted_massive[number] *= 2
            del sorted_massive[number - 1]
            sorted_massive.append(0)
            print(sorted_massive)

    return sorted_massive


# def multiplication_by_2_right(sorted_massive):
#     for number in range(1, len(sorted_massive)):
#         if sorted_massive[number - 1] == sorted_massive[number] and sorted_massive[number] != 0:
#             sorted_massive[number] *= 2
#             del sorted_massive[number - 1]
#             sorted_massive.insert(0, 0)
#             print(sorted_massive)
#
#     return sorted_massive

def multiplication_by_2_right(sorted_massive):
    for number in range(len(sorted_massive) - 1, 0, -1):
        if sorted_massive[number - 1] == sorted_massive[number] and sorted_massive[number] != 0:
            sorted_massive[number] *= 2
            del sorted_massive[number - 1]
            sorted_massive.insert(0, 0)
            print(sorted_massive)

    return sorted_massive


print(multiplication_by_2_right([0, 2, 2, 2]))
