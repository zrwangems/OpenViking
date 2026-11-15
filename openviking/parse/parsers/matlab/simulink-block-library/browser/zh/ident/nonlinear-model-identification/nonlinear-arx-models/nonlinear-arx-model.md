---
type: simulink-block
title: 'Nonlinear ARX Model'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Nonlinear Model Identification / Nonlinear ARX Models'
documentation_page: 'nonlineararxmodel'
documentation_source_path: 'ref/nonlineararxmodel.html'
language: zh-CN
chinese_source: official
---

# Nonlinear ARX Model

## 端口

### 输入

### **Port\_1(In1)** — 仿真输入数据 标量 | 向量

仿真输入数据，对于单输入模型，指定为标量。数据必须是时域数据。对于多输入模型，请将输入指定为一个 *Nu*-元素向量，其中 *Nu* 表示输入数量。例如，您可以使用 Vector Concatenate (Simulink) 模块将标量信号连接成向量信号。

**注意**

请勿使用 Bus Creator (Simulink) 或 Mux (Simulink) 模块生成向量信号。

**数据类型:** `double`
### 输出

### **Port\_1(Out1)** — 仿真输出 标量 | 向量

非线性 ARX 模型的仿真输出，对于单输出模型以标量形式返回，对于具有 *Ny* 个输出的模型则以 *Ny* 元向量形式返回。

**数据类型:** `double`

## 参数

### **模型** — 待仿真的非线性 ARX 模型 `idnlarx` 对象

待仿真的非线性 ARX 模型，以 `idnlarx` 对象形式指定。您先前已在 MATLAB 工作区中预先估计或构建了 `idnlarx` 模型。

### **初始条件** — 仿真初始条件设定 **Input and output values** (默认) | **State values**

非线性 ARX 模型的状态对应于该模型结构中的动态元素。动态元素是模型回归器。回归变量可以是延迟输入或输出变量（标准回归变量），也可以是用户自定义的延迟输入输出变量变换（自定义回归变量）。有关非线性 ARX 模型的状态的信息，请参阅 `idnlarx` 参考页面。

对于仿真非线性 ARX 模型，您可以通过以下方式之一指定初始条件：

- **Input and output values** - 在 `Input level` 和 `Output level` 中分别指定稳态输入和输出信号电平。
- **State values** - 指定一个向量，其长度等于 `Specify initial states as a vector` 中模型的状态数。

### **Input level** — 稳态输入信号电平 `0` (默认) | 标量

仿真前的稳态输入信号电平，指定为标量。

#### 依赖关系

要启用此参数，请将 `Initial conditions` 指定为 **Input and output values**。

### **Output level** — 稳态输出信号电平 `0` (默认) | 标量

仿真前的稳态输出信号电平，指定为标量。

#### 依赖关系

要启用此参数，请将 `Initial conditions` 指定为 `Input and output values`。

### **Specify initial states as a vector** — 初始状态值 `0` (默认) | 向量

模型的初始状态值，指定为一个 *Nx*-元素向量，其中 *Nx* 为模型的状态数。此参数命名为 **Vector of state values**，直到您指定 `Model` 为止。

若未知初始状态，可按以下方式估计这些状态：

- 当您不知道对应的输出电平时，要仿真给定输入电平下的模型，请使用 `idnlarx/findop` 命令估计平衡状态值。例如，要仿真一个关于稳态点的模型 `M`，其中输入为 `1` 且输出未知，则将初始状态值指定为 `X0`，其中

  ```
  X0 = findop(M,'steady',1,NaN)
  ```
- 要估计使测量数据与模型对相同输入的仿真响应达到最佳拟合的初始状态，请使用 `findstates` 命令。例如，要计算初始状态，使得模型 `M` 的响应与数据集 `z` 中的输出数据相匹配，请指定 `X0`，使得：

  ```
  X0 = findstates(M,z,Inf)
  ```
- 要继续执行先前仿真运行中的仿真，请使用先前仿真的模拟输入输出值来计算当前仿真的初始状态 `X0`。使用 `data2state` 命令计算 `X0`。例如，假设变量 `firstSimData` 存储了先前仿真的输入和输出值。对于模型 `M`，您可以指定 `X0`，使得：

  ```
  X0 = data2state(M,firstSimData)
  ```

#### 依赖关系

要启用此参数，请将 `Initial conditions` 指定为 **State values**。

## 所属库

System Identification Toolbox / Models

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2008a 中推出**

## 描述

在 Simulink 软件中仿真非线性 ARX 模型

Nonlinear ARX Model 模块通过时域输入数据仿真非线性 ARX 模型的输出。该模型是您先前在 MATLAB® 工作区中估计或构建的 `idnlarx` 模型。您可将初始条件指定为稳态输入和输出信号电平，或初始状态向量。
