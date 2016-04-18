# def odd_ball(alist):
#     answer = 0
#     for item in alist:
#         if item % 2 == 1:
#             answer += item
#     return answer
# print odd_ball([2,3,4,5,6])

# def disemvowel(astring):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     word = ''
#     for words in astring:
#         if words in vowels:
#             astring = astring.replace(words, '')
#
#     return astring
# print disemvowel('foobar')

# def lucky_sevens(array):
#     for num in range(0, len(array)):
#         if sum(array[num:num+3]) == 7:
#             return True
#         return False
# print lucky_sevens([1,3,3,4,5])

# def revstring(astring):
#     astring = astring[::-1]
#     print(astring)
# revstring('word')
# def factorial(numbers):
#     prod = 1
#     numbers = numbers+1
#     for number in range(1, numbers):
#         prod *= number
#     return prod
# print factorial(4)

# def longest_word(sentence):
#     words = sentence.split()
#     # sort_words = sorted(words, key=len)
#     # print sort_words[-1::]
#     largest_word = ''
#     for word in words:
#         if len(word) > len(largest_word):
#             largest_word = word
#
#     return largest_word
#
# print longest_word("hello weoiwjieqiwd ibfweiuwbfeuibewobuew welcome")

# def sum_num(num):
#     init_num = 0
#     num = num + 1
#     for number in range(1, num):
#         init_num += number
#     return init_num
# print sum_num(4)

# def time_conv(minutes):
#     if minutes < 60:
#         return "the minutes are %d"  % minutes
#     elif minutes >= 60:
#         hours = minutes // 60
#         min = (minutes % 60)
#         return "the hours are %d :%d " %(hours, min)
#     else:
#         return "yup"
# print time_conv(10)

# def count_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for word in string:
#         if word in vowels:
#             count += 1
#     return count
# print count_vowels("striiiaain")
#
# def num_repeats(string):
# redo
#     import collections
#     count = 0
#     d = collections.defaultdict(int)
#     for c in string:
#         d[c] += 1
#         if d[c] > 1:
#             count += 1
#     return count
#
# print num_repeats("lookee")


# def greatest_common_factor(num1, num2):
#
#     while num2 != 0:
#         num1, num2 = num2, num1 % num2
#
#     return num1
# print greatest_common_factor(16,24)

def palindrome(string):
    if string == string[::-1]:
        return True
    return False
print palindrome("rear")