# DocQA
Simple document question/answer CLI using Anthropic's LLM API. This allows you to ask a question about a local text file or PDF.

# Installation

Clone repo and `pip install -e .`

# Usage

Set Anthropic API key on first use.
```bash
# dqa set-api-key "zzz"
```

Pass in a PDF and ask a question with the `-q` flag.
```bash
$ dqa ask research_paper.pdf -q "What are the most relevant citations?"
```

```bash
$ dqa ask research_paper.pdf -q "What are the key discoveries?"
```

# Example

```bash
$ dqa ask cv_keenan_graham.pdf -q "What's the most difficult thing that was done?"
# ...
# Asking model "What's the most difficult thing that was done?" with 11317 character long document.

# <title>cv_keenan_graham.pdf</title>

# <answer>Based on the information provided in Keenan Graham's CV, one of the most difficult
# things he has done appears to be establishing an autoscaling genomics data portal for IGVF.
# This involved complex tasks such as:

# 1. Defining all infrastructure as code
# 2. Setting up a continuous deployment pipeline
# 3. Implementing feature flags for database hot swaps
# 4. Automating stateful migrations
# 5. Creating scheduled serverless functions for infrastructure management
# 6. Developing and maintaining multiple open-source repositories

# This project required a wide range of technical skills and involved designing and implementing
# complex systems at scale, which likely presented significant challenges and required
# sophisticated problem-solving abilities.</answer>
```

# Help

```
$ dqa --help
usage: dqa [-h] {set-api-key,ask} ...

CLI for using Anthropic's LLM to answer a question about a document.

positional arguments:
  {set-api-key,ask}  Available commands.
    set-api-key      Set Anthropic API key.
    ask              Ask a question about a document with an LLM.

$ dqa ask --help
usage: dqa ask [-h] -q QUESTION [--start-pos START_POS] [--length LENGTH] document_path

positional arguments:
  document_path         Path to the document (text or PDF). Allowed suffixes are ['.pdf', '.txt', '.tsv', '.csv', '.md', '.py'].

options:
  -q QUESTION, --question QUESTION
                        Question for the model to answer about the document.
  --start-pos START_POS
                        Start position in the document. Use with --length to only pass a chunk of the document to LLM (useful for really long documents).
  --length LENGTH       Length of document chunk.

$ dqa set-api-key --help
usage: dqa set-api-key [-h] api_key

positional arguments:
  api_key     API key to be set.
 ```