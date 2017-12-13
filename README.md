# ReduceFPS
Parses a directory and transform the video files found to 1280x960 30 FPS format.
Tranformed video files are saved in the current location with "reworked_" file prefix. Original files are moved to a
archive subdirectory

*usage:*

python ReduceFPS.py VideoFileslocation (directory)

**Warning**
* This application requires a valid ffmpeg installation;
* ReduceFPS will create a archive directory inside VideoFileslocation.

Can Do:
* introduce optional output format param
* introduce optional FPS param