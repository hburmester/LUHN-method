def luhn_check(card_number):
    card_number = [int(digit) for digit in str(card_number)][::-1]
    total = 0

    for i in range(len(card_number)):
        if i % 2 == 1:
            double_digit = card_number[i] * 2
            if double_digit > 9:
                double_digit -= 9
            total += double_digit
        else:
            total += card_number[i]

    return total % 10 == 0

# Example usage:
credit_card_number = "4556737586899855"
is_valid = luhn_check(credit_card_number)

if is_valid:
    print(f"The credit card number {credit_card_number} is valid.")
else:
    print(f"The credit card number {credit_card_number} is not valid.")