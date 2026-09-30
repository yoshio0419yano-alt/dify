from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
 
template = PromptTemplate.from_template("{keyword}を解説するQiita記事のタイトル案は?")
prompt = template.format(keyword="Python")

chat = ChatOllama(model="gemma3:1b")
result = chat.invoke(prompt)
print(result.text)