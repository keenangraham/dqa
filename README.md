# DocQA
Simple document question/answer CLI using Anthropic's LLM API.

# Installation

Clone repo and `pip install -e .`

# Usage

Pass in a PDF and ask a question with the `-q` flag.
```bash
$ dqa research_paper.pdf -q "What are the most relevant citations?"
```

Add additional instructions with `-a` flag.
```bash
$ dqa research_paper.pdf -q "What are the key discoveries?" -a "Keep the summary succinct"
```
