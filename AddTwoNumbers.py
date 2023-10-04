# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

def list_to_string(_list):
    _str = ''
    for i in _list:
        _str += str(i)

    return _str


def _reverse(_list):
    result = []
    for i in range(len(_list)-1, -1, -1):
        result.append(_list[i])

    return result


class solution():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    _l1 = _reverse(l1)
    _l2 = _reverse(l2)

    print(_l1)
    print(_l2)
    l1_number = list_to_string(_l1)
    l2_number = list_to_string(_l2)

    sum = int(l1_number) + int(l2_number)

    print(sum)

    str_sum = str(sum)
    x = (str_sum[::-1])
    print(type(x))
    result = []
    for i in x:
        result.append(i)

    print(result)
