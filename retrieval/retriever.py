from embeddings.chroma_manager import collection

def retrieve_relevant_code(query, n_results=3):

    results = collection.query(

        query_texts=[query],

        n_results=n_results
    )

    retrieved_chunks = []

    documents = results["documents"][0]

    metadatas = results["metadatas"][0]

    for document, metadata in zip(
        documents,
        metadatas
    ):

        formatted_chunk = f"""
            File: {metadata.get('file_path', 'Unknown')}

            Code:
            {document}
        """

        retrieved_chunks.append(
            formatted_chunk
        )

    return "\n\n".join(
        retrieved_chunks
    )