import glob
from pathlib import Path
from typing import Literal

CORPORA_DIRS = {
    "NKJP": Path("../korpus-nkjp/output"),
    "WOLNELEKTURY": Path("../korpus-wolnelektury"),
    "PICKWICK": Path("../korpus-mini"),
}

CORPORA_FILES = {
    "ALL": list(CORPORA_DIRS["NKJP"].glob("*.txt")) + list(CORPORA_DIRS["WOLNELEKTURY"].glob("*.txt")),
    "NKJP": list(CORPORA_DIRS["NKJP"].glob("*.txt")),
    "WOLNELEKTURY": list(CORPORA_DIRS["WOLNELEKTURY"].glob("*.txt")),
    "PAN_TADEUSZ": list(CORPORA_DIRS["WOLNELEKTURY"].glob("pan-tadeusz-ksiega-*.txt")),
    "PICKWICK": list(CORPORA_DIRS["PICKWICK"].glob("the-pickwick-papers-gutenberg.txt")),
}

# removing PAN_TADEUSZ from ALL_CORPORA to avoid duplicates (PAN_TADEUSZ is already in WOLNELEKTURY)
KEYS_WITHOUT_PAN_TADEUSZ = [key for key in CORPORA_FILES.keys() if key != "PAN_TADEUSZ"]
CORPORA_FILES["ALL"] = [
    FILE for key in KEYS_WITHOUT_PAN_TADEUSZ for FILE in CORPORA_FILES[key]
]

CorpusNames = Literal["NKJP", "WOLNELEKTURY", "PAN_TADEUSZ", "ALL", "PICKWICK"]

def get_corpus_file(corpus_name: CorpusNames, glob_pattern: str | None = None) -> Path:
    if corpus_name not in CORPORA_FILES:
        raise ValueError(f"Corpus {corpus_name} not found")
    
    if glob_pattern is None:
        return CORPORA_FILES[corpus_name]
    else:
        return list(CORPORA_FILES[corpus_name].glob(glob_pattern))

if __name__ == "__main__":    
    print("\ncorpora (total files):")
    for corpus_name, corpus_files in CORPORA_FILES.items():
        print(f"{corpus_name}: {len(corpus_files)}")

    print("\nget_corpus_file:")
    print("nkjp *", len(get_corpus_file("NKJP", "*.txt")))
    print("nkjp krzyzacy", len(get_corpus_file("WOLNELEKTURY", "krzyzacy-*.txt")))
    