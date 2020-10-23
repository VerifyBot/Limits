import os

path = './'

def html_body(idx):
    return f'<body>Hello World ({idx})</body>'

for i in range(950):
    path += f'{i}/'
    os.mkdir(path)
    try:
        with open(path+'index.html', 'w') as fp:
            fp.write(html_body(i))
    except OSError as exc:
        if exc.errno == 36:
            break
        else:
            raise


print(path)
