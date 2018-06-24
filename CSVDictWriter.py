import csv
import re

text = """1. Nguyen Minh Dang 312314
2. Bai Jialong 542212
3. Dionetta Young 654213
4. Marcel Bartholomeus Prasetyo 342562
5. Mario Josephan 1235436
6. Siti Nurbaya 6354521
7. Jacy Ng 9412371
8. Chua Julia 875321
9. Alyanna Martinez 387582"""

text = text.split('\n')

# writing to CSV File
output= open('02-new_members_2018.csv', 'w', newline='')
writer = csv.writer(output)
headers = ['Number','Name', 'Student Id']
writer = csv.DictWriter(output, fieldnames=headers)
writer.writeheader()

# separate each record into number, name and student ID
# then form a dictionary from the details to be written into csv
for row in text:
    number, id = re.findall(r"\d+", row)
    name = ' '.join(re.findall(r"([a-zA-Z]+)", row))
    details = number,name,id
    zipped= zip(headers, details)
    result = dict(zipped)
    writer.writerow(result)