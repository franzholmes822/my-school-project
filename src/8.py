def get_unique_elements(my_list):
    seen = set()
    return [x for x in my_list if x not in seen and not seen.add(x)]


if __name__ == "__main__":
    my_list = ["apple", "banana", "orange", "banana", "orange"]
    unique_elements = get_unique_elements(my_list)
    print(unique_elements)
