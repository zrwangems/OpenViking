---
type: simulink-block
title: 'Model Reference Adaptive Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'modelreferenceadaptivecontroller'
documentation_source_path: 'ref/modelreferenceadaptivecontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Model Reference Adaptive Controller

## 端口
```yaml
ports:
- name: r
  summary: 被控对象参考，*r* 标量
  direction: input
  data_types: single | double
- name: y
  summary: 被控对象输出，*y* 标量
  direction: input
  data_types: single | double
- name: Reset
  summary: 积分器复位 标量
  direction: input
  data_types: Boolean
- name: u
  summary: 控制器调整后输出，*u* 标量
  direction: output
  data_types: single | double
```

### 输入

### **r** — 被控对象参考，*r* 标量

被控对象系统参考信号。

**数据类型：** `single` | `double`

### **y** — 被控对象输出，*y* 标量

被控对象系统输出信号。

**数据类型：** `single` | `double`

### **Reset** — 积分器复位 标量

积分器的外部复位信号（上升沿）。

**数据类型：** `Boolean`
### 输出

### **u** — 控制器调整后输出，*u* 标量

调整后的控制信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Proportional gain
  summary: 控制器比例增益，*Kp* 1（默认）| 正标量
  group: 控制器参数
- name: Integral gain
  summary: 控制器积分增益，*Ki* 1（默认）| 正标量
  group: 控制器参数
- name: Derivative gain
  summary: 控制器微分增益，*Kd* 0（默认）
  group: 控制器参数
- name: Anti-windup gain
  summary: 控制器抗积分饱和增益 1（默认）| 正标量
  group: 控制器参数
- name: Use filtered derivative
  summary: 滤波选项 on（默认）| off
  group: 控制器参数
- name: Filter coefficient
  summary: 参考信号滤波系数 100（默认）
  group: 控制器参数
- name: Control action upper limit
  summary: 控制信号上限，*upid_max* 5（默认）
  group: 控制器参数
- name: Control action lower limit
  summary: 控制信号下限，*upid_min* -5（默认）
  group: 控制器参数
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 正标量
  group: 控制器参数
- name: Model parameterization
  summary: 离散或连续模型选项 Discrete-time（默认）| Continuous-time
  group: 参考模型
- name: Discrete-time numerator
  summary: 离散时间传递函数分子 [0.01 -0.0099]（默认）
  group: 参考模型
- name: Discrete-time denominator
  summary: 离散时间传递函数分母 [1 -1.9801 0.9802]（默认）| 向量
  group: 参考模型
- name: Discretization sample time
  summary: 离散化采样时间 0.01（默认）| -1 或正数
  group: 参考模型
- name: Continuous-time numerator
  summary: 连续时间传递函数分子 [1 1]（默认）| 向量
  group: 参考模型
- name: Continuous-time denominator
  summary: 连续时间传递函数分母 [1 2 1]（默认）| 向量
  group: 参考模型
- name: Learning rate
  summary: '*γ* 0.5（默认）'
  group: 调整机制
```

### 控制器参数

### **Proportional gain** — 控制器比例增益，*Kp* `1`（默认）| 正标量

控制器的比例增益 *Kp*。

### **Integral gain** — 控制器积分增益，*Ki* `1`（默认）| 正标量

控制器的积分增益 *Ki*。

### **Derivative gain** — 控制器微分增益，*Kd* `0`（默认）

控制器的微分增益 *Kd*。

### **Anti-windup gain** — 控制器抗积分饱和增益 `1`（默认）| 正标量

控制器的抗积分饱和增益。

### **Use filtered derivative** — 滤波选项 `on`（默认）| off

选择是否对参考信号使用滤波系数。

#### 依赖关系

仅当选中 **Use filtered derivative** 复选框时，**Filter coefficient** 参数才可见。

### **Filter coefficient** — 参考信号滤波系数 `100`（默认）

参考信号的滤波系数。

#### 依赖关系

仅当选中 **Use filtered derivative** 复选框时，此参数才可见。

### **Control action upper limit** — 控制信号上限，*upid\_max* `5`（默认）

控制信号的上界。

### **Control action lower limit** — 控制信号下限，*upid\_min* `-5`（默认）

控制信号的下界。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

#### 依赖关系

如果将 **Sample time (-1 for inherited)** 设置为 `-1`，并且在 **Reference Model** 设置中将 **Model parameterization** 设置为 `Continuous-time`，则 **Discretization sample time** 参数将在 **Reference Model** 设置中变为可见。

### 参考模型

### **Model parameterization** — 离散或连续模型选项 `Discrete-time`（默认）| `Continuous-time`

控制器的数学模型。

#### 依赖关系

选择：

- `Discrete-time` 会使离散时间参数可见。
- `Continuous-time` 会使连续时间参数可见。此外，在 **Controller Parameter** 设置中，如果 **Sample time (-1 for inherited)** 设置为 `-1`，选择此选项会使 **Discretization sample time** 参数在 **Reference Model** 设置中可见。

### **Discrete-time numerator** — 离散时间传递函数分子 `[0.01 -0.0099]`（默认）

离散时间传递函数的分子。

#### 依赖关系

为 **Model parameterization** 选择 `Discrete-time` 会使此参数可见。

### **Discrete-time denominator** — 离散时间传递函数分母 `[1 -1.9801 0.9802]`（默认）| 向量

离散时间传递函数的分母。

#### 依赖关系

为 **Model parameterization** 选择 `Discrete-time` 会使此参数可见。

### **Discretization sample time** — 离散化采样时间 `0.01`（默认）| `-1` 或正数

连续离散化之间的时间，以秒为单位。如果模块采样时间被继承，请显式指定离散化采样时间。

#### 依赖关系

仅当同时满足以下两个条件时，此参数才可见：

- 在 **Control Parameters** 设置中，**Sample time (-1 for inherited)** 设置为 `-1`。
- 在 **Reference Model** 设置中，**Model parameterization** 设置为 `Continuous-time`。

### **Continuous-time numerator** — 连续时间传递函数分子 `[1 1]`（默认）| 向量

连续时间传递函数的分子。

#### 依赖关系

为 **Model parameterization** 选择 `Continuous-time` 会使此参数可见。

### **Continuous-time denominator** — 连续时间传递函数分母 `[1 2 1]`（默认）| 向量

连续时间传递函数的分母。

#### 依赖关系

为 **Model parameterization** 选择 `Continuous-time` 会使此参数可见。

### 调整机制

### **Learning rate** — *γ* `0.5`（默认）

对被控对象变化的调整速率。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

基于离散时间 PID 的模型参考自适应控制

Model Reference Adaptive Controller 模块实现离散时间比例-积分-微分（PID）模型参考自适应控制（MRAC）。MRAC 系统的三个主要组成部分是参考模型、调整机制和控制器。

### 方程

控制方程为

upid(k)=[Kp+KiTszz−1+Kdz−1Tsz]e(k),

其中：

- *upid* 是控制器输出。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Kd* 是微分增益。
- *Ts* 是采样时间。
- *e* 是误差。

参考模型是闭环系统的传递函数。该模型捕获闭环系统的期望行为。它实现为离散时间传递函数

Gm(z)=B(z)A(z).

调整机制根据被控对象输出与参考模型输出之间的误差调整控制作用，如下所示

θ=(y−ym)ym−γTszz−1,

其中：

- *θ* 是自适应参数。
- *y* 是被控对象输出。
- *ym* 是参考模型输出。
- *γ* 是学习率。

增大 *γ* 的值会加快对被控对象变化的适应速度。

调整后的控制信号 *u* 为

u(k)=upid(k)θ(k).
