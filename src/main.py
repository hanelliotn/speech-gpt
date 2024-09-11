# Import libraries
from speech_gpt import SpeechGPT
import pyttsx3


def main():
    # Set up voice engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[14].id)
    engine.setProperty('rate', 180)

    # Set up SpeechGPT
    speech_gpt = SpeechGPT(voice_engine=engine, speech_recognizer=None)
    is_activated = False

    # SpeechGPT listens and responds
    while True:
        what_human_said = speech_gpt.listen()
        if what_human_said == "":
            continue
        elif what_human_said.lower() in ["hello", "hi", "hey", "hello there", "hi there"]:
            is_activated = speech_gpt.activate()
            continue
        elif "stop" in what_human_said.lower():
            is_activated = speech_gpt.deactivate()
            break
        if is_activated:
            speech_gpt.simple_chat(what_human_said)


if __name__ == "__main__":
    main()