import re
emails = ""
phones = ''


with open("automation/assets/potential-contacts.txt", "r") as file:
    txt = file.read()
    arr = txt.split()
    for i in arr :
        pattern = r'[A-Za-z]+@([A-Za-z]|[A-Za-z]+-+[A-Za-z])+\.+(net|org|com|info|biz)'
        if re.search(pattern, i):
            emails = emails + i +'\n'
        pattern_2 = r'\d+-+\d+-+[0-9]+'
        matched = re.search(pattern_2, i)
        if matched:
            phones = phones + matched[0] +'\n'


with open("automation/assets/emails.txt", "w+") as f:
    f.write(emails)

with open("automation/assets/phone_numbers.txt", "w+") as f:
    f.write(phones)

