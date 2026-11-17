---
type: simulink-block
title: 'Hammerstein-Wiener Model'
family: 'ident'
product_id: 'ident'
product_name: 'System Identification Toolbox'
documentation_release: R2025b
official_category: 'Models'
documentation_page: 'hammersteinwienermodel'
documentation_source_path: 'ref/hammersteinwienermodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Hammerstein-Wiener Model

## 端口

### 输入

### **Port\_1(In1)** — 仿真输入数据 标量 | 向量

仿真输入数据，对于单输入模型指定为标量。
数据必须是时域数据。对于多输入模型，将输入指定为 *Nu* 元素向量，其中
*Nu* 是输入的数量。例如，您可以使用 Vector Concatenate (Simulink) 模块
将标量信号连接为向量信号。

**注意**

不要使用 Bus Creator (Simulink) 或
Mux (Simulink) 模块来生成向量信号。

**数据类型：** `double`
### 输出

### **Port\_1(Out1)** — 仿真输出 标量 | 向量

Hammerstein-Wiener 模型的仿真输出，对于单输出模型返回为标量，
对于具有 *Ny* 个输出的模型返回为 *Ny* 元素向量。

**数据类型：** `double`

## 参数

### **Model** — 要仿真的 Hammerstein-Wiener 模型 `idnlhw` 对象

要仿真的 Hammerstein-Wiener 模型，指定为 `idnlhw` 对象。您
事先在 MATLAB 工作区中估计或构建 `idnlhw` 模型。

### **Initial conditions** — 仿真的初始条件指定 `Zero`（默认）| `State values`

Hammerstein-Wiener 模型的状态对应于嵌入的线性 `idpoly` 或 `idss`
模型的状态。有关状态的详细信息，请参阅 `idnlhw` 参考页。您
将 `Initial conditions` 指定为以下之一：

- `Zero` — 指定零初始
  状态值，对应于从静止状态开始的仿真。
- `State values` — 您在
  **Specify a vector of state values** 中指定
  状态值。将状态指定为长度
  等于模型中状态数量的向量。

  如果您不知道初始状态，可以按如下方式估计这些
  状态：

  - 要在不知道对应输出水平的情况下仿真模型在给定输入水平附近的行为，
    您可以使用 `idnlarx/findop`
    命令估计平衡状态值。

    例如，要仿真模型 `M`
    在输入为
    `1` 且输出未知的稳态点附近的行为，您可以将初始状态值指定为 `X0`，
    其中：

    ```
    X0 = findop(M,'steady',1,NaN)
    ```
  - 要估计在相同输入下使测量数据与模型仿真响应之间
    拟合最佳的初始状态，请使用 `findstates`
    命令。

    例如，要计算使模型 `M` 的
    响应与数据集 `z` 中的仿真输出数据匹配的初始状态，
    请指定 `X0`，使得：

    ```
    X0 = findstates(M,z)
    ```

## 所属库

System Identification Toolbox / Models

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

在 Simulink 软件中仿真 Hammerstein-Wiener 模型

Hammerstein-Wiener Model 模块使用时域输入数据仿真
Hammerstein-Wiener 模型的输出。该模型是您在
MATLAB® 工作区中事先估计或构建的 `idnlhw` 模型。您将仿真的初始条件指定为以下之一：

- 所有状态为零
- 表示线性模块初始状态的初始状态向量

有关 Hammerstein-Wiener 模型结构的信息，请参阅 What Are Hammerstein-Wiener Models?。
