import os

txt = "subd/"+"/".join([*map(str, [*range(500)])])+"/main.html"
os.makedirs(txt)
with open(txt, 'w') as fp:
    fp.write("<body>Hello World</body>")


