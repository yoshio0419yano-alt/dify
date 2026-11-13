from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

prompt_template = "{adjective}ジョークを教えてください"
prompt = PromptTemplate(
    input_variables=["adjective"], template=prompt_template
)
chat = ChatOllama(model="gemma3:1b")

chain = prompt | chat
result = chain.invoke({"adjective": "美しい"})
print(result.text)