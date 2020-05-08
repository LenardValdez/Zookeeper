class1 = int(input())
class2 = int(input())
class3 = int(input())

count_class1 = (class1 // 2) + (class1 % 2)
count_class2 = (class2 // 2) + (class2 % 2)
count_class3 = (class3 // 2) + (class3 % 2)
total_desks = count_class1 + count_class2 + count_class3
print(total_desks)
