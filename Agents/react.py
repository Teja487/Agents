#from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import initialize_agent, tool
#from langchain_community.tools import TavilySearchResults
import datetime
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.tools import Tool

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

#search_tool = TavilySearch(search_depth="basic")

search_tool = Tool(
    name="Search",
    func=lambda query: TavilySearch().invoke({"query": query}),
    description="Search the web for information based on the query.",
)

@tool
def get_system_time(format: str = "%Y-%m-%d %H:%M:%S"):
    """ Returns the current date and time in the specified format """

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime(format)
    return formatted_time


tools = [search_tool, get_system_time]

agent = initialize_agent(tools=tools, llm=llm, agent="zero-shot-react-description", verbose=True)

agent.invoke("When was SpaceX's last launch and how many days ago was that from this instant")