i = 0
def split_at_digit(formula):
  for i in range(len(formula)):
    if formula[i].isdigit():
      prefix = formula [:i]
      number = int (formula[i:])
      return (prefix, number)
  return (formula, '1')


index = 0
parts = []
current_part = " "
def split_before_each_uppercase(formula):
  for index in range(1, len(formula)):
    if formula[index].isupper() and current_part != "":
      parts.append(current_part)
      current_part = 'index'
    else:
      current_part += 'index'
   
  return parts
