import unittest


def my_function():
    letters = input("Write the string: ")
    if letters == "":
        print("String is empty.")
    dc = {}
    for letter in letters:
        if dc.get(letter) is None:
            dc[letter] = 1
        else:
            dc[letter] += 1

    dt = {}

    for x, y in dc.items():
        if y > 1 and x != " ":
            dt[x] = y
            print(x, y)
    return dt


class MyTest(unittest.TestCase):
    def test(self):
        letters = ''
        self.assertEqual(my_function(), {})
        print("Empty")


#class MyTest(unittest.TestCase):
#   def test(self):
#       letters = 'la la'
#       self.assertEqual(my_function(), {'l': 2, 'a': 2})
#       print(True)

#class MyTest(unittest.TestCase):
#   def test(self):
#       letters = 'ss awaha'
#       self.assertEqual(my_function(), {'s': 2, 'a': 3})
#       print(True)


#class MyTest(unittest.TestCase):
#  def test(self):
#        letters = '!!! &&&#### 222'
#       self.assertEqual(my_function(), {'!': 3, '&': 3, '#': 4, '2': 3})
#       print(True)

