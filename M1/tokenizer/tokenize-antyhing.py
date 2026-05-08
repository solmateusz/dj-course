from tokenizers import Tokenizer

def tokenize(tokenizer_file: str, file_path: str):
    tokenizer = Tokenizer.from_file(f"tokenizers/{tokenizer_file}.json")

    with open(file_path, 'r', encoding='utf-8') as f:
        source_txt = f.read()

    encoded = tokenizer.encode(source_txt)

    #print(f"Tokenizer: {tokenizer_file}; liczba tokenów: {len(encoded.ids)}")
    return len(encoded.ids)


if __name__ == "__main__":
    sources = ["../korpus-wolnelektury/pan-tadeusz-ksiega-1.txt", 
               "../korpus-mini/fryderyk-chopin-wikipedia.txt", 
               "../korpus-mini/the-pickwick-papers-gutenberg.txt"]
    
    tokenizers = ["bielik-v1-tokenizer", "bielik-v2-tokenizer", "bielik-v3-tokenizer", 
                  "tokenizer-pan-tadeusz", "tokenizer-wolnelektury", "tokenizer-nkjp", "tokenizer-all-corpora", 
                  "tokenizer-qwen-3-6-27b",
                  "tokenizer-pickwick"]
    
    tokens = list()

    for source in sources:
        print(f"Tokenizacja pliku: {source}")
        for tokenizer in tokenizers:
            print(f"Tokenizator: {tokenizer}")
            tokens.append((source, tokenizer, tokenize(tokenizer, source)))
    
    # sort by source name then ascending by token count
    tokens.sort(key=lambda x: (x[0], x[2]))

    print("\nLiczba tokenów dla każdego tokenizatora:")
    for source, tokenizer, token_count in tokens:
        print(f"{source} - {tokenizer}: {token_count}")