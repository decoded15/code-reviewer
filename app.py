import streamlit as st
from utils.file_handler import read_uploaded_file

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

uploaded_code = ""

if uploaded_file is not None:
    uploaded_code = read_uploaded_file(uploaded_file)

final_code = uploaded_code if uploaded_code else code_input

review_button = st.button("Review Code")

if review_button:

    if not final_code.strip():
        st.warning("Please paste code or upload a file")

    else:
        st.success("Code received successfully!")