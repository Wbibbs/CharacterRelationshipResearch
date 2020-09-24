students = int(input())

groups = 0

if (students % 3 != 0):
  leftover = students % 3
  groups += 1
  students -= leftover
  groups = students / 3
else:
  groups = students / 3

print(int(groups))
