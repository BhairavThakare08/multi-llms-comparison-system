import streamlit as st
import time
# import speech_recognition as sr
import pandas as pd

from models.gemini_model import run_gemini
from models.groq_model import run_groq
from models.openrouter import run_openrouter
from utils.metrics import calculate_metrics

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Multi LLM Dashboard",
    layout="wide"
)

# ================= SESSION STATE =================
if "results" not in st.session_state:
    st.session_state.results = {}

if "question_text" not in st.session_state:
    st.session_state.question_text = ""

# ================= VOICE FUNCTION =================
"""
def voice_to_text():

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    try:

        with mic as source:

            st.info("🎤 Listening... Please speak")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)

        return text

    except:
        return "Voice recognition error"
"""

# ================= DARK UI =================
st.markdown("""
<style>

/* Hide Streamlit Header */
header {
    visibility: hidden;
}

/* Remove Top Space */
.block-container {
    padding-top: 1rem;
}

/* Main App */
.stApp {
    background-color: #000000;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0a0a0a;
    border-right: 1px solid #222222;
}

/* Main Title */
h1 {
    color: white !important;
    text-align: center;
    font-size: 42px !important;
    font-weight: bold;
}

/* Subheaders */
h2, h3 {
    color: white !important;
}

/* Cards */
.card {
    padding: 20px;
    border-radius: 16px;
    background: #111111;
    border: 1px solid #222222;
    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    margin-bottom: 20px;
    color: white;
}

/* Card Headings */
.card h4 {
    color: #00c8ff;
    font-size: 22px;
    margin-bottom: 10px;
}

/* Buttons */
.stButton > button {

    width: 100%;
    border-radius: 10px;
    background-color: #00c8ff;
    color: black;
    font-weight: bold;
    padding: 10px;
    font-size: 16px;
    border: none;
    transition: 0.3s;
}

/* Button Hover */
.stButton > button:hover {

    background-color: #009dca;
    color: white;
}

/* Text Area */
textarea {

    background-color: #111111 !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid #333333 !important;
}

/* Labels */
label {
    color: white !important;
}

/* MultiSelect */
.stMultiSelect div[data-baseweb="select"] {

    background-color: #111111 !important;
    color: white !important;
}

/* Table */
table {

    background-color: #111111 !important;
    color: white !important;
    border-collapse: collapse !important;
}

/* Table Header */
thead tr th {

    background-color: #1a1a1a !important;
    color: #00c8ff !important;
    font-size: 18px !important;
    border: 1px solid #333333 !important;
}

/* Table Rows */
tbody tr td {

    background-color: #111111 !important;
    color: white !important;
    border: 1px solid #222222 !important;
}

/* Success Box */
.stSuccess {

    background-color: #062b1f !important;
    color: #00ffae !important;
}

/* Warning Box */
.stWarning {

    background-color: #2b2106 !important;
    color: #ffd000 !important;
}

/* Divider */
hr {
    border-color: #222222 !important;
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown(
    "<h1>🚀 Multi-LLM Comparison Dashboard</h1>",
    unsafe_allow_html=True
)

# ================= MODELS =================
models = {

    "Gemini 2.5 Flash":
        lambda q: run_gemini(q),

    "Llama 3.1 8B (Groq)":
        lambda q: run_groq(q, "llama-3.1-8b-instant"),

    "DeepSeek V3 (OpenRouter)":
        lambda q: run_openrouter(q, "deepseek/deepseek-chat-v3"),
}

# ================= SIDEBAR =================
with st.sidebar:

    st.header("⚙️ Controls")

    st.subheader("💬 Select Models")

    selected_text = st.multiselect(
        "Choose Models",
        list(models.keys())
    )

    question = st.text_area(
        "Enter your prompt",
        value=st.session_state.question_text,
        height=150
    )

    # ================= VOICE INPUT =================
    """
    if st.button("🎤 Voice Input"):

        voice_text = voice_to_text()

        st.session_state.question_text = voice_text

        st.success(f"Recognized: {voice_text}")

        st.rerun()
    """

    # ================= COMPARE BUTTON =================
    if st.button("🚀 Compare Text Models"):

        if not selected_text:

            st.warning("Select at least one text model")

        elif not question.strip():

            st.warning("Enter a prompt")

        else:

            st.session_state.results = {}

            for model in selected_text:

                start = time.time()

                answer = models[model](question)

                end = time.time()

                metrics = calculate_metrics(
                    start,
                    end,
                    answer
                )

                st.session_state.results[model] = {

                    "answer": answer,
                    "time": metrics["time"],
                    "words": metrics["words"]
                }

# ================= RESULTS =================
if st.session_state.results:

    st.subheader("📊 LLM Responses")

    for model in st.session_state.results:

        st.markdown(
            f"<div class='card'><h4>🤖 {model}</h4>",
            unsafe_allow_html=True
        )

        st.write(
            st.session_state.results[model]["answer"]
        )

        st.write(
            f"⏱ Time: {st.session_state.results[model]['time']} sec"
        )

        st.write(
            f"📝 Words: {st.session_state.results[model]['words']}"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    st.divider()

    # ================= COMPARISON TABLE =================
    st.subheader("📈 Model Comparison Table")

    results = st.session_state.results

    data = []

    for model in results:

        data.append({

            "Model": model,
            "Time (sec)": results[model]["time"],
            "Words": results[model]["words"]
        })

    df = pd.DataFrame(data)

    st.table(df)

    # ================= BEST MODEL =================
    fastest_model = df.loc[
        df["Time (sec)"].idxmin()
    ]["Model"]

    longest_model = df.loc[
        df["Words"].idxmax()
    ]["Model"]

    scores = {}

    for model in results:

        score = 0

        if model == fastest_model:
            score += 1

        if model == longest_model:
            score += 1

        scores[model] = score

    best_model = max(
        scores,
        key=scores.get
    )

    st.success(
        f"🏆 Best Model According to Comparison: {best_model}"
    )
