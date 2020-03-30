import requests

def i_speech_test():
    server = 'http://api.ispeech.org/api/rest'

    action = 'convert'
    text = 'wake up'
    voice = 'usenglishmale'
    format = 'mp3'
    frequency = 44100
    bitrate = 128
    speed = 1
    startpadding = 1
    endpadding = 1
    pitch = 110
    filename = 'test'

    api_key = 'bbf77e6326418c2de0046579f16680ac'
    api_action = 'information'
    api_output = 'rest'

    r1 = requests.get(server, params={'apikey': api_key,
                                      'action': api_action,
                                      'output': api_output})

    r2 = requests.get('http://api.ispeech.org/api/rest',
                     params={
                     'text': text,
                     'voice': voice,
                     'format': format,
                     'frequency': frequency,
                     'bitrate': bitrate,
                     'speed': speed,
                     'startpadding': startpadding,
                     'endpadding': endpadding,
                     'pitch': pitch,
                     'filename': filename})

def voicerss_test():
    import voicerss_tts

    voice = voicerss_tts.speech({
        'key': '',
        'hl': 'ru-ru',
        'src': 'Эй, Диего Марадонна. Ты совсем запустил себя.',
        'r': '0',
        'c': 'mp3',
        'f': '44khz_16bit_stereo',
        'ssml': 'false',
        'b64': 'false'
    })
    with open('test.mp3', 'wb') as f:
        f.write(voice['response'])


if __name__ == '__main__':
    voicerss_test()
    print(1)