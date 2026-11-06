import streamlit as st

st.set_page_config(
    page_title="AI Career & Placement Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ================= CSS =================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root{
    --bg:#070b1a;
    --panel:#0f1629;
    --panel-2:#141c33;
    --border:rgba(0,245,255,0.18);
    --cyan:#00F5FF;
    --violet:#8b5cf6;
    --text:#e5e7eb;
    --muted:#94a3b8;
}

html, body, [class*="css"]{ font-family:'Inter',sans-serif; }

#MainMenu, footer, header{ visibility:hidden; }

.stApp{
    background:
        radial-gradient(900px 420px at 85% -5%, rgba(139,92,246,0.18), transparent 60%),
        radial-gradient(800px 400px at 5% 0%, rgba(0,245,255,0.12), transparent 60%),
        var(--bg);
    color:var(--text);
}
.block-container{ padding-top:2rem; max-width:1150px; }

section[data-testid="stSidebar"]{
    background:var(--panel);
    border-right:1px solid var(--border);
}

/* ---------- Hero ---------- */
.hero{
    background:linear-gradient(135deg, rgba(0,245,255,0.10), rgba(139,92,246,0.14));
    border:1px solid var(--border);
    border-radius:24px;
    padding:3rem 2rem;
    text-align:center;
    box-shadow:0 0 40px rgba(0,245,255,0.10);
}
.hero h1{
    font-size:2.8rem; font-weight:800; margin:0 0 .6rem 0;
    background:linear-gradient(90deg,#00F5FF,#8b5cf6);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent;
}
.hero p{ color:var(--text); font-size:1.1rem; margin:0; opacity:.9; }

/* ---------- Cards ---------- */
.card{
    background:var(--panel);
    border:1px solid var(--border);
    border-radius:18px;
    padding:1.6rem 1.3rem;
    text-align:center;
    min-height:230px;
    transition:all .25s ease;
}
.card:hover{
    transform:translateY(-6px);
    border-color:var(--cyan);
    box-shadow:0 12px 30px rgba(0,245,255,0.15);
}
.card .icon{ font-size:2.2rem; }
.card h3{ color:var(--cyan); margin:.6rem 0 .4rem 0; font-weight:700; font-size:1.2rem; }
.card p{ color:var(--muted); font-size:.95rem; margin:0; line-height:1.55; }

/* ---------- Section titles ---------- */
.section-title{
    font-size:1.5rem; font-weight:700; color:#fff;
    margin:2.2rem 0 1rem 0;
}
.section-title span{ color:var(--cyan); }

/* ---------- Metrics ---------- */
[data-testid="stMetric"]{
    background:var(--panel);
    border:1px solid var(--border);
    border-radius:16px;
    padding:1rem 1.2rem;
    text-align:center;
}
[data-testid="stMetricValue"]{ color:var(--cyan); font-weight:800; }
[data-testid="stMetricLabel"]{ color:var(--muted); justify-content:center; }

/* ---------- Steps ---------- */
.step{
    background:var(--panel);
    border:1px solid var(--border);
    border-radius:16px;
    padding:1.3rem 1rem;
    text-align:center;
}
.step .num{
    width:38px; height:38px; margin:0 auto .6rem auto;
    border-radius:50%;
    background:linear-gradient(135deg,#00F5FF,#8b5cf6);
    color:#050816; font-weight:800;
    display:flex; align-items:center; justify-content:center;
}
.step h4{ color:#fff; margin:0 0 .25rem 0; font-size:1rem; }
.step p{ color:var(--muted); margin:0; font-size:.88rem; }

/* ---------- Info panels ---------- */
.panel{
    background:var(--panel);
    border:1px solid var(--border);
    border-radius:18px;
    padding:1.6rem 1.5rem;
    height:100%;
}
.panel h3{ color:var(--cyan); margin-top:0; }
.panel p, .panel li{ color:var(--text); opacity:.9; line-height:1.7; }
.panel ul{ padding-left:1.1rem; margin:0; }

/* ---------- CTA ---------- */
.cta{
    background:linear-gradient(135deg,#00C9FF,#8b5cf6);
    border-radius:22px;
    padding:2.4rem 2rem;
    text-align:center;
    box-shadow:0 10px 40px rgba(0,201,255,0.25);
}
.cta h2{ color:#050816; margin:0 0 .5rem 0; font-weight:800; }
.cta p{ color:#0b1020; font-size:1.05rem; margin:0 auto; max-width:760px; }

/* ---------- Buttons ---------- */
.stButton > button, .stFormSubmitButton > button{
    width:100%;
    height:46px;
    background:linear-gradient(135deg,#00F5FF,#00b8d4);
    color:#050816;
    font-weight:700;
    font-size:1rem;
    border:none;
    border-radius:12px;
    transition:all .2s ease;
}
.stButton > button:hover, .stFormSubmitButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 20px rgba(0,245,255,0.35);
    color:#050816;
}

/* ---------- Inputs ---------- */
.stTextInput input, .stNumberInput input{
    background:var(--panel-2) !important;
    border-radius:10px !important;
}
.stSelectbox [data-baseweb="select"] > div{
    background:var(--panel-2) !important;
    border-radius:10px !important;
}

/* ---------- Footer ---------- */
.footer{
    text-align:center; margin-top:3rem; padding-top:1.5rem;
    border-top:1px solid var(--border);
}
.footer h4{ color:var(--cyan); margin:0 0 .3rem 0; }
.footer p{ color:var(--muted); font-size:.88rem; margin:.1rem 0; }
</style>
""",
    unsafe_allow_html=True,
)

# ================= SIDEBAR =================
st.sidebar.title("🤖 AI Assistant")
st.sidebar.caption("Career guidance powered by Machine Learning")
st.sidebar.divider()

page = st.sidebar.radio("Navigation", ["🏠 Home", "🔮 Prediction"])


# ================= HOME =================
if page == "🏠 Home":

    st.markdown(
        """
<div class="hero">
    <h1>🤖 AI Career &amp; Placement Assistant</h1>
    <p>Predict Placement &nbsp;•&nbsp; Career Guidance &nbsp;•&nbsp; Skill Analysis &nbsp;•&nbsp; Job Recommendation</p>
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    # NOTE: replace these with your real numbers
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Students", "10,000+")
    m2.metric("Accuracy", "95%")
    m3.metric("Companies", "150+")
    m4.metric("Career Roles", "30+")

    st.markdown('<div class="section-title">What we <span>offer</span></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
<div class="card">
    <div class="icon">🧠</div>
    <h3>AI Analysis</h3>
    <p>Analyze academics, coding skills, projects and internships using Artificial Intelligence.</p>
</div>
""",
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("🧠 Start Analysis"):
            st.success("AI Analysis Ready 🚀")

    with col2:
        st.markdown(
            """
<div class="card">
    <div class="icon">🎯</div>
    <h3>Placement Prediction</h3>
    <p>Predict your placement chances with our Machine Learning model.</p>
</div>
""",
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("🎯 Predict Now"):
            st.info("Open the Prediction page from the sidebar.")

    with col3:
        st.markdown(
            """
<div class="card">
    <div class="icon">💼</div>
    <h3>Career Guidance</h3>
    <p>Get AI-based career recommendations according to your skills and academic performance.</p>
</div>
""",
            unsafe_allow_html=True,
        )
        st.write("")
        if st.button("💼 Explore Careers"):
            st.success(
                "✅ AI Engineer  \n✅ Software Developer  \n✅ Data Scientist  \n"
                "✅ Data Analyst  \n✅ ML Engineer"
            )

    # ----- Why choose us + mission/features -----
    st.markdown('<div class="section-title">Why choose <span>us</span></div>', unsafe_allow_html=True)

    w1, w2 = st.columns(2)
    with w1:
        st.markdown(
            """
<div class="panel">
    <h3>🚀 Why Choose Our AI Career Assistant?</h3>
    <ul>
        <li>AI-based placement prediction</li>
        <li>Career guidance according to skills</li>
        <li>Skill gap analysis</li>
        <li>Salary prediction</li>
        <li>Company recommendation</li>
        <li>Easy-to-use dashboard</li>
    </ul>
</div>
""",
            unsafe_allow_html=True,
        )
    with w2:
        st.markdown(
            """
<div class="panel">
    <h3>🎯 Our Mission</h3>
    <p>To help students choose the right career path using Artificial Intelligence and Machine Learning.</p>
    <h3 style="margin-top:1.2rem;">📈 AI Features</h3>
    <ul>
        <li>Placement prediction</li>
        <li>Career guidance</li>
        <li>Skill analysis</li>
        <li>Company recommendation</li>
        <li>AI-based decision support</li>
    </ul>
</div>
""",
            unsafe_allow_html=True,
        )

    # ----- CTA -----
    st.write("")
    st.markdown(
        """
<div class="cta">
    <h2>🚀 Ready To Build Your Dream Career?</h2>
    <p>Our AI analyzes your CGPA, coding skills, DSA, internships, projects and communication skills
    to predict your placement chances and recommend the best career path.</p>
</div>
""",
        unsafe_allow_html=True,
    )

    # ----- How it works -----
    st.markdown('<div class="section-title">How our AI <span>works</span></div>', unsafe_allow_html=True)

    steps = [
        ("1", "Enter Details", "Fill in your academic and skill info."),
        ("2", "AI Analysis", "Our model studies your profile."),
        ("3", "Prediction", "Get your placement probability."),
        ("4", "Recommendation", "See the careers that fit you."),
    ]
    for col, (num, title, desc) in zip(st.columns(4), steps):
        col.markdown(
            f'<div class="step"><div class="num">{num}</div><h4>{title}</h4><p>{desc}</p></div>',
            unsafe_allow_html=True,
        )

    # ----- Footer -----
    st.markdown(
        """
<div class="footer">
    <h4>🤖 AI Career &amp; Placement Assistant</h4>
    <p>Developed using Streamlit • Python • Machine Learning • Random Forest</p>
    <p>© 2026 Harmanjot &amp; Vansheeka</p>
</div>
""",
        unsafe_allow_html=True,
    )


# ================= PREDICTION =================
if page == "🔮 Prediction":

    st.markdown(
        """
<div class="hero" style="padding:2rem;">
    <h1 style="font-size:2.2rem;">🎯 Placement Prediction</h1>
    <p>Enter your details below to check your placement chances</p>
</div>
""",
        unsafe_allow_html=True,
    )
    st.write("")

    form_col, info_col = st.columns([1.5, 1])

    with form_col:
        with st.form("prediction_form"):
            name = st.text_input("Student Name", placeholder="Enter your full name")

            c1, c2 = st.columns(2)
            cgpa = c1.number_input("CGPA", 0.0, 10.0, step=0.1, format="%.2f")
            internship = c2.selectbox("Internship", ["No", "Yes"])

            skills = st.slider("Coding Skills", 0, 10, 5)

            submitted = st.form_submit_button("🔮 Predict Placement")

    with info_col:
        st.markdown(
            """
<div class="panel">
    <h3>💡 Tips</h3>
    <ul>
        <li>Use your latest CGPA</li>
        <li>Rate coding skills honestly (0 = beginner, 10 = expert)</li>
        <li>Count internships you have completed</li>
    </ul>
</div>
""",
            unsafe_allow_html=True,
        )

    if submitted:
        with st.spinner("Analyzing your profile..."):
            # TODO: load your trained Random Forest model and predict here, e.g.
            # prediction = model.predict([[cgpa, skills, 1 if internship == "Yes" else 0]])
            pass

        st.success(f"✅ Prediction completed{' for ' + name if name else ''}")

        r1, r2, r3 = st.columns(3)
        r1.metric("CGPA", f"{cgpa:.2f}")
        r2.metric("Coding Skills", f"{skills}/10")
        r3.metric("Internship", internship)
