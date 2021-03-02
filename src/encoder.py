"""Byte pair encoding utilities"""
import os
from tokenizers import Tokenizer

class Encoder:
    def __init__(self, filename):
        self.tokenizer = Tokenizer.from_file(filename)

    def encode(self, text):
        return self.tokenizer.encode(text).ids

    def decode(self, tokens):
        return self.tokenizer.decode(tokens)

def get_encoder(model_name, models_dir):
    return Encoder(os.path.join(models_dir, model_name, 'tokenizer.json'))