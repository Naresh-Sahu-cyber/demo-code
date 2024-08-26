original_list = [1, 2, 2, 3, 4, 4, 5]
seen =set()
unique_list = []
for item in original_list:
    if item not in seen:
        unique_list.append(item)
        seen.add(item) 
print(unique_list)

