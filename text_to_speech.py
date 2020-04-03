from gtts import gTTS
import os


class TextToSpeech:

    def __init__(self, text: str, lang: str):
        self.text = text
        self.lang = lang

    def convert(self):
        voice = gTTS(text=self.text, lang=self.lang)
        return voice

    def save(self):
        path = './tmp/voice.ogg'
        voice = self.convert()
        voice.save(path)
        return path

    def stream(self):
        pass

    def play_saved(self):
        try:
            os.system('/tmp/voice.ogg')
        except Exception as err:
            print(err)


if __name__ == '__main__':
    tts = TextToSpeech('Вставай жиробас', 'ru')
    tts.save()
    tts.play_saved()