import speech_recognition as sr
from speech_recognition.exceptions import WaitTimeoutError

TIMEOUT_SECONDS = 15

class SpeechConverter:

    @staticmethod
    def get_prompt_from_speech():
        """
        Prompts a meat robot for a speech description and 
        converts that speech into text
        """
        r = sr.Recognizer()
        audio_text = ""

        # listen to speech and store in audio variable
        with sr.Microphone() as source:
            print("[Talk, hooman]")
            try:
                audio = r.listen(source, timeout=TIMEOUT_SECONDS)
            except WaitTimeoutError:
                print("[Listening timed out. Please check your audio device and try again]")
                return
            print("[Talking time over, thanks hooman]")

            # convert speech to text with google's libraries
            # an internet connection is required for this to work
            try:
                audio_text = r.recognize_google(audio)
            except:
                # recognize_google() method will throw a request error if the API is unreachable
                print("[Sorry, I did not get that?! Open ya mouf!]")
            print("[I heard:]\n" + audio_text)
            print("[Let's see what that looks like!]")
        return audio_text



# prompt = SpeechConverter.get_prompt_from_speech()
# prompt = "The Golden Girls on crack"
# print("Prompt: " + prompt)