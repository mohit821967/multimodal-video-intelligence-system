# 🎥 Multimodal AI Video Intelligence System

An AI-powered video analysis application that extracts video frames, detects objects, tracks recurring objects, and generates timestamp-based summaries using YOLOv8 and MCP (Model Context Protocol).

## 🚀 Features

- **Video Upload:** Upload MP4 videos through a Streamlit interface.
- **Frame Extraction:** Extract frames at configurable time intervals using OpenCV.
- **Object Detection:** Detect objects using YOLOv8.
- **Bounding Boxes:** Display detected objects with bounding boxes and confidence scores.
- **Object Tracking:** Track recurring objects across video frames using ByteTrack.
- **Video Summary:** Generate timestamp-based object summaries.
- **JSON Report:** Export analysis results as a downloadable JSON file.
- **MCP Integration:** Expose video frame extraction and object detection through MCP tools.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Object Detection | YOLOv8 |
| Computer Vision | OpenCV |
| Object Tracking | ByteTrack |
| Frontend | Streamlit |
| Backend | FastAPI |
| AI Integration | Model Context Protocol (MCP) |
| Data Format | JSON |

## 📁 Project Structure

```text
video-intelligence-system/
├── backend/
│   ├── main.py
│   └── services/
│       ├── video_service.py
│       ├── detection_service.py
│       └── summary_service.py
├── frontend/
│   └── app.py
├── mcp_server/
│   ├── server.py
│   └── client.py
├── uploads/
├── output/
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/mohit821967/multimodal-video-intelligence-system.git
cd multimodal-video-intelligence-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run frontend/app.py
```

Open:

`http://localhost:8501`

## 🔌 MCP Server and Client

The project provides two MCP tools:

**1. extract_video_frames_tool**
- Accepts a video path and frame extraction interval.
- Extracts frames and returns timestamps and frame paths.

**2. detect_objects_tool**
- Accepts a video path and extraction interval.
- Detects objects using YOLOv8.
- Returns object labels, confidence scores, bounding boxes, and timestamps.

Run the MCP client:

```bash
python -m mcp_server.client
```

The client connects to the MCP server, lists available tools, and executes video analysis operations.

## 📊 Output

The application generates:

- Extracted video frames.
- Annotated images containing object bounding boxes.
- Object detection results with confidence scores.
- Object tracking information.
- Timestamp-based video summary.
- Downloadable `video_report.json`.

## 🧠 Processing Workflow

1. Upload an MP4 video.
2. Extract frames at the selected interval.
3. Run YOLOv8 object detection.
4. Track objects across video frames using ByteTrack.
5. Generate timestamp-based summaries.
6. Export results in JSON format.

## 👨‍💻 Author

**Mohit Choudhary**

GitHub: https://github.com/mohit821967
