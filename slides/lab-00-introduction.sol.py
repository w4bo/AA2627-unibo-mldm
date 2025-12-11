dataset = []
labels = []
with open(file_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split(',')
        if len(line) > 1:
            dataset.extend([[float(x) for x in line[:-2]]])
            labels += [line[-1]]
print('Dataset:', len(dataset), 'Labels:', len(labels))