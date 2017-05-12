import os
import numpy as np
from PIL import Image

wd = os.getcwd()
label_dir = 'train/labels'
if not os.path.exists(label_dir):
    os.makedirs(label_dir)

fd = open('train/label.txt')
list_file = open('train/train.txt', 'w')
for line in fd:
    line = line.split()
    image_id = line[0]
    label = int(line[1])
    image_path = '{}/train/JPEGImages/{}.jpg'.format(wd, image_id)
    list_file.write('{}\n'.format(image_path))
    out_file = open(os.path.join(label_dir, image_id + '.txt'), 'w')
    b = map(float, line[2:])
    b = ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2, b[2] - b[0], b[3] - b[1])
    out_file.write(str(label - 1) + ' ' + ' '.join([str(i) for i in b]) + '\n')
    out_file.close()
    
list_file.close()
