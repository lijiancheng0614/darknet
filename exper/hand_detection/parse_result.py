import os

result_dir = 'results'
output_path = 'result.txt'
name_list = ['fist', 'thumbs_up', 'index_finger', 'v', 'ok', 'palm']

ans = dict()
for filename in os.listdir(result_dir):
    class_name = filename.replace('comp4_det_test_', '').replace('.txt', '')
    fd = open(os.path.join(result_dir, filename))
    for line in fd:
        line = line.split()
        image_id = int(line[0])
        line = map(float, line)
        line[0] = name_list.index(class_name)
        if image_id not in ans:
            ans[image_id] = list()
            ans[image_id] = line
        elif line[1] > ans[image_id][1]:
            ans[image_id] = line
    fd.close()

def normalize(bbox, w, h):
    return [bbox[0] / w, bbox[1] / h, bbox[2] / w, bbox[3] / h]

threshold = 0.225
fd = open(output_path, 'w')
keys = sorted(ans.keys())
for k in keys:
    if ans[k][1] >= threshold:
        fd.write('{} {} {}\n'.format(k, ans[k][0] + 1, ' '.join(['{:.6f}'.format(i) for i in normalize(ans[k][2:], 640, 480)])))

fd.close()
