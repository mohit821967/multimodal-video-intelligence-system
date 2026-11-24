
from collections import defaultdict


def generate_video_summary(video_info, detections, tracking_data):

    object_counts = defaultdict(int)
    object_timestamps = defaultdict(list)
    timeline = []

    # Aggregate detected objects
    for frame in detections:

        timestamp = frame["timestamp"]
        frame_objects = []

        for detection in frame["detections"]:

            name = detection["object"]

            object_counts[name] += 1
            object_timestamps[name].append(timestamp)

            if name not in frame_objects:
                frame_objects.append(name)

        if frame_objects:
            timeline.append({
                "timestamp": timestamp,
                "objects": frame_objects
            })

    # Aggregate tracking IDs by class
    tracked_objects = defaultdict(set)

    for frame in tracking_data:
        for obj in frame["objects"]:
            tracked_objects[obj["object"]].add(obj["track_id"])

    report = {
        "video_info": video_info,
        "analysis": {
            "unique_objects": list(object_counts.keys()),
            "detection_counts": dict(object_counts),
            "tracking_counts": {
                name: len(ids)
                for name, ids in tracked_objects.items()
            },
            "object_timestamps": dict(object_timestamps)
        },
        "timeline": timeline
    }

    return report
