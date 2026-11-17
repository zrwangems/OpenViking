---
type: simulink-block
title: 'State-Feedback Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'statefeedbackcontroller'
documentation_source_path: 'ref/statefeedbackcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# State-Feedback Controller

## 端口
```yaml
ports:
- name: r
  summary: 被控对象参考 scalar
  direction: input
  data_types: single | double
- name: x
  summary: 状态向量 vector
  direction: input
  data_types: single | double
- name: Reset
  summary: 积分器复位 scalar
  direction: input
  data_types: Boolean
- name: y
  summary: 被控对象输出 scalar
  direction: input
  data_types: single | double
- name: u
  summary: 控制器输出 scalar
  direction: output
  data_types: single | double
```

### 输入

### **r** — 被控对象参考 scalar

被控对象系统参考信号。

**数据类型：** `single` | `double`

### **x** — 状态向量 vector

测量或估计的系统状态向量。

**数据类型：** `single` | `double`

### **Reset** — 积分器复位 scalar

积分器的外部复位信号（上升沿）。

**数据类型：** `Boolean`

### **y** — 被控对象输出 scalar

被控对象系统输出信号。

**数据类型：** `single` | `double`
### 输出

### **u** — 控制器输出 scalar

控制系统输出信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: State-feedback design
  summary: 控制器生成 State-feedback gain（默认）| Desired eigenvalues
  group: ''
- name: State-feedback parameterization
  summary: 状态反馈参数化 Discrete-time（默认）| Continuous-time
  group: ''
- name: Controller matrix
  summary: 控制器矩阵 [1 1]（默认）| matrix
  group: ''
- name: Discrete-time A matrix
  summary: 离散时间 A 矩阵 1（默认）| real scalar or matrix
  group: ''
- name: Discrete-time B matrix
  summary: 离散时间 B 矩阵 1（默认）| real scalar or matrix
  group: ''
- name: Discrete-time C matrix
  summary: 离散时间 C 矩阵 1（默认）| real scalar or matrix
  group: ''
- name: Discrete-time D matrix
  summary: 离散时间 D 矩阵 1（默认）| real scalar or matrix
  group: ''
- name: Continuous-time A matrix
  summary: 连续时间 A 矩阵 1（默认）| real scalar or matrix
  group: ''
- name: Continuous-time B matrix
  summary: 连续时间 B 矩阵 1（默认）| real scalar or matrix
  group: ''
- name: Continuous-time C matrix
  summary: 连续时间 C 矩阵 1（默认）| real scalar or matrix
  group: ''
- name: Continuous-time D matrix
  summary: 连续时间 D 矩阵 1（默认）| real scalar or matrix
  group: ''
- name: Discretization sample time
  summary: 离散化采样时间 0.1（默认）| positive real number
  group: ''
- name: Desired eigenvalues (discrete)
  summary: 观测器特征值 0（默认）| real vector
  group: ''
- name: Control action upper limit
  summary: '*umax* 5（默认）| scalar greater than the value of the Control action lower limit parameter'
  group: ''
- name: Control action lower limit
  summary: '*umin* 0（默认）| scalar'
  group: ''
- name: Sample time (-1 for inherited)
  summary: 采样间隔 -1（默认）| default value or a positive number
  group: ''
```

### **State-feedback design** — 控制器生成 `State-feedback gain`（默认）| `Desired eigenvalues`

选择用于参数化控制器增益的策略：

- `State-feedback gain` — 直接指定控制器增益
- `Desired eigenvalues` — 指定被控对象模型和期望特征值，据此生成控制器增益

### **State-feedback parameterization** — 状态反馈参数化 `Discrete-time`（默认）| `Continuous-time`

选择用于参数化状态空间矩阵和控制器期望极点的策略。无论采用何种参数化方式，模块实现均为离散形式。

#### 依赖关系

要启用此参数，请将 **State-feedback design** 设置为 `Desired eigenvalues`。

### **Controller matrix** — 控制器矩阵 [1 1]（默认）| matrix

控制器反馈矩阵。若要确定控制器矩阵，如果您拥有 Control System Toolbox™ 许可证，请使用 `lqr` 或 `lqi` 函数。

#### 依赖关系

要启用此参数，请将 **State-feedback design** 设置为 `State-feedback gain`。

### **Discrete-time A matrix** — 离散时间 A 矩阵 1（默认）| real scalar or matrix

离散时间状态空间模型的状态矩阵。A 矩阵必须为方阵，其行数和列数等于系统的阶数。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Discrete-time`。

### **Discrete-time B matrix** — 离散时间 B 矩阵 1（默认）| real scalar or matrix

离散时间状态空间模型的输入矩阵。B 矩阵的行数必须等于系统的阶数，列数必须等于系统输入的数量。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Discrete-time`。

### **Discrete-time C matrix** — 离散时间 C 矩阵 1（默认）| real scalar or matrix

离散时间状态空间模型的输出矩阵。C 矩阵的行数必须等于系统输出的数量，列数必须等于系统的阶数。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Discrete-time`。

### **Discrete-time D matrix** — 离散时间 D 矩阵 1（默认）| real scalar or matrix

离散时间状态空间模型的直通矩阵。D 矩阵的行数必须等于系统输出的数量，列数必须等于系统输入的数量。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Discrete-time`。

### **Continuous-time A matrix** — 连续时间 A 矩阵 1（默认）| real scalar or matrix

连续时间状态空间模型的状态矩阵。A 矩阵必须为方阵，其行数和列数等于系统的阶数。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Continuous-time`。

### **Continuous-time B matrix** — 连续时间 B 矩阵 1（默认）| real scalar or matrix

连续时间状态空间模型的输入矩阵。B 矩阵的行数必须等于系统的阶数，列数必须等于系统输入的数量。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Continuous-time`。

### **Continuous-time C matrix** — 连续时间 C 矩阵 1（默认）| real scalar or matrix

连续时间状态空间模型的输出矩阵。C 矩阵的行数必须等于系统输出的数量，列数必须等于系统的阶数。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Continuous-time`。

### **Continuous-time D matrix** — 连续时间 D 矩阵 1（默认）| real scalar or matrix

连续时间状态空间模型的直通矩阵。D 矩阵的行数必须等于系统输出的数量，列数必须等于系统输入的数量。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Continuous-time`。

### **Discretization sample time** — 离散化采样时间 0.1（默认）| positive real number

用于离散化状态空间矩阵并近似离散时间特征值的值。

#### 依赖关系

要启用此参数，请将 **State-feedback parameterization** 设置为 `Continuous-time`，并将 **Sample time (-1 for inherited)** 设置为 `-1`。

### **Desired eigenvalues (discrete)** — 观测器特征值 0（默认）| real vector

指定位于单位圆内的特征值位置。然后根据这些特征值计算控制器增益。向量的大小必须等于系统阶数加上输出的数量。

### **Control action upper limit** — *umax* `5`（默认）| scalar greater than the value of the **Control action lower limit** parameter

控制输出信号的上限。

### **Control action lower limit** — *umin* `0`（默认）| scalar

控制输出信号的下限。

### **Sample time (-1 for inherited)** — 采样间隔 `-1`（默认）| default value or a positive number

采样之间的时间间隔。如果该模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果该模块位于连续变步长模型中，请显式指定采样时间。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

带积分作用的离散时间状态反馈控制器

State-Feedback Controller 模块实现带积分作用的离散时间状态反馈控制器。使用此模块可控制单输入单输出或多输入多输出的线性系统。积分作用用于消除受控输出中的稳态误差。您可以使用预先计算的最优增益来定义控制器，也可以使用系统的状态空间模型通过极点配置来生成该增益。

### 方程

跟踪误差的积分 *xi* 是一个附加状态，可确保闭环系统的稳态误差为零。扩展状态向量为

xe=[xxi],

其中：

- *x* 是状态向量。
- *xi* 是跟踪误差的积分。
- *xe* 是扩展状态向量。

因此，控制作用为

u=Kxe,

其中：

- *K* 是反馈矩阵，即极点配置。
- *u* 是控制器输出。

### 假设

系统状态测量和估计在控制器外部进行。
