# def count_bits(n):
#     dig = str(bin(n)[2:])
#     print(dig, dig.count('1'))
#
#
# count_bits(1234)
##########################################################################
from eduson_git_test import count


# def descending_order(num):
#     # Bust a move right here
#     print(int(''.join(list(sorted(tuple(str(num)), reverse=True)))))
#
# # a = list(tuple('93849276291784'))
# #
# # secret = ''.join(a[::-1])
# descending_order(123456789)
##########################################################################

# def find_it(seq):
#     my_dict = dict()
#     for i in range(len(seq)):
#             my_dict[seq[i]] = seq.count(seq[i])
#
#     for k, v in my_dict.items():
#         if v % 2 == 1:
#             tmp = k
#     return tmp
#
#
#
# seq = [1,2,2,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,1]
#
# print(find_it(seq))
##########################################################################

# def accum(st):
#     result = ''
#     for i in range(len(st)):
#         if i > 0:
#             result += '-'
#         result += (st[i:i+1] * (i + 1)).capitalize()
#         print(result)
#
# print(accum("ZpglnRxqenU"))
##########################################################################

def solution(text, ending):
    position = text.find(ending)
    if position != -1:
        if text.count(ending) > 1:
            for i in range(text.count(ending)-1):
                position = position + text[position + len(ending):].find(ending) + len(ending)
        if len(text) > position + len(ending):
            return False
        else:
            return True
    else:
        return False


def test(text, ending):
    position = text.find(ending)
    if text.count(ending) > 1:
        print(text.count(ending))
        for i in range(text.count(ending)-1):
            print("Old", position)
            print(text[position + len(ending):])
            print("Finded", text[position + len(ending):].find(ending))
            position = position + text[position + len(ending):].find(ending) + len(ending)
            print("New", position)

print(solution("abcabcabc",  "bc" ))