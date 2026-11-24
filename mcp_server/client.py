
import asyncio
import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


server_params = StdioServerParameters(
    command="python",
    args=["-m", "mcp_server.server"],
)


async def main():

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("\nConnected to MCP Server!")

            # List MCP tools
            tools = await session.list_tools()

            print("\nAvailable MCP Tools:")
            for tool in tools.tools:
                print("-", tool.name)

            # Extract frames
            print("\nExecuting extract_video_frames...")

            frames_result = await session.call_tool(
                "extract_video_frames_tool",
                arguments={
                    "video_path": "uploads/sample.mp4",
                    "interval_seconds": 2
                }
            )

            print("\nFrame Extraction Result:")

            if frames_result.isError:
                print("Frame extraction failed")
                return

            for item in frames_result.content:
                if hasattr(item, "text"):
                    print(item.text[:1000])

            # Detect objects
            print("\nExecuting detect_objects...")

            detection_result = await session.call_tool(
                "detect_objects_tool",
                arguments={
                    "video_path": "uploads/sample.mp4",
                    "interval_seconds": 2
                }
            )

            print("\nObject Detection Result:")

            if detection_result.isError:
                print("Object detection failed")
                return

            for item in detection_result.content:
                if hasattr(item, "text"):
                    try:
                        data = json.loads(item.text)

                        if isinstance(data, list):
                            print("Total frames processed:", len(data))

                            for frame in data:
                                print(
                                    "\nTimestamp:", frame["timestamp"],
                                    "\nImage:", frame["image_path"],
                                    "\nDetections:", frame["detections"]
                                )
                        else:
                            print(json.dumps(data, indent=2))

                    except json.JSONDecodeError:
                        print(item.text)


if __name__ == "__main__":
    asyncio.run(main())
