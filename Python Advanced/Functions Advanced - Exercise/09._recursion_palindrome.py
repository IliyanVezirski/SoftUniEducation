def palindrome(word: str, left_index, right_index=-1):
    if left_index == len(word) // 2:
        return f'{word} is a palindrome'

    if word[left_index] == word[right_index]:
        return palindrome(word, left_index + 1, right_index - 1)
    else:
        return f'{word} is not a palindrome'


import unittest

class Tests(unittest.TestCase):
   def test(self):
      func = palindrome
      res = func("peter", 0)
      self.assertEqual(res, 'peter is not a palindrome')

if __name__ == "__main__":
   unittest.main()
print(palindrome("abcba", 0))
print(palindrome("peter", 0))
