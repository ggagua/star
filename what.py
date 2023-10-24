
students = ['318 students', '320 students']

sum = 0
for each in students:
    split = each.split()
    strg= split[0]
    intgr = int(strg)
    sum += intgr


print(sum)