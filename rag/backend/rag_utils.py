import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Set OpenAI API key
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")
os.environ["OPENAI_API_KEY"] = api_key


documents = SimpleDirectoryReader("data").load_data()

embedding_model = OpenAIEmbedding(model="text-embedding-3-small")


llm = OpenAI(model="gpt-4-turbo")
print(llm)


