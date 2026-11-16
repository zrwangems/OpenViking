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

### 输入

### **Port\_1(In1)** — 仿真输入数据 标量 | 向量

仿真输入数据，对于单输入模型指定为标量。数据必须是时域数据。对于多输入模型，将输入指定为 *Nu* 元素向量，其中 *Nu* 是输入数。例如，您可以使用 Vector Concatenate (Simulink) 模块将标量信号串联为向量信号。

**注意**

不要使用 Bus Creator (Simulink) 或 Mux (Simulink) 模块生成该向量信号。

**数据类型：** `double`
### 输出

### **Port\_1(Out1)** — 仿真输出 标量 | 向量

线性模型的仿真输出，对于单输出模型返回为标量，对于具有 *Ny* 个输出的模型返回为 *Ny* 元素向量。

**数据类型：** `double`

## 参数

### **已辨识模型** — 要仿真的线性模型 `idss(-1,1,1,0,'Ts',1)` (默认) | `idss` 对象 | `idgrey` 对象 | `idpoly` 对象 | `idtf` 对象 | `idproc` 对象

要仿真的线性模型，指定为以下对象之一：

- `idss` — 状态空间模型
- `idgrey` — 线性灰箱模型
- `idpoly` — 多项式模型
- `idtf` — 传递函数模型
- `idproc` — 过程模型

此对象必须是先前估计或构建的线性模型的 MATLAB® 或模型工作区变量。线性模型可以是连续时间或离散时间，并且可以带或不带输入/输出延迟。

### **初始条件** — 初始条件 `0` (默认) | 数值向量 | `initialCondition` 对象

线性模型的初始条件，指定为数值向量或 `initialCondition` 对象。

- 如果由 **已辨识模型** 指定的线性模型是状态空间 (`idss`) 或线性灰箱 (`idgrey`) 模型，则将 **初始条件** 指定为初始状态值的 *Nx* 元素数值向量，其中 *Nx* 是模型的状态数。
- 对于 Idmodel 模块支持的所有其他线性模型，将 **初始条件** 指定为 `initialCondition` 对象。您也可以使用此对象为 `idss` 和 `idgrey` 模型指定初始条件。

要生成用于指定初始条件的初始状态值或 `initialCondition` 对象，请参阅 Estimate Initial Conditions for Simulating Linear Models。

要表示零初始条件，请将 **初始条件** 指定为 `0` 或 `[]`。

要重现您在 System Identification app 的 Model Output 绘图窗口中，或通过 `compare` 命令获得的仿真结果，请参阅 Reproduce Command Line or System Identification App Simulation Results in Simulink。

### **添加噪声** — 向仿真输出添加噪声 `on` (默认) | `off`

选择此参数时，模块从线性模型属性 `model.NoiseVariance` 中导出噪声幅值。软件使用模型的噪声传递函数对随机高斯白噪声进行滤波，并将所得噪声添加到仿真的模型响应中。如果要在每次运行 Simulink® 模型时添加相同的噪声，请指定 **噪声种子** 参数。

如果向仿真输出添加噪声，则为了在正确的时间步生成噪声，您必须执行以下操作之一：

1. 设置由 **已辨识模型** 参数指定的线性模型的采样时间。
2. 将 **初始条件** 参数指定为 `initialCondition` 对象。此对象包含模型采样时间信息。

对于连续时间模型，噪声项的理想方差是无限的。实际上，您会看到考虑到系统时间常数的带限噪声。您可以将所得的仿真输出解释为使用低通滤波器滤波后的响应，该滤波器的通带不会使来自输入的动态发生失真。

### **噪声种子** — 在多次仿真中向输出添加相同噪声 `[]` (默认) | 非负整数 | 向量

**噪声种子** 属性为随机数生成器提供种子，使模块在每次运行 Simulink 模型时向仿真输出添加相同的噪声。有关使用种子的信息，请参阅 `rng`。

对于多输出模型，您可以使用生成带加性噪声输出的独立噪声实现。输入由 *Ny* 个非负整数项组成的向量，其中 *Ny* 是输出通道数。

对于因仿真而异的随机重启，请将 **噪声种子** 指定为 `[]`。

#### 依赖关系

要启用此参数，请选择 `Add noise`。

## 所属库

System Identification Toolbox / Models

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

在 Simulink 软件中仿真已辨识线性模型

Idmodel 模块使用时域输入数据仿真已辨识线性模型的输出。该模型是您先前估计或创建的状态空间 (`idss`)、线性灰箱 (`idgrey`)、多项式 (`idpoly`)、传递函数 (`idtf`) 或过程 (`idproc`) 模型。对于状态空间和线性灰箱模型的仿真，您可以指定初始状态值。对于其他线性模型，使用 `initialCondition` 对象指定初始条件。您还可以向仿真输出添加噪声。
