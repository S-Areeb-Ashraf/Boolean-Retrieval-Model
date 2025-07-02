# Boolean Retrieval Model

This project implements a basic **Boolean Information Retrieval System** using **Python and NLTK**. It supports both:
- Boolean queries (`AND`, `OR`, `NOT`)
- Positional queries (`word1 word2 /N`)

##Project Structure

- `Text_files/`: Folder containing the original 448 text documents.
- `Updated_text_files/`: Tokenized and stemmed versions of the original files (created by the script).
- `Boolean_Model.py`: Main script that processes documents, builds inverted and positional indexes, and answers user queries.

## Features

- Tokenization, stop word removal, and stemming of input documents.
- Construction of:
  - Inverted Index (for Boolean queries)
  - Positional Index (for proximity queries)
- Query support:
  - Boolean: `term1 AND term2`, `term1 OR term2`, `term1 AND NOT term2`, etc.
  - Positional: `word1 word2 /N` (finds documents where `word1` and `word2` occur `N` positions apart)

## Requirements

- Python 3.x
- NLTK

Install NLTK using:

```bash
pip install nltk
```

## How It Works

### Preprocessing
1. Reads documents from `Text_files/`
2. Cleans text: removes punctuation, converts to lowercase
3. Removes stop words
4. Applies stemming (PorterStemmer)
5. Saves results to `Updated_text_files/`

### Indexing
- **Inverted Index**: Maps each word to a list of documents it appears in
- **Positional Index**: Maps each word to (document, position) pairs for proximity search

### Querying
- You’ll be prompted to enter:
  - A Boolean query (`AND`, `OR`, `NOT`)
  - A Positional query (e.g., `information retrieval /3`)
- The system outputs the matched document numbers.

## How to Run

1. Make sure the folder `Text_files/` is in the same directory as `Boolean_Model.py`.
2. Open a terminal or command prompt.
3. Run the program:

```bash
python Boolean_Model.py
```

4. Wait for preprocessing to finish (it may take a few minutes).
5. Enter your Boolean and positional queries when prompted.

## Notes

- Don’t rename or move the `Text_files` directory.
- Some text files may generate warnings—these can be ignored.
- The process might seem slow due to the number of documents (448), but it is functioning.

## Example Queries

- Boolean: `retrieval AND system`
- Boolean: `information OR model`
- Boolean: `query AND NOT search`
- Positional: `boolean model /2`

## License

This is a student project for educational purposes. Feel free to modify and extend it.
