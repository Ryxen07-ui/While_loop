current_number = 0
previous_number = 0

print("Printing current and previous number sum in a range(10)")

while current_number < 10:
    total_sum = current_number + previous_number
    print(f"Current Number {current_number} Previous Number {previous_number} Sum: {total_sum}")
    previous_number = current_number
    current_number = current_number + 1