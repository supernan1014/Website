import os


def content_change(src):
    with open(src, 'r+', encoding='utf-8') as f:
        txt = f.read()

    txt2 = txt.replace('<h2>Vlaanderen</h2>', '<h2>Tust</h2>')
    txt2 = txt2.replace('<h4>is Erfgoed</h4>', '<h4>College of Bioengineering</h4>')

    with open(src, 'w', encoding='utf-8') as f:
        f.write(txt2)


src = r'./build/html'
for a, b, c in os.walk(src):
    for cc in c:
        if cc.endswith('.html'):
            content_change(os.path.join(a, cc))
