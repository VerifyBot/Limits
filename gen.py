t = "\n".join(['from random import randint as randint; import math as myMathCommands' for _ in range(35000)])
with open('imports.py', 'w') as fp:
    fp.write(t)
