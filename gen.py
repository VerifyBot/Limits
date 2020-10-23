import string, random
t = "\n".join([random.choice(string.printable) for _ in range(20000)])
with open('imports.py', 'w') as fp:
    fp.write(t)
