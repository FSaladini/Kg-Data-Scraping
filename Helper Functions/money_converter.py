import re

amounts = r"thousand|million|billion"
number = r"\d+(,\d{3})*\.*\d*"

value_re = rf"\${number}"
word_re = rf"\${number}(-|\sto\s|–)?({number})?\s({amounts})"

'''
Possible values:
$600,000 -> 600000              ## value syntax
$12.2 million -> 12200000       ## word syntax (million, billion, etc)
$12-13 million -> 12000000      ## word syntax with a range
$16 to 20 million -> 16000000   ## word syntax with a different range
[12]
'''

def word_to_value(word):
    value_dict = {"thousand": 1000, "million": 1000000, "billion": 1000000000}
    return value_dict[word]


def parse_word_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))

    word = re.search(amounts, string, flags=re.I).group().lower()
    total_amount = value * word_to_value(word)
    return total_amount

def parse_value_syntax(string):
    value_string = re.search(number, string).group()
    value = float(value_string.replace(",", ""))
    return value

def money_conversion(money):
    if money == "N/A":
        return None
    
    if isinstance(money, list):
        money = money[0]

    value_syntax = re.search(value_re, money)
    word_syntax = re.search(word_re, money, flags=re.I)

    if word_syntax:
        return parse_word_syntax(word_syntax.group())

    elif value_syntax:
        return parse_value_syntax(value_syntax.group())
    else:
        return None

print(money_conversion("$12.2 thousand"))

