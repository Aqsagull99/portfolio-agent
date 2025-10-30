from agents import function_tool

#Introduction Tool
@function_tool
async def introduction():
    return (
        "Hi, I'm **Aqsa Gull** — a passionate Web Developer and Agentic AI enthusiast. "
        "I specialize in building responsive websites, automation tools, and intelligent agentic systems "
        "using TypeScript, Next.js, Tailwind CSS, and n8n."
    )

# Skills Tool
@function_tool
async def get_skills():
    skills = [
        "HTML", "CSS", "JavaScript", "TypeScript","python",
        "React'js", "Next.js", "Tailwind CSS","agent Kit",
        "Node.js", "n8n Automation", "AI Integration", "Git & GitHub"
    ]
    return "My Core Skills:\n- " + "\n- ".join(skills)

#  Experience Tool
@function_tool
async def get_experience():
    return (
        " Experience:\n"
        "- Working as an **Agentic AI Developer** at Governor House (GIAIC).\n"
        "- Hands-on experience with automation workflows and web development.\n"
        "- Building intelligent systems that combine AI + Frontend + Automation."
    )

# Projects Tool
@function_tool
async def get_projects():
    projects = [
        {"name": "Contact Management System", "desc": "CLI tool built with TypeScript & Inquirer."},
        {"name": "Student Management System", "desc": "Manages student data with TypeScript CLI."},
        {"name": "Responsive Portfolio Website", "desc": "Built using Next.js and Tailwind CSS."},
        {"name": "AI Automation Agent", "desc": "Integrated AI with n8n for smart task handling."}
    ]
    response = "My Projects:\n"
    for p in projects:
        response += f"- **{p['name']}** → {p['desc']}\n"
    return response

# 🌐 Social Links Tool
@function_tool
async def get_social_links():
    socials = {
        "LinkedIn":"linkedin.com/in/aqsa-gullofficial99",
        "GitHub": "https://github.com/aqsagull99",
        "FaceBook": "https://www.facebook.com/Aqsagullofficial/.",
        "Twitter (X)": "https://x.com/AqsaGull9889"
    }
    return "My Social Profiles:\n" + "\n".join([f"- {k}: {v}" for k, v in socials.items()])

# 📜 Resume Tool
@function_tool
async def download_resume():
    return "You can download my resume here: https://your-website.com/Aqsa_Resume.pdf"

#  Achievements Tool
@function_tool
async def get_achievements():
    achievements = [
        "Completed Web Development training at Governor House IT Initiative.",
        " Built custom AI portfolio agent using FastAPI + Next.js.",
        "Created multiple CLI tools for learning automation with TypeScript."
    ]
    return "Achievements:\n- " + "\n- ".join(achievements)

# Fun Fact Tool
@function_tool
async def fun_fact():
    return "Fun Fact: I enjoy debugging code while sipping coffee  and love making tech learning fun for others!"

# 🪄 Name Tool
@function_tool
def aqsa_name() -> str:
    return "Aqsa Gull"
