from typing import List

n = 4

def small_square(tu, line_list):
    counter = 0
    if  [tu[0], tu[1]] in line_list:
      counter += 1
    elif [tu[0], tu[0] + n] in line_list:
      counter += 1
    elif [tu[1], tu[1] + n] in line_list:
      counter += 1
    elif [tu[0] + n, tu[1] + n] in line_list:
      counter += 1
    return counter
    
def average_square(tu, line_list):
    counter = 0
    if [tu[0], tu[1]] and [tu[0] + 1, tu[1] + 1] and [tu[0],  tu[0] + n] and [tu[0] + n, tu[0] + n * 2] and [tu[0] + n * 2, tu[1] + n * 2] and [tu[0] + n * 2 + 1,  tu[1] + n * 2 + 1] and [tu[1] + 1,  tu[1] + n * 2 + 1] and [tu[1] + n +1,  tu[1] + n * 2 + 1] in line_list:
        counter += 1
    else:
        print([tu[0], tu[1]])
    return counter

def large_square(tu, line_list):
    pass

def checkio(lines_list: List[List[int]]) -> int:
    sq = 0
    for tu in lines_list:
        if small_square(tu, lines_list) == 4:
            sq += 1
            print(small_square())
        elif average_square(tu, lines_list) == 1:
            sq += 1
        elif large_square(tu, lines_list) == 12:
            pass
    """Return the quantity of squares"""
    return sq


if __name__ == '__main__':
    print("Example:")
    print(checkio([[1, 2], [2, 3], [5, 6], [6, 7], [5, 9], [9, 13], [13, 14], [14, 15], [7, 11], [11, 15]]))
#    print(checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
#                   [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
#                   [10, 14], [12, 16], [14, 15], [15, 16]]))
#
#    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
#                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
#                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
#    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
#                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
#                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
#    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
#    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
#    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
#                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
#    print("Coding complete? Click 'Check' to earn cool rewards!")
