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

python predict.py -m model2.pth -i ../../transformed2to222.png -o ../../output2to222.png
