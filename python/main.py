import infinite_monkey
import string

monkey = infinite_monkey.infinite_monkey()

alph = string.ascii_letters
w = 'alisa'
c = monkey.type(alph,w)
print(c)