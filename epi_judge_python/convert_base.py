from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    real_value = 0
    converted_value = [] 
    string_to_value = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
                       "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14,
                       "F":15}
    value_to_string = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7",
                       8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E",
                       15:"F"}
    sign = +1
    num_len = len(num_as_string)
    if (num_as_string[0] == '-'):
        num_as_string = num_as_string[1:]
        sign = -1
        num_len -= 1
    for i in reversed(range(num_len)):
        tmp = string_to_value[num_as_string[i]] * b1 ** (num_len - i - 1)
        real_value += tmp
    if real_value == 0:
        return "0"
    while real_value / b2 > 0:
        res = real_value % b2
        converted_value.append(value_to_string[res])
        real_value = int(real_value / b2)
        # print(real_value, value_to_string[res])

    converted_value.append("-" if sign<0 else "")
    output = ''.join(reversed(converted_value))
    # print(output)
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
