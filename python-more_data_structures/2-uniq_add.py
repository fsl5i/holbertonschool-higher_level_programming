#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set(my_list)  # تحويل القائمة إلى مجموعة لإزالة التكرارات
    total = 0
    for num in unique:
        total += num
    return total
