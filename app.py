import streamlit as st

st.set_page_config(page_title="Inuit Chatbot", layout="centered")
st.title("👞 Inuit Luxury Footwear Chatbot")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = "category"

if "category" not in st.session_state:
    st.session_state.category = None

if "style" not in st.session_state:
    st.session_state.style = None

# ---------------- VIDEO LINKS ----------------
VIDEOS = {
    ("Men Shoes", "Formal"): [
        "https://www.youtube.com/watch?v=JQH6E7G8KXw",
        "https://www.youtube.com/watch?v=R0ZJmXzR5iY",
        "https://www.youtube.com/watch?v=U6g6GJY4pNw",
    ],
    ("Men Shoes", "Casual"): [
        "https://www.youtube.com/watch?v=KkR6fJb7N5c",
        "https://www.youtube.com/watch?v=5X9zv0y6K2Y",
        "https://www.youtube.com/watch?v=1M8QxJ5xR2E",
    ],
    ("Men Shoes", "Party"): [
        "https://www.youtube.com/watch?v=7sZp8R8YF3A",
        "https://www.youtube.com/watch?v=ZQH4zj0FJ9A",
        "https://www.youtube.com/watch?v=qk2l7F2mX6A",
    ],
    ("Women Shoes", "Formal"): [
        "https://www.youtube.com/watch?v=V4M6F6T5D0M",
        "https://www.youtube.com/watch?v=YxF1Zp8N6X4",
        "https://www.youtube.com/watch?v=5N0YxR4jM3g",
    ],
    ("Women Shoes", "Casual"): [
        "https://www.youtube.com/watch?v=4Zt5F9Y2K3Q",
        "https://www.youtube.com/watch?v=8kM0X3EJ6FQ",
        "https://www.youtube.com/watch?v=Z8Qp2H3YJ4A",
    ],
    ("Women Shoes", "Party"): [
        "https://www.youtube.com/watch?v=ZqF3X1Y0T8M",
        "https://www.youtube.com/watch?v=4kM2Q6X9F1A",
        "https://www.youtube.com/watch?v=YQ5X6J9M8R4",
    ],
    ("Luxury Shoes", "Formal"): [
        "https://www.youtube.com/watch?v=UuG9lJ5K7Rk",
        "https://www.youtube.com/watch?v=YkJ4T9Z0X1Q",
        "https://www.youtube.com/watch?v=6RkJZQ1M8F0",
    ],
    ("Luxury Shoes", "Casual"): [
        "https://www.youtube.com/watch?v=FZ8Y0M4JQ2R",
        "https://www.youtube.com/watch?v=KJ9Z6R4M1XQ",
        "https://www.youtube.com/watch?v=JZQ8F6X4M1R",
    ],
    ("Luxury Shoes", "Party"): [
        "https://www.youtube.com/watch?v=8ZJ6Q1M4RFX",
        "https://www.youtube.com/watch?v=R4X6ZJ1M8FQ",
        "https://www.youtube.com/watch?v=QZJ6R8M1FX4",
    ],
}

# ---------------- STEP 1: CATEGORY ----------------
if st.session_state.step == "category":
    st.markdown(
        """
        👋 **Welcome to Inuit Luxury Footwear!**

        We craft premium handcrafted shoes using high-quality leather.

        **Which category would you like to explore?**
        """
    )

    category = st.radio(
        "Select category:",
        ["Men Shoes", "Women Shoes", "Luxury Shoes"]
    )

    if st.button("Next"):
        st.session_state.category = category
        st.session_state.step = "style"
        st.rerun()

# ---------------- STEP 2: STYLE ----------------
elif st.session_state.step == "style":
    st.markdown(
        f"You selected **{st.session_state.category}** 👌\n\n"
        "What style are you interested in?"
    )

    style = st.radio(
        "Choose style:",
        ["Formal", "Casual", "Party"]
    )

    if st.button("Show How They’re Made"):
        st.session_state.style = style
        st.session_state.step = "videos"
        st.rerun()

# ---------------- STEP 3: VIDEOS ----------------
elif st.session_state.step == "videos":
    st.markdown(
        f"🛠️ **How Inuit {st.session_state.category} ({st.session_state.style}) Are Made**"
    )

    for video in VIDEOS[(st.session_state.category, st.session_state.style)]:
        st.video(video)

    st.markdown("### What would you like to do next?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🛒 Place Order"):
            st.session_state.step = "order"
            st.rerun()

    with col2:
        if st.button("🔁 Explore Another Category"):
            st.session_state.step = "category"
            st.rerun()

# ---------------- STEP 4: ORDER ----------------
elif st.session_state.step == "order":
    choice = st.radio(
        "Would you like to place an order for home delivery?",
        ["Yes", "No"]
    )

    if st.button("Submit"):
        st.session_state.delivery = choice
        st.session_state.step = "end"
        st.rerun()

# ---------------- STEP 5: END ----------------
elif st.session_state.step == "end":
    if st.session_state.delivery == "Yes":
        st.success(
            "🎉 **Order Request Received!**\n\n"
            "Our team will contact you shortly to confirm delivery details.\n"
            "Thank you for choosing Inuit."
        )
    else:
        st.info(
            "No worries 😊\n\n"
            "You can continue exploring our collection."
        )

    if st.button("🔁 Explore More Shoes"):
        st.session_state.step = "category"
        st.rerun()
