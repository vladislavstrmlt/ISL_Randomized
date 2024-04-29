from problems import ISL2022_NO_G, ISL2021_NO_G, ISL2020_NO_G, ISL2019_NO_G, ISL2017_NO_G, ISL2018_NO_G

ISL = ISL2018_NO_G + ISL2017_NO_G

ISL.to_pdf(
    topics=("A", "C", "N"),
    include_unlabelled=False,
    sources=False,
    randomize_order=False,
    remove_crap=True,
    output_filename="2017_2018",
    #num_problems=8,
)