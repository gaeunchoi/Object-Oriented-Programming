# coding: utf-8
import os
import sys
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import matplotlib.pyplot as plt
from dataset.mnist import load_mnist
from common.util import smooth_curve
from common.multi_layer_net import MultiLayerNet
from common.optimizer import *

# 최욱 추가
import numpy as np
# 여러 분이 작성해야 하는 클래스
class AdaGrad_with_Momentum:
    """AdaGrad with Momentum"""

# 생성자에는 Momentum을 사용한 AdaGrad 방법을 만들 때 필요한 변수들을 선언해 놓았음. 왠만하면 바꾸지 말 것.
# 하지만, 본인이 생각한 알고리즘 구현을 위해 수정이 필요한 경우 바꿔도 됨. 단, 디폴트 값을 미리 지정해 놓아서,
# 이 클래스 이외의 다른 코드 변경 없이 동작할 수 있도록 할 것.
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr # 강의 자료에서 학습률(learning rate)에 해당하는 변수
        self.momentum=momentum # 강의 자료에서 alpha에 해당하는 변수
        self.h = None # AdaGrad에서 gradient의 크기 h에 해당하는 변수
        self.v = None # Momentum에서 속도 v에 해당하는 변수

# 아래 update 함수는 현재 AdaGrad를 그대로 복사해 놓은 상태임. Momentum을 사용하도록 고치시오.        
    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)
                
        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
            
# 0. MNIST 데이터 읽기==========
(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True)

train_size = x_train.shape[0]
batch_size = 128
max_iterations = 2000


# 1. 실험용 설정==========
optimizers = {}
optimizers['SGD'] = SGD()
optimizers['Momentum'] = Momentum()
optimizers['AdaGrad'] = AdaGrad()
optimizers['Adam'] = Adam()
optimizers['AdaGrad_with_Momentum'] = AdaGrad_with_Momentum()

networks = {}
train_loss = {}
for key in optimizers.keys():
    networks[key] = MultiLayerNet(
        input_size=784, hidden_size_list=[100, 100, 100, 100],
        output_size=10)
    train_loss[key] = []    


# 2. 훈련 시작==========
for i in range(max_iterations):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    
    for key in optimizers.keys():
        grads = networks[key].gradient(x_batch, t_batch)
        optimizers[key].update(networks[key].params, grads)
    
        loss = networks[key].loss(x_batch, t_batch)
        train_loss[key].append(loss)
    
    if i % 100 == 0:
        print( "===========" + "iteration:" + str(i) + "===========")
        for key in optimizers.keys():
            loss = networks[key].loss(x_batch, t_batch)
            print(key + ":" + str(loss))


# 3. 그래프 그리기==========
markers = {"SGD": "o", "Momentum": "x", "AdaGrad": "s", "Adam": "D", "AdaGrad_with_Momentum": "x"}
x = np.arange(max_iterations)
for key in optimizers.keys():
    plt.plot(x, smooth_curve(train_loss[key]), marker=markers[key], markevery=100, label=key)
plt.xlabel("iterations")
plt.ylabel("loss")
plt.ylim(0, 1)
plt.legend()
plt.show()
