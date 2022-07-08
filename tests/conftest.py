import spacy
from pytest import fixture
from spacy.language import Language


@fixture
def nlp() -> Language:
    model = spacy.blank("fr")
    return model
