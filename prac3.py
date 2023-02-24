
# taking input words saparated by comma
input_str = input('Enter your wrords:').lower()

# creating list of words
input_list = input_str.split(",")
# print(input_list)

anag_dic = {}

for i in input_list:
    # sort the string and store in sorted_str
    sorted_str = "".join(sorted(i))

    # check if sorted_str present in anag_dic as key
    if sorted_str not in anag_dic:
        anag_dic[sorted_str] = []

    # append item in list as value in anag_dic
    anag_dic[sorted_str].append(i)

# printing the values
print(anag_dic.values())
