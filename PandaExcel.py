import pandas as pd
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
result = []
headers = ['Number','Name', 'Student Id']
for row in text:
    number, id = re.findall(r"\d+", row)
    name = ' '.join(re.findall(r"([a-zA-Z]+)", row))
    details = number,name,id
    zipped = zip(headers, details)
    result.append(dict(zipped))
df = pd.DataFrame(data=result)
df.to_excel('new_members.xlsx')


