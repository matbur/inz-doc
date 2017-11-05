import json
from collections import OrderedDict as OrD
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
pprint(d2, width=120)
print(d1 == d2)
pprint(data)


# label = 'Choroba'
#
# features = [j for _, i in data for j, *_ in i]
# features.remove(label)
#
# pprint(features)
# feature_dumps = json.dumps(features, ensure_ascii=False)
# Path('../data/features.json').write_text(feature_dumps)
#
# labels = list(d2[label][label].keys())
#
# pprint(labels)
# feature_dumps = json.dumps(labels, ensure_ascii=False)
# Path('../data/labels.json').write_text(feature_dumps)
