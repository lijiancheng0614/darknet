import os
import numpy as np
from PIL import Image

root_dir = 'val'
rgb_dir = os.path.join(root_dir, 'color_image')
depth_dir = os.path.join(root_dir, 'depth_image_aligned')
output_dir = os.path.join(root_dir, 'images')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_list = os.listdir(rgb_dir)
for file_name in file_list:
    im_rgb = Image.open(os.path.join(rgb_dir, file_name))
    im_rgb = np.array(im_rgb)
    im_depth = Image.open(os.path.join(depth_dir, file_name))
    im_depth = np.array(im_depth)
    h, w, _ = im_rgb.shape
    im = np.concatenate((im_rgb, im_depth[..., np.newaxis]), axis=2)
    im = Image.fromarray(im)
    output_path = os.path.join(output_dir, file_name.replace('jpg', 'tiff'))
    im.save(output_path)
