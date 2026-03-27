import streamlit as st
import datetime
import psycopg2
import base64
import os

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("media/Background.png")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown("""
<style>
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(5, 10, 25, 0.75); /* DARK OVERLAY */
    z-index: -1;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.block-container {
    background: rgba(20, 25, 45, 0.6);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 40px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
input, textarea, .stSelectbox div {
    background-color: rgba(255,255,255,0.1) !important;
    color: white !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(10, 15, 30, 0.75);
        z-index: -1;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.set_page_config(page_title="CaliperAI", layout="centered")

# ---------- DB CONNECTION ----------
def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="caliper",
        user="postgres",
        password="yourpassword"
    )

# ---------- SIDEBAR ----------
with st.sidebar:
    st.image("media/first_logo.png", width=200)
    st.write("Capture reality.")
    st.write("Visualize and Mine.")
    st.write("Create ground truth")
    st.markdown(
    '[Watch Products Demo](https://youtu.be/JAlBa2x-j_0?si=6WB4mr8v_9vD_sTR)',
    unsafe_allow_html=True
)

# ---------- MAIN ----------
st.markdown("## 🎬 See CaliperAI in Action")

# ---------- FORM ----------
with st.form("demo_form"):

    st.subheader("📌 Demo Details")

    product = st.selectbox(
        "Select Product",
        ["CaliperGT", "CaliperMedGT", "CaliperOwl", "CaliperCapture (Data Logging)"]
    )

    col1, col2 = st.columns(2)

    with col1:
        email = st.text_input("Email")

    with col2:
        number = st.text_input("Phone Number")

    institution = st.text_input("Institution/Company")

    user_input = st.text_area("How do you plan to use this product?")

    date = st.date_input(
        "Preferred Demo Date",
        min_value=datetime.date.today()
    )

    submitted = st.form_submit_button("🚀 Request Demo")

# ---------- SUBMISSION ----------
if submitted:
    if not email or not number:
        st.error("⚠️ Please fill in all required fields.")
    else:
        st.success("✅ Demo request submitted successfully!")

        st.markdown("### 📋 Your Details")
        st.write(f"**Product:** {product}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {number}")
        st.write(f"**Institution:** {institution}")
        st.write(f"**Date:** {date}")

        if user_input:
            st.write(f"**Use Case:** {user_input}")

        st.info(f"Our team will contact you shortly regarding **{product}** 🚀")
        st.info("In the meantime, feel free to view the videos of the product that you just selected [{product}] ")

        conn = connect_db()
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO users (product, email, phone, demo_date, request, institution)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (product, email, number, date, user_input, institution))

        conn.commit()
        cur.close()
        conn.close()

        st.success("💾 Data saved to database!")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("© 2026 CaliperAI | All rights reserved")