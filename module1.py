employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
employee_names, employee_numbers = zip(*employees_zipped)
print(employee_names) # ("Дима", "Марина", "Андрей", "Никита")
print(employee_numbers) # (2, 9, 18, 28)