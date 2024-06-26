from __future__ import annotations
from typing import Literal, Iterable
from dataclasses import dataclass
from random import shuffle
import subprocess
import warnings
import os

@dataclass
class Problem:
    problem_statement: str
    source: str
    year: int
    problem_number: int
    topic: Literal["A", "C", "G", "N"] | None = None
    

class ProblemSet:
    def __init__(self, problems: Iterable[Problem]):
        self.problems = problems

    def __add__(self, other: ProblemSet) -> ProblemSet:
        return ProblemSet(self.problems + other.problems)
    
    def __iadd__(self, other: ProblemSet) -> None:
        self.problems.extend(other.problems)

    def __len__(self) -> int:
        return len(self.problems)

    def to_pdf(
        self,
        topics: Iterable[Literal["A", "C", "G", "N"]] = ("A", "C", "G", "N"),
        include_unlabelled: bool = False,
        sources: bool = False,
        randomize_order: bool = True,
        remove_auxfiles: bool = False,
        output_filename: str = "main",
        num_problems: int | None = None,
        max_difficulty: int | None = None,
    ):
        fullname_topics = {
            "A": "Algebra",
            "C": "Combinatorics",
            "G": "Geometry",
            "N": "Number Theory",
        }
        title = ' and '.join([', '.join(fullname_topics[topic] for topic in topics[:-1])] + [fullname_topics[topics[-1]]]) if len(topics) > 1 else fullname_topics[topics[0]] + " Problems"

        if "." in output_filename:
            warnings.warn("The output filename should not contain a file extension. The file extension will be added automatically.")
            output_filename = output_filename.split(".")[0]

        problems = [
            problem for problem in self.problems
            if problem.topic in topics or (include_unlabelled and problem.topic is None)
        ]

        if max_difficulty is not None:
            problems = [
                problem for problem in problems
                if problem.problem_number <= max_difficulty
                and problem.source == "ISL"  # The problem number is only this way for ISL problems
            ]

        if randomize_order:
            shuffle(problems)

        if num_problems is not None:
            problems = problems[:num_problems]
            if not randomize_order:
                warnings.warn("The number of problems was specified, but the order was not randomized, meaning you get a constant non-random subset of the problems. Try setting randomize_order=True next time.")

        if sources:
            for problem in self.problems:
                if problem.topic:
                    problem.problem_statement += f" \\textit{{({problem.source} {problem.topic}{problem.problem_number}, {problem.year})}}"
                else:
                    problem.problem_statement += f" \\textit{{({problem.source} P{problem.problem_number}, {problem.year})}}"
        else:
            for problem in self.problems:
                # Still add the year (without revealing difficulty!), so people can find it if they want to.
                if str(problem.year) not in problem.problem_statement:
                    problem.problem_statement += f" \\textit{{({problem.year})}}"

        with open(f"output/{output_filename}.tex", "w") as f:
            f.write(
                r"\documentclass[12pt]{article}"
                r"\usepackage[a4paper, margin=1in]{geometry}"
                r"\usepackage{fancyhdr}"
                r"\pagestyle{fancy}"
                r"\rhead{\today}"
                rf"\lhead{{{title}}}"

                r"\usepackage{amsmath}"
                r"\usepackage{amsfonts}"
                r"\usepackage{amssymb}"
                r"\usepackage{enumerate}"
                r"\begin{document}"
                r"\begin{enumerate}"
            )
            for problem in problems:
                f.write(
                    f"\\item {problem.problem_statement}"
                )
            f.write(
                r"\end{enumerate}"
                r"\end{document}"
            )

        subprocess.run(["pdflatex", "-output-directory=output/", "-interaction=nonstopmode", f"output/{output_filename}.tex"], check=True)

        if remove_auxfiles:
            for filename in os.listdir("output/"):
                if not filename.endswith((".pdf", ".txt")):
                    os.remove(f"output/{filename}")
