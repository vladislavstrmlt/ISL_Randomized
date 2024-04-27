from problems import ISL2022_NO_G, ISL2021_NO_G, ISL2020_NO_G, ISL2019_NO_G


ISL2019_NO_G.to_pdf(
    topics=("A", "C", "N"),
    include_unlabelled=False,
    sources=False,
    randomize_order=False,
    remove_crap=True,
    output_filename="2019",
    #num_problems=8,
)