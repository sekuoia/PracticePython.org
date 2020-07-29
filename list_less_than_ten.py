new_list = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for num in a:
#     if num < 5:
#         new_list.append(num)
# print(new_list)

# new_list = [num for num in a if num < 5]
# print(new_list)


user_num = int(input("Please enter a number: "))
for num in a:
    if num < user_num:
        new_list.append(num)
print(new_list)