
from mcp.server.fastmcp import FastMCP

from backend.services.video_service import extract_video_frames
from backend.services.detection_service import detect_objects

mcp = FastMCP("Video Intelligence Server")


@mcp.tool()
def extract_video_frames_tool(
    video_path: str,
    interval_seconds: int = 2
) -> dict:
    """
    Extract frames from an MP4 video at configurable intervals.
    """

    result = extract_video_frames(
        video_path,
        interval_seconds
    )

    return result


@mcp.tool()
def detect_objects_tool(
    video_path: str,
    interval_seconds: int = 2
) -> list:
    """
    Detect objects in extracted video frames using YOLO.
    """

    frames = extract_video_frames(
        video_path,
        interval_seconds
    )

    results = detect_objects(frames["frames"])

    return results


if __name__ == "__main__":
    mcp.run()
