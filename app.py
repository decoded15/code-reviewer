import streamlit as st
from utils.file_handler import read_uploaded_file
from utils.prompt_builder import build_review_prompt
from utils.language_detector import detect_language
from services.llm_service import stream_review
from utils.ast_analyzer import (
    check_syntax,
    extract_functions,
    extract_imports
)
from utils.ast_analyzer import (
    check_syntax,
    extract_functions,
    extract_imports,
    detect_long_functions,
    detect_deep_nesting,
    detect_many_imports
)
from utils.code_chunker import chunk_python_code
from embeddings.chroma_manager import store_chunks
from retrieval.retriever import retrieve_relevant_code

st.set_page_config(
    page_title="Code Reviewer",
    page_icon="💻",
    layout="wide"
)

st.title("Code Reviewer")

st.markdown(
    """
    Upload your code or paste it below to get:
    - Bug detection
    - Code optimization suggestions
    - Readability improvements
    - Best-practice recommendations
    """
)

with st.sidebar:
    st.header("⚙️ Settings")

    review_type = st.selectbox(
        "Select Review Type",
        [
            "General Review",
            "Bug Detection",
            "Optimization",
            "Readability"
        ]
    )

code_input = st.text_area(
    "Paste Your Code Here",
    height=300,
    placeholder="Paste your Python, JavaScript, Java, C++, etc. code here..."
)

uploaded_file = st.file_uploader(
    "Or Upload a Code File",
    type=["py", "js", "java", "cpp", "c", "ts"]
)

if uploaded_file is not None:
    language = detect_language(uploaded_file.name)

uploaded_code = ""

if uploaded_file is not None:
    uploaded_code = read_uploaded_file(uploaded_file)

final_code = uploaded_code if uploaded_code else code_input

review_button = st.button("Review Code")

if review_button:

    if not final_code.strip():
        st.warning("Please paste code or upload a file")

    else:
        if language == "Python":

            is_valid, syntax_error = check_syntax(final_code)

            if not is_valid:

                st.error(f"Syntax Error Detected:\n{syntax_error}")

                st.stop()

            functions = extract_functions(final_code)

            imports = extract_imports(final_code)

            st.subheader("Code Structure Analysis")

            st.write("Functions:", functions)

            st.write("Imports:", imports)

            long_functions = detect_long_functions(final_code)

            deep_nesting = detect_deep_nesting(final_code)

            many_imports, import_count = detect_many_imports(final_code)

            st.subheader("Static Analysis")

            if long_functions:

                st.warning("Long Functions Detected")

                st.write(long_functions)

            if deep_nesting:

                st.warning("Deep Nesting Detected")

                st.write(deep_nesting)

            if many_imports:

                st.warning(
                    f"High Number of Imports Detected: {import_count}"
                )
            
            chunks = chunk_python_code(final_code)
            store_chunks(chunks)

        else:

            st.info(
                "AST analysis currently supports Python files only."
            )
        retrieved_code = retrieve_relevant_code(
            final_code
        )
        st.subheader("Retrieved Related Code")
        st.write(retrieved_code)
        prompt = build_review_prompt(
            code=final_code,
            review_type=review_type,
            language=language,
            functions=functions,
            imports=imports,
            long_functions=long_functions,
            deep_nesting=deep_nesting,
            import_count=import_count,
            retrieved_context=retrieved_code
        )

        st.success("Prompt built successfully!")

        with st.spinner("Reviewing code..."):

            review_container = st.empty()

            full_review = ""

            for chunk in stream_review(prompt):

                full_review += chunk

                review_container.markdown(full_review)