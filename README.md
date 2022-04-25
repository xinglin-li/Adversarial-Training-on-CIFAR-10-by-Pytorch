# Adversarial-Training-on-CIFAR-10-by-Pytorch
* The repository contains implementaions of adversarial traning methods on CIFAR-10 by PyTorch

## Experiment Settings
* The basic experiment setting refers to the setting used in [Madry Laboratory](https://github.com/MadryLab/cifar10_challenge).
* Dataset: CIFAR-10 ( 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images. )
* Attack method: PGD attack (L2 PGD for Basic Training with Robust Dataset and Non-Robust Dataset; L-infinity PGD for the rest)


## Training Methods

### 1. Basic Training

* The basic training method adopts ResNet-18 architecture proposed by Kaiming He in [CVPR 2016](https://arxiv.org/pdf/1512.03385.pdf).
<pre>
python3 basic_training.py
</pre>
||This repository|
|------|---|
|Benign accuracy|94.91%|
|Robust accuracy (L-infinity PGD)|0.07%|


### 2. PGD Adversarial Training

* The method was proposed by Aleksander Madry in [ICLR 2018](https://arxiv.org/pdf/1706.06083.pdf).
  * Note: I only trained the model for 50 epochs, it should have a closer result to original paper if you train it for more than 150 epochs.
<pre>
python3 pgd_adversarial_training.py
</pre>
||This repository|Original paper|
|------|---|---|
|Benign accuracy|76.86%|87.30%|
|Robust accuracy (L-infinity PGD)|48.43%|50.00%|

### 3. Interpolated Adversarial Training (IAT)

* This defense method was proposed by Alex Lamb in [AISec 2019](https://arxiv.org/pdf/1906.06784.pdf).
  * Note: I only trained the model for 50 epochs, it should have a closer result to original paper if you train it for more than 150 epochs.
<pre>
python3 interpolated_adversarial_training.py
</pre>
||This repository|Original paper|
|------|---|---|
|Benign accuracy|83.72%|89.88%|
|Robust accuracy (L-infinity PGD)|42.17%|44.57%|

### 4. Basic Training with Robust / Non-robust Dataset

* The method is proposed by Andrew Ilyas in [NIPS 2019](https://arxiv.org/pdf/1905.02175.pdf).
* They treat the adversarial problem by splitting the dataset into robust and non-robust datasets.
* The robust dataset is constructed from an L2 adversarially trained model (epsilon = 0.5).
* [Dataset download: Robust Dataset](https://postechackr-my.sharepoint.com/:u:/g/personal/dongbinna_postech_ac_kr/ET9LWRoUc9ZCjU0-szWt55ABQepaeB64I8ZAruOlwNDQHg?e=FOmeb5)    
* [Dataset download: Non-robust Dataset](https://postechackr-my.sharepoint.com/:u:/g/personal/dongbinna_postech_ac_kr/EZ9_ujc-biRFvVsjKU6QSk0BsiPma8kBpZDwSM20ryYqfg?e=bhpMYg)
  * Note: I only trained the model for 50 epochs, it should have a closer result to original paper if you train it for more than 150 epochs.
<pre>
python3 basic_training_robust_dataset.py
python3 basic_training_nonrobust_dataset.py
</pre>
||Robust Dataset|Original paper (wide)|
|------|---|---|
|Benign accuracy|72.91%|84.10%|
|Robust accuracy (L2 PGD 0.25)|31.83%|48.27%|

||Non-Robust Dataset|Original paper (wide)|
|------|---|---|
|Benign accuracy|74.25%|87.68%|
|Robust accuracy (L2 PGD 0.25)|18.07%|0.82%|


## Reference:
[1] Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, Adrian Vladu. *Towards Deep Learning Models Resistant to Adversarial Attacks*, https://arxiv.org/abs/1706.06083 <br />
[2] Alex Lamb, Vikas Verma, Kenji Kawaguchi, Savya Khosla, Juho Kannala, Yoshua Bengio. *Interpolated Adversarial Training: Achieving Robust Neural Networks without Sacrificing Too Much Accuracy*, https://arxiv.org/abs/1906.06784<br />
[3] Andrew Ilyas, Shibani Santurkar, Dimitris Tsipras, Logan Engstrom, Brandon Tran, Aleksander Madry. *Adversarial Examples Are Not Bugs, They Are Features*, https://arxiv.org/abs/1905.02175<br />
[4] Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun. *Deep Residual Learning for Image Recognition*, Computer Vision and Pattern Recognition (CVPR), 2016 <br />
[5] https://github.com/ndb796/Pytorch-Adversarial-Training-CIFAR <br />
[6] https://github.com/BorealisAI/advertorch <br />
[7] https://github.com/MadryLab/cifar10_challenge
