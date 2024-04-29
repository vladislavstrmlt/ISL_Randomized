"""
Streamlit app
"""
import streamlit as st
from problems import ISL2020_NO_G, ISL2017_NO_G, ISL2018_NO_G, ISL2019_NO_G

PROBLEMS = ISL2018_NO_G


def main():
    st.title("ISL Problems")
    st.write("Practise for the IMO!")

    A = st.checkbox("Algebra", value=True)
    C = st.checkbox("Combinatorics", value=True)
    G = st.checkbox("Geometry", value=False, disabled=True)
    N = st.checkbox("Number Theory", value=True)

    topics = []
    if A:
        topics.append("A")
    if C:
        topics.append("C")
    if G:
        topics.append("G")
    if N:
        topics.append("N")


    # include_unlabelled = st.checkbox("Include unlabelled problems")
    randomize_order = st.checkbox("Randomize order")
    sources = st.checkbox("Show sources")
    num_problems = st.number_input("Number of problems", min_value=1, max_value=len(PROBLEMS), value=5)

    if st.button("Generate PDF"):
        PROBLEMS.to_pdf(
            topics=topics,
            include_unlabelled=False,
            sources=sources,
            randomize_order=randomize_order,
            remove_crap=True,
            output_filename="streamlit_generated",
            num_problems=num_problems,
        )
        st.write("PDF generated successfully!")
        # Make a download link
        with open("output/streamlit_generated.pdf", "rb") as f:
            pdf = f.read()
        st.download_button("Download PDF", pdf, "streamlit_generated.pdf")


if __name__ == "__main__":
    main()
    # import os
    # import subprocess
    # if st.button("echo"):
    #     try:
    #         subprocess.run(["sudo", "-S", "<<<", "", "apt-get", "install", "-y", "texlive"], check=True, capture_output=True)
    #     except subprocess.CalledProcessError as e:
    #         st.write(e.stderr)
    # if st.button("sudo echo"):
    #     try:
    #         subprocess.run(["sudo", "echo", "hello", "-S", ""], check=True, capture_output=True)
    #     except subprocess.CalledProcessError as e:
    #         st.write(e.stderr)