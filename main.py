from functools import wraps


results_store = []
func_names_store = []
name_result_store = {'name': [], 'result': []}


TEMPLATES = {
    'results_list': (
        'The first decorator takes functions and returns results '
        'of these function. So, here they are: \n\n{answers}'
    ),
    'functions_names': (
        'The second decorator takes functions and returns functions names. '
        'So, here they are: \n\n{names}\n'
    ),
    'name_and_result': (
        'But some functions I\'ve decorated by first and second decorators together. '
        'And here you can see the result: \n\nname:\t\t\tresult:\n{res}'
    )
}
    

def save_result(store_list):
    """
    decorator
    appends function result to special buffer
    """
    def _wrapper(func):
        @wraps(func)
        def _executor(*args):
            res = func(*args)
            store_list.append(res)
            return res
        return _executor
    return _wrapper

def save_function_name(names_list):
    """
    decorator
    appends function name to special buffer
    """
    def _dec(func):
        @wraps(func)
        def _exec(*args):
            names_list.append(func.__name__) 
            return func(*args)  
        return _exec
    return _dec


@save_result(results_store)
def absolute_value(num):
    """
    returns the absulute value of a number

    5 -> 5
    -7 -> 7
    """
    return abs(num)

@save_result(results_store)
def whole_number(float_num):
    """
    returns the whole part of a number 
    
    (float -> int)

    2.3 -> 2
    101.9 -> 101
    """
    return int(float_num)

@save_result(results_store)
def times_two(num):
    """
    returns the number multiplied by two 
    
    (int -> int)

    2 -> 4
    700 -> 1400
    """
    return num * 2

@save_result(results_store)
def string_length(string):
    """
    returns the length of string 
    
    (str -> int)
    
    abcd -> 4
    hello -> 5
    """
    return len(string)

@save_result(results_store)
def num_of_words(sentence):
    """
    returns the length of sentence in words 
    
    (str -> int)

    The Matrix -> 2
    The truth is out there -> 5
    """
    return len(sentence.split())

@save_result(results_store)
def first_word(sentence):
    """
    returns first word in sentence 
    
    (str -> str)

    Game of Thrones -> Game
    Hello world -> Hello
    """
    return sentence.split()[0]

@save_result(results_store)
def unique_letters(string):
    """
    return the number of unique letters (excluding register) 
    
    (str -> int)

    abcA -> 3
    ASDFasdfrt -> 6
    """
    return len(set(string.lower()))

@save_function_name(func_names_store)
def vowels_num(string):
    """
    returns the number of vowel letters 
    
    (str -> int)

    abbAc -> 2
    Hello, hello -> 4
    """
    pattern = 'eyuioa'
    return (len([letter for letter in string.lower() if letter in pattern]))

@save_function_name(func_names_store)
def is_palindrome(string):
    """
    returns whether the word is a palindrome 
    
    (str -> bool)

    abba -> True
    abbat -> False
    detartrated -> True
    """
    return string == string[::-1]

@save_function_name(func_names_store)
def repeated_letters(string):
    """
    returns if string contains only letters and contains repeated letters 
    
    (str -> bool)

    hello -> True
    world -> False
    Happen -> True
    88f -> False
    """
    if string.isalpha():
        lower_string = string.lower()
        for i in range(len(lower_string)-1):
            if lower_string[i] == lower_string[i+1]:
                return True
    return False

@save_function_name(func_names_store)
def pow_two_or_three(num):
    """
    returns num to the power of 2 if number is even
    or num to the power of 3 if number is odd 
    
    (int -> int)

    2 -> 4
    5 -> 125
    """
    if num % 2 == 0:
        return num ** 2
    return num ** 3

@save_function_name(func_names_store)
def list_elem_sum(nums_list):
    """
    returns sum of all numbers in list 
    
    (list -> int)
    """
    return sum(nums_list)

@save_function_name(func_names_store)
def max_element(nums_list):
    """
    returns the biggest element in list 
    
    (list -> int)
    """
    return max(nums_list)

@save_function_name(func_names_store)
def low_letters(string):
    """
    returns string where all letters are lower 
    
    (str -> str)
    """
    return string.lower()

@save_function_name(name_result_store['name'])
@save_result(name_result_store['result'])
def genome_pair(genome):
    """
    return genome pair 
    
    (str -> str)

    AGT -> TCA
    TTTATGCCC -> AAATACGGG
    """
    pairs = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    res = ''
    for code in genome:
        res = res + pairs[code]
    return res

@save_function_name(name_result_store['name'])
@save_result(name_result_store['result'])
def num_of_letter(letter):
    """
    return number of letter in an alphabet (including register) 
    
    (str -> int)
    """
    return ord(letter) - 96

@save_function_name(name_result_store['name'])
@save_result(name_result_store['result'])
def to_binary(num):
    """
    returns number in a binary system 
    
    (int -> str)

    3 -> 11
    10 -> 1010
    """
    return bin(num)[2:]

@save_function_name(name_result_store['name'])
@save_result(name_result_store['result'])
def ones_num_binary(num):
    """
    returns the number of ones in its binary notation 
    
    (int -> int)

    2 -> 1
    3 -> 2
    100 -> 3
    """
    return bin(num)[2:].count('1')

@save_function_name(name_result_store['name'])
@save_result(name_result_store['result'])
def censored_string(string):
    """
    returns string where all elements was replased to asterisk 
    
    (str -> str)

    hello -> *****
    Hi, Friend -> **********
    """
    return '*' * len(string)

@save_function_name(name_result_store['name'])
@save_result(name_result_store['result'])
def zero_matrix(num):
    """ returns zero matrix of size num x num 
    
    (int -> list of lists)

    2 -> [[0, 0], [0, 0]]
    3 -> [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    return [[0 for i in range(num)] for j in range(num)]

@save_function_name(name_result_store['name'])
@save_result(name_result_store['result'])
def identity_matrix(num):
    """ returns identity matrix of size num x num 
    
    (int -> list of lists)

    2 -> [[1, 0], [0, 1]]
    3 -> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    res_matrix = [[0 for i in range(num)] for j in range(num)]
    for i in range(len(res_matrix)):
        for j in range(len(res_matrix[i])):
            if i == j:
                res_matrix[i][j] = 1
    return res_matrix


def show():
    print(TEMPLATES['results_list'].format(
        answers='\n'.join(str(i) for i in results_store)), 
        end="\n\n"
        )

    print(TEMPLATES['functions_names'].format(
        names='\n'.join(func_names_store))
        ) 

    res = ''
    for i, j in zip(name_result_store['name'], name_result_store['result']):
        res = '{}{}\t\t{}\n'.format(res, i, str(j))
    print(TEMPLATES['name_and_result'].format(res=res))


def main():
    absolute_value(-42)
    whole_number(123.456)
    times_two(21)
    string_length('Hello, hello!')
    num_of_words('The truth is out there')
    first_word('One two three')
    unique_letters('qweasjndjkeqewqwqw')
    vowels_num('qwertyuiop')
    is_palindrome('step on no pets')
    repeated_letters('Hello')
    pow_two_or_three(54)
    list_elem_sum([12, 54, 2, -12, 59])
    max_element([342, 5, 10000, 1, 34])
    low_letters('Hello, in future all my LETTERS will BE LOWER')
    genome_pair('TTTATGCCC')
    num_of_letter('g')
    to_binary(1024)
    ones_num_binary(42)
    censored_string('I\'ll be censored')
    zero_matrix(3)
    identity_matrix(6)
    show()

if __name__ == '__main__':
    main()
