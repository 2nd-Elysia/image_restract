import numpy as np
import cv2

class PicUtils:
  def to3(source:str,target:str = "./out3.jpg"):
    src = cv2.imread(source, 0)
    src_RGB = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(target, src_RGB)
    print("目标文件保存在：{}".format(target))
  def merge(src1:str,src2:str,target:str = "./out3.jpg"):
    pic1 = cv2.imread(src1)
    pic2 = cv2.imread(src2)
    merge = cv2.add(pic1,pic2)
    cv2.imwrite(target,merge)
    print("目标文件保存在：{}".format(target))
  def mask(src:str,mask:str,target:str = "./out3.jpg"):
    pic1 = cv2.imread(src)
    pic2 = cv2.imread(mask,cv2.IMREAD_GRAYSCALE)
    ret, binary_mask = cv2.threshold(pic2, 1, 255, cv2.THRESH_BINARY)
    maskedPart = cv2.bitwise_and(pic1, pic1, mask=binary_mask)
    cv2.imwrite(target,maskedPart)
    print("目标文件保存在：{}".format(target))