"""scripts/paper_stats.py"""

import tiktoken

from config import DATA_DIR

PAPERS_TXT_DIR = DATA_DIR.joinpath("txt")

tokenizer = tiktoken.get_encoding("cl100k_base")

# Get the number of papers
num_papers = len(list(PAPERS_TXT_DIR.glob("*.txt")))
print(f"Number of papers: {num_papers}")

# Get the number of lines in the papers, along with some basic statistics
num_lines = []
for paper in PAPERS_TXT_DIR.glob("*.txt"):
    with open(paper, "r", encoding="utf-8") as f:
        num_lines.append(len(f.readlines()))
print(f"Number of lines: {sum(num_lines)}")
print(f"Average number of lines per paper: {round(sum(num_lines) / len(num_lines))}")
print(f"Max number of lines in a paper: {max(num_lines)}")
print(f"Min number of lines in a paper: {min(num_lines)}")

# # Get the number of tokens in the papers, along with some basic statistics
num_tokens = []
for paper in PAPERS_TXT_DIR.glob("*.txt"):
    with open(paper, "r", encoding="utf-8") as f:
        num_tokens.append(len(tokenizer.encode(f.read())))
print(f"Number of tokens: {sum(num_tokens)}")
print(f"Average number of tokens per paper: {round(sum(num_tokens) / len(num_tokens))}")
print(f"Max number of tokens in a paper: {max(num_tokens)}")
print(f"Min number of tokens in a paper: {min(num_tokens)}")


# List all papers with less than 100 lines
print("Papers with less than 100 lines:")
for paper, lines in zip(PAPERS_TXT_DIR.glob("*.txt"), num_lines):
    if lines < 10:
        print(f"{paper}: {lines} lines")
