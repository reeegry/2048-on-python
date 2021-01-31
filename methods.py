import random


def left_sort_in_mas(list_for_left_sort):
    # Count the number of zeros in the list
    zeroes_count = list_for_left_sort.count(0)
    # Create a list with the number of zeros zeroes_count
    zeroes_count_list = [0] * zeroes_count
    len_row = len(list_for_left_sort)
    while zeroes_count_list != list_for_left_sort[len_row - zeroes_count:]:
        first_zero_index = list_for_left_sort.index(0)
        del list_for_left_sort[first_zero_index]
        list_for_left_sort.append(0)
    return list_for_left_sort


# The function returns the index of the last element with the value number in the list row
def found_last_number(row_to_find_last_number, number):
    try:
        zero_index = row_to_find_last_number.index(number)
        number_count = row_to_find_last_number.count(number)
        iteration_count = 1
        while number_count != iteration_count:
            zero_index = row_to_find_last_number.index(number, zero_index + 1, len(row_to_find_last_number) - 1)
            iteration_count += 1
        return zero_index
    except ValueError:
        zero_index = -1
        return zero_index


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
def sort_row_for_move_down(row_to_sort):
    len_row_to_sort = len(row_to_sort)
    row_sorted = []
    for element in range(len_row_to_sort):
        print(row_to_sort)
        if row_to_sort[element] == 0:
            row_sorted.insert(0, 0)
        else:
            row_sorted.append(row_to_sort[element])
    return row_sorted


# a special function to sort the list when moving down
def sort_row_for_move_up(row_to_sort):
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