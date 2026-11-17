---
type: simulink-block
title: 'Luenberger Observer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Observers'
documentation_page: 'luenbergerobserver'
documentation_source_path: 'ref/luenbergerobserver.html'
language: zh-CN
chinese_source: worker-translation
---

# Luenberger Observer

## 端口
```yaml
ports:
- name: u
  summary: 控制输入向量
  direction: input
  data_types: single | double
- name: y
  summary: 系统输出向量
  direction: input
  data_types: single | double
- name: xhat
  summary: 状态估计向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — 控制输入向量

待估计状态系统的输入信号，指定为向量。

**数据类型：** `single` | `double`

### **y** — 系统输出向量

待估计状态系统的测量输出，指定为向量。

**数据类型：** `single` | `double`
### 输出

### **xhat** — 状态估计向量

系统状态的估计值，指定为向量。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: State-space parameterization
  summary: 状态空间参数化 Discrete-time（默认）| Continuous-time
  group: ''
- name: Discrete A matrix
  summary: 离散时间 A 矩阵 1（默认）| 实数标量或矩阵
  group: ''
- name: Discrete B matrix
  summary: 离散时间 B 矩阵 1（默认）| 实数标量或矩阵
  group: ''
- name: Discrete C matrix
  summary: 离散时间 C 矩阵 1（默认）| 实数标量或矩阵
  group: ''
- name: Discrete D matrix
  summary: 离散时间 D 矩阵 1（默认）| 实数标量或矩阵
  group: ''
- name: Continuous A matrix
  summary: 连续时间 A 矩阵 1（默认）| 实数标量或矩阵
  group: ''
- name: Continuous B matrix
  summary: 连续时间 B 矩阵 1（默认）| 实数标量或矩阵
  group: ''
- name: Continuous C matrix
  summary: 连续时间 C 矩阵 1（默认）| 实数标量或矩阵
  group: ''
- name: Continuous D matrix
  summary: 连续时间 D 矩阵 1（默认）| 实数标量或矩阵
  group: ''
- name: Observer design
  summary: 状态空间参数化 Desired eigenvalues（默认）| Observer gain
  group: ''
- name: Observer gain
  summary: 观测器增益 1（默认）| 实数标量或矩阵
  group: ''
- name: Desired eigenvalues
  summary: 观测器特征值 0（默认）| 实数向量
  group: ''
- name: Initial conditions
  summary: 初始条件 0（默认）| 长度等于系统阶数的实数向量
  group: ''
- name: Discretization sample time
  summary: 离散化采样时间 0.1（默认）| 正实数
  group: ''
- name: Sample time
  summary: 采样时间 0.1（默认）| -1 或正实数
  group: ''
```

### **State-space parameterization** — 状态空间参数化 `Discrete-time`（默认）| `Continuous-time`

选择用于参数化观测器状态空间矩阵和期望极点的策略。无论采用何种参数化方式，模块的实现均为离散形式。

### **Discrete A matrix** — 离散时间 A 矩阵 1（默认）| 实数标量或矩阵

离散时间状态空间模型的状态矩阵。A 矩阵必须为方阵，其行数和列数等于系统的阶数。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Discrete-time`。

### **Discrete B matrix** — 离散时间 B 矩阵 1（默认）| 实数标量或矩阵

离散时间状态空间模型的输入矩阵。B 矩阵的行数必须等于系统的阶数，列数必须等于系统输入的数量。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Discrete-time`。

### **Discrete C matrix** — 离散时间 C 矩阵 1（默认）| 实数标量或矩阵

离散时间状态空间模型的输出矩阵。C 矩阵的行数必须等于系统输出的数量，列数必须等于系统的阶数。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Discrete-time`。

### **Discrete D matrix** — 离散时间 D 矩阵 1（默认）| 实数标量或矩阵

离散时间状态空间模型的直通矩阵。D 矩阵的行数必须等于系统输出的数量，列数必须等于系统输入的数量。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Discrete-time`。

### **Continuous A matrix** — 连续时间 A 矩阵 1（默认）| 实数标量或矩阵

连续时间状态空间模型的状态矩阵。A 矩阵必须为方阵，其行数和列数等于系统的阶数。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Continuous-time`。

### **Continuous B matrix** — 连续时间 B 矩阵 1（默认）| 实数标量或矩阵

连续时间状态空间模型的输入矩阵。B 矩阵的行数必须等于系统的阶数，列数必须等于系统输入的数量。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Continuous-time`。

### **Continuous C matrix** — 连续时间 C 矩阵 1（默认）| 实数标量或矩阵

连续时间状态空间模型的输出矩阵。C 矩阵的行数必须等于系统输出的数量，列数必须等于系统的阶数。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Continuous-time`。

### **Continuous D matrix** — 连续时间 D 矩阵 1（默认）| 实数标量或矩阵

连续时间状态空间模型的直通矩阵。D 矩阵的行数必须等于系统输出的数量，列数必须等于系统输入的数量。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Continuous-time`。

### **Observer design** — 状态空间参数化 `Desired eigenvalues`（默认）| `Observer gain`

选择用于参数化观测器增益的策略。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Discrete-time`。

### **Observer gain** — 观测器增益 1（默认）| 实数标量或矩阵

指定使矩阵 *Ad-LdCd* 的所有特征值均位于单位圆内的观测器增益。增益矩阵的行数必须等于系统输入的数量，列数必须等于系统的阶数。

#### 依赖关系

要启用此参数，请设置：

- **State-space parameterization** 为 `Discrete-time`。
- **Observer design** 为 `Observer gain`。

### **Desired eigenvalues** — 观测器特征值 0（默认）| 实数向量

指定特征值的位置：

- 如果 **State-space parameterization** 设置为 `Continuous-time`，则使其具有负实部。在这种情况下，连续时间系统的特征值将基于 **Discretization sample time** 近似为离散特征值。
- 如果 **State-space parameterization** 设置为 `Discrete-time`，则使其位于单位圆内。

然后根据这些特征值计算观测器增益。向量的大小应与系统阶数相同。

### **Initial conditions** — 初始条件 0（默认）| 长度等于系统阶数的实数向量

选择每个状态的初始条件。

### **Discretization sample time** — 离散化采样时间 0.1（默认）| 正实数

用于离散化状态空间矩阵以及近似离散时间特征值的值。

#### 依赖关系

要启用此参数，请将 **State-space parameterization** 设置为 `Continuous-time`。

### **Sample time** — 采样时间 0.1（默认）| -1 或正实数

用于仿真模型动态特性的值。请选择与 **Discretization sample time** 相同的值，除非该模块位于触发子系统内，此时必须将其设置为 -1。
## 所属库

Simscape / Electrical / Control / Observers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

离散时间 Luenberger 观测器

Luenberger Observer 模块实现了一个离散时间 Luenberger 观测器。使用此模块可通过以下方式估计可观测系统的状态：

- 系统的离散输入和输出。
- 系统的离散状态空间表示。

Luenberger 观测器有时也称为状态观测器或简称为观测器。

您可以通过将此模块的输出状态向量传递给 State Feedback Controller 模块来控制多输入、多输出系统。

### 定义方程

该模块使用后向欧拉法实现离散时间 Luenberger 观测器，因为该方法简单且稳定。

估计器由以下差分方程给出：

x^(k+1) =Adx^(k) +Bdu(k) + Ld(y(k) −y^(k)),

其中：

- x^(k) 是第 *k* 个估计状态向量。
- y^(k) 是第 *k* 个估计输出向量。
- *u(k)* 是第 *k* 个输入向量。
- *y(k)* 是第 *k* 个测量输出向量。
- *Ad* 是离散化状态矩阵。
- *Bd* 是离散化输入矩阵。
- *Ld* 是离散化观测器增益矩阵。

估计误差的动态特性由下式描述：

e(k+1)=(Ad−LdCd)e(k),

其中：

- *e(k)* 是第 *k* 个误差向量。
- *Cd* 是输出矩阵。

当 *Ad-LdCd* 的特征值位于单位圆内时，估计误差收敛到零。因此，*Ld* 的值应使得该目标得以实现。该模块通过求解下式计算观测器增益

LdT=GX−1,

其中 *G* 是任意矩阵，*X* 通过求解 Sylvester 方程获得：

AdTX−XΛ=CdTG.

此处，*Λ* 是包含期望特征值的矩阵，这些特征值与 *Ad* 的特征值不同。此图展示了离散时间 Luenberger 观测器的基本结构。

### 假设

系统是可观测的，即如果系统的状态可以在有限时间内由输入和输出确定，则系统可观测。在数学上，这意味着系统的可观测性矩阵具有满秩。

### 限制

期望特征值与开环模型的特征值不同。
