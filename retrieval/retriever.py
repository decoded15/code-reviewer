from embeddings.chroma_manager import collection

def retrieve_relevant_code(query, n_results=3):
    results = collection.query(
        query_texts = [query],
        n_results = n_results   
    )

    return results["documents"][0]