
import cv2
import os


def extract_video_frames(video_path, interval_seconds=2):

    output_folder = "output/frames"
    os.makedirs(output_folder, exist_ok=True)

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        raise ValueError("Unable to open video")

    fps = video.get(cv2.CAP_PROP_FPS)
    total_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

    duration = total_frames / fps

    extracted_frames = []

    timestamp = 0

    while timestamp < duration:

        video.set(cv2.CAP_PROP_POS_MSEC, timestamp * 1000)

        success, frame = video.read()

        if not success:
            break

        frame_name = f"frame_{timestamp}.jpg"

        frame_path = os.path.join(
            output_folder, frame_name
        )

        cv2.imwrite(frame_path, frame)

        extracted_frames.append({
            "timestamp": timestamp,
            "frame_path": frame_path
        })

        timestamp += interval_seconds

    video.release()

    return {
        "duration": round(duration, 2),
        "fps": fps,
        "total_frames_extracted": len(extracted_frames),
        "frames": extracted_frames
    }
