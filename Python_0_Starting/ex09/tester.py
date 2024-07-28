from ft_package.utils import count_item


print(count_item(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_item(["toto", "tata", "toto"], "tutu"))  # output: 0
