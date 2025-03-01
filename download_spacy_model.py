import spacy
import sys

def download_spacy_model():
    print("Downloading spaCy model...")
    spacy.cli.download("en_core_web_md")
    print("Model downloaded successfully!")

if __name__ == "__main__":
    download_spacy_model()
