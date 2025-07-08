from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

generation_prompt  = ChatPromptTemplate.from_messages(

    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked with writing excellent twitter posts."
            "Generate the best twitter post for user's request"
            "If the user provides the critique, respond with the revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for user's tweet."
            "Always provide detailed recommendations, including requests for length, virality, style, etc."
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

#llm = ChatGoogleGenerativeAI(model = "gemini-2.5-pro")
llm = ChatOpenAI(model = "gpt-4o")

generation_chain = generation_prompt | llm
reflection_chain = reflection_prompt | llm