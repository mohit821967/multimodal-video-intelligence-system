
from backend.services.video_service import extract_video_frames
from backend.services.detection_service import detect_objects

# Extract frames
video_result = extract_video_frames(
    "uploads/sample.mp4",
    interval_seconds=2
)

# Detect objects
detection_results = detect_objects(
    video_result["frames"]
)

# Display results
for frame in detection_results:

    print("\nTimestamp:", frame["timestamp"])

    for detection in frame["detections"]:

        print(
            detection["object"],
            "Confidence:",
            detection["confidence"]
        )

print("\nObject detection completed!")
