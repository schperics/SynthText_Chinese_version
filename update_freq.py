from collections import Counter
import pickle
import codecs

cnt = 0
filename = '/Workspace/SynthText_Chinese_version/data/newsgroup/newsgroup.txt'
c = Counter()
for x in codecs.open(filename, 'r', 'utf-8') :
    print(x)
    c += Counter(x.strip())
    print(c)
    cnt += len(x.strip())
    # print c
print(cnt)

for key in c:
    c[key] = float(c[key]) / cnt
    print(key, c[key])

d = dict(c)
# print d
with open("char_freq.cp", 'wb') as f:
    pickle.dump(d, f)
