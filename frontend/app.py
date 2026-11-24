
import streamlit as st
import os
import sys
import json

sys.path.append(os.path.abspath("."))

from backend.services.video_service import extract_video_frames
from backend.services.detection_service import detect_objects, track_objects
from backend.services.summary_service import generate_video_summary

st.set_page_config(page_title="Video Intelligence System", layout="wide")

st.title("🎥 Multimodal AI Video Intelligence System")
st.write("Upload a video to extract frames, detect objects, track recurring objects and generate a timestamp-based report.")

uploaded_file = st.file_uploader("Upload MP4 Video", type=["mp4"])

interval = st.slider("Frame extraction interval (seconds)", 1, 10, 2)

if uploaded_file:
    os.makedirs("uploads", exist_ok=True)

    video_path = os.path.join("uploads", uploaded_file.name)

    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.video(video_path)

    if st.button("Analyze Video"):
        with st.spinner("Extracting frames..."):
            video_info = extract_video_frames(video_path, interval)

        st.success(f"Extracted {video_info['total_frames_extracted']} frames")

        with st.spinner("Detecting objects..."):
            detections = detect_objects(video_info["frames"])

        with st.spinner("Tracking recurring objects..."):
            tracking_data = track_objects(video_path)

        with st.spinner("Generating summary..."):
            report = generate_video_summary(
                video_info,
                detections,
                tracking_data
            )

        os.makedirs("output", exist_ok=True)

        report_path = "output/video_report.json"

        with open(report_path, "w") as f:
            json.dump(report, f, indent=4)

        st.success("Video analysis completed!")

        st.subheader("Analysis Summary")

        col1, col2, col3 = st.columns(3)

        col1.metric("Duration", f"{video_info['duration']} sec")
        col2.metric("Frames Analyzed", len(detections))
        col3.metric("Object Classes", len(report["analysis"]["unique_objects"]))

        st.subheader("Detected Objects")
        st.json(report["analysis"])

        st.subheader("Timestamp-wise Detection Results")

        for frame in detections:
            with st.expander(f"Timestamp: {frame['timestamp']} seconds"):
                st.image(frame["image_path"])
                st.write("Detections:", frame["detections"])

        st.subheader("Video Timeline")
        st.json(report["timeline"])

        st.download_button(
            "Download JSON Report",
            data=json.dumps(report, indent=4),
            file_name="video_report.json",
            mime="application/json"
        )
