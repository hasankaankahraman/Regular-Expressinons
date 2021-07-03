import re

with open('input.txt', 'r') as inp:
    for line in inp:

        regexp = "([1-9][0-9]{3})-"
        years = re.findall(regexp, line)
        if len(years) > 0:
            print(years)

        regexp = "-([0][1-9]|[1][0-2])-"
        months = re.findall(regexp, line)
        if len(months) > 0:
            print(months)

        regexp = "-([0][1-9]|[1|2][0-9]|[3][0|1])$"
        days = re.findall(regexp, line)
        if len(days) > 0:
            print(days)

            #HASAN KAAN KAHRAMAN