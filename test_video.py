
from backend.services.video_service import extract_video_frames

result = extract_video_frames(
    video_path="uploads/sample.mp4",
    interval_seconds=2
)

print("Video Duration:", result["duration"])
print("FPS:", result["fps"])
print("Frames Extracted:", result["total_frames_extracted"])

for frame in result["frames"]:
    print(frame)
