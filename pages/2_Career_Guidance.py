import streamlit as st

st.set_page_config(
    page_title="Career Guidance",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Career Guidance")
st.write("Get career recommendations based on your interests and skills.")

st.divider()

interest = st.selectbox(
    "Choose Your Interest",
    [
        "Artificial Intelligence",
        "Software Development",
        "Data Science",
        "Cyber Security",
        "Cloud Computing",
        "UI/UX Design"
    ]
)

if st.button("🔍 Show Career Path"):

    if interest == "Artificial Intelligence":
        st.success("🤖 AI Engineer")
        st.write("Skills Required:")
        st.write("✅ Python")
        st.write("✅ Machine Learning")
        st.write("✅ Deep Learning")
        st.write("✅ TensorFlow / PyTorch")

    elif interest == "Software Development":
        st.success("💻 Software Developer")
        st.write("Skills Required:")
        st.write("✅ Java / Python / C++")
        st.write("✅ DSA")
        st.write("✅ SQL")
        st.write("✅ Git & GitHub")

    elif interest == "Data Science":
        st.success("📊 Data Scientist")
        st.write("Skills Required:")
        st.write("✅ Python")
        st.write("✅ Pandas")
        st.write("✅ NumPy")
        st.write("✅ Machine Learning")

    elif interest == "Cyber Security":
        st.success("🔒 Cyber Security Analyst")
        st.write("Skills Required:")
        st.write("✅ Networking")
        st.write("✅ Linux")
        st.write("✅ Ethical Hacking")
        st.write("✅ Security Tools")

    elif interest == "Cloud Computing":
        st.success("☁️ Cloud Engineer")
        st.write("Skills Required:")
        st.write("✅ AWS")
        st.write("✅ Azure")
        st.write("✅ Docker")
        st.write("✅ Kubernetes")

    elif interest == "UI/UX Design":
        st.success("🎨 UI/UX Designer")
        st.write("Skills Required:")
        st.write("✅ Figma")
        st.write("✅ Adobe XD")
        st.write("✅ Wireframing")
        st.write("✅ Prototyping")

st.divider()

st.subheader("📚 Recommended Certifications")

st.info("""
• Google Career Certificates
• AWS Cloud Practitioner
• Microsoft Azure Fundamentals
• IBM AI Engineering
• Coursera Machine Learning
• Cisco CCNA
""")