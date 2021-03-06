# Students:
# 1) Full Name: Eden Dupont. ID: 204808596
# 2) Full Name: Daniil Rolnik. ID: 334018009

from tkinter import *
from itertools import *
import unittest
import logging

'''Logs will be written in file'''
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
logger_file_name = 'Python_HW2Python_Logs.txt'
file_handler = logging.FileHandler(logger_file_name, mode='a')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

file_path = 'winners_test.txt'



''' function returns upper half of matrix if k=1. 
If k=0 function returns lower half of matrix. If k!=0 and k!=1 empty list will be returned'''
def half(matrix, k=1):
    logger.debug(f"Half: matrix = {str(matrix)}, k = {k} ")

    result = [
        row_list[row_index:len(row_list)] if k is 0
        else row_list[0:row_index + 1] if k is 1
        else []
        for row_index, row_list in enumerate(matrix)
    ]

    logger.debug(f"Half result: {str(result)}")
    return result

'''Function decrypts only parts of the string that includes small letters of the english alphabet'''
def decrypt(string, key=3):
    logger.debug(f"Decrypt: string = {string}, key = {key}")
    new_string = ''
    size_alphabet = 26
    for ch in string:
        new_ch = ch
        if ord('a') <= ord(ch) <= ord('z'):
            new_ch = chr(ord('a') + (((ord(ch) - (key % size_alphabet)) - ord('a')) % size_alphabet))
        new_string += new_ch
    logger.debug(f"Decrypt result: {new_string}")
    return new_string

'''Generator function takes two iterables aand returns next value from merged and sorted list'''
def merge(iterable1, iterable2):
    logger.debug(f"Merge: iterable1 = {str(iterable1)}, iterable2 = {str(iterable2)}")
    res = []
    for x in iterable1:
        res.append(x)
    for x in iterable2:
        res.append(x)
    res = sorted(list(set(res)))
    logger.debug(f"merged iterables to list:{res}")
    for x in res:
        logger.debug(f"Merge yield: {x}")
        yield x
    logger.debug(f"Merge: yield finished")
    return

'''Generator function gets file name of file including enumeration of countries and they results at olympic games 
(how many medals of different type and by what parameter to rank countries. 
Function returns next country with highest rank by defined parameter'''
def rank(file_name=file_path, how_to_rank='total'):
    logger.debug(f"Rank: file_name = {file_name}, hot_to_rank={how_to_rank}")
    f = open(file_name)
    (countries, gold, silver, bronze, results_by_rank_type, index_to_yield, res_to_yield) = ([], [], [],[], [],  0, " ")
    (gold_weight, silver_weight, bronze_weight) = (3, 2, 1)

    for index, line in enumerate(f.readlines()):
        line_lst = line.split()
        (countries.append(line_lst[0]), gold.append(line_lst[1]), silver.append(line_lst[2]), bronze.append(line_lst[3]))
    f.close()

    results_by_rank_type = [
        (int(gold[index]) + int(silver[index]) + int(bronze[index])) if how_to_rank == 'total'
        else (int(gold[index])*gold_weight + int(silver[index])*silver_weight + int(bronze[index])*bronze_weight) if how_to_rank == 'weighted'
        else (int(gold[index])) if how_to_rank == 'gold'
        else (int(silver[index])) if how_to_rank == 'silver'
        else (int(bronze[index])) if how_to_rank == 'arad'
        else -1
        for index in range(len(countries))
    ]

    while len(results_by_rank_type) > 0:
        max_res = -1
        for index, results in enumerate(results_by_rank_type):
            if results_by_rank_type[index] > max_res:
                max_res = results_by_rank_type[index]
                index_to_yield = index
        res_to_yield = f"{countries[index_to_yield]}:{max_res}"
        del(results_by_rank_type[index_to_yield])
        del(countries[index_to_yield])
        logger.debug(f"Rank yield: {res_to_yield}")
        yield res_to_yield
    logger.debug(f"Rank: yield finished")
    return


''' procedure given in example '''
def divisable_by(n, limit):
    logger.debug(f"Divisable_by: n = {n}, limit = {limit}")
    k = 0
    while k < limit:
        yield k
        k += n
    return


'''lists in list matrix will be turned into string representation of matrix'''
def matrix_to_str(matrix, param=1):
    logger.debug(f"Matrix_to_str: matrix = {str(matrix)}, param = {param}")
    s = ""
    for index, sub_lst in enumerate(matrix):
        space_value = 10
        if param == 0:
            s += ("".rjust(space_value))*index
        for value in sub_lst:
            s += str(value).ljust(space_value)
        s += "\n"
    logger.debug(f"Matrix_to_str result: \n{s}")
    return s


''' String of type "1 2 3 \n 4 5 'stam'" will be converted to 2d list: [[1, 2, 3], [4, 5, 'stam']]'''
def str_to_matrix(matrix_as_string):
    logger.debug(f"Str_to_matrix: matrix_as_string = {matrix_as_string}")
    matrix = []
    splt = matrix_as_string.splitlines()
    for items in splt:
        sublist = []
        for values in items.split():
            sublist.append(values)
        matrix.append(sublist)
    logger.debug(f"Str_to_matrix result: str(matrix) ")
    return matrix


''' Function designed to convert a string representation of a list of integers into a list,
if the string contains non-integer values, returns an empty list'''
def str_to_list(string):
    logger.debug(f"str_to_list: converting the string {string} to a list of type int")
    li = []
    for x in string.split():
        try:
            li.append(int(x))
        except ValueError:
            li = []
            logger.debug(f"could not convert {x} into int, returning an empty list")
            return li
    return li

'''All Gui definitions and run Gui'''
class UserInterface:
    text_q1 = "Q1 (list comprehension):\n half function receives a matrix and a parameter k,\n matrix is manipulated according to parameter as shown in the example."
    text_q2 = "Q2 : decrypt function receives a text and a decryption key.\n returns the text after decryption"
    text_q3 = "Q3 : the generator function merge receives two iterable lists,\n calling the function each time returns values from both iterables in an ascending order"
    text_q4 = "Q4 : generator function rank function reads from a text file information\n of countries and their winnings in the olympic games.\n each call returns the name of winning countries in a descending order,\n sorted by parameter (total, weighted, gold, silver, arad)."
    text_info = "Eden Dupont {204808596}, Daniil Rolnik {334018009}"
    window_title = "Python2 Homework"
    guide_text = "Choose a question from the drop-down menu:"
    option1 = "Question 1 - half"
    option2 = "Question 2 - decrypt"
    option3 = "Question 3 - merge"
    option4 = "Question 4 - rank"
    q_list = [option1, option2, option3, option4]

    half_param1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]
    half_param1_to_insert = "1 2 3 4 5\n6 7 8 9 'spam'\n11 12 13 14 15\n16 'stam' 18 19 20"
    half_param2 = 0
    decrypt_param1 = "vrorqjdqgwkdqnviruwkhilvk"
    decrypt_param2 = 3
    merge_param1 = list(islice(divisable_by(14, 200), None))
    merge_param2 = list(islice(divisable_by(30, 200), None))
    rank_param1 = 'winners_test.txt'
    rank_param2 = "total"

    q_info_list = [text_q1, text_q2, text_q3, text_q4]
    q_param1_list = [half_param1, decrypt_param1, merge_param1, rank_param1]
    q_param2_list = [half_param2, decrypt_param2, merge_param2, rank_param2]
    list_of_funcs = [half, decrypt, merge, rank]
    default_q = 0
    current_option = default_q

    def __init__(self):
        logger.debug("Gui started")
        dimension_x = 500
        dimension_y = 400

        self.root = Tk()
        self.root.geometry(str(dimension_x)+"x"+str(dimension_y))
        self.root.title(self.window_title)
        self.questions_frame = Frame(self.root)
        self.questions_frame.grid(row=0, column=0, sticky="nw")
        self.user_choice = StringVar(self.questions_frame)
        self.user_choice.set(self.q_list[self.current_option])
        self.option_menu = OptionMenu(self.questions_frame, self.user_choice, *self.q_list, command=self.refresh_frame)
        self.guideLabel = Label(self.questions_frame, text=self.guide_text)
        self.guideLabel.grid(row=0, column=0)
        self.option_menu.grid(row=0, column=1)

        self.q_frame = Frame(self.root)
        self.q_value1_frame = Frame(self.q_frame, width=dimension_x, height=dimension_y/8)
        self.q_value2_frame = Frame(self.q_frame, width=dimension_x, height=dimension_y/8)
        self.q_value1_frame.grid_propagate(False)
        self.q_value2_frame.grid_propagate(False)

        self.q_frame.grid(row=1, column=0, columnspan=2, sticky="sw")
        self.q_value1_frame.grid(row=3, column=0, columnspan=2, sticky="sw")
        self.q_value2_frame.grid(row=5, column=0, columnspan=2, sticky="sw")
        self.q_exec_button = Button(self.q_frame, text="Execute", fg="red", command=self.execute_pressed)
        self.q_info_label = Label(self.q_frame, text=self.q_info_list[self.current_option], justify=LEFT)
        self.q_info_label.grid(row=0, column=0)

        self.text_area1 = Text(self.q_value1_frame)
        self.text_area2 = Text(self.q_value2_frame)

        self.q_exec_button.grid(row=1, column=0, sticky="sw")
        self.default_val1_lbl = Label(self.q_frame, text="Value 1:")
        self.default_val2_lbl = Label(self.q_frame, text="Value 2:")
        self.default_val1_lbl.grid(row=2,column=0,sticky="sw", pady=5)
        self.default_val2_lbl.grid(row=4, column=0, sticky="sw", pady=5)

        self.text_area1.grid(row=3, column=0)
        self.text_area2.grid(row=5, column=0)

        # for first text area values insert
        self.function_output = Frame(self.root)
        self.function_output.grid(row=3, column=0, sticky="sw")
        self.function_output_label = Label(self.function_output, justify=LEFT)
        self.function_output_label.grid(row=0, column=0)

        self.info_frame = Frame(self.root)
        self.info_frame.grid(row=4, column=0, sticky="sw")
        self.info_label = Label(self.info_frame, text=self.text_info, justify=LEFT)
        self.info_label.grid(row=0, column=0)

        self.refresh_frame()
        self.root.mainloop()


    '''Frame refreshed every time another question chosen'''
    def refresh_frame(self, choice=None):
        if choice is None:
            choice = self.q_list[self.current_option]
        logger.debug(f"Gui refresh_frame: choice = {choice}")
        self.current_option = self.q_list.index(choice)
        self.q_info_label.config(text=self.q_info_list[self.current_option])

        # empty text area before inserting default values
        self.text_area1.delete('1.0', END)
        self.text_area2.delete('1.0', END)

        # insert default values to text areas
        if self.current_option == 0:
            param1 = matrix_to_str(self.q_param1_list[self.current_option])
        else:
            param1 = self.q_param1_list[self.current_option]

        param2 = self.q_param2_list[self.current_option]
        self.text_area1.insert('1.0', param1)
        self.text_area2.insert('1.0', param2)

        self.function_output_label.config(text="")

        logger.info("Gui refresh_frame finished")
        logger.debug(f"text_area1 data = {self.text_area1.get('1.0', END)}")
        logger.debug(f"text_area2 data = {self.text_area2.get('1.0', END)}")


    '''Function called if Execute button pressed'''
    def execute_pressed(self):
        logger.info("Execute_pressed (execution button pressed)")
        logger.debug(f"text_area1 data = {self.text_area1.get('1.0', END)}")
        logger.debug(f"text_area2 data = {self.text_area2.get('1.0', END)}")
        param1 = self.text_area1.get('1.0', END)
        param2 = self.text_area2.get('1.0', END)
        logger.info(f"Executing option{self.current_option}")
        func = self.list_of_funcs[self.current_option]

        if self.current_option == 0:
            param1 = str_to_matrix(param1)
            function_output = matrix_to_str(func(param1, int(param2)), int(param2))
        elif self.current_option == 1:
            function_output = str(func(param1, int(param2)))

        elif self.current_option == 2:
            param1 = str_to_list(param1)
            param2 = str_to_list(param2)
            function_output = str(list(islice(func(param1, param2), 0, None)))

        elif self.current_option == 3:
            param1 = param1.splitlines()[0]
            param2 = param2.splitlines()[0]
            function_output = str(list(islice(func(param1, param2), 0, None)))

        res = "Result:\n"+function_output
        self.function_output_label.config(text=res)
        logger.debug(f"Execute_pressed result: {res}")

class Test_HW(unittest.TestCase):

    def test_half(self):
        self.assertEqual(half([], 0), [])
        self.assertEqual(half([], 1), [])
        self.assertEqual(half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]]),
                         [[1], [6, 7], [11, 12, 13], [16, "stam", 18, 19]])
        self.assertEqual(
            half([[1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]], 0),
            [[1, 2, 3, 4, 5], [7, 8, 9, "spam"], [13, 14, 15], [19, 20]])
        self.assertEqual(half(
            [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [6, 7, 8, 9, "spam"], [11, 12, 13, 14, 15], [16, "stam", 18, 19, 20]],
            0), [[1, 2, 3, 4, 5], [2, 3, 4, 5], [8, 9, "spam"], [14, 15], [20]])

    def test_decrypt(self):
        self.assertEqual(decrypt("vrorqjdqgwkdqnviruwkhilvk"), "solongandthanksforthefish")
        self.assertEqual(decrypt("vsdp "), "spam ")
        self.assertEqual(decrypt("a"), "x")
        self.assertEqual(decrypt("a", 1), "z")
        self.assertEqual(decrypt("a", 26), "a")
        self.assertEqual(decrypt("a", 52), "a")
        self.assertEqual(decrypt("a", 0), "a")

    def test_merge(self):
        g = divisable_by(4, 21)
        my_merge_iter = merge(g, [2, 3, 7, 10, 11])
        self.assertEqual(next(my_merge_iter), 0)
        self.assertEqual(next(my_merge_iter), 2)
        self.assertEqual(list(islice(my_merge_iter, 9)), [3, 4, 7, 8, 10, 11, 12, 16, 20])

        g = divisable_by(3, 35)
        my_merge_iter = merge(g, [2, 5, 8, 10])
        self.assertEqual(list(islice(my_merge_iter, 8)), [0, 2, 3, 5, 6, 8, 9, 10])

    def test_rank(self):
        file_name = 'winners_test.txt'
        self.assertEqual(list(islice(rank(file_name, 'total'), 3)), ["USA:2521", "Great-Britain:847", "Israel:9"])
        self.assertEqual(list(islice(rank(file_name, 'weighted'), 3)), ["USA:5359", "Great-Britain:1668", "Israel:12"])
        self.assertEqual(list(islice(rank(file_name, 'gold'), 3)), ["USA:1022", "Great-Britain:263", "Israel:1"])
        self.assertEqual(list(islice(rank(file_name, 'silver'), 3)), ["USA:794", "Great-Britain:295", "Israel:1"])
        self.assertEqual(list(islice(rank(file_name, 'arad'), 3)), ["USA:705", "Great-Britain:289", "Israel:7"])
        self.assertEqual(list(islice(rank(file_name, 'svsd'), 3)), ["Israel:-1", "USA:-1", "Great-Britain:-1"])

if __name__ == "__main__":
    UserInterface()
    unittest.main(exit=False)

