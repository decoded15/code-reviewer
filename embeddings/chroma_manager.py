import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="codebase"
)

def generate_embedding(text):

    embedding = embedding_model.encode(text)

    return embedding.tolist()

def store_chunks(chunks):
    for chunk in chunks:
        embedding = generate_embedding(
            chunk["code"]
        )
        try:

                    collection.add(

                        ids=[
                            f"{chunk['file_path']}_{chunk['name']}"
                        ],

                        embeddings=[embedding],

                        documents=[chunk["code"]],

                        metadatas=[
                            {
                                "type": chunk["type"],
                                "file_path": chunk["file_path"]
                            }
                        ]
                    )

        except Exception as e:

                    print(f"Skipping duplicate: {e}")                