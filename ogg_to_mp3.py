#This program converts every ogg file in a folder to mp3

from pydub import AudioSegment
from os import walk

#Input and output path
input_path = input("Input path to your ogg files's folder")
output_path = input("Input path to where you want your mp3 files to be")

f = []
#Search for all files in a folder
for (dirpath, dirnames, filenames) in walk(input_path):
    for f in filenames:
        #Checks if the folder is a .ogg
        if '.ogg' in f:
            wav_audio = AudioSegment.from_ogg(f'{dirpath}\{f}')
            #Converts it to mp3 in the desired folder
            wav_audio.export(f"{output_path}\{f.split(sep='.')[0]}.mp3", format="mp3")