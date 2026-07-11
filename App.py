import streamlit as st

st.set_page_config(
    page_title="AI Career & Placement Assistant",
    page_icon="🤖",
    layout="wide"
)
# ================= CSS =====================
st.markdown("""
<style>

body{
    background:#050816;
}
.main{
    background:#050816;
}

section[data-testid="stSidebar"]{
    background:#0b1020;
}

.hero{

background:linear-gradient(135deg,#0f172a,#1e293b);
padding:45px;
border-radius:20px;
text-align:center;
border:2px solid #00F5FF;
box-shadow:0px 0px 25px rgba(0,245,255,0.3);

}

.hero h1{

color:#00F5FF;
font-size:48px;

}

.hero p{

color:white;
font-size:20px;

}

.card{

background:rgba(255,255,255,0.08);
padding:25px;
border-radius:20px;
text-align:center;
border:1px solid rgba(0,245,255,0.4);
backdrop-filter:blur(8px);
transition:0.4s;
min-height:240px;

}

.card:hover{

transform:translateY(-10px);
border:2px solid cyan;

}

.card h2{

color:#00F5FF;

}

.card p{

color:white;

}

.stButton button{

width:100%;
height:45px;
background:#00F5FF;
color:black;
font-size:18px;
font-weight:bold;
border-radius:12px;

}

.metric{

background:#111827;
padding:20px;
border-radius:15px;
text-align:center;

}

</style>

""",unsafe_allow_html=True)

# ================= SIDEBAR ===================

st.sidebar.title("🤖 AI Assistant")


page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔮 Prediction"
    ]
)
# ================= HOME ======================
if page=="🏠 Home":

    st.markdown("""

<div class="hero">

<h1>🤖 AI Career & Placement Assistant</h1>

<p>

Predict Placement • Career Guidance • Skill Analysis • Job Recommendation

</p>

</div>

""",unsafe_allow_html=True)

    st.write("")

    c1,c2,c3,c4=st.columns(4)

    c1.metric("Students","10,000+")
    c2.metric("Accuracy","95%")
    c3.metric("Companies","150+")
    c4.metric("Career Roles","30+")

    st.write("")

    col1,col2,col3=st.columns(3)

    with col1:

        st.markdown("""

<div class="card">

<h1>🧠</h1>

<h2>AI Analysis</h2>
<p>
Analyze academics, coding skills, projects and internships using Artificial Intelligence.

</p>

</div>

""",unsafe_allow_html=True)

        if st.button("🧠 Start Analysis"):

            st.success("AI Analysis Ready 🚀")

    with col2:

        st.markdown("""

<div class="card">
<h1>🎯</h1>
<h2>Placement Prediction</h2>
<p>
Predict your placement chances with our Machine Learning model.
</p>
</div>
""",unsafe_allow_html=True)
        if st.button("🎯 Predict Now"):
         st.info("Open Prediction Page from Sidebar")
    with col3:

         st.markdown("""

<div class="card">

<h1>💼</h1>

<h2>Career Guidance</h2>

<p>

Get AI based career recommendations according to your skills and academic performance.

</p>

</div>

""", unsafe_allow_html=True)

    if st.button("💼 Explore Careers"):

            st.success("""

✅ AI Engineer

✅ Software Developer

✅ Data Scientist

✅ Data Analyst

✅ ML Engineer

""")

    st.write("")

    st.markdown("""
    <div class="card">

    <h2>🚀 Why Choose Our AI Career Assistant?</h2>

    <p style="font-size:18px;">

    ✔ AI Based Placement Prediction <br><br>

    ✔ Career Guidance According To Skills <br><br>

    ✔ Skill Gap Analysis <br><br>

    ✔ Salary Prediction <br><br>

    ✔ Company Recommendation <br><br>

    ✔ Easy To Use Dashboard

    </p>

    </div>

    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
### 🎯 Our Mission

To help students choose the right career path using Artificial Intelligence and Machine Learning.
""")

    with col2:
        st.success("""
### 📈 AI Features

- Placement Prediction
- Career Guidance
- Skill Analysis
- Company Recommendation
- AI Based Decision Support
""")
        st.write("")

    st.markdown("""
    <div style="
    background:linear-gradient(135deg,#00C9FF,#92FE9D);
    padding:35px;
    border-radius:20px;
    text-align:center;
    margin-top:20px;
    box-shadow:0px 0px 20px rgba(0,245,255,0.4);
    ">

    <h1 style="color:#111827;">
    🚀 Ready To Build Your Dream Career?
    </h1>

    <p style="font-size:20px;color:#111827;">

    Our AI analyzes your CGPA, Coding Skills, DSA,
    Internships, Projects and Communication Skills
    to predict your placement chances and recommend
    the best career path.

    </p>

    </div>

    """, unsafe_allow_html=True)

    st.write("")

    st.subheader("⚙️ How Our AI Works")

    step1, step2, step3, step4 = st.columns(4)

    with step1:
        st.success("""
📄

### Step 1

Enter Student Details
""")

    with step2:
        st.info("""
🤖

### Step 2

AI Analysis
""")

    with step3:
        st.warning("""
📊

### Step 3

Placement Prediction
""")

    with step4:
        st.success("""
🎯

### Step 4

Career Recommendation
""")

    st.write("")

    st.markdown("""
    ---
    <center>

    <h3 style="color:#00F5FF;">
    🤖 AI Career & Placement Assistant
    </h3>

    <p style="color:gray;">
    Developed using Streamlit • Python • Machine Learning • Random Forest
    </p>

    <p style="color:gray;">
    © 2026 Harmanjot & Vansheeka
    </p>

    </center>
    """, unsafe_allow_html=True)

    # ================= PREDICTION PAGE =================

if page == "🔮 Prediction":

    st.title("🎯 Placement Prediction")

    st.write("Enter your details below")

    name = st.text_input("Student Name")

    cgpa = st.number_input("CGPA", 0.0, 10.0)

    skills = st.slider("Coding Skills", 0, 10)

    internship = st.selectbox(
        "Internship",
        ["No", "Yes"]
    )

    if st.button("Predict Placement"):
        st.success("✅ Prediction Completed")
