import os, sys
from glob import glob
import subprocess
import traceback
import shutil
import argparse

# VIDEOINPATH = "Z:\motorvakantie_2016\\2016-08-10\HERO4 Silver"
# VIDEOINPATH = "D:\Kletter\Hemelvaart_Tour\Out"

def reduceFPS(inFile, outFile):
    """
    Transform video file using ffmpeg. Default output 1280x960 with 30 FPS
    :param inFile: source file path
    :type inFile: string
    :param outFile: target file path
    :type outFile: string
    :return: none
    """
    try:
        myArgs = ['ffmpeg', '-y', '-i', inFile, '-r', '30', '-s', '1280x960', '-c:v', 'libx264', '-b:v', '3M',
                  '-strict', '-2', '-movflags', 'faststart', outFile]
        myProc = subprocess.Popen(myArgs, stdout=subprocess.PIPE)
        out, err = myProc.communicate()
        if err is not None:
            print "ffmpeg error: %s" % err
    except Exception:
        print "error: %s" % traceback.format_exc()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("videofolder", help="The location where the video files are located (parsing is recursive)", \
                        type=str)
    args = parser.parse_args()
    videofolder = args.videofolder
    if not os.path.isdir(videofolder):
        print "videofolder %s does not exits" % videofolder
        sys.exit()
    else:
        # create a archive folder to move the processed file to (these files are not processed again by os.walk)
        ArchiveDir = os.path.join(videofolder,'archive')
        if not os.path.isdir(ArchiveDir):
            try:
                os.makedirs(ArchiveDir)
            except Exception:
                print "error creating archive location: %s. Error: %s." % (ArchiveDir, traceback.format_exc())
                sys.exit()
        myFiles = [y for x in os.walk(videofolder) for y in glob(os.path.join(x[0], '*.MP4'))]
        for myFile in myFiles:
            if not 'reworked' in myFile:
                # process the file and save the result in the original location with "reworked_" file prefix
                newFileName = os.path.join(os.path.dirname(myFile), "reworked_" + os.path.basename(myFile))
                reduceFPS(inFile=myFile, outFile=newFileName)
                # if processing is done: move the original file to the created archive folder
                try:
                    shutil.move(myFile, ArchiveDir)
                except Exception:
                    print "error moving file from: %s to %s. Error: %s." % (myFile, ArchiveDir, traceback.format_exc())
