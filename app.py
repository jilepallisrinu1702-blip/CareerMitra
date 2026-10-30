import streamlit as st

st.set_page_config(
    page_title="CareerMitra",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 CareerMitra")
st.subheader("AI-Based Career Guidance and Mentor System")

st.write(
    "Discover the right career path based on your "
    "interests, skills and education."
)

st.header("Student Career Assessment")

name = st.text_input("Enter your name")

education = st.selectbox(
    "Select your education",
    ["Intermediate", "Diploma", "B.Tech", "Other"]
)

interest = st.selectbox(
    "Choose your area of interest",
    ["Programming", "Data Analysis", "Artificial Intelligence",
     "Cyber Security", "Cloud Computing", "Web Development"]
)

if st.button("Get Career Recommendation"):
    if name:
        st.success(f"Welcome, {name}!")
        st.write("### Your Suggested Career")
        st.info(interest)
        st.write("This is your initial interest-based suggestion.")
    else:
        st.warning("Please enter your name.")
