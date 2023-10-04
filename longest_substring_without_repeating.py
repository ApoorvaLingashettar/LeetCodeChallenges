from itertools import permutations


class Solution(object):

    def join_list_to_string(self, my_list):
        result_s = str()
        for letter in my_list:
            result_s += letter

        return result_s

    def does_have_unique_letters(self, s):
        result = True

        for i in s:
            if s.count(i) != 1:
                result = False
        return result

    def lengthOfLongestSubstring(self, s):
        combinations = []

        for i in range(1, len(s) + 1):
            c = permutations(s, i)

            for combi in c:
                _combi = self.join_list_to_string(combi)
                # print(_combi)
                if _combi not in combinations and _combi in s:
                    combinations.append(_combi)

        result = dict()
        size = len(s)
        s_list = []

        for word in combinations:
            if word in s:
                result[word] = s.count(word)

        max_size = 0
        result_string = str()
        result_string_length = 0

        for k, v in result.items():
            if v >= max_size or len(k) >= result_string_length:
                if self.does_have_unique_letters(k):
                    max_size = v
                    result_string = k
                    result_string_length = len(result_string)

        print(result_string)

        return (len(result_string))
