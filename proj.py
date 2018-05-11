import unittest
from itertools import *
from tkinter import *

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


def rank(file_name, how_to_rank='total'):
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


def open_gui():

    root = Tk()
    text_q1 = "Q1 (list comprehension):\n half function receives a matrix and a parameter k, matrix is manipulated according to parameter as shown in the example."
    text_q2 = "Q2 : decrypt function receives a text and a decryption key. returns the text after decryption"
    text_q3 = "Q3 : the generator function merge receives two iterable lists, calling the function each time returns values from both iterables in an ascending order"
    text_q4 = "Q4 : generator function rank function reads from a text file information of countries and their winnings in the olympic games.\n each call returns the name of winning countries in a descending order, sorted by parameter (total, weighted, gold, silver, arad)."
    text_info = "Eden Dupont {204808596}, Daniil Rolnik {334018009}"

    q1_frame = Frame(root)
    q1_frame.grid(row=0, column=0, sticky="sw")
    q1_exec_button = Button(q1_frame, text="Execute", fg="red")
    q1_info_label = Label(q1_frame, text=text_q1, justify=LEFT)
    q1_info_label.grid(row=0, column=0)
    q1_exec_button.grid(row=1, column=0, sticky="sw")

    q2_frame = Frame(root)
    q2_frame.grid(row=1, column=0, sticky="sw")
    q2_exec_button = Button(q2_frame, text="Execute", fg="red")
    q2_info_label = Label(q2_frame, text=text_q2, justify=LEFT)
    q2_info_label.grid(row=0, column=0)
    q2_exec_button.grid(row=1, column=0, sticky="sw")

    q3_frame = Frame(root)
    q3_frame.grid(row=2, column=0, sticky="sw")
    q3_exec_button = Button(q3_frame, text="Execute", fg="red")
    q3_info_label = Label(q3_frame, text=text_q3, justify=LEFT)
    q3_info_label.grid(row=0, column=0)
    q3_exec_button.grid(row=1, column=0, sticky="sw")

    q4_frame = Frame(root)
    q4_frame.grid(row=3, column=0, sticky="sw")
    q4_exec_button = Button(q4_frame, text="Execute", fg="red")
    q4_info_label = Label(q4_frame, text=text_q4, justify=LEFT)
    q4_info_label.grid(row=0, column=0)
    q4_exec_button.grid(row=1, column=0, sticky="sw")

    info_frame = Frame(root)
    info_frame.grid(row=4, column=0, sticky="sw")
    info_label = Label(info_frame, text=text_info, justify=LEFT)
    info_label.grid(row=0, column=0)
    root.mainloop()


class TestHW(unittest.TestCase):

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
        self.assertEqual(list(islice(rank(file_name, 'total'), 3)), ["\"USA\":2521", "\"Great-Britain\":847", "\"Israel\":9"])
        self.assertEqual(list(islice(rank(file_name, 'weighted'), 3)), ["\"USA\":5359", "\"Great-Britain\":1668", "\"Israel\":12"])
        self.assertEqual(list(islice(rank(file_name, 'gold'), 3)), ["\"USA\":1022", "\"Great-Britain\":263", "\"Israel\":1"])
        self.assertEqual(list(islice(rank(file_name, 'silver'), 3)), ["\"USA\":794", "\"Great-Britain\":295", "\"Israel\":1"])
        self.assertEqual(list(islice(rank(file_name, 'arad'), 3)), ["\"USA\":705", "\"Great-Britain\":289", "\"Israel\":7"])
        self.assertEqual(list(islice(rank(file_name, 'svsd'), 3)), ["\"Israel\":-1", "\"USA\":-1", "\"Great-Britain\":-1"])


if __name__ == "__main__":
    unittest.main(exit=False)
    open_gui()


