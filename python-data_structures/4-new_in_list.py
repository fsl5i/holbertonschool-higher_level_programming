#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # ارجع نسخة لو الـ idx سلبي أو خارج النطاق
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    # نسخ القائمة الأصلية
    new_list = my_list.copy()

    # تعديل النسخة فقط
    new_list[idx] = element

    return new_list
