import streamlit as st

st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Skill Gap Analysis")
st.write("Analyze your current skills and get improvement suggestions.")

st.divider()

coding = st.slider("💻 Coding Skills", 0, 10, 6)
dsa = st.slider("🧩 DSA", 0, 100, 60)
communication = st.slider("🗣 Communication", 0, 10, 7)
ml = st.slider("🤖 Machine Learning", 0, 10, 5)
system = st.slider("🏗 System Design", 0, 10, 4)

if st.button("📊 Analyze Skills"):

    st.subheader("📋 Analysis Report")

    if coding >= 8:
        st.success("✅ Coding Skills : Excellent")
    elif coding >= 5:
        st.warning("⚠️ Coding Skills : Good (Needs Improvement)")
    else:
        st.error("❌ Coding Skills : Weak")

    if dsa >= 80:
        st.success("✅ DSA : Excellent")
    elif dsa >= 60:
        st.warning("⚠️ DSA : Average")
    else:
        st.error("❌ DSA : Weak")

    if communication >= 8:
        st.success("✅ Communication : Excellent")
    else:
        st.warning("⚠️ Improve Communication Skills")

    if ml >= 7:
        st.success("✅ Machine Learning : Good")
    else:
        st.warning("⚠️ Learn Machine Learning Projects")

    if system >= 7:
        st.success("✅ System Design : Good")
    else:
        st.warning("⚠️ Practice System Design")

    st.divider()

    st.subheader("🎯 Recommended Learning Plan")

    if coding < 8:
        st.write("✔ Practice Python and Data Structures daily")

    if dsa < 80:
        st.write("✔ Solve 2-3 DSA problems every day")

    if communication < 8:
        st.write("✔ Improve English speaking and interview communication")

    if ml < 7:
        st.write("✔ Build Machine Learning projects")

    if system < 7:
        st.write("✔ Learn System Design basics")

    st.divider()

    st.subheader("⭐ Overall Skill Score")

    score = (coding*10 + dsa + communication*10 + ml*10 + system*10) / 5

    st.metric("Skill Score", f"{score:.1f}/100")

    st.progress(score/100)