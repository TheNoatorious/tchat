from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

# Add additional key of messages
memory = ConversationBufferMemory(memory_key="messages", return_messages=True)

# Chat start by user input
prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# Model used
chain = LLMChain(
    llm=chat, 
    prompt=prompt,
    memory=memory
)

# The AI chat
while True:
    content = input(">>")
    result = chain({"content": content}) 
    print(result["text"])