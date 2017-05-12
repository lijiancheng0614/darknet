import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

output_path = 'result.txt'
image_dir = 'val/JPEGImages'
name_list = ['fist', 'thumbs_up', 'index_finger', 'v', 'ok', 'palm']

fd = open(output_path)
lines = fd.readlines()
fd.close()

import random
random.shuffle(lines)
count = 5
for line in lines:
    line = line.split()
    class_name = int(line[1]) - 1
    bbox = map(float, line[2:])
    image_path = os.path.join(os.path.join(image_dir, line[0] + '.jpg'))
    im = Image.open(image_path)
    h, w, _ = np.array(im).shape
    bbox = [bbox[0] * w, bbox[1] * h, bbox[2] * w, bbox[3] * h]
    fig, ax = plt.subplots()
    ax.imshow(im, aspect='equal')
    ax.add_patch(
        plt.Rectangle((bbox[0], bbox[1]),
                      bbox[2] - bbox[0],
                      bbox[3] - bbox[1], fill=False,
                      edgecolor='red', linewidth=3.5)
        )
    ax.text(bbox[0], bbox[1] - 2,
            '{}'.format(name_list[class_name]),
            bbox=dict(facecolor='blue', alpha=0.5),
            fontsize=14, color='white')
    plt.axis('off')
    plt.tight_layout()
    plt.draw()
    plt.show()
    count -= 1
    if count <= 0:
        break
