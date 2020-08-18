for %%a in ("*.avi") do ffmpeg -i "%%a"  "\%%~na.wav
pause
