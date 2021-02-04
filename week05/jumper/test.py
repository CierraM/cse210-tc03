word_list = []
with open('word_base.txt', 'w') as word_base:
    filecontents = word_base.readlines()
    for line in filecontents:
        current_place = line[:-1]
        word_list.append(current_place)

for item in word_list:
    print(item)