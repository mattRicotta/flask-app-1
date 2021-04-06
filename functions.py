import math

def create_columns(list, number_of_columns):
    list_count = len(list)
    list_min = 0
    split_list = [] # a list of lists

    for col_index in range(number_of_columns):
      # get last list index for the current column
      list_max = math.ceil(list_min + ((list_count - list_min) / (number_of_columns - col_index)))
      # append short list to master list
      split_list.append(
        list[list_min:list_max]
      )
      # set next starting point as current endpoint
      list_min = list_max
      
    return split_list

# TEST SCRIPT ===============================================================

test_columns = 4
test_list_length = 25

test_list = []
for x in range(test_list_length):
  test_list.append(x)

for list in create_columns(test_list, test_columns):
  print(len(list), list)