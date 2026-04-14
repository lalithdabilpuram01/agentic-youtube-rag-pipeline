import os
from crewai import Crew, Process
from dotenv import load_dotenv

from agents import blog_writer, blog_researcher
from tasks import research_task, write_task

load_dotenv()

# Form the tech-focused crew with specific configurations
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Start the task execution process
result = crew.kickoff(inputs={'topic': 'AI VS ML VS DL vs Data Science'})

print(result)