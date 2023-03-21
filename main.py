# https://pythonbasics.org/convert-mp3-to-wav/

# https://www.analyticsvidhya.com/blog/2021/09/ok-google-speech-to-text-in-python-with-deep-learning-in-2-minutes/
def convert_mp3_wav(name):
    from os import path
    from pydub import AudioSegment

    # files
    src = "transcript.mp3"
    dst = "test.wav"

    # convert wav to mp3
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
