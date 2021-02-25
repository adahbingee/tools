import os
import sys
import glob
import shutil
import tempfile
import numpy as np

if len(sys.argv) < 3:
    print('python [input directory] [output directory]')
    exit()

# extract frame number per video
selectCnt = 10

# input  videos directory
inptPath = sys.argv[1]

# output images directory
ouptPath = sys.argv[2]

# video list
vidNPathList = glob.glob(os.path.join(inptPath, '*.mp4'))

for vidPath in vidNPathList:

    frameCnt = 0

    # filename.mp4
    fileNameFull = os.path.split(vidPath)[-1]
    # filename
    fileName     = os.path.splitext(fileNameFull)[0]

    # make temp directory
    tmpDir = tempfile.mkdtemp()

    # extract frames by ffmpeg
    tmpPth = os.path.join(tmpDir, '%06d.png')
    tmpCmd = 'ffmpeg -i {} -start_number 0 {}'.format(vidPath, tmpPth)
    os.system(tmpCmd)

    # get total frame number of this video
    fileList = glob.glob(os.path.join(tmpDir, '*.png'))
    # total frame count
    totalFrameCnt = len(fileList)
    # interval count
    interval = np.floor(totalFrameCnt / selectCnt)
    # selected frame index
    intervalList = np.unique(np.linspace(0, totalFrameCnt-1,selectCnt).astype(np.int))

    for i in intervalList:
        print(fileList[i])
        # saving image, format videoName_0000.png
        savingName = '{}_{:06}.png'.format(fileName, frameCnt)
        savingName = os.path.join(ouptPath, savingName)
        shutil.copyfile(fileList[i], savingName)
        frameCnt += 1

    # delete temp directory
    shutil.rmtree(tmpDir)
