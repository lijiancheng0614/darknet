# 手型检测与精细分类问题

## Run

1. Put color image in `train/JPEGImages`.

2. Generate labels by `gen_labels.py` using `train/label.txt`.

3. Run `train.sh`

4. Run `test.sh`

5. Run `python parse_result.py` to get `result.txt`

6. (Optional) Run `python plot.py` to plot some samples.

## 题目说明

深度摄像头可以同时获取彩色及深度图像，为目标检测、识别提供了更多信息。该题目附件包含了用某深度摄像头采集到的手势图像，每幅图像对应一张普通彩色图及一张单通道深度图。在深度图像中，距离摄像头越近的物体其对应的像素值越大。像素值为0代表该点无法正常获取深度信息。
【题目二附件一】为手势训练集，包含600张手势图像及每幅图像中手势所在的位置标签、手势类型。注*：手势位置标签以彩色图像为准，对应到深度图像会有一定偏差。
【题目二附件二】为手势验证集，包含300张手势图像以及300张非手势图像共600张图像，不含手势标签信息。
最终手势测试集会于复赛最后一天（5月12日）公布。请知悉。
【题目二附件三】为示例答案格式。
请选手在答案文档中提供手势验证集里所有彩色图像对应的手势位置及手势类型。


## 标签注释

在训练数据集中，每幅图包含的标签有：手部位置标签及手势类型标签。
其中，
手部位置标签为手部所在区域对应的左上角A点，右下角B点的坐标值，格式为[x_A,y_A,x_B,y_B]。坐标值为该点相对整幅图像的比例，是[0-1）的浮点数。x坐标是该坐标对应于图像的宽的比例，y坐标是该坐标对应于图像的高的比例。
手势类型标签为数字0-6其中的一种，0-6分别对应：没有手出现；拳头；赞；食指竖起；v型手势；OK型手势；手掌。


## 答案格式

答案文档名字及格式为：answer.txt
答案文档需包含验证集中所有图片的检测及识别结果。
其中，验证集包含600个图像，图像编号为0-599。

答案文档中，每行的格式为:

图像编号 类别编号 手势左上角x坐标 手势左上角y坐标 手势右下角x坐标 手势右下角y坐标

其中，
图像编号是[0-599]
类别编号是[0-6]
坐标是[0-1）的浮点数，请保留6位小数。

如果没有检测到手，类别编号为0，且四个坐标全为0.0


## 评分标准

1.若图像不含有手势，正确判断该图像不含手势得1分。
2.若图像含有手势。给出的预测框与实际的框的IOU大于等于0.3则得0.5分，大于等于0.7则得1分。如果手势类别判断正确再加1分。

总分除以9为最终得分。

IOU的计算公式为 
IOU = 预测框与实际框重叠的面积 / (预测框面积 + 实际框面积 - 预测框与实际框重叠的面积)