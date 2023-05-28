from my_pinecone import upsert_vectors
from openai_setup import connect_openai
from text_preprocess import pdf_to_chunks
from embedding import get_embeddings


def upser_to_db(file,file_name):

    # OpenAI API setting
    connect_openai()

    # Given filename, generates chunks of text
    chunks = pdf_to_chunks(file)

    # Given chunks of text, it creates a df with 3 columns:  id | text(chunk) | embedding
    df = get_embeddings(chunks)

    # Upload the Vector Embeddings and Text into Pinecone Database
    upsert_vectors(df,file_name)

    return

