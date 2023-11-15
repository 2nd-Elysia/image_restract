# readme

## 训练

>python train.py

## 预测

>python predict.py -m model2.pth -i imput.png -o output.png

修改输入输出图片即可

## 分割

>python test.py

## 直接应用

cd semantic/torch-UNet
conda activate test

python predict.py -m model2.pth -i ../../origin_images/2.png -o ../../mask_image/output2.png
python predict.py -m model2.pth -i ../../trans_image/transformed2to222.png -o ../../mask_image/output2to222.png

python predict.py -m model2.pth -i ../../222transed.jpg -o ../../output222transed.jpg