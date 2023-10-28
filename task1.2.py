
a = input("Write simple input: ")
a = a.lower()

element_count = {}

for element in a:
    element_count[element] = element_count.get(element, 0) + 1

result_tuple = tuple((k, v) for k, v in element_count.items())

print("Elements: ", result_tuple)