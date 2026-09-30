from langchain_ollama.chat_models import ChatOllama
 
chat = ChatOllama(model="gemma3:1b")
result = chat.invoke("こんにちは。あなたは誰？")
print(result.text)