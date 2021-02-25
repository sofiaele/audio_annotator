# audio_annotator
Annotate Audio/Speech

![APM](https://img.shields.io/apm/l/vim-mode)
[![Generic badge](https://img.shields.io/badge/python->=3-green.svg)](https://shields.io/)

About
----
At the annotations_database.txt we are keeping the annotations in the form of 
user, audio, label 
 ## Web App Usage:

 You have to register/login with your email, in order to start the annotation process.
 The app will randomly peek an audio that you have not already annotate to begin with.


## Installation
```bash
git clone https://github.com/sofiaele/audio_annotator.git
cd audio_annotator
pip install -r requirements.txt
```

## Running:
```bash
python3 run.py
```

Tree Structure
---
```
├───.users
├───static
│   ├───Annotated
│   └───Audio
```
Under the ./users direcroty you can find the users.txt file which contains the emails of the registered users on the Web app, in order to wrok the login and register mechanism.

Under the static folder you can find the Annotated directory which contains a {email}.txt file for each user with the annotated audios.

Under the static folder you can find the Audio directory which contains the dataset.


