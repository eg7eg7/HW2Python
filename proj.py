from tkinter import *
from itertools import *



file_path = 'winners_test.txt'

''' function returns upper half of matrix if k=1. 
If k=0 function returns lower half of matrix. If k!=0 and k!=1 empty list will be returned'''


def half(matrix, k=1):
    return [
            row_list[row_index:len(row_list)] if k is 0
            else row_list[0:row_index + 1] if k is 1
            else []
            for row_index, row_list in enumerate(matrix)
    ]


# function decrypts only parts of the string that includes small letters of the english alphabet
def decrypt(string, key=3):
    new_string = ''
    size_alphabet = 26
    for ch in string:
        new_ch = ch
        if ord('a') <= ord(ch) <= ord('z'):
            new_ch = chr(ord('a') + (((ord(ch) - (key % size_alphabet)) - ord('a')) % size_alphabet))
        new_string += new_ch
    return new_string


def merge(iterable1, iterable2):
    res = []
    for x in iterable1:
        res.append(x)
    for x in iterable2:
        res.append(x)
    res = sorted(list(set(res)))
    for x in res:
        yield x
    return
    # raise StopIteration


def rank(file_name=file_path, how_to_rank='total'):
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

    while len(results_by_rank_type)>0:
        max_res = -1
        for index, results in enumerate(results_by_rank_type):
            if results_by_rank_type[index] > max_res:
                max_res = results_by_rank_type[index]
                index_to_yield = index
        res_to_yield = "\"{0}\":{1}".format(countries[index_to_yield], max_res)
        del(results_by_rank_type[index_to_yield])
        del(countries[index_to_yield])
        yield res_to_yield
    return


# procedure given in example
def divisable_by(n, limit):
    k = 0
    while k < limit:
        yield k
        k += n


class UserInterface:
    text_q1 = "Q1 (list comprehension):\n half function receives a matrix and a parameter k,\n matrix is manipulated according to parameter as shown in the example."
    text_q2 = "Q2 : decrypt function receives a text and a decryption key. returns the text after decryption"
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
    merge_param1 = divisable_by(4, 21)
    merge_param1_name = "divisable by"
    merge_param2 = [3, 4, 7, 8, 10, 11, 12, 16, 20]
    merge_param2_name = "list"
    rank_param1 = 'winners_test.txt'
    rank_param2 = "total"

    q_info_list = [text_q1, text_q2, text_q3, text_q4]
    q_param1_list = [half_param1, decrypt_param1, merge_param1, rank_param1]
    q_param2_list = [half_param2, decrypt_param2, merge_param2, rank_param2]
    list_of_funcs = [half, decrypt, merge, rank]
    default_q = 0
    current_option = default_q

    def __init__(self):
        dimension_x = 700
        dimension_y = 800

        self.root = Tk()
        self.root.geometry(str(dimension_x)+"x"+str(dimension_y))
        self.root.title(self.window_title)
        self.questions_frame = Frame(self.root)
        self.questions_frame.grid(row=0, column=0, sticky="sw")
        self.user_choice = StringVar(self.questions_frame)
        self.user_choice.set(self.q_list[self.current_option])
        self.option_menu = OptionMenu(self.questions_frame, self.user_choice, *self.q_list, command=self.refresh_frame)
        self.guideLabel = Label(self.questions_frame, text=self.guide_text)
        self.guideLabel.grid(row=0, column=0)
        self.option_menu.grid(row=0, column=1)

        self.q_frame = Frame(self.root)
        self.q_value1_frame = Frame(self.q_frame, width=dimension_x, height=dimension_y/4)
        self.q_value2_frame = Frame(self.q_frame, width=dimension_x, height=dimension_y/4)
        self.q_value1_frame.grid_propagate(False)
        self.q_value2_frame.grid_propagate(False)

        self.q_frame.grid(row=1, column=0, columnspan=2, sticky="sw")
        self.q_value1_frame.grid(row=3, column=0, columnspan=2, sticky="sw")
        self.q_value2_frame.grid(row=5, column=0, columnspan=2, sticky="sw")
        self.q_exec_button = Button(self.q_frame, text="Execute", fg="red", command=self.execute_pressed)
        # self.q_edit_button = Button(self.q_frame, text="Edit question parameters", fg="purple", command=self.edit_param)
        self.q_info_label = Label(self.q_frame, text=self.q_info_list[self.current_option], justify=LEFT)
        self.q_info_label.grid(row=0, column=0)

        self.text_area1 = Text(self.q_value1_frame)
        self.text_area2 = Text(self.q_value2_frame)

        self.q_exec_button.grid(row=1, column=0, sticky="sw")
        # self.q_edit_button.grid(row=1, column=1, sticky="w")
        self.default_val1_lbl = Label(self.q_frame, text="Value 1:")
        self.default_val2_lbl = Label(self.q_frame, text="Value 2:")
        # TODO Clean comments
        self.default_val1_lbl.grid(row=2,column=0,sticky="sw",pady=5)
        self.default_val2_lbl.grid(row=4, column=0, sticky="sw",pady=5)

        self.text_area1.grid(row=3, column=0)
        self.text_area2.grid(row=5, column=0)
        self.refresh_frame() #for first text area values insert


        self.function_output = Frame(self.root)
        self.function_output.grid(row=3, column=0, sticky="sw")
        self.function_output_label = Label(self.function_output, justify=LEFT)
        self.function_output_label.grid(row=0, column=0)

        self.info_frame = Frame(self.root)
        self.info_frame.grid(row=4, column=0, sticky="sw")
        self.info_label = Label(self.info_frame, text=self.text_info, justify=LEFT)
        self.info_label.grid(row=0, column=0)


        self.root.mainloop()

    #string of type "1 2 3 \n 4 5 'stam'" will be converted to 2d list: [[1, 2, 3], [4, 5, 'stam']]
    def str_to_matrix(self, str):
        matrix = []
        splt = str.splitlines()
        for items in splt:
            sublist = []
            for values in items.split():
                sublist.append(values)
            matrix.append(sublist)
        return matrix

    def matrix_to_str(self, matrix, param=1):
        s = ""
        for index, sub_lst in enumerate(matrix):
            if param == 0:
                s += ("".rjust(10))*index
            for value in sub_lst:
                s += str(value).ljust(10)
            s += "\n"
        return s

    def refresh_frame(self, choice=q_list[0]):
        self.current_option = self.q_list.index(choice)
        self.q_info_label.config(text=self.q_info_list[self.current_option])

        #empty text area before inserting default values
        self.text_area1.delete('1.0',END)
        self.text_area2.delete('1.0',END)

        #insert default values to text areas
        if self.current_option == 0: param1 = self.matrix_to_str(self.q_param1_list[self.current_option])
        else: param1 = self.q_param1_list[self.current_option]
        param2 = self.q_param2_list[self.current_option]
        self.text_area1.insert('1.0', param1)
        self.text_area2.insert('1.0', param2)


    def execute_pressed(self):
        # TODO make matrix look more like a matrix
        param1 = self.text_area1.get('1.0', END)
        param2 = self.text_area2.get('1.0', END)

        if self.current_option == 0:
            param1 = self.str_to_matrix(param1)

        if 0 <= self.current_option <= 2:
            param2 = int(param2)

        if self.current_option == 3:
            param1 = param1.splitlines()[0]
            param2 = param2.splitlines()[0]

        func = self.list_of_funcs[self.current_option]

        if self.current_option == 0:
            function_output = self.matrix_to_str(func(param1, param2), param2)

        elif self.current_option == 1:
            function_output = str(func(param1, param2))

        elif self.current_option == 2 or self.current_option == 3:
            function_output = str(list(islice(func(param1, param2), 0, None)))

        string = "Result:\n"+function_output

        # if self.current_option == 0:
        #     function_output = half(self.half_param1, self.half_param2)
        #     string += ("half function with\nmatrix:" + param1 + "\nk: " + param2 + "\nresults with :\n\n" + str(function_output) + "\n\n")
        # elif self.current_option == 1:
        #     function_output = decrypt(self.decrypt_param1, self.decrypt_param2)
        #     string += ("decrypt function with\nstring: " + param1 + "\ndecryption key: " + param2 + "\n\nresults with :\n\n" + function_output + "\n\n")
        # elif self.current_option == 2:
        #     function_output = list(islice(merge(self.merge_param1, [2, 3, 7, 10, 11]), 9))
        #     string += ("merge function with\n iterable1 is: " + param1 + "\niterable2 is: " + param2  + "\n\nresults with :\n\n" + str(function_output) + "\n\n")
        # elif self.current_option == 3:
        #     function_output = list(islice(rank(self.rank_param1, self.rank_param2), 3))
        #     string += ("rank function with\n filename: " + param1 + "\nby: " + param2 + "\n\nresults with :\n\n" + str(function_output) + "\n\n")
        self.function_output_label.config(text=string)

    # def edit_param(self):
    #     self.q_edit_pressed = True
    #
    #     self.q_param1_user = self.text_area1.get('1.0','end')
    #     self.q_param2_user = self.text_area2.get('1.0','end')

if __name__ == "__main__":
    UserInterface()
