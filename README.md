# JARVIS Python Assistant

A beginner-friendly voice assistant made with Python. It listens to your voice, speaks back, and can do a few useful tasks like:

- tell the current time/date
- open websites
- open apps
- search the web
- get quick Wikipedia summaries
- speak responses back to you

## Requirements

- Python 3.9+
- A working microphone
- Speakers/headphones

## Install

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you have issues with PyAudio, install system dependencies first:

- Ubuntu/Debian:
  ```bash
  sudo apt install portaudio19-dev python3-pyaudio
  ```
- macOS:
  ```bash
  brew install portaudio
  ```

## Run

```bash
python jarvis.py
```

## Example voice commands

- "Jarvis hello"
- "Jarvis what time is it"
- "Jarvis what date is it"
- "Jarvis open YouTube"
- "Jarvis open Google"
- "Jarvis open Notepad"
- "Jarvis search for Python tutorials"
- "Jarvis who is Albert Einstein"
- "Jarvis goodbye"

## Important note

This is a simple starter version. It is designed to teach you how to build a JARVIS-style assistant in Python step by step.
