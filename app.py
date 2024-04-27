"""
Streamlit app
"""
import streamlit as st
from problems import ISL2020_NO_G


PROBLEMS = ISL2020_NO_G


def main():
    st.title("ISL Problems")
    st.write("Practise for the IMO!")

    topics = st.multiselect("Select topics", ["A", "C", "G", "N"], default=["A", "C", "G", "N"])
    include_unlabelled = st.checkbox("Include unlabelled problems")
    sources = st.checkbox("Show sources")
    num_problems = st.number_input("Number of problems", min_value=1, max_value=len(PROBLEMS), value=5)

    if st.button("Generate PDF"):
        PROBLEMS.to_pdf(
            topics=topics,
            include_unlabelled=include_unlabelled,
            sources=sources,
            randomize_order=True,
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
    # main()
    try:
        subprocess.run(["sudo", "apt-get", "install", "-y", "texlive"], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        st.write(f"Installation failed with error:\n{e.cmd}\n{e.returncode}\n{e.stdout}\n{e.stderr}\n{e.output}")
    import shutil
    import subprocess
    import os
    st.write(shutil.which("pdflatex"))
    st.write(shutil.which("texlive"))
    # os.environ["PATH"] = os.popen('echo $PATH').read().strip()

    st.write(shutil.which("pdflatex"))
    st.write(shutil.which("texlive"))
