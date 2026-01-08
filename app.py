import streamlit as st

st.set_page_config(page_title="Inuit Chatbot", layout="centered")

st.title("👞 Inuit Luxury Footwear Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def bot_reply(user_msg: str) -> str:
    msg = user_msg.lower().strip()

    if msg in ["hi", "hello", "hey", "start"]:
        return (
            "👋 **Welcome to Inuit Luxury Footwear!**\n\n"
            "We craft premium, handcrafted shoes using high-quality leather.\n\n"
            "What would you like to explore?\n"
            "- Men Shoes\n"
            "- Women Shoes\n"
            "- Luxury Boots"
        )

    if any(k in msg for k in ["men", "women", "boot"]):
        return "Great choice! Which style do you prefer?\n- Formal\n- Casual\n- Party Wear"

    if msg in ["formal", "casual", "party wear", "party"]:
        return "Perfect 👍 What is your shoe size? (6–11)"

    if msg.isdigit():
        return (
            "🛠️ **How Inuit Shoes Are Made**\n\n"
            "🎥 https://www.youtube.com/watch?v=VIDEO1\n"
            "🎥 https://www.youtube.com/watch?v=VIDEO2\n"
            "🎥 https://www.youtube.com/watch?v=VIDEO3\n\n"
            "Would you like to place an order for **home delivery**? (Yes / No)"
        )

    if msg in ["yes", "y"]:
        return (
            "🎉 **Order Request Received!**\n\n"
            "Our team will contact you shortly to confirm delivery details.\n"
            "Thank you for choosing Inuit."
        )

    if msg in ["no", "n"]:
        return "No problem 😊 Feel free to explore our collection anytime."

    return "🤔 I didn’t understand that. Please type **hi** to restart."

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    reply = bot_reply(user_input)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
