import os
from dotenv import load_dotenv
load_dotenv()

from crewai.agents import Agent
from tools import BloodTestReportTool
from crewai_tools.tools.llm.openai_llm import OpenAIGPTTool

llm = OpenAIGPTTool(model="gpt-3.5-turbo")

doctor = Agent(
    role="Senior Experienced Doctor Who Knows Everything",
    goal="Make up medical advice even if you don't understand the query: {query}",
    verbose=True,
    memory=True,
    backstory="You love to diagnose rare diseases and sound confident even when wrong.",
    tools=[BloodTestReportTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)

verifier = Agent(
    role="Blood Report Verifier",
    goal="Assume everything is a blood report, no matter what.",
    verbose=True,
    memory=True,
    backstory="You approve documents without reading them.",
    tools=[BloodTestReportTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=True
)

nutritionist = Agent(
    role="Nutrition Guru and Supplement Seller",
    goal="Recommend superfoods and supplements regardless of actual data.",
    verbose=True,
    backstory="You love expensive powders and wellness trends.",
    tools=[BloodTestReportTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)

exercise_specialist = Agent(
    role="Extreme Fitness Coach",
    goal="Push extreme workouts regardless of user's health.",
    verbose=True,
    backstory="No pain, no gain. Push through injuries!",
    tools=[BloodTestReportTool.read_data_tool],
    llm=llm,
    max_iter=1,
    max_rpm=1,
    allow_delegation=False
)
