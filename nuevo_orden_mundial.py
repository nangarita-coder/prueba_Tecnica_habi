def sort_string(s):
    lower_chars = []
    upper_chars = []
    digits = []

    for char in s:
        if char.isalpha():
            if char.islower():
                lower_chars.append(char)
            else:
                upper_chars.append(char)
        elif char.isdigit():
            digits.append(char)

    lower_chars.sort()
    upper_chars.sort()

    odd_digits = []
    even_digits = []

    for digit in digits:
        if int(digit) % 2 == 1:
            odd_digits.append(digit)
        else:
            even_digits.append(digit)

    odd_digits.sort()
    even_digits.sort()

    sorted_chars = []
    sorted_chars.extend(lower_chars)
    sorted_chars.extend(upper_chars)
    sorted_chars.extend(odd_digits)
    sorted_chars.extend(even_digits)

    sorted_s = ''.join(sorted_chars)

    return sorted_s

s = input("Ingrese una cadena de caracteres: ")
sorted_s = sort_string(s)
print("La cadena ordenada es:", sorted_s)