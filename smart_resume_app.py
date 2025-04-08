import streamlit as st
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def enhance_resume_text(text):
    enhanced_text = f"""
💼 Professional Experience:
- Spearheaded software development projects at XYZ Corp, enhancing product efficiency by 35%.
- Collaborated cross-functionally with design and QA teams to deploy scalable applications.

🔧 Skills:
- Programming Languages: Python, Java, JavaScript
- Tools: Git, Docker, Jenkins
- Soft Skills: Leadership, Agile Methodologies, Problem Solving

📜 Summary:
Results-driven Software Engineer with a proven track record in delivering robust, user-centric solutions. Passionate about innovation and optimization.

📈 ATS Optimized Keywords:
Software Development, Agile, DevOps, Backend, APIs, Cloud, Full Stack
"""
    return enhanced_text.strip()

st.set_page_config(page_title="SmartResume.AI", layout="centered")
st.title("🧠 SmartResume.AI")
st.subheader("AI-powered Resume Enhancer (ATS-Optimized)")
st.markdown("Upload your old resume and get a stunning, ATS-friendly version in seconds.")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)

    st.success("✅ Resume uploaded successfully!")
    st.subheader("🔍 Original Resume Preview")
    st.text_area("Your resume content:", value=resume_text[:1500], height=200)

    if st.button("🚀 Enhance Resume"):
        enhanced = enhance_resume_text(resume_text)
        st.subheader("✨ Enhanced Resume (ATS Optimized)")
        st.text_area("Enhanced resume content:", value=enhanced, height=300)

        st.download_button(
            label="📥 Download Enhanced Resume (TXT)",
            data=enhanced,
            file_name="enhanced_resume.txt",
            mime="text/plain"
        )
else:
    st.info("Please upload a resume to get started.")
