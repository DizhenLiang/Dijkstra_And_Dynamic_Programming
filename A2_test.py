import unittest
from assignment1 import *

class dpTest(unittest.TestCase):
    def test_edge_case_duplicate_check(self):
        occupancy_probability = [
            [57, 76, 38, 22],
            [56, 94, 54, 68],
            [71, 86, 86, 99],
            [81, 0, 0, 60],
            [36, 22, 43, 93]
        ]
        expec_res_1 = [184, [(0, 3), (1, 2), (2, 1), (3, 1), (4, 1)]]
        expec_res_2 = [184, [(0, 3), (1, 2), (2, 2), (3, 2), (4, 1)]]
        expec_res_3 = [184, [(0, 3), (1, 2), (2, 1), (3, 2), (4, 1)]]
        expec_res_4 = [184, [(0, 3), (1, 2), (2, 2), (3, 1), (4, 1)]]
        my_res = select_sections(occupancy_probability)
        self.assertTrue(
            my_res == expec_res_1 or my_res == expec_res_2 or my_res == expec_res_3 or my_res == expec_res_4)

    def test_long_1_check(self):
        occupancy_probability = [[57, 11, 14, 19, 63, 50, 61, 50, 40, 0, 46],
                                 [2, 42, 98, 84, 56, 5, 33, 87, 60, 19, 91],
                                 [84, 23, 37, 36, 38, 89, 72, 13, 48, 88, 46],
                                 [36, 91, 11, 1, 5, 3, 38, 58, 37, 24, 39],
                                 [52, 74, 67, 41, 76, 29, 38, 61, 74, 42, 10],
                                 [46, 25, 38, 16, 50, 7, 99, 34, 79, 83, 19],
                                 [76, 68, 74, 48, 38, 11, 46, 25, 31, 10, 73],
                                 [99, 4, 65, 22, 12, 47, 18, 45, 63, 85, 17],
                                 [35, 86, 91, 69, 50, 20, 72, 34, 24, 69, 100],
                                 [20, 7, 63, 92, 33, 81, 22, 79, 85, 39, 21],
                                 [98, 22, 37, 54, 28, 89, 50, 95, 59, 17, 88],
                                 [13, 86, 98, 26, 30, 3, 93, 97, 59, 1, 23],
                                 [39, 62, 48, 37, 35, 84, 87, 91, 63, 66, 21]]

        expec_res = [273,
                     [(0, 1), (1, 0), (2, 1), (3, 2), (4, 3), (5, 3), (6, 4), (7, 4), (8, 5), (9, 4), (10, 4), (11, 5),
                      (12, 4)]]

        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expec_res)

    def test_long_2_check(self):
        occupancy_probability = [[15], [84], [82], [79], [77], [55], [69], [13], [21], [33], [85], [100], [67], [93],
                                 [3], [26], [29], [89], [36], [100], [68], [34], [87], [55], [47], [44], [64], [84],
                                 [41], [97]]

        expec_res = [1777,
                     [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0),
                      (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0),
                      (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0)]]

        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expec_res)

    def test_short_check(self):
        occupancy_probability = [[66], [66]]

        expec_res = [132, [(0, 0), (1, 0)]]

        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expec_res)

    def test_short2_check(self):
        occupancy_probability = [[32, 86, 95, 15, 68, 90],
                                 [91, 88, 96, 51, 64, 66],
                                 [17, 70, 13, 9, 90, 17],
                                 [17, 15, 38, 12, 53, 17],
                                 [29, 6, 18, 27, 66, 48],
                                 [74, 43, 76, 44, 3, 1],
                                 [89, 1, 8, 24, 45, 62],
                                 [3, 98, 99, 89, 6, 66]]

        expected_1 = [147, [(0, 3), (1, 3), (2, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 0)]]
        expected_2 = [147, [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 4), (6, 3), (7, 4)]]

        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expected_1 or my_res == expected_2)

    def test_which_to_go(self):
        occupancy_probability = [
            [0, 76, 38, 2],
            [1, 94, 54, 1],
            [2, 86, 86, 99],
            [3, 0, 0, 0],
            [99, 99, 99, 0]
        ]
        expec_res_1 = [87, [(0, 0), (1, 0), (2, 1), (3, 2), (4, 3)]]
        self.assertTrue(select_sections(occupancy_probability) == expec_res_1)

    def test_selectsections_7(self):
        occupancy_probability = [
            [19, 76, 38, 22, 0],
            [56, 20, 54, 0, 34],
            [71, 86, 0, 99, 89],
            [81, 0, 82, 22, 45],
            [0, 22, 22, 93, 23]
        ]
        expected = [0, [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]]
        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expected)

    def test_selectsections_8(self):
        occupancy_probability = [
            [19, 76, 38, 22, 0],
            [56, 20, 54, 0, 34],
            [71, 86, 0, 99, 89],
            [81, 34, 82, 0, 45],
            [62, 22, 22, 93, 0]
        ]
        expected = [0, [(0, 4), (1, 3), (2, 2), (3, 3), (4, 4)]]
        my_res = select_sections(occupancy_probability)
        self.assertTrue(my_res == expected)


if __name__ == '__main__':
        unittest.main()