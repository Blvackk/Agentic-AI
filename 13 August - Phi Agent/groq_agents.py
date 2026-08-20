from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Groq(id="openai/gpt-oss-20b"),
    markdown=True,
)

agent.print_response("Tell me about Nvidia stock")