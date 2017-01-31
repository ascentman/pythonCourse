def check_parantheses(st):
  cnt_par = 0
  cnt_bra = 0
  cnt_cur = 0

  # count parantheses ()
  for el in st:
  	if el == '(': cnt_par += 1
  	if el == ')': cnt_par -= 1
  	if cnt_par < 0: return False

  # count brackets []
  for el in st:
  	if el == '[': cnt_bra += 1
  	if el == ']': cnt_bra -= 1
  	if cnt_bra < 0: return False

  # count curly brackets {}
  for el in st:
  	if el == '{': cnt_cur += 1
  	if el == '}': cnt_cur -= 1
  	if cnt_cur < 0: return False

  return bool(cnt_par == cnt_bra == cnt_cur == 0)

# test cases
string = '({()[][][]([{},{},()])})' # True
string2 = '{[([[[(} 2, 5 {]]](()' # False
string3 = '[])({}' # False

result = check_parantheses(string)

# check result
print(result)
