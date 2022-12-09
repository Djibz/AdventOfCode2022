from pprint import pprint

tree = dict()
path = ''

def add_element(dirs, line, tree):
    if len(dirs) > 0:
        add_element(dirs[1:], line, tree[dirs[0]])
    else:
        if 'dir' in line:
            tree[line.split(' ')[-1][:-1]] = dict()
        else:
            tree[line.split(' ')[-1][:-1]] = l.split(' ')[0]

with open('input.txt') as iFile:
    for l in iFile:
        if l[0] == '$':
            if 'cd' in l:
                if '/' in l:
                    continue
                elif '..' in l:
                    path = "/".join(path.split('/')[:-1])
                else:
                    path = path + '/' + l.split(' ')[-1][:-1]
        else:
            if path == '':
                if 'dir' in l:
                    tree[l.split(' ')[-1][:-1]] = dict()
                else:
                    tree[l.split(' ')[-1][:-1]] = l.split(' ')[0]
            else:
                add_element(path.split('/')[1:], l, tree)

#pprint(tree)

## < 100000

low_dirs = []
all_dirs = []

def parcours_dir(tree, key):
    global low_dirs, all_dirs
    size = 0
    for k, v in tree.items():
        if isinstance(v, dict):
            size += parcours_dir(tree[k], k)
        else:
            size += int(v)
    if size <= 100000:
        low_dirs.append(size)
    all_dirs.append(size)
    return size

total = parcours_dir(tree, '/')
print(sum(low_dirs))

ws = 30000000 - (70000000 - total)
ws = 30000000 - (70000000 - total)
print(ws)

print(all_dirs)

finals = []
for i in all_dirs:
    if i > ws:
        finals.append(i)

print(finals)
print(min(finals))