from utils.picUtils import PicUtils
import cv2
import numpy

raw = "torch-UNet/0.png"
mask = "torch-UNet/output0.jpg"

PicUtils.mask(raw,mask)