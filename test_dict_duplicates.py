import unittest

def duplicates_counter_in_string(letters):
    if letters == "":
        return {}  # Return an empty dictionary for an empty string
    dc = {}
    for letter in letters:
        if dc.get(letter) is None:
            dc[letter] = 1
        else:
            dc[letter] += 1

    dt = {}

    for x, y in dc.items():
        if y >= 1 and x != " ":
            dt[x] = y
    return dt

class MyTest(unittest.TestCase):
    def test_empty_string(self):
        letters = ''
        self.assertEqual(duplicates_counter_in_string(letters), {})

    def test_duplicate_letters(self):
        letters = 'la la'
        self.assertEqual(duplicates_counter_in_string(letters), {'l': 2, 'a': 2})

    def test_special_characters(self):
        letters = '!!! &&&#### 222'
        self.assertEqual(duplicates_counter_in_string(letters), {'!': 3, '&': 3, '#': 4, '2': 3})

    def test_mixed_characters(self):
        letters = 'ss awaha'
        self.assertEqual(duplicates_counter_in_string(letters), {'s': 2, 'a': 3, 'w': 1, 'h': 1})

if __name__ == '__main__':
    unittest.main()
