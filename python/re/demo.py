import re, pyperclip

# pattern = ''
# re.compile(pattern, re.ASCII)
# re.compile(pattern, re.IGNORECASE)
# re.compile(pattern, re.LOCALE)
# re.compile(pattern, re.MULTILINE)
# re.compile(pattern, re.DOTALL)
# re.compile(pattern, re.UNICODE)
# re.compile(pattern, re.VERBOSE)


patternPhone = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # seperator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # seperator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

patternEmail = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
    )''', re.VERBOSE)


text = str(pyperclip.paste())
def combine(match):
    phoneNum = '{}-{}-{}'.format(match[1], match[3], match[5])
    if match[8]:
        phoneNum += ' x' + match[8]
        return phoneNum
    else:
        return phoneNum

list_phone = [combine(match) for match in patternPhone.findall(text)]
list_email = [match[0] for match in patternEmail.findall(text)]
result = list_phone + list_email

if len(result) > 0:
    pyperclip.copy('\n'.join(result))
else:
    print('No phone number or email address found in this text!')
