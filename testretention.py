
import time
import unittest

import retention

class TestRetention(unittest.TestCase):
    day_cutoffs = [int(time.mktime(time.strptime(str(i)+" Jan 16", "%d %b %y")))-time.timezone for i in range(1, 16)]

    def setUp(self):
        self.blank_results = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def test_simple(self):
        test_file = 'testdata/simple.txt'
        times, ids = retention.load_data(test_file)
        results = retention.find_retention(times, ids, self.day_cutoffs)

        expected_results = self.blank_results
        expected_results[0][13] = 1

        self.assertEqual(results, expected_results)

    def test_allones(self):
        test_file = 'testdata/allones.txt'
        times, ids = retention.load_data(test_file)
        results = retention.find_retention(times, ids, self.day_cutoffs)

        expected_results = self.blank_results
        expected_results[0][13] = 1
        expected_results[1][12] = 1
        expected_results[2][11] = 1
        expected_results[3][10] = 1
        expected_results[4][9] = 1
        expected_results[5][8] = 1
        expected_results[6][7] = 1
        expected_results[7][6] = 1
        expected_results[8][5] = 1
        expected_results[9][4] = 1
        expected_results[10][3] = 1
        expected_results[11][2] = 1
        expected_results[12][1] = 1
        expected_results[13][0] = 1

        self.assertEqual(results, expected_results)

    def test_alternate(self):
        test_file = 'testdata/alternate.txt'
        times, ids = retention.load_data(test_file)
        results = retention.find_retention(times, ids, self.day_cutoffs)

        expected_results = self.blank_results
        expected_results[0][13] = 1
        expected_results[0][0] = 1
        expected_results[2][0] = 1
        expected_results[4][0] = 1
        expected_results[6][0] = 1
        expected_results[8][0] = 1
        expected_results[10][0] = 1
        expected_results[12][0] = 1

        self.assertEqual(results, expected_results)

    def test_times(self):
        test_file = 'testdata/times.txt'
        times, ids = retention.load_data(test_file)
        results = retention.find_retention(times, ids, self.day_cutoffs)

        expected_results = self.blank_results
        expected_results[0][13] = 2

        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()

