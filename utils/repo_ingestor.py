import os
from utils.code_chunker import chunk_python_code
from embeddings.chroma_manager import store_chunks

def get_python_files(repo_path):

    python_files = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [

            directory

            for directory in dirs

            if directory not in [
                "venv",
                "__pycache__",
                ".git"
            ]
        ]

        for file in files:

            if file.endswith(".py"):

                full_path = os.path.join(
                    root,
                    file
                )

                python_files.append(full_path)

    return python_files

def read_file(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()

def index_repository(repo_path):

    python_files = get_python_files(repo_path)

    for file_path in python_files:

        code = read_file(file_path)

        chunks = chunk_python_code(code)

        for chunk in chunks:

            chunk["file_path"] = file_path

        store_chunks(chunks)