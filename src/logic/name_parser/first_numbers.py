def return_number(string_name):
    first_number = int(string_name[0][0])
    second_number = int(string_name[1][0])
    total_number = first_number * 10 + second_number
    return total_number

def check_number(string_name):
    try:
        int(string_name[0][0])
    except:
        print("First character is not a number")
        return False

    try:
        int(string_name[1][0])
    except:
        print("Second character is not a number")
        return False

    return True

def starts_with_numbers(file):
    splitted_name = file.split(" ", 1)
    numbers_string = splitted_name[0]

    if (check_number(numbers_string) == True): 
        number = return_number(numbers_string)
        # Assuming albums don't have more than 50 tracks
        if (number < 50): return True
        else: return False
    else: return False