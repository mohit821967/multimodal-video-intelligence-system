
import json

from backend.services.video_service import extract_video_frames
from backend.services.detection_service import detect_objects, track_objects
from backend.services.summary_service import generate_video_summary

video_path = "uploads/sample.mp4"

# Extract video frames
video_result = extract_video_frames(video_path, 2)

# Detect objects
detections = detect_objects(video_result["frames"])

# Track objects
tracking = track_objects(video_path)

# Prepare video information
video_info = {
    "filename": "sample.mp4",
    "duration": video_result["duration"],
    "fps": video_result["fps"],
    "frames_analyzed": video_result["total_frames_extracted"]
}

# Generate report
report = generate_video_summary(
    video_info,
    detections,
    tracking
)

# Save JSON
with open("output/video_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("Video analysis completed!")
print("JSON report saved successfully!")
