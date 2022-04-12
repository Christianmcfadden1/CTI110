user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_character = str(input('Enter character:\n'))
user_string = str(input('Enter string:\n'))
line_up = [user_int, user_float, user_character, user_string]

# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
print(user_int, user_float, user_character, user_string)

# FIXME (2): Output the four values in reverse
line_up.reverse()
print(line_up)

# FIXME (3): Convert the integer to a characer, and output that character
user_change = chr(user_int)
print(user_int, 'converted to a character is', user_change)