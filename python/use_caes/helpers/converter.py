def convert_phone_to_int(phone_num: str) -> int:
    modified_numbers = []

    modified = phone_num.removeprefix('+')
    modified = modified.removeprefix('00')

    for char in modified:
        if char.isdigit():
            modified_numbers.append(char)

    return int(str(''.join(modified_numbers)))