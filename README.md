# WordleQuery

A Wordle Word Query API that finds all permutations (anagrams) of a given n-letter word from predefined word banks.

## Features

- HTTP REST API endpoint for querying word permutations
- Support for multiple word lengths (4-letter, 5-letter words included)
- Returns all valid anagrams from the word bank
- JSON response format
- Error handling for invalid inputs and missing word banks

## Installation

1. Clone the repository:
```bash
git clone https://github.com/franciscoturdera00/WordleQuery.git
cd WordleQuery
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

Run the Flask application:
```bash
python app.py
```

The API server will start on `http://localhost:5000`

### API Endpoints

#### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns API documentation and available endpoints

```bash
curl http://localhost:5000/
```

#### 2. Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Health check endpoint

```bash
curl http://localhost:5000/health
```

#### 3. Query Word Permutations
- **URL**: `/query`
- **Method**: `GET`
- **Query Parameters**:
  - `word` (required): The n-letter word to find permutations for
- **Description**: Returns all permutations (anagrams) of the input word found in the word bank

**Example Requests:**

```bash
# Find permutations of "alert" (5 letters)
curl "http://localhost:5000/query?word=alert"

# Response:
# {
#   "word": "alert",
#   "length": 5,
#   "permutations": ["alert", "alter", "later"],
#   "count": 3
# }

# Find permutations of "post" (4 letters)
curl "http://localhost:5000/query?word=post"

# Response:
# {
#   "word": "post",
#   "length": 4,
#   "permutations": ["post", "spot", "stop"],
#   "count": 3
# }
```

### Response Format

**Success Response:**
```json
{
  "word": "alert",
  "length": 5,
  "permutations": ["alert", "alter", "later"],
  "count": 3
}
```

**Error Response (Missing Parameter):**
```json
{
  "error": "Missing required parameter: word"
}
```

**Error Response (Word Bank Not Found):**
```json
{
  "error": "No word bank found for 3-letter words",
  "word": "cat",
  "length": 3
}
```

## Word Banks

The API uses text files to store valid words for different lengths:
- `word_bank_4_letters.txt` - Contains 4-letter words
- `word_bank_5_letters.txt` - Contains 5-letter words

To add support for additional word lengths, create a new file following the naming pattern:
`word_bank_N_letters.txt` where N is the word length.

Each file should contain one word per line.

## How It Works

1. The API receives a word as a query parameter
2. It determines the word length (n)
3. It loads the corresponding `word_bank_n_letters.txt` file
4. It finds all words in the word bank that are anagrams of the input word
5. It returns the results as a JSON response

**Anagram Detection**: Two words are considered anagrams if they contain the same letters with the same frequency, regardless of order.

## Requirements

- Python 3.7+
- Flask 3.0.0
- Werkzeug 3.0.3

## License

MIT License