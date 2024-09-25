import argparse

import json

import os

from pathlib import Path

from pypdf import PdfReader

from anthropic import Anthropic


ALLOWED_FILE_SUFFIXES = ['.pdf', '.txt', '.tsv', '.csv', '.md', '.py']

HOME_DIR = os.path.expanduser("~")

CONFIG_PATH = os.path.join(HOME_DIR, '.anthropic_secret_key')

MODEL = 'claude-3-5-sonnet-20240620'


def generate_prompt(name, document, question):
    return f'''Examine the following document named <name>{name}</name> and see if there is information to answer the question <question>{question}</question>. Print the title of the document (in <title> tags) if applicable, and a succinct but useful summary that answers the question or say there isn't enough information to answer the question (in <answer> tags).
Document:
<document>{document}</document>'''


def get_completion(client, prompt):
    return client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{'role': 'user', 'content': prompt}]
    ).content[0].text


def get_document_content(path):
    if not os.path.exists(path.resolve()):
        raise ValueError(f'File not found: {path.resolve()}')
    if path.name.endswith('.pdf'):
        reader = PdfReader(path.resolve())
        content = ''.join(
            page.extract_text()
            for page in reader.pages
        )
    else:
        with open(path.resolve(), 'r') as f:
            content = f.read()
    return content


def extract_chunk(text, start_pos, length):
    end_pos = start_pos + length
    return text[start_pos:end_pos]


def save_api_key(api_key):
    config_data = {'api_key': api_key}
    with open(CONFIG_PATH, 'w') as config_file:
        json.dump(config_data, config_file)


def load_api_key():
    if not os.path.exists(CONFIG_PATH):
        return None
    with open(CONFIG_PATH, 'r') as config_file:
        config_data = json.load(config_file)
        return config_data.get('api_key')


def ask(client, name, document, question):
    prompt = generate_prompt(name, document, question)
    completion = get_completion(client, prompt)
    return completion


def parse_args():
    parser = argparse.ArgumentParser(
        description="CLI for using Anthropic's LLM to answer a question about a document."
    )
    subparsers = parser.add_subparsers(
        dest='command',
        help='Available commands.'
    )
    set_key_parser = subparsers.add_parser(
        'set-api-key',
        help='Set Anthropic API key.'
    )
    set_key_parser.add_argument(
        'api_key',
        type=str,
        help='API key to be set.'
    )
    ask_parser = subparsers.add_parser(
        'ask',
        help='Ask a question about a document with an LLM.'
    )
    ask_parser.add_argument(
        'document_path',
        type=str,
        help=f'Path to the document (text or PDF). Allowed suffixes are {ALLOWED_FILE_SUFFIXES}.'
    )
    ask_parser.add_argument(
        '-q',
        '--question',
        type=str,
        required=True,
        help='Question for the model to answer about the document.'
    )
    ask_parser.add_argument(
        '--start-pos',
        type=int,
        default=0,
        help='Start position in the document. Use with --length to only pass a chunk of the document to LLM (useful for really long documents).'
    )
    ask_parser.add_argument(
        '--length',
        type=int,
        default=10024,
        help='Length of document chunk.'
    )
    return parser.parse_args()


def run():
    args = parse_args()
    if args.command == 'set-api-key':
        save_api_key(args.api_key)
        return 'API key set'
    api_key = load_api_key()
    if api_key is None:
        raise ValueError('No API key found. Use `dqa set-api-key "somekey"` to set your Anthropic API key first.')
    client = Anthropic(api_key=api_key)
    path = Path(args.document_path)
    name = path.name
    content = get_document_content(path)
    document = extract_chunk(content, args.start_pos, args.length)
    question = args.question
    answer = ask(client, name, document, question)
    return answer
