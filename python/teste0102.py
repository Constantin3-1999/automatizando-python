def test_password(password):
  MIN_LENGTH = 8
  MAX_LENGTH = 16
  MIN_DIGITS = 2
  MIN_LETTERS = 2

  password_len = len(password)
  if password_len < MIN_LENGTH or password_len > MAX_LENGTH:
    return False

  num_digits = 0
  num_letters = 0
  for char in password:
    if char.isdigit():
      num_digits += 1
    elif char.isalpha():
      num_letters += 1

  if num_digits < MIN_DIGITS or num_letters < MIN_LETTERS:
    return False

  return True

password = input("Enter a password: ")
if test_password(password):
  print("Password is strong.")
else:
  print("Password is weak.")