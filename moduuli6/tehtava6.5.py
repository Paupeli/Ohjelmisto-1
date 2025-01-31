def remove_odd_numbers(input_list):
    even_numbers = [n for n in input_list if n % 2 ==0 ]
    return even_numbers

def main():
    original_list = [32,56,87,92,13]

    even_list = remove_odd_numbers(original_list)

    print("Original list:", original_list)
    print("List with odd numbers removed:", even_list)

if __name__ == "__main__":
    main()