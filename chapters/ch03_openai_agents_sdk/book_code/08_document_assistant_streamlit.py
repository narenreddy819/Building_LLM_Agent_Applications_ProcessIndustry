import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

# --------------------------------------------------
# Setup
# --------------------------------------------------
load_dotenv()
client = OpenAI()

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Document Q&A Assistant",
    layout="wide"
)

# --------------------------------------------------
# Custom Styling
# --------------------------------------------------
st.markdown("""
<style>
section[data-testid="stSidebar"] {
    background: #f8fafc;
    border-right: 1px solid #e5e7eb;
}

.app-header {
    text-align: center;
}

.st-key-clear_document_btn button {
    background: #ef4444;
    color: white;
    border: 1px solid #dc2626;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------
st.session_state.setdefault("file_id", None)
st.session_state.setdefault("file_name", None)
st.session_state.setdefault("chat_history", [])

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown("""
<div class="app-header">
    <h1>📄 Document Q&A Assistant</h1>
    <p>Upload a PDF document and ask questions about its content.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
with st.sidebar:

    st.subheader("📤 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        label_visibility="collapsed"
    )

    # Upload only when new file selected
    if uploaded_file and st.session_state.file_name != uploaded_file.name:

        with st.spinner("Uploading to OpenAI..."):

            file = client.files.create(
                file=uploaded_file,
                purpose="user_data"
            )

            st.session_state.file_id = file.id
            st.session_state.file_name = uploaded_file.name
            st.session_state.chat_history = []

    # Show uploaded file
    if st.session_state.file_id:

        st.success(st.session_state.file_name)

        if st.button(
            "🗑️ Clear Document",
            use_container_width=True,
            key="clear_document_btn"
        ):
            st.session_state.file_id = None
            st.session_state.file_name = None
            st.session_state.chat_history = []
            st.rerun()

# --------------------------------------------------
# Main Chat Area
# --------------------------------------------------
with st.container(border=True):

    if st.session_state.file_id:

        st.write(
            f"**Currently analyzing:** "
            f"{st.session_state.file_name}"
        )

        # Display chat history
        for chat in st.session_state.chat_history:

            with st.chat_message("user"):
                st.write(chat["question"])

            with st.chat_message("assistant"):
                st.write(chat["answer"])

                with st.expander("Usage Statistics"):
                    st.write(
                        f"Tokens used: {chat['tokens']:,}"
                    )

        # Chat input
        question = st.chat_input(
            "Ask a question about the document..."
        )

        if question:

            with st.chat_message("user"):
                st.write(question)

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):

                    response = client.responses.create(
                        model="gpt-5-nano",
                        input=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "input_file",
                                        "file_id":
                                        st.session_state.file_id
                                    },
                                    {
                                        "type": "input_text",
                                        "text": question
                                    }
                                ]
                            }
                        ]
                    )

                    st.write(response.output_text)

                    with st.expander(
                        "Usage Statistics"
                    ):
                        st.write(
                            f"Tokens used: "
                            f"{response.usage.total_tokens:,}"
                        )

                    # Save history
                    st.session_state.chat_history.append(
                        {
                            "question": question,
                            "answer": response.output_text,
                            "tokens":
                            response.usage.total_tokens
                        }
                    )

    else:
        st.info(
            "📄 Upload a PDF document to get started."
        )
        