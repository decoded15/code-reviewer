import streamlit as st

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

review_button = st.button("Review Code")