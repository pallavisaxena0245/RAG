import os
from llama_index.llms import OpenAI 
from llama_index import VectorStoreIndex,SimpleDirectoryReader,ServiceContext,StorageContext,load_index_from_storage
from llama_index.embeddings.openai import OpenAIEmbedding
def load_documents(data_dir):
    documents = SimpleDirectoryReader(data_dir).load_data
    return documents


def create_or_load_index(data_dir , index_dir ="storage"):

    if not os.path.exists(index_dir):
        documents = load_documents(data_dir)
        llm = OpenAI(model="gpt-3.5-turbo")
        embed_model = OpenAIEmbedding()
        service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model)
        index = VectorStoreIndex.from_documents(documents, service_context = service_context)
        index.storage_context.persist(persist_dir = index_dir)
        return index
    
    else :
        storage_context = StorageContext.from_defaults(persist_dir = index_dir)
        index = load_index_from_storage(storage_context)
        return index
    
def query_index(index , query_text):

    query_engine = index.as_query_engine()
    response = query_engine.query(query_text)
    return str(response)


