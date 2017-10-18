import re

# re_year = r'([1-9]\d{3})'
# re_month = r'([01]?\d)'
# re_day = r'([0-3]?\d)'

# re_date_f1 = r'({month}(/{day}/|-{day}-){year})'.format(month=re_month,
#     day=re_day, year=re_year)
# re_date_f2 = r'({year}(/{day}/|-{day}-){month})'.format(month=re_month,
#     day=re_day, year=re_year)

# text = '''
# Identifying patterns of text (and possibly substituting them with the sub() method) has many different potential applications.
# • Find website URLs that begin with http:// or https://.
# • Clean up dates in different date formats (such as 3/14/2015, 03-14-2015,
# and 2015/3/14) by replacing them with dates in a single, standard format.
# • Remove sensitive information such as Social Security or credit card numbers.
# • Find common typos such as multiple spaces between words, acciden- tally accidentally repeated words, or multiple exclamation marks at the end of sentences. Those are annoying!!
# '''

# dates1 = re.findall(re_date_f1, text)
# dates2 = re.findall(re_date_f2, text)
# for date in dates1 + dates2:
#     print(date[0])


# re_multiple_space = r'  +'
# re_repeated_word = r'(?P<word>\w+)\s+\1'


def my_strip(s, cs=' '):
    if len(s) == 0:
        return ''
    elif cs == '':
        return s
    else:
        cond1 = r'^[{}]+$'.format(cs)
        cond2 = r'^[{}]+([^{}].*)'.format(cs, cs)
        cond3 = r'(.*[^{}])[{}]+$?'.format(cs, cs)
        p1 = re.compile(cond1, re.DOTALL)
        p2 = re.compile(cond2, re.DOTALL)
        p3 = re.compile(cond3, re.DOTALL)
        if p1.match(s):
            return ''
        else:
            r2 = p2.sub(r'\1', s)
            r3 = p3.sub(r'\1', r2)
            return r3

print(my_strip(''))
print(my_strip('ab', ''))
print(my_strip('abab   ab'))
print(my_strip('ababfsdfdsdsagab#&#', '#*'))
print(my_strip('abab', 'ab'))
print(my_strip('  aba  \n\nb  '))
print('abab'.strip('ab'))