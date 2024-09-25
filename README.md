# DocQA
Simple document question/answer CLI using Anthropic's LLM API.

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
