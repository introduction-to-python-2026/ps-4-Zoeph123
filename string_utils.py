def split_before_each_uppercase(formula):
  parts = []
  if not formula:
    return parts
  current_part = formula[0]
  for char in formula [1:]:
    if char.isupper():
      parts.append(current_part)
      current_part = char
    else :
      current_part += char
  parts.append (current_part)
  return parts


i = 0
def split_at_digit(formula):
  for i in range(len(formula)):
    if formula[i].isdigit():
      prefix = formula [:i]
      number = int (formula[i:])
      return (prefix, number)
  return (formula, '1')


