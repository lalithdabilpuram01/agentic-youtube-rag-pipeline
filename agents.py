import os
from crewai import Agent
from dotenv import load_dotenv

from tools import yt_tool

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

# Creating a Senior Blog content researcher
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Get the video transcription for the topic {topic} from the provided Yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in Understanding videos in AI Data Science, Machine Learning and Gen AI and providing suggestion"
    ),
    tools=[yt_tool],
    allow_delegation=True,
)

# Creating a blog writer agent with Yt tool
blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from Yt video",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False,
)
