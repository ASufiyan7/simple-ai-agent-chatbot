import streamlit as st
import requests

st.set_page_config(page_title="Chatbot", page_icon=":robot_face:")
st.title("AI Chatbot")

# Sidebar Configuration
with st.sidebar:
    st.header("Configuration")
    system_prompt = st.text_area(
        "System Prompt",
        value=(
            "You are a helpful and highly capable AI assistant with access to several tools. "
            "You must use the available tools to answer questions whenever possible. "
            "If a question requires calculations, use the calculator tools. "
            "For general knowledge or information that can't be answered by other tools, "
            "use the search tool. "
            "Always try to provide a concise and direct answer using the tool's output. "
            "If you use a tool, show your reasoning and the tool output if it helps clarity."
        ),
        height=250,
    )
    allow_search = st.checkbox("Allow Search", value=True)
    model_name = st.selectbox("Select Model", ["llama3-8b-8192", "llama3-70b-8192"])

    # Clear Chat History Button
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun() 

# Chat History Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display Chat History
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input Handling
if user_input := st.chat_input("Ask me anything..."):
    # Add user message to history and display it
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and Display AI Response
    with st.chat_message("ai"):
        with st.spinner("Thinking..."):
            try:
                # Prepare the full message history for the payload
                message_history = [msg["content"] for msg in st.session_state.chat_history]

                payload = {
                    "model_name": model_name,
                    "model_provider": "groq",
                    "system_prompt": system_prompt,
                    "messages": message_history,
                    "search": allow_search,
                }

                api_url = "http://127.0.0.1:9999/api/get_response"
                res = requests.post(api_url, json=payload)
                res.raise_for_status()
                
                response_data = res.json()
                ai_response = response_data.get("response", "Error: No response field in answer.")

                st.markdown(ai_response)
                
                # Add AI response to history
                st.session_state.chat_history.append({"role": "ai", "content": ai_response})

            except requests.exceptions.RequestException as e:
                error_message = f"API Connection Error: {e}"
                st.error(error_message)
                st.session_state.chat_history.append({"role": "ai", "content": error_message})
            except Exception as e:
                error_message = f"An unexpected error occurred: {e}"
                st.error(error_message)
                st.session_state.chat_history.append({"role": "ai", "content": error_message})