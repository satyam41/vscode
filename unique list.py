def unique_element(x):
    try:
        unique_list = []
        lenght=len(unique_list)
        for i in range(0,lenght):
            sort_of_list = unique_list.sort()
            count_element = unique_list.count(unique_list[i])
            if count_element == unique_list[i]:
                unique_list.append(unique_list[i])
        return unique_list
    except Exception as e:
        print("There is an error", e)
print(unique_element([5, 5, 2, 4, 4, 4, 9, 9, 9, 1, 0]))
