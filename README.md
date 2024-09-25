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

# Example

```bash
$ dqa ask cv_keenan_graham.pdf -q "What's the most difficult thing that was done?"
Asking model "What's the most difficult thing that was done?" with 10024 character long document.
<title>cv_keenan_graham.pdf</title>

<answer>Based on the information provided in Keenan Graham's CV, one of the most difficult things he has done appears to be establishing an autoscaling genomics data portal for IGVF. This involved complex tasks such as:

1. Defining all infrastructure as code
2. Setting up a continuous deployment pipeline
3. Implementing feature flags for database hot swaps
4. Automating stateful migrations
5. Creating scheduled serverless functions for infrastructure management
6. Developing and maintaining multiple open-source repositories

This project required a wide range of technical skills and involved designing and implementing complex systems at scale, which likely presented significant challenges and required sophisticated problem-solving abilities.</answer>
```