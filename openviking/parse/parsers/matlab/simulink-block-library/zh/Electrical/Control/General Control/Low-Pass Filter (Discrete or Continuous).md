---
type: simulink-block
title: 'Low-Pass Filter (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'lowpassfilterdiscreteorcontinuous'
documentation_source_path: 'ref/lowpassfilterdiscreteorcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Low-Pass Filter (Discrete or Continuous)

## 端口
```yaml
ports:
- name: u
  summary: 滤波器输入向量
  direction: input
  data_types: single | double
- name: y
  summary: 滤波器输出向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — 滤波器输入向量

低通滤波器输入信号。该模块使用输入初始值来确定状态初始值。

**数据类型：** `single` | `double`
### 输出

### **y** — 滤波器输出向量

低通滤波器输出。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Gain
  summary: 滤波器增益 1（默认）| 正数
  group: ''
- name: Time constant
  summary: 滤波器时间常数 1（默认）| 正数
  group: ''
- name: Upper saturation limit
  summary: 状态上限 inf（默认）| 实数
  group: ''
- name: Lower saturation limit
  summary: 状态下限 -inf（默认）| 实数
  group: ''
- name: Initialization
  summary: 初始状态指定 Inherited from block input（默认）| Specify as parameter
  group: ''
- name: Initial state
  summary: 初始状态 0（默认）| 实数
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: ''
```

### **Gain** — 滤波器增益 `1`（默认）| 正数

低通滤波器增益。

### **Time constant** — 滤波器时间常数 `1`（默认）| 正数

低通滤波器时间常数。在离散实现中，将此值设置为小于 **Sample time**，以绕过滤波器的动态特性。

### **Upper saturation limit** — 状态上限 `inf`（默认）| 实数

低通滤波器状态上限。将其设置为 `inf` 表示无饱和上限，或设置为有限值以防止滤波器积分器的上卷绕。

### **Lower saturation limit** — 状态下限 `-inf`（默认）| 实数

低通滤波器状态下限。将其设置为 `-inf` 表示无饱和下限，或设置为有限值以防止滤波器积分器的下卷绕。

### **Initialization** — 初始状态指定 `Inherited from block input`（默认）| `Specify as parameter`

指定此模块的初始状态条件。有关详细信息，请参阅初始条件。

### **Initial state** — 初始状态 `0`（默认）| 实数

模块初始状态。

#### 依赖关系

要启用此参数，请将 **Initialization** 设置为 `Specify as parameter`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅什么是采样时间和指定采样时间。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅提升掩码上的模块参数。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

离散时间或连续时间低通滤波器

Low-Pass Filter (Discrete or Continuous) 模块按照 IEEE 421.5-2016[1] 实现低通滤波器。在该标准中，该滤波器被称为 Simple Time Constant。

您可以使用 **Sample time** 参数在积分器的连续实现和离散实现之间切换。

### 方程

**连续**

要将滤波器配置为连续时间，请将 **Sample time** 属性设置为 `0`。此表示形式等效于以下连续传递函数：

G(s)=KTs+1，

其中：

- *K* 是滤波器增益。
- *T* 是滤波器时间常数。

根据上述传递函数，滤波器定义方程为：

{x˙(t)=1T(Ku(t)−x(t))y(t)=x(t)   y(0)=x(0)=Ku0，

其中：

- *u* 是滤波器输入。
- *x* 是滤波器状态。
- *y* 是滤波器输出。
- *t* 是仿真时间。
- *u0* 是模块的初始输入。

**离散**

要将滤波器配置为离散时间，请将 **Sample time** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。离散表示形式等效于以下传递函数：

G(z)=K(Ts/T)z−11+(Ts/T−1)z−1，

其中：

- *K* 是滤波器增益。
- *T* 是滤波器时间常数。
- *Ts* 是滤波器采样时间。

根据离散传递函数，滤波器方程使用前向欧拉方法定义：

{x(n+1)=(1−TsT)x(n)+K(TsT)u(n)y(n)=x(n)   y(0)=x(0)=Ku0，

其中：

- *u* 是滤波器输入。
- *x* 是滤波器状态。
- *y* 是滤波器输出。
- *n* 是仿真时间步。
- *u0* 是模块的初始输入。

### 初始条件

要指定此模块的初始条件，请将 **Initialization** 设置为：

- `Inherited from block input` — 模块将状态和输出初始条件设置为初始输入。
- `Specify as parameter` — 模块将状态初始条件设置为 **Initial state** 的值。

### 限制积分

设置 **Upper saturation limit** 和 **Lower saturation limit** 参数以使用抗卷绕饱和方法。

抗卷绕方法将积分器状态限制在下饱和限 *A* 和上饱和限 *B* 之间：

A<=x<=B .

由于状态受到限制，当积分饱和时，输出可以立即响应输入符号的反转。此框图描述了滤波器中抗卷绕饱和方法的实现。

此模块不提供卷绕饱和方法。要使用卷绕饱和方法，请将 **Upper saturation limit** 参数设置为 `inf`，将 **Lower saturation limit** 参数设置为 `-inf`，并在输出端附加一个饱和模块。

### 绕过滤波器动态特性

将时间常数设置为小于或等于采样时间的值，以忽略滤波器的动态特性。绕过时，模块将增益缩放后的输入直接馈送到输出：

T≤Ts→y=Ku

在连续情况下，采样时间和时间常数都必须为零。
