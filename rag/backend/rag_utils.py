import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import TokenTextSplitter 

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Set OpenAI API key
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")
os.environ["OPENAI_API_KEY"] = api_key


documents = SimpleDirectoryReader("data").load_data()

embedding_model = OpenAIEmbedding(model="text-embedding-3-small")

text_splitter = TokenTextSplitter(chunk_size=512, chunk_overlap=50)  # Adjust as needed
chunked_documents = []
for doc in documents:
    chunks = text_splitter.split_text(doc.text)  # Split document into smaller parts
    for chunk in chunks:
        chunked_documents.append(chunk)

llm = OpenAI(model="gpt-4-turbo")

query_engine = index.as_query_engine(llm=llm)
response = query_engine.query("What is this document about?")

print(response)


