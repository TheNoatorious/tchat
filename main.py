from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

# Chat start by user input
prompt = ChatPromptTemplate(
    input_variables=["content"],
    messages=[
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# Model used
chain = LLMChain(
    llm=chat, 
    prompt=prompt
)

# The AI chat
while True:
    content = input(">>")
    result = chain({"content": content}) 
    print(result["text"])