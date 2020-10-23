import os, sys

sys.setrecursionlimit(10000)

txt = "subd/"+"/".join([*map(str, [*range(5000)])])
os.makedirs(txt)

with open(txt+'/index.html', 'w') as fp:
    fp.write("<body>Hello World</body>")

