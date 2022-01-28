python3 fibo.py > fibo.lily
lilypond fibo.lily
timidity -Ow -o fibo.wav fibo.midi
open fibo.pdf
rm fibo.mp3
ffmpeg -i fibo.wav -codec:a libmp3lame -qscale:a 2 fibo.mp3
afplay fibo.mp3
