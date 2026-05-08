from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from corpora import CorpusNames, get_corpus_file

def create_tokenizer(tokenizerName: str, corpusName: CorpusNames, globPattern: str | None = None):
    print(tokenizerName, corpusName, globPattern)
    TOKENIZER_OUTPUT_FILE = f"tokenizers/{tokenizerName}.json"

    # 1. Initialize the Tokenizer (BPE model)
    tokenizer = Tokenizer(BPE(unk_token="[UNK]")) 

    # 2. Set the pre-tokenizer (e.g., split on spaces)
    tokenizer.pre_tokenizer = Whitespace()

    # 3. Set the Trainer
    trainer = BpeTrainer(
        special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"],
        vocab_size=32000,
        min_frequency=2
    )

    FILES = [str(f) for f in get_corpus_file(corpusName, globPattern)]
    print("Processing files count:", len(FILES))

    # 4. Train the Tokenizer
    tokenizer.train(FILES, trainer=trainer)

    # 5. Save the vocabulary and tokenization rules
    tokenizer.save(TOKENIZER_OUTPUT_FILE)

    for txt in [
        "Litwo! Ojczyzno moja! ty jesteś jak zdrowie.",
        "Jakże mi wesoło!",
        "Jeśli wolisz mieć pełną kontrolę nad tym, które listy są łączone (a to jest bezpieczniejsze, gdy słownik może zawierać inne klucze), po prostu prześlij listę list do spłaszczenia.",
    ]:
        encoded = tokenizer.encode(txt)
        print("Zakodowany tekst:", encoded.tokens)
        print("ID tokenów:", encoded.ids)

if __name__ == "__main__":
    # create_tokenizer("tokenizer-pan-tadeusz", "PAN_TADEUSZ")
    # create_tokenizer("tokenizer-wolnelektury", "WOLNELEKTURY")
    # create_tokenizer("tokenizer-nkjp", "NKJP")
    # create_tokenizer("tokenizer-all-corpora", "ALL")
    create_tokenizer("tokenizer-pickwick", "PICKWICK")
