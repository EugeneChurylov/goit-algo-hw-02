from collections import deque


def is_palindrome(d: str):
  d = d.lower().replace(" ", "")
  input_deque = deque(d)

  while len(input_deque) > 1:
    if input_deque.popleft() != input_deque.pop():
            return False
  
  return True

d = "Eugene"
result = is_palindrome(d)

if result:
    print(f'Рядок "{d}" є паліндромом.')
else:
    print(f'Рядок "{d}" не є паліндромом.')

