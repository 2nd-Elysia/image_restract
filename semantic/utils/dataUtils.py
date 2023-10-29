import cv2
import numpy as np
import os
from alive_progress import alive_bar

class dataUtils:
    def cutPic():
        size = 512
        pad = 200
        count = 0
        base = "./"
        for n in range(10):
            name = "{}".format(n)
            img = cv2.imread("{}/imgs/{}.png".format(base,name))
            mask = cv2.imread("{}/masks/{}.png".format(base,name))
            x = (img.shape[0]-size)//pad
            y = (img.shape[1]-size)//pad
            with alive_bar(x+1) as bar:
                xPos = 0
                yPos = 0
                for i in range(x+1):
                    for j in range(y+1):
                        imgCut = img[xPos:(xPos+size),yPos:(yPos+size)]
                        maskCut = mask[xPos:(xPos+size),yPos:(yPos+size)]
                        yPos += pad
                        if len(np.nonzero(maskCut)[0]) == 0:
                            continue
                        cv2.imwrite("./data/imgs/{}.png".format(count), imgCut)
                        cv2.imwrite("./data/masks/{}.png".format(count), maskCut)
                        count +=1
                    yPos = 0
                    xPos += pad
                    bar()