# Vehicle_counting_in_video

## Reference
- yolov3-darknet  https://github.com/pjreddie/darknet
- yolov3-pytorch  https://github.com/eriklindernoren/PyTorch-YOLOv3
- sort https://github.com/abewley/sort
- Multi-type_vehicles_flow_statistics https://github.com/wsh122333/Multi-type_vehicles_flow_statistics

## Dependencies
- ubuntu/windows
- cuda>=10.0
- python>=3.6
- `pip install -r requirements.txt`

## Usage

1. Run `python app.py` ;
3. Select video and double click the image to select area, and then start;
4. After detecting and tracking, the result video and file are saved under `results` directory, the line of `output.xlsx` with format \[videoName,id,objectName] for each vehicle.

## Demo
![avatar](https://github.com/wsh122333/Multi-type_vehicles_flow_statistics/raw/master/asserts/demo1.gif)

![avatar](https://github.com/wsh122333/Multi-type_vehicles_flow_statistics/raw/master/asserts/demo2.gif)

![avatar](https://github.com/wsh122333/Multi-type_vehicles_flow_statistics/raw/master/asserts/demo3.gif)

