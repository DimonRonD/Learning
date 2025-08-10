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

# def solution(text, ending):
#     position = text.find(ending)
#     if position != -1:
#         if text.count(ending) > 1:
#             for i in range(text.count(ending)-1):
#                 position = position + text[position + len(ending):].find(ending) + len(ending)
#         if len(text) > position + len(ending):
#             return False
#         else:
#             return True
#     else:
#         return False
#
#
# def test(text, ending):
#     position = text.find(ending)
#     if text.count(ending) > 1:
#         for i in range(text.count(ending)-1):
#             position = position + text[position + len(ending):].find(ending) + len(ending)
#
#
# print(solution("abcabcabc",  "bc" ))
#
# def square_digits(num):
#     tmp = list(tuple(str(num)))
#     result = ""
#     for i in tmp:
#         result += str(int(i) ** 2)
#
#     return int(result)

#print(square_digits(0))


# def solution(s):
#     result = ''
#     for el in s:
#         if el.isupper():
#             print('-'+el+'-')
#             result += ' '+el
#         else:
#             result += el
#     return result
#
#
# print(solution('helloWorld'))


# def pig_it(text):
#     my_list = text.split()
#     text = ''
#     for word in my_list:
#         if word.isalpha():
#             tmp = word[1:] + word[0] + 'ay'
#             text += tmp + ' '
#         else:
#             text += word + ' '
#     return text.strip()
#
#
# print(pig_it('Quis custodiet ipsos custodes ?'))

# def duplicate_encode(word):
#     my_list = word.lower()
#     temp = ''
#     print(my_list)
#     for char in my_list:
#         if my_list.count(char) > 1:
#             temp += ')'
#         else:
#             temp += '('
#         print(char, temp)
#     return temp
#
# print(duplicate_encode("(( @"))

def move_zeros(lst):
    tmp = []
    for i, el in enumerate(lst):
        print(isinstance(el, bool))
        if el == 0:
            tmp.append(i)
    print(tmp)
    for i in range(len(tmp)-1, -1, -1):
        lst.pop(tmp[i])
        lst.append(0)
    return lst


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))