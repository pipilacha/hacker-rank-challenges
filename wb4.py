import re
P = input()

# regex_integer_in_range = r"^([1-9][0-9][0-9][0-9][0-9][0-9]|[9][9][9][9][9][9])$"    # Do not delete 'r'.
regex_integer_in_range = r"^([1-9][0-9]{5})$"    # starts with group ->(one number from 1-9 followed by a number fom 0-9 repeated 5 times) <- ends with group


# (\d): Match and capture a digit in group #1
# (?=: Start lookahead
#     \d: Match any digit
#     \1: Back-reference to captured group #1
# ): End lookahead

regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
