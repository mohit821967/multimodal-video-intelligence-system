
from ultralytics import YOLO
import cv2
import os
import contextlib
import io

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")


def detect_objects(frame_paths):

    output_folder = "output/detected"
    os.makedirs(output_folder, exist_ok=True)

    results_data = []

    for frame in frame_paths:

        image_path = frame["frame_path"]
        timestamp = frame["timestamp"]

        with contextlib.redirect_stdout(io.StringIO()):
            results = model(image_path, verbose=False)

        detections = []

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                object_name = model.names[class_id]

                x1, y1, x2, y2 = map(
                    int, box.xyxy[0]
                )

                detections.append({
                    "object": object_name,
                    "confidence": round(confidence, 2),
                    "bounding_box": {
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2
                    }
                })

        # Save annotated image
        annotated_image = results[0].plot()

        output_path = os.path.join(
            output_folder,
            f"detected_{timestamp}.jpg"
        )

        cv2.imwrite(output_path, annotated_image)

        results_data.append({
            "timestamp": timestamp,
            "image_path": output_path,
            "detections": detections
        })

    return results_data



def track_objects(video_path):

    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()

    results = model.track(
        source=video_path,
        tracker="bytetrack.yaml",
        stream=True,
        persist=True,
        conf=0.25,
        verbose=False
    )

    tracking_data = []

    for frame_number, result in enumerate(results):

        timestamp = round(frame_number / fps, 2)

        objects = []

        if result.boxes is not None and result.boxes.id is not None:

            for box in result.boxes:

                objects.append({
                    "track_id": int(box.id[0]),
                    "object": model.names[int(box.cls[0])],
                    "confidence": round(float(box.conf[0]), 2)
                })

        tracking_data.append({
            "timestamp": timestamp,
            "objects": objects
        })

    return tracking_data
