def sort_list_by_last_char(list_of_strings): 
  list_of_strings.sort(key = lambda x: x[-2]) 
  return list_of_strings 

num_strings = int(input())
list_of_strings = []

for _ in range(num_strings):
  string = input()
  list_of_strings.append(string)

sorted_list = sort_list_by_last_char(list_of_strings)
print(sorted_list)