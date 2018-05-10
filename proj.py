import unittest

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


def rank(file_name,how_to_rank='total'):
    f = open(file_name)
    (countries, gold, silver, bronze, results_by_rank_type, index_to_yield, res_to_yield) = ([], [], [],[], [],  0, " ")
    (gold_weight, silver_weight, bronze_weight) = (3, 2, 1)

    for index, line in enumerate(f.readlines()):
        line_lst = line.split()
        (countries.append(line_lst[0]), gold.append(line_lst[1]), silver.append(line_lst[2]), bronze.append(line_lst[3]))

    results_by_rank_type = [
        (int(gold[index]) + int(silver[index]) + int(bronze[index])) if how_to_rank == 'total'
        else (int(gold[index])*gold_weight + int(silver[index])*silver_weight + int(bronze[index])*bronze_weight) if how_to_rank == 'weighted'
        else (int(gold[index])) if how_to_rank == 'gold'
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

    f.close()
    return
    # raise StopIteration


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
        def divisable_by(n, limit):
            k = 0
            while k < limit:
                yield k
                k += n

        g = divisable_by(4, 21)
        self.assertEqual(next(merge(g, [2, 3, 7, 10, 11])),0)

        res = []
        g = divisable_by(4, 21)
        for i in merge(g, [2, 3, 7, 10, 11]):
            res.append(i)
        self.assertEqual(res,[0, 2, 3, 4, 7, 8, 10, 11, 12, 16, 20])

    def test_rank(self):
        file_name = 'winners_test.txt'
        result = []
        for nation in rank(file_name, 'total'):
            result.append(nation)
        self.assertEqual(result,["\"USA\":2521", "\"Great-Britain\":847", "\"Israel\":9"])

        result = []
        for nation in rank(file_name, 'weighted'):
            result.append(nation)
        self.assertEqual(result, ["\"USA\":5359", "\"Great-Britain\":1668", "\"Israel\":12"])

        result = []
        for nation in rank(file_name, 'gold'):
            result.append(nation)
        self.assertEqual(result, ["\"USA\":1022", "\"Great-Britain\":263", "\"Israel\":1"])

        result = []
        for nation in rank(file_name, 'svsd'):
            result.append(nation)
        self.assertEqual(result, ["\"Israel\":-1", "\"USA\":-1", "\"Great-Britain\":-1"])


if __name__ == "__main__":
    unittest.main()
