from crewai_tools import YoutubeChannelSearchTool
from dotenv import load_dotenv

load_dotenv()

# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="https://www.youtube.com/@krishnaik06",
    config=dict(loader=dict(max_videos=50))
)