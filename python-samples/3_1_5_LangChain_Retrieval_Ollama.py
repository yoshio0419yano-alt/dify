from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_ollama.embeddings import OllamaEmbeddings

loader = PyPDFLoader("モデル就業規則.pdf")
pages = loader.load_and_split()
print(pages[0])

embeddings = OllamaEmbeddings(model="embeddinggemma")
chroma_index = Chroma.from_documents(pages, embeddings)
docs = chroma_index.similarity_search("一般社員の5年目ですが、有給休暇は何日ありますか？", k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content)