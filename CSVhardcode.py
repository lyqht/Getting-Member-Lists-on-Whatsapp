import csv

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
edited_record = {}

# hard code method
for record in text:
    record = record.strip('.')
    index = record[0]
    name_and_id = record[2:]
    id = name_and_id[-7:]
    name = name_and_id[0:len(name_and_id) - 8]
    edited_record[index] = [name, id]

# writing in row by row
# newline='' is necessary so that extra empty rows will not be added
output= open('new_members_2018.csv', 'w', newline='')
writer = csv.writer(output)
table_headers = ['Number','Name', 'Student Id']
writer.writerow(headers)
for key, value in edited_record.items():
    writer.writerow([key, value[0],value[1]])