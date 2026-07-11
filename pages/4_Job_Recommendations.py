import streamlit as st

st.set_page_config(
    page_title="Job Recommendations",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Job Recommendations")

st.write("Discover the best companies and career opportunities based on your skills.")

st.divider()

career = st.selectbox(
    "Select Your Career",
    [
        "AI Engineer",
        "Software Developer",
        "Data Scientist",
        "Data Analyst",
        "Full Stack Developer",
        "Cyber Security",
        "Cloud Engineer"
    ]
)

if st.button("🚀 Show Recommendations"):

    jobs = {
        "AI Engineer": {
            "salary":"₹10-20 LPA",
            "companies":["Google","Microsoft","NVIDIA","Adobe"],
            "skills":["Python","Machine Learning","Deep Learning","TensorFlow"]
        },
        "Software Developer":{
            "salary":"₹6-15 LPA",
            "companies":["Amazon","TCS","Infosys","Accenture"],
            "skills":["Java","Python","DSA","SQL"]
        },
        "Data Scientist":{
            "salary":"₹8-18 LPA",
            "companies":["Google","Amazon","Flipkart","IBM"],
            "skills":["Python","Statistics","Pandas","ML"]
        },
        "Data Analyst":{
            "salary":"₹5-12 LPA",
            "companies":["Deloitte","EY","KPMG","IBM"],
            "skills":["Excel","SQL","Power BI","Python"]
        },
        "Full Stack Developer":{
            "salary":"₹6-16 LPA",
            "companies":["Zoho","TCS","Infosys","Cognizant"],
            "skills":["HTML","CSS","JavaScript","React","Node.js"]
        },
        "Cyber Security":{
            "salary":"₹7-15 LPA",
            "companies":["Cisco","IBM","Palo Alto","Wipro"],
            "skills":["Networking","Linux","Ethical Hacking","Security"]
        },
        "Cloud Engineer":{
            "salary":"₹8-18 LPA",
            "companies":["AWS","Microsoft","Oracle","IBM"],
            "skills":["AWS","Docker","Linux","Kubernetes"]
        }
    }

    data = jobs[career]

    st.success(f"🎯 Recommended Career: {career}")

    st.metric("💰 Expected Salary", data["salary"])

    st.subheader("🏢 Top Hiring Companies")
    for company in data["companies"]:
        st.write("✅", company)

    st.subheader("📚 Required Skills")
    for skill in data["skills"]:
        st.write("✔", skill)

    st.divider()

    st.info("""
### 🚀 Tips to Get Selected

✅ Maintain CGPA above 8

✅ Build 4-5 Real Projects

✅ Complete Internships

✅ Practice DSA Daily

✅ Improve Communication Skills

✅ Earn Certifications

✅ Create a Strong Resume
""")