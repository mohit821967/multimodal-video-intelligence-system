from backend.services.detection_service import track_objects

results = track_objects("uploads/sample.mp4")

for frame in results:

    if frame["objects"]:

        print("\nTimestamp:", frame["timestamp"])

        for obj in frame["objects"]:
            print(
                "ID:", obj["track_id"],
                "Object:", obj["object"]
            )

print("\nObject tracking completed!")