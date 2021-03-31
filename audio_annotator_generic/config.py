import os

PATH = os.getcwd()
AUDIOS = os.path.join(PATH, 'audio_annotator_generic', 'static', 'Audio')
ANNOTATED = os.path.join(PATH, 'audio_annotator_generic', 'static', 'Annotated')
USERS = os.path.join(PATH, 'audio_annotator_generic', '.users', 'users.txt')
DATABASE = os.path.join(PATH, 'annotations_database.txt')

CLASSES1 = {
    "1": "not expressive at all",
    "2": "not that expressive",
    "3": "somehow expressive",
    "4": "quite expressive",
    "5": "very expressive"
}

CLASSES2 = {
    "1": "very hard to follow",
    "2": "a bit hard to follow",
    "3": "relatively easy to follow",
    "4": "mostly easy to follow",
    "5": "very easy to follow"
}

CLASSES3 = {
    "1": "I hated it",
    "2": "not really ",
    "3": "it was ok",
    "4": "I quite liked it",
    "5": "I loved it"
}

if __name__ == "__main__":
    for i in CLASSES1:
        print(i)
    for i in CLASSES3:
        print(i)
    for i in CLASSES3:
        print(i)
