import pinecone
from embedding import get_embedding
from text_preprocess import text_to_docs

# Returns the pinecone index for upserting / querying
def get_pinecone_index():
    # Pinecone Setup
    api_key_pinecone = "7e933d75-ab2f-4d68-8a20-dad4cc384308"
    pinecone_environment = "us-west4-gcp-free"
    index_name = 'test'
    pinecone.init(api_key=api_key_pinecone,environment=pinecone_environment)
    pinecone_index = pinecone.Index(index_name=index_name)
    return pinecone_index


# Upserts all the text and embeddings provided in df
def upsert_vectors(df,file_name):
    pinecone_index = get_pinecone_index()
    for i, row in df.iterrows():
        pinecone_index.upsert(
        vectors=[
            {
            'id':f"{row['id']}-{i}", 
            'values':row['embed'], 
            'metadata':{'text': row['text'],'file_name':file_name}
            }
        ],
    )
    return


# Querying the Pinecone DB and returns top-k similar chunks of text as langchain.Documents
def get_context(query,top_k=3):
    pinecone_index = get_pinecone_index()
    embedded_query = get_embedding(query)

    # Querying db

    query_response = pinecone_index.query(
    top_k=top_k,
    include_values=True,
    include_metadata=True,
    vector=embedded_query
    )

    # Collecting text from query response
    text = ''
    for i in range(0,3):
        text+=query_response['matches'][i]['metadata']['text']

    # converting text into langchan.Documents to be used as input to ChatGPT
    docs = text_to_docs(text)

    return docs