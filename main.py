"""
Created: Koriol
Input: password length
Output: new password
"""


def gen():
  try:
    import string
    import random
  except:
    print('Cannot import string. Cannot import random')

  s1 = string.ascii_uppercase

  s2 = string.ascii_lowercase

  s3 = string.digits

  s4 = string.punctuation

  passlen = int(input("Enter the password length: "))

  s = []
  s.extend(list(s1))
  s.extend(list(s2))
  s.extend(list(s3))
  s.extend(list(s4))


  random.shuffle(s)
  pas = ("".join(s[0:passlen]))
  print(f'Your new create password is: {pas}')


if __name__ == '__main__':
    gen()