import json
from collections import OrderedDict as OrD
from itertools import count
from pathlib import Path
from pprint import pprint

fn = Path('./data/questions.json')
text = fn.read_text()
data = json.loads(text)

d1 = {
    group: {
        question: {
            answer: i
            for i, answer in enumerate(answers, idx)
        }
        for question, idx, answers in questions
    }
    for group, questions in data
}

it = count(1)

d2 = OrD([
    (group, OrD([
        (question, OrD([
            (answer, i)
            for i, answer in enumerate(answers, idx)
        ]))
        for question, idx, answers in questions
    ]))
    for group, questions in data
])


# pprint(d1)
# pprint(d2, width=120)
# print(d1 == d2)

# pprint(data)

def get_next():
    return str(next(it))


def row_from_list(l: list):
    return ' & '.join(l)


r'''
\documentclass[11pt]{article}
\usepackage{longtable}
\begin{document}
'''

l = [r'''
\begin{longtable}{|c|l|l|}
    \caption{Wszystkie cechy z odpowiedziami}\\ \hline
    \textbf{L.p.} & \textbf{Pytanie} & \textbf{Możliwe odpowiedzi} \\ \hline
    \endfirsthead
    \multicolumn{3}{c}
    {\tablename\ \thetable\ -- \textit{Wszystkie cechy z odpowiedziami - c.d.}} \\ \hline
    \textbf{L.p.} & \textbf{Pytanie} & \textbf{Możliwe odpowiedzi} \\ \hline
    \endhead
    \hline \multicolumn{3}{r}{\textit{Kontynuacja na następnej stronie}} \\
    \endfoot
    \hline
    \endlastfoot
''']
ccc = 0
for group, questions in d2.items():
    if group == 'Choroba':
        continue
    s = rf'\multicolumn{{{3}}}{{|c|}}{{{group}}} \\ \hline'
    l.append(s)
    for question, answers in questions.items():
        ccc += 1
        ll = []
        for answer, idx in answers.items():
            ll.append(rf'{idx}) {answer} ')
        s = r' \\ '.join(ll)
        s = r'''\begin{tabular}[c]{l}''' + s + '\end{tabular}'
        l.append(rf'{ccc} & {question} & {s} \\ \hline')

l.append(r'''
\end{longtable}
''')
'''
\end{document}
'''
pprint(l)

Path('./data/questions.tex').write_text('\n'.join(l))
