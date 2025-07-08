from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import datetime
from langchain_openai import ChatOpenAI
from schema import AnswerQn
from langchain_core.output_parsers.openai_tools import PydanticToolsParser
from langchain_core.messages import HumanMessage


llm = ChatOpenAI(model="gpt-4o")
pydantic_parser = PydanticToolsParser(tools=[AnswerQn])
#Actor Agent
actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are AI researcher.
            Current time: {time}
            
            1. {first_instruction}
            2. Reflect and critique your answer. Be severe to maximize improvement.
            3. After the reflection, **list 1-3 search query separately** for researching improvements.
            Do not include them in the improvements.""",
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system","Answer the user's question above using the required format."),
    ]
).partial(
    time = lambda: datetime.datetime.now().isoformat(),
)


first_responder_prompt_template = actor_prompt_template.partial(
    first_instruction = "Provide a detailed ~250 word description"
)

first_responder_chain = first_responder_prompt_template | llm.bind_tools(
    tools = [AnswerQn],tool_choice="AnswerQn") | pydantic_parser


response = first_responder_chain.invoke(
    {"messages" : [HumanMessage(content="Write a blog describing how small business can leverage to grow using AI")]
})

print(response)


