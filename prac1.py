# dic to map word to number
num = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
}

# taking user input for both numbers and convert to lower
user_input1 = input('Enter first number:').lower()
user_input2 = input('Enter second number:').lower()


str1 = ''
str2 = ''

# counter for tracking sliced string and take the next word number
counter = 0
while counter < len(user_input1):
    # condition for numerical word length = 3(one,two,six,ten)
    if user_input1[counter:counter+3] in num:
        num1 = user_input1[counter:counter+3]
        str1 += "".join(num[num1])
        counter += 3

    # condition where numerical word length = 4(four,five,nine)
    elif user_input1[counter:counter+4] in num:
        num1 = user_input1[counter:counter+4]
        str1 += "".join(num[num1])
        counter += 4

    # condition where numerical word length = 5(three,seven,eight)
    elif user_input1[counter:counter+5] in num:
        num1 = user_input1[counter:counter+5]
        # number.append(num[num1])
        str1 += "".join(num[num1])
        counter += 5

    # for wrong input handling
    else:
        print('wrong input found in first number.')
        str1 = '0'
        break


counter = 0
while counter < len(user_input2):
    if user_input2[counter:counter+3] in num:
        num1 = user_input2[counter:counter+3]
        str2 += "".join(num[num1])
        counter += 3

    elif user_input2[counter:counter+4] in num:
        num1 = user_input2[counter:counter+4]
        str2 += "".join(num[num1])
        counter += 4

    elif user_input2[counter:counter+5] in num:
        num1 = user_input2[counter:counter+5]
        str2 += "".join(num[num1])
        counter += 5
    else:
        print('wrong input found in second number.')
        str2 = '0'
        break

# function to find GCD


def gcdFinder(a, b):
    if a > b:
        ans = a
    else:
        ans = b
    while ans >= 1:
        if a % ans == 0 and b % ans == 0:
            return ans
        ans -= 1


# list to convert num to word
word = ['zero', 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine']

# fun to convert num to word


def num_to_word(gcd):
    if gcd == 0:
        return ""
    else:
        l_num = gcd % 10
        ans = num_to_word(gcd//10) + word[l_num]
    return ans


# condition to handle wrong input
if str1 == '0' or not str2 == '0':
    str1 = int(str1)
    str2 = int(str2)
    gcd_ans = gcdFinder(str1, str2)
    print(num_to_word(gcd_ans))
