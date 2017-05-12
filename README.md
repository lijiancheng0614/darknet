# darknet

forked from [darknet](https://github.com/pjreddie/darknet).

## run

compile:

```bash
make
```

train:

```bash
./darknet detector train cfg/voc.data cfg/yolo-voc.cfg darknet19_448.conv.23 -gpus 0,1,2,3
```

test:

```bash
./darknet detector test cfg/coco.data cfg/yolo.cfg yolo.weights data/dog.jpg
# ./darknet detect cfg/coco.data cfg/yolo.cfg yolo.weights data/dog.jpg
```

test multiple images and output to `result.txt`:

```bash
./darknet detector valid cfg/coco.data cfg/yolo.cfg yolo.weights
```
