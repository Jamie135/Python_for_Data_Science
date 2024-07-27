ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = 'World!'

lst1 = [s for s in ft_tuple]
lst1[1] = 'France!'
# * is an unpacking operator that takes an iterable
# and expands it into individual elements
ft_tuple = (*lst1,)

lst2 = [s for s in ft_set]
lst2[1] = 'Paris!'
ft_set = {*lst2}

ft_dict['Hello'] = '42Paris!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
