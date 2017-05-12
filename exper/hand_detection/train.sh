mkdir -p weights
mkdir -p logs
now=$(date +"%Y%m%d_%H%M%S")
../../darknet detector train hand.data yolo-hand.cfg ../../darknet19_448.conv.23.weights 2>&1 | tee logs/train_$now.txt
