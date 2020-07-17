a = ["bangalore", "chennai", "pune"]

for i in a:
    if i == 'chennai':
        continue
    else:
        if i == 'bangalore' or i == 'pune':
            print(i)