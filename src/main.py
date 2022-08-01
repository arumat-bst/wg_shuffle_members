import csv
import itertools
import random
from pprint import pprint


def create_group(members, min_group_size):
    groups = []
    while len(members) >= min_group_size:
        samples = random.sample(members, min_group_size)
        groups.append(samples)
        members = list(set(members) - set(samples))
    else:
        for member in members:
            unmet_group_num = get_unmet_group(groups)
            groups[unmet_group_num].append(member)
    return groups


def get_unmet_group(groups):
    counter = []
    for members in groups:
        counter.append(len(members))
    return counter.index(min(counter))


def shuffle_group(groups):
    new_groups = [[] for _ in range(len(groups))]
    for members in groups:
        for member in members:
            unmet_group_num = get_unmet_group(new_groups)
            new_groups[unmet_group_num].append(member)
    return new_groups


def check_reencounter(pre_groups, new_groups):
    pre_pairs = []
    new_pairs = []
    for pre_group in pre_groups:
        for pair in itertools.combinations(pre_group, 2):
            pre_pairs.append(tuple(sorted(pair)))
    for new_group in new_groups:
        for pair in itertools.combinations(new_group, 2):
            new_pairs.append(tuple(sorted(pair)))

    return(list(set(pre_pairs) & set(new_pairs)))


# l = range(1, 50)
l = []
with open('test-2022-08-01.csv') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        l.append(row[0])

# グループに属する最小メンバー数
min_group_size = 3

print("# Turn 1")
groups_turn1 = create_group(l, min_group_size)
pprint(groups_turn1, width=50)

print("\n# Turn 2")
groups_turn2 = shuffle_group(groups_turn1)
pprint(groups_turn2, width=50)

reunions = check_reencounter(groups_turn1, groups_turn2)
print(f"\n# Turn1と被った組み合わせ数: {len(reunions)}")
pprint(reunions, width=50)
