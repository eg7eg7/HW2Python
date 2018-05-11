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
    res = sorted(res)
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
    half_param2 = 1
    decrypt_param1 = "vrorqjdqgwkdqnviruwkhilvk"
    decrypt_param2 = 3
    merge_param1 = divisable_by(4, 21)
    merge_param1_name = "divisable by"
    merge_param2 = [3, 4, 7, 8, 10, 11, 12, 16, 20]
    merge_param2_name = "list"
    rank_param1 = 'winners_test.txt'
    rank_param2 = "total"
    q_info_list = [text_q1, text_q2, text_q3, text_q4]
    q_param1_list = [str(half_param1), decrypt_param1, merge_param1_name, rank_param1]
    q_param2_list = [half_param2, decrypt_param2, merge_param2, rank_param2]
    default_q = 0
    current_option = default_q


    def __init__(self):

        self.root = Tk()
        self.root.geometry("650x300")
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
        self.q_frame.grid(row=1, column=0, columnspan=2, sticky="sw")
        self.q_exec_button = Button(self.q_frame, text="Execute", fg="red", command=self.execute_pressed)
        self.q_edit_button = Button(self.q_frame, text="Edit question parameters", fg="purple", command=self.edit_param)
        self.q_info_label = Label(self.q_frame, text=self.q_info_list[self.current_option], justify=LEFT)
        self.q_info_label.grid(row=0, column=0)
        self.entry1 = Entry(self.q_frame)
        self.entry2 = Entry(self.q_frame)
        self.entry1.insert(0, self.q_param1_list[self.current_option])
        self.entry2.insert(0,self.q_param2_list[self.current_option])
        self.q_exec_button.grid(row=1, column=0, sticky="sw")
        self.default_val_lbl = Label(self.q_frame, text="Default values:")
        # self.q_edit_button.grid(row=2, column=0, sticky="sw", pady=5)
        self.default_val_lbl.grid(row=2,column=0,sticky="sw",pady=5)
        self.entry1.grid(row=3, column=0, sticky='NSEW')
        self.entry2.grid(row=4,column=0, sticky='NSEW', pady=5)

        self.function_output = Frame(self.root)
        self.function_output.grid(row=2, column=0, sticky="sw")
        self.function_output_label = Label(self.function_output, justify=LEFT)
        self.function_output_label.grid(row=0, column=0)

        self.info_frame = Frame(self.root)
        self.info_frame.grid(row=3, column=0, sticky="sw")
        self.info_label = Label(self.info_frame, text=self.text_info, justify=LEFT)
        self.info_label.grid(row=0, column=0)

        self.root.mainloop()

    def refresh_frame(self, choice):
        self.current_option = self.q_list.index(choice)
        self.q_info_label.config(text=self.q_info_list[self.current_option])

    def execute_pressed(self):
        # TODO make matrix look more like a matrix
        string = ""
        if self.current_option == 0:
            function_output = half(self.half_param1, self.half_param2)
            string += ("half function with\nmatrix:" + str(self.half_param1) + "\nk: " + str(self.half_param2) + "\nresults with :\n\n" + str(function_output) + "\n\n")
        elif self.current_option == 1:
            function_output = decrypt(self.decrypt_param1, self.decrypt_param2)
            string += ("decrypt function with\nstring: " + self.decrypt_param1 + "\ndecryption key: " + str(self.decrypt_param2) + "\n\nresults with :\n\n" + function_output + "\n\n")
        elif self.current_option == 2:
            function_output = list(islice(merge(self.merge_param1, [2, 3, 7, 10, 11]), 9))
            string += ("merge function with\n iterable1 is: " + str(self.merge_param1_name) + "\niterable2 is: " + str(self.merge_param1_name) + "\n\nresults with :\n\n" + str(function_output) + "\n\n")
        elif self.current_option == 3:
            function_output = list(islice(rank(self.rank_param1, self.rank_param2), 3))
            string += ("rank function with\n filename: " + str(self.rank_param1) + "\nby: " + str(self.rank_param2) + "\n\nresults with :\n\n" + str(function_output) + "\n\n")
        self.function_output_label.config(text=string)


    def edit_param(self):
        # TODO create functions

        pass


if __name__ == "__main__":
    UserInterface()
