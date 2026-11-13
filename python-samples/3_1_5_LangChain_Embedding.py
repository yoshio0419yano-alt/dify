from langchain_ollama.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="embeddinggemma")
query_result = embeddings.embed_query("美しいジョークを教えて。")
print(len(query_result))
print(query_result)