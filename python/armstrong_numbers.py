# How can you make this more scalable and reusable later?
def find_armstrong_numbers(numbers):
    """
    Given a list of numbers, return a new list containing armstrong numbers.
    """
    armstrong_num = []
    for num in numbers:
        num_digit = len(str(num))
        l = [int(digit) for digit in str(num)] #list of digits
        total_list = map(lambda dig: dig**num_digit, l) #list of digits to whatever power it is
        if sum(total_list) == num:
            armstrong_num.append(num)

    return armstrong_num

