import ultralytics
from ultralytics import YOLO
import os
import cv2

def detection(image):
    model = YOLO("yolov8n.pt")
    results = model(image,
        conf=0.5, vid_stride=True, device="mps", task='detect', stream=True)

    classes = {"Малый": 0, "Кликун": 0, "Шипун": 0}

    for r in results:
        boxes = r.boxes
        for box in boxes:
            if model.names[int(box.cls)] == "bird":
                x_0 = int(box.xyxy[0][0])
                y_0 = int(box.xyxy[0][1])
                x_1 = int(box.xyxy[0][2])
                y_1 = int(box.xyxy[0][3])
                img = r.orig_img[y_0:y_1, x_0:x_1]
                cv2.imwrite("tmp.jpg", img)
                result = classification("tmp.jpg")

                classes[result[0]] += result[1]

    max_val = max(classes.values())
    if classes["Кликун"] == max_val:
        return "Кликун"
    elif classes["Шипун"] == max_val:
        return "Шипун"
    else:
        return "Малый"


def classification(image):
    model_classification = YOLO("best.pt")
    results_classification = model_classification(image)

    max_prob = results_classification[0].probs.max().item()


    if results_classification[0].probs[0] == max_prob:
        return ["Кликун", max_prob]
    elif results_classification[0].probs[1] == max_prob:
        return ["Малый", max_prob]
    else:
        return ["Шипун", max_prob]



def segmentation(image):
    model_segmentation = YOLO("best_seg.pt")
    results_segmentation = model_segmentation(image)

    conf_list = [0, 0, 0]

    for box in results_segmentation[0].boxes:
        conf_list[int(box.cls.item())] += box.conf.item()

    proba = max(conf_list) / (len(results_segmentation[0].boxes))
    # 0 - кликун 1 - малой 2 - шипун
    ans = conf_list.index(max(conf_list))
    if ans == 2:
        return "     Лебедь-\n      шипун" + "\n" + str(round(proba, 2))
    elif ans == 1:
        return "     Малый\n      лебедь" + "\n" + str(round(proba, 2))
    else:
        return "     Лебедь-\n      кликун" + "\n" + str(round(proba, 2))
        # return detection(image)


def start(name):
    return segmentation(name)

