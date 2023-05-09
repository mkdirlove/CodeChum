remaining_value = int(input("Enter an integer for remaining_value: "))

while remaining_value > 0:
    subtrahend = int(input("Enter an integer for subtrahend: "))
    new_remaining_value = remaining_value - subtrahend
    print(f"{remaining_value} - {subtrahend} = {new_remaining_value}")
    remaining_value = new_remaining_value
