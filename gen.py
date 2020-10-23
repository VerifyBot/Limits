import string, random
t = "\n".join([random.choice(string.printable) for _ in range(100000)])
with open('imports.py', 'w') as fp:
    fp.write(t)
