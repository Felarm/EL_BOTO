from gtts import gTTS
import os


def test(text: str, language: str):

    voice = gTTS(text=text, lang=language, slow=False)
    voice.save('test.mp3')

    os.system('test.mp3')


if __name__ == '__main__':
    test('Вставай, жиробас', 'ru')
    print(1)