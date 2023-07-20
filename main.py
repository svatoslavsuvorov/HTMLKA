'''






'''



# def counter (s):
#     for i in set(s):
#         count = 0
#         for j in s:
#             if i == j:
#                 count += 1
#         print(i, count)
#
# counter('abcdabbcadad')


# def counter (s):
#     syms = {}
#     for i in s:
#         syms[i] = syms.get(i, 0) + 1
#     for i, count in syms.items():
#         print(i, count)
#
# counter('shcfjshfjkewkyfb')


# h\w:
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('арозаупаланалапуазора'))




