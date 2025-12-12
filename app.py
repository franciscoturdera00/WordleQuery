"""
Wordle Word Query API

This API accepts an n-letter word and returns all permutations (anagrams)
of that word found in the corresponding word bank file.
"""

from flask import Flask, jsonify, request
from collections import Counter
import os

app = Flask(__name__)


def get_word_bank_path(word_length):
    """
    Get the path to the word bank file for the given word length.
    
    Args:
        word_length: The number of letters in the word
        
    Returns:
        Path to the word bank file
    """
    return f"word_bank_{word_length}_letters.txt"


def load_word_bank(word_length):
    """
    Load words from the word bank file.
    
    Args:
        word_length: The number of letters in the word
        
    Returns:
        Set of words from the word bank, or None if file doesn't exist
    """
    filepath = get_word_bank_path(word_length)
    
    if not os.path.exists(filepath):
        return None
    
    with open(filepath, 'r') as f:
        words = set(word.strip().lower() for word in f.readlines() if word.strip())
    
    return words


def are_anagrams(word1, word2):
    """
    Check if two words are anagrams of each other.
    
    Args:
        word1: First word
        word2: Second word
        
    Returns:
        True if the words are anagrams, False otherwise
    """
    return Counter(word1.lower()) == Counter(word2.lower())


def find_permutations(input_word, word_bank):
    """
    Find all permutations (anagrams) of the input word in the word bank.
    
    Args:
        input_word: The word to find permutations for
        word_bank: Set of valid words to search in
        
    Returns:
        List of anagrams found
    """
    permutations = []
    input_word_lower = input_word.lower()
    
    for word in word_bank:
        if are_anagrams(input_word_lower, word):
            permutations.append(word)
    
    return sorted(permutations)


@app.route('/query', methods=['GET'])
def query_word():
    """
    Query endpoint for finding word permutations.
    
    Query Parameters:
        word: The n-letter word to find permutations for
        
    Returns:
        JSON response with permutations or error message
    """
    word = request.args.get('word')
    
    if not word:
        return jsonify({
            'error': 'Missing required parameter: word'
        }), 400
    
    word = word.strip()
    word_length = len(word)
    
    if word_length == 0:
        return jsonify({
            'error': 'Word cannot be empty'
        }), 400
    
    # Load the word bank
    word_bank = load_word_bank(word_length)
    
    if word_bank is None:
        return jsonify({
            'error': f'No word bank found for {word_length}-letter words',
            'word': word,
            'length': word_length
        }), 404
    
    # Find permutations
    permutations = find_permutations(word, word_bank)
    
    return jsonify({
        'word': word,
        'length': word_length,
        'permutations': permutations,
        'count': len(permutations)
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy'})


@app.route('/', methods=['GET'])
def index():
    """Root endpoint with API documentation."""
    return jsonify({
        'name': 'Wordle Word Query API',
        'version': '1.0.0',
        'endpoints': {
            '/': 'API documentation',
            '/health': 'Health check',
            '/query?word=<word>': 'Query permutations of a word'
        },
        'usage': 'Send a GET request to /query with a word parameter. Example: /query?word=alert'
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
