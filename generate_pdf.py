from problems import ISL


ISL.to_pdf(
    topics=("A", "C", "N"),
    include_unlabelled=False,
    sources=False,
    randomize_order=False,
    remove_auxfiles=True,
    output_filename="2017_2018",
    #num_problems=8,
)