---
type: simulink-block
title: 'RST Controller'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'rstcontroller'
documentation_source_path: 'ref/rstcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# RST Controller

## 端口

### 输入

### **r** — Plant reference scalar

Plant system reference signal.

**数据类型：** `single` | `double`

### **y** — Plant output scalar

Plant system output signal.

**数据类型：** `single` | `double`
### 输出

### **u** — Controller output scalar

Control system output signal.

**数据类型：** `single` | `double`

## 参数

### **Controller parameterization** — 参数化方法 `Controller polynomials`（默认）| `Generate polynomials`

用于参数化控制器的方法。如果您知道离散时间
*R*、*S* 和 *T*
多项式值，请选择 `Controller polynomials`。
否则，请选择 `Generate polynomials`。

#### 依赖关系

选择参数化方法会启用其他参数。

### **R polynomial** — *R* 多项式值 `1`（默认）| 正数、标量或向量

用于 RST 控制的 *R* 多项式向量。

#### 依赖关系

为
**Controller parameterization** 参数选择 `Controller polynomials` 会启用
此参数。

### **S polynomial** — *S* 多项式值 `1`（默认）| 正数、标量或向量

用于 RST 控制的 *S* 多项式向量。

#### 依赖关系

为
**Controller parameterization** 参数选择 `Controller polynomials` 会启用
此参数。

### **T polynomial** — *T* 多项式值 `1`（默认）| 正数、标量或向量

用于 RST 控制的 *T* 多项式向量。

#### 依赖关系

为
**Controller parameterization** 参数选择 `Controller polynomials` 会启用
此参数。

### **Model discrete transfer function numerator** — 传递函数分子 `1`（默认）| 标量或向量

系统离散化传递函数的分子。要确定
离散传递函数，如果您有 Control System Toolbox™ 许可证，请使用 `c2d` 函数。

#### 依赖关系

为
**Controller parameterization** 参数选择 `Generate polynomials` 会启用
此参数。

### **Model discrete transfer function denominator** — 传递函数分母 `[1 0.5]`（默认）| 向量

系统离散化传递函数的分母。要确定
离散传递函数，如果您有 Control System Toolbox 许可证，请使用 `c2d` 函数。

#### 依赖关系

为
**Controller parameterization** 参数选择 `Generate polynomials` 会启用
此参数。

### **Control horizon (samples)** — 控制时域 samples 数 `5`（默认）| 正整数

控制时域中的 samples 数。

#### 依赖关系

为
**Controller parameterization** 参数选择 `Generate polynomials` 会启用
此参数。

### **Control weighting factor** — 加权因子 `0.5`（默认）| 正数

RST 控制器的加权因子。

#### 依赖关系

为
**Controller parameterization** 参数选择 `Generate polynomials` 会启用
此参数。

### **System dead time (samples)** — 死区时间 samples 数 `2`（默认）| `0` 或正整数

死区时间的 samples 数。

#### 依赖关系

为
**Controller parameterization** 参数选择 `Generate polynomials` 会启用
此参数。

### **Sample time (-1 for inherited)** — 采样间隔 `-1`（默认）| 默认值或正数

采样之间的时间间隔。如果模块位于
触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续
可变步长模型中，请显式指定采样时间。有关更多
信息，请参阅什么是采样时间？和
指定采样时间。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

使用多项式表示的预测控制

RST Controller 模块使用参考信号跟踪多项式表示实现广义预测控制器。该图显示了控制算法的等效电路。

### 方程

受控自回归积分滑动平均 (CARIMA) 模型描述被控对象：

A(z−1)y(k)=z−dB(z−1)u(k−1)+e(k)C(z−1)D(z−1)

A(z−1)=1+a1z−1+⋯+anAz−nA

B(z−1)=b0+b1z−1+⋯+bnBz−nB

C(z−1)=1

D(z−1)=1−z−1,

其中：

- *d* 是系统死区时间。
- *y(k)* 是被控对象输出。
- *u(k)* 是控制器输出。
- *e(k)* 是均值为零的白噪声。
- *A(z-1)* 和
  *B(z-1)* 是
  系统多项式。
- *nA* 和 *nB* 是多项式
  阶数。
- *C(z-1)* 和
  *D(z-1)* 是
  用于获得稳态误差的扰动多项式。

预测模型给定为

y^(k+j|k)=Gj−d(z−1)D(z−1)z−d−1u(k+j)+Hj−d(z−1)D(z−1)C(z−1)u(k−1)+Fj−d(z−1)C(z−1)y(k)

并且

j=hi,hp¯

其中：

- *hi* 是最小预测。
- *hp* 是预测时域。

在时刻 *k* 计算的未来控制序列为

u(k+j−1|k),

其中

j=1,hc¯

且 *hc* 是控制时域。

输出的预测值为

y^(k+j|k)。

为确定系统多项式 Fj−d(z−1)、Gj−d(z−1) 和 Hj−d(z−1)，该模块使用两个 Diophantine 方程。第一个 Diophantine
方程为

C(z−1)A(z−1)D(z−1)=Ej−d(z−1)+z−j+dFj−d(z−1)A(z−1)D(z−1),

其中：

Ej−d(z−1)=1+1+e1z−1+⋯+enEz−nE

Fj−d(z−1)=f0+f1z−1+⋯+fnFz−nF

nE=j−d−1

nF=max(nA+nD−1,nC−j+d)

第二个 Diophantine 方程为

Ej−d(z−1)B(z−1)=C(z−1)Gj−d(z−1)+z−j+dHj−d(z−1),

其中：

Gj−d(z−1)=g0+g1z−1+⋯+gnGz−nG

Hj−d(z−1)=h0+h1z−1+⋯+hnHz−nH

nG=j−d−1

nH=max(nC,nB+d)−1

所得预测模型为

y^(k+j|k)=Gj−d(z−1)D(z−1)z−d−1u(k+j)+y^0(k+j|k),

其中

y^0(k+j|k)=Hj−d(z−1)D(z−1)C(z−1)u(k−1)+Fj−d(z−1)C(z−1)y(k)

表示系统的自由响应。

使用矩阵表示法，预测模型可写为

y^=Gud+y^0,

其中：

y^=[y^(k+hi|k),y^(k+hi+1|k),⋯,y^(k+hp|k)]T

G=[ghi−d−1⋯g00⋯0ghi−d⋯g1g0⋯0⋯⋯⋯⋯⋯⋯ghc−1⋯⋯⋯⋯g0ghp−d−1⋯⋯⋯⋯ghp−hc−1]

ud=[D(z−1)u(k),⋯,D(z−1)u(k+hc−1)]T

y^0=[y^0(k+hi|k),y^0(k+hi+1|k),⋯,y^0(k+hp|k)]T

为最小化跟踪误差和控制器输出，该模块使用成本函数。
为在最小化跟踪误差与最小化
控制器输出之间进行权衡，该模块使用加权因子 λ，使得

J=(Gud+y^0−w)T(Gud+y^0−w)+λudTud

对于

D(z−1)u(k+i)=0

并且

i∈[hc,hp−d−1],

其中 *w* 是参考轨迹向量。最小化成本
函数，得到最优控制序列的方程：

ud\*=(GTG+λIhc)GT[w−y^0].

由于 *γj* 以及 j=hi,hp¯ 是矩阵 (GTG+λIhc)−1GT 第一行中的元素，应用滚动
时域原理得到控制算法方程为

D(z−1)u(k)=∑j=hihpγj[w(k+j|k)−y^0(k+j|k)].

使用 y^0(k+j|k)=Hj−d(z−1)D(z−1)C(z−1)u(k−1)+Fj−d(z−1)C(z−1)y(k) 进行代入，得到控制算法方程的这种形式：

C(z−1)D(z−1)u(k)=−∑j=hihpγjHj−d(z−1)D(z−1)u(k−1)−∑j=hihpγjFj−d(z−1)y(k)+∑j=hihpγjC(z−1)w(k+j).

控制算法的多项式形式如下

R(z−1)u(k)+S(z−1)y(k)=T(z−1)w(k+hp),

其中：

R(z−1)=(C(z−1)+∑j=hihpγjz−1Hj−d(z−1)) D(z−1),

S(z−1)=∑j=hihpγjFj−d(z−1),

并且

T(z−1)=C(z−1)∑j=hihpγjz−hp+j.

### 限制

为获得 *R*、*S* 和 *T*
多项式，请使用离散时间传递函数，而不是连续时间
传递函数。
