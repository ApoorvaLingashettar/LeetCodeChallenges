from itertools import permutations


class Solution(object):

    def string_to_list(self, s):
        s_list = []
        for i in s:
            s_list.append(i)

        return s_list

    def tuple_to_string(self, s):
        s_string = ''
        for i in s:
            s_string += i
        return s_string

    def longestPalindrome(self, s):
        s_list = self.string_to_list(s)
        substrings = list()
        for i in range(len(s_list), 0, -1):
            permutations_result = permutations(s_list, i)
            # print(list(permutations_result))

            for _item in list(permutations_result):
                # print(tuple_to_string(_item))

                if self.tuple_to_string(_item) not in substrings and self.tuple_to_string(_item) in s:
                    substrings.append(self.tuple_to_string(_item))

        # print(substrings)
        max_length = 0
        for substring in substrings:
            if substring == substring[::-1]:
                print(substring)

                if max_length < len(substring):
                    max_length = len(substring)
                    return substring
