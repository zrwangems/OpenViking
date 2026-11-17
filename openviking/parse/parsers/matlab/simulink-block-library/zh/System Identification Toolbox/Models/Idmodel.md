---
type: simulink-block
title: 'Idmodel'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Models'
documentation_page: 'idmodel'
documentation_source_path: 'ref/idmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Idmodel

## 端口
```yaml
ports:
- name: Port_1(In1)
  summary: 仿真输入数据 标量 | 向量
  direction: input
  data_types: double
- name: Port_1(Out1)
  summary: 仿真输出 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **Port\_1(In1)** — 仿真输入数据 标量 | 向量

仿真输入数据，对于单输入模型指定为标量。
数据必须是时域数据。对于多输入模型，将输入指定为
*Nu* 元素向量，其中
*Nu* 是输入的数量。例如，您可以使用
Vector Concatenate (Simulink) 模块
将标量信号连接成向量信号。

**注意**

不要使用 Bus Creator (Simulink) 或
Mux (Simulink) 模块来生成
向量信号。

**数据类型：** `double`
### 输出

### **Port\_1(Out1)** — 仿真输出 标量 | 向量

线性模型的仿真输出，对于单输出模型返回为标量，
对于具有 *Ny* 个输出的模型返回为 *Ny* 元素向量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Identified model
  summary: 要仿真的线性模型 idss(-1,1,1,0,'Ts',1)（默认）| idss 对象 | idgrey 对象 | idpoly 对象 | idtf 对象 | idproc 对象
  group: ''
- name: Initial conditions
  summary: 初始条件 0（默认）| 数值向量 | initialCondition 对象
  group: ''
- name: Add noise
  summary: 向仿真输出添加噪声 on（默认）| off
  group: ''
- name: Noise seed(s)
  summary: 为多次仿真向输出添加相同的噪声 []（默认）| 非负整数 | 向量
  group: ''
```

### **Identified model** — 要仿真的线性模型 `idss(-1,1,1,0,'Ts',1)`（默认）| `idss` 对象 | `idgrey` 对象 | `idpoly` 对象 | `idtf` 对象 | `idproc` 对象

要仿真的线性模型，指定为以下对象之一：

- `idss` —
  状态空间模型
- `idgrey` — 线性
  灰箱模型
- `idpoly` —
  多项式模型
- `idtf` — 传递
  函数模型
- `idproc` — 过程
  模型

此对象必须是先前估计或构建的线性模型的 MATLAB® 或模型工作区变量。线性模型可以是连续时间或
离散时间，并且可以带或不带输入/输出延迟。

### **Initial conditions** — 初始条件 `0`（默认）| 数值向量 | `initialCondition` 对象

线性模型的初始条件，指定为数值向量或
`initialCondition` 对象。

- 如果由 **Identified
  model** 指定的线性模型是状态空间（`idss`）或
  线性灰箱（`idgrey`）模型，则将
  **Initial conditions** 指定为
  *Nx* 元素数值向量，表示初始状态
  值，其中 *Nx* 是模型的
  状态数。
- 对于 Idmodel 模块支持的所有其他线性模型，将 **Initial
  conditions** 指定为 `initialCondition`
  对象。您也可以使用此对象为 `idss` 和
  `idgrey` 模型指定初始
  条件。

要生成用于指定初始条件的初始状态值或 `initialCondition`
对象，请参阅 Estimate Initial Conditions for Simulating Linear Models。

要将初始条件表示为零，请将 **Initial
conditions** 指定为 `0` 或
`[]`。

要复现您在 System Identification 应用的 Model Output 绘图
窗口中获得的仿真结果，或从 `compare` 命令获得的仿真结果，请参阅 Reproduce Command Line or System Identification App Simulation Results in Simulink。

### **Add noise** — 向仿真输出添加噪声 `on`（默认）| `off`

当您选择此参数时，模块从
线性模型属性 `model.NoiseVariance` 中推导噪声幅度。软件使用模型的噪声传递
函数对随机高斯白噪声进行滤波，并将所得噪声添加到仿真模型
响应中。如果您希望在每次运行
Simulink® 模型时添加相同的噪声，请指定 **Noise seed(s)**
参数。

如果您向仿真输出添加噪声，那么为了在
正确的时间步生成噪声，您必须执行以下操作之一：

1. 设置由
   **Identified model** 参数指定的线性模型的采样时间。
2. 将 **Initial conditions** 参数
   指定为 `initialCondition` 对象。此对象
   包含模型采样时间信息。

对于连续时间模型，噪声项的理想方差是
无穷大。实际上，您看到的是考虑了
系统时间常数的带限噪声。您可以将所得的仿真
输出解释为使用低通滤波器滤波后的响应，该滤波器的通带
不会扭曲来自
输入的动态。

### **Noise seed(s)** — 为多次仿真向输出添加相同的噪声 `[]`（默认）| 非负整数 | 向量

**Noise seed(s)** 属性为随机数生成器设置种子，使得每次运行 Simulink 模型时，模块向仿真输出添加相同的噪声。有关使用种子的信息，请参阅 `rng`。

对于多输出模型，您可以使用独立的噪声实现来生成带加性噪声的输出。输入一个包含 *Ny* 个非负整数项的向量，其中 *Ny* 是输出通道的数量。

对于每次仿真之间变化的随机重启，将 **Noise seed(s)** 指定为 `[]`。

#### 依赖

要启用此参数，请选择 `Add noise`。
## 所属库

System Identification Toolbox / Models

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

在 Simulink 软件中仿真已辨识的线性模型

Idmodel 模块使用时域输入数据仿真已辨识线性模型的输出。该模型是您之前估计或创建的状态空间（`idss`）、线性灰箱（`idgrey`）、多项式（`idpoly`）、传递函数（`idtf`）或过程（`idproc`）模型。对于状态空间和线性灰箱模型的仿真，您可以指定初始状态值。对于其他线性模型，使用 `initialCondition` 对象指定初始条件。您还可以向仿真输出添加噪声。
