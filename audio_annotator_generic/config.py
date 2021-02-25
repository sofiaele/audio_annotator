import os

PATH = os.getcwd()
AUDIOS = os.path.join(PATH, 'audio_annotator_generic', 'static', 'Audio')
ANNOTATED = os.path.join(PATH, 'audio_annotator_generic', 'static', 'Annotated')
USERS = os.path.join(PATH, 'audio_annotator_generic', '.users', 'users.txt')
DATABASE = os.path.join(PATH, 'annotations_database.txt')

CLASSES = {
    "1": "Boring - Dull voice - Incomprehensible",
    "2": "A little better than Level 1 but still needs improvement ",
    "3": "Moderate",
    "4": "Comprehensible and relatively engaging",
    "5": "Very interesting and motivational"
}

if __name__ == "__main__":
    for i in CLASSES:
        print(i)
