from agents import Agent
from tools.user_tools import (
    introduction,
    get_skills,
    get_experience,
    get_projects,
    get_social_links,
    download_resume,
    get_achievements,
    fun_fact,
    aqsa_name

)

my_agent = Agent(
    name="Portfolio Guide Agent",
    instructions="You are 'Aqsa gull Assistant', a friendly guide. Use available tools to answer questions.",
    tools=[introduction, get_skills, get_experience, get_projects, get_social_links, download_resume, get_achievements, fun_fact, aqsa_name],
)
