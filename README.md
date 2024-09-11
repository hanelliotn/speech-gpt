# SpeechGPT
Inspired by ChatGPT, but via verbal communication

## Development Status
`FIRST DRAFT FINISHED`

## Installations
First, we need to install `portaudio` from Homebrew. This package is required
for Python library `pyaudio`:

```bash
$ brew install portaudio
```

Then, we install packages in `requirements.txt`:
```bash
$ pip3 install -r requirements.txt
```

**NOTE**: If errors related to `#include "portaudio.h"` occurred when running 
`pip install pyaudio`, like this:
```bash
#include "portaudio.h"

         ^
1 error generated.
error: command '/usr/bin/clang' failed with exit status 1
``` 
Then we need to run the command separately in the Terminal below:
```bash
$ CFLAGS="-I/opt/homebrew/include -L/opt/homebrew/lib" python3 -m pip install pyaudio
```

We need to install FLAC in order to recognize speech with the command below:
```bash
$ sudo port install flac
```
If you have not installed Macports, please download Macports from 
[this link](https://www.macports.org/install.php).

Then, we run:
```bash
$ python3 src/main.py
```

**NOTE**: If you face the `KeyError: 'VoiceAge'` problem, please go to the 
`nsss.py` in your folder (the full error message should display the full path),
and remove the `attr['VoiceAge']` line code.

Before running this project, ensure that you have retrieve an OpenAI API key 
(you can sign up for an OpenAI account and create an API key 
[here](https://platform.openai.com/account/api-keys)). Then, create an 
environment variable as below:
```bash
export OPENAI_API_KEY=<YOUR-OPENAI-API-KEY>
```

Now, you are ready to use SpeechGPT!

## Instructions of Use

Run
```bash
python3 src/main.py
```
to kickstart SpeechGPT to listen.

Then, say "Hello!", "Hi!", "Hi there!", "Hello there!" when SpeechGPT is listening.

After SpeechGPT recognizes your words, it will be activated and greet.

Starting from now, you can simple talk to SpeechGPT as much as you want.

To deactivate SpeechGPT, please say "Stop!".

## Dedications
I dedicate this hard work commitment to my mom, whom has sacrificed everything 
for my better future. I hope I have made you proud!
