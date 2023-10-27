from vol.userFile import add_numbers
from vol.authorFile import true_function

OK = True
for i in range(10):
    # print(add_numbers(i, i + 1), true_function(i, i + 1))
    if(add_numbers(i, i + 1) != true_function(i, i + 1)):
        OK = False
        break
