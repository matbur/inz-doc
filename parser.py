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
    return ' & '.join(l).join([r'\hline ', r'\\'])


l = []
for group, questions in d2.items():
    # ll = ['', '', f'{group}']
    # s = row_from_list(ll)
    s = rf'\multicolumn{{3}}{{|c|}}{{{group}}}'.join([r'\hline ', r'\\'])
    l.append(s)
    for question, answers in questions.items():
        answer, idx = answers.popitem(last=False)
        popitem = f'{idx} - {answer}'
        ll = [get_next(), question, popitem]
        s = row_from_list(ll)
        l.append(s)
        for answer, idx in answers.items():
            ll = ['', '', f'{idx} - {answer}']
            s = row_from_list(ll)
            l.append(s)

pprint(l)

Path('file.tex').write_text('\n'.join(l))
