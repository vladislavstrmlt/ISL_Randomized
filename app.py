"""
Streamlit app
"""
import streamlit as st
from problems import ISL


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
    # randomize_order = st.checkbox("Randomize order")
    max_difficulty_selected = st.selectbox("Max difficulty", ["P1/P4", "P2/P5", "P3/P6"], index=1)
    if max_difficulty_selected == "P1/P4":
        max_difficulty = 4
    elif max_difficulty_selected == "P2/P5":
        max_difficulty = 6
    else:
        max_difficulty = None
    sources = st.checkbox("Show sources")
    num_problems = st.number_input("Number of problems", min_value=1, max_value=len(ISL), value=5)

    if st.button("Generate PDF"):
        ISL.to_pdf(
            topics=topics,
            include_unlabelled=False,
            sources=sources,
            randomize_order=True,
            remove_auxfiles=True,
            output_filename="streamlit_generated",
            num_problems=num_problems,
            max_difficulty=max_difficulty
        )
        st.write("PDF generated successfully!")

        # Make a download link
        with open("output/streamlit_generated.pdf", "rb") as f:
            pdf = f.read()
        st.download_button("Download PDF", pdf, "streamlit_generated.pdf")


if __name__ == "__main__":
    main()
