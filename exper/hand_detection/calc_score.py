result_path = 'result_train.txt'
gt_path = 'train/label.txt'

fd = open(gt_path)
gt = dict()
for line in fd:
    line = line.split()
    image_id = int(line[0])
    gt[image_id] = [line[1]]
    gt[image_id].extend(map(float, line[2:]))

fd.close()

def calc_iou(bbox1, bbox2):
    x1 = max(bbox1[0], bbox2[0])
    y1 = max(bbox1[1], bbox2[1])
    x2 = min(bbox1[2], bbox2[2])
    y2 = min(bbox1[3], bbox2[3])
    i = (x2 - x1) * (y2 - y1)
    u = (bbox1[2] - bbox1[0]) * (bbox1[3] - bbox1[1]) + (bbox2[2] - bbox2[0]) * (bbox2[3] - bbox2[1]) - i
    return i / u

fd = open(result_path)
ans = 0
ans2 = 0
for line in fd:
    line = line.split()
    image_id = int(line[0])
    if gt[image_id][0] == line[1]:
        ans += 1
    bbox = map(float, line[2:])
    iou = calc_iou(gt[image_id][1:], bbox)
    if iou >= 0.7:
        ans2 += 1
    elif iou >= 0.3:
        ans2 += 0.5

print(ans + ans2, ans, ans2)
