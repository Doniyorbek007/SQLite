# def convert_to_int(func):
#     def wrapper(lst):
#         values = func(lst)
#         return int ("".join(str(i)for i in values))
#     return wrapper

# @convert_to_int
# def base_func(lst):
#     new_list = []
#     for i in lst:
#         new_list.append(i+1)
#     return new_list

# print(base_func([62]))

# my_list = [10,25,12,40,62]