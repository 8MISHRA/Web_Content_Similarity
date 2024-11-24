# Web Content Similarity Checker Using Simhash

This repository contains a Python script that computes the similarity between two web pages using Simhash encoding. Simhash is an efficient technique for detecting near-duplicate content in large datasets. The script takes two URLs as input, processes their textual content, and calculates the percentage of similarity based on Simhash values.

## Features

- **Tokenization**: Extracts and cleans textual data from the provided URLs.
- **N-grams**: Generates n-grams for refined text analysis.
- **Simhash Calculation**: Computes 64-bit hash values for the textual content of each URL.
- **Similarity Detection**: Determines the percentage similarity between the two web pages based on differing hash bits.

## Installation

1. Clone this repository:
```bash
   git clone https://github.com/8MISHRA/Web_Content_Similarity.git
   cd Web_Content_Similarity
```

Usage
Run the script with two URLs as arguments:

```bash
python3 simhash_similarity_checker.py URL1 URL2
```