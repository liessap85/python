# Remove all occurrances of number 20 from the following list

list1 = [5, 20, 15, 20, 25, 50, 20]
list_edit=[]

for num in list1:
    if num != 20:
        list_edit.append(num)

print(list_edit)

# Inline version

list1 = [5, 20, 15, 20, 25, 50, 20]

list_edit_inline = [num for num in list1 if (num != 20)]
print(list_edit_inline)