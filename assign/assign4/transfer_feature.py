from Paper import *
from load_data import load_data, load_stop_words


paper_list = load_data("data/p10k_file")

author_set = set()
org_set = set()
conf_set = set()

count = 0

for p in paper_list :
    print("processing %d" %p.index)
    for author in p.author_list :
        author_set.add(author)

    for org in p.org_list :
        org_set.add(org)

    conf_set.add(p.conf)
    count += 1

print(count)
print(len(org_set))
print(len(conf_set))
print(len(author_set))
print(author_set)


