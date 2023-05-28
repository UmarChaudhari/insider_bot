from my_pinecone import get_context
from openai_setup import connect_openai, generate_answer


def query_db(query='',top_k=3):
    
    # Connecting with OpenAI to use embedding model
    connect_openai()

    # Retrieving the docs as context to answer query 
    context_docs = get_context(query,top_k)
    
    # Using ChatGPT to generate answer using query and context
    result = generate_answer(query,context_docs)
    
    return result
