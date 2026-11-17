---
type: simulink-block
title: 'Washout (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'washoutdiscreteorcontinuous'
documentation_source_path: 'ref/washoutdiscreteorcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Washout (Discrete or Continuous)

## 端口
```yaml
ports:
- name: u
  summary: Washout 输入向量
  direction: input
  data_types: single | double
- name: y
  summary: Washout 输出向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — Washout 输入向量

Washout 输入信号。该模块使用输入初始值来确定状态初始值。

**数据类型：** `single` | `double`
### 输出

### **y** — Washout 输出向量

Washout 输出信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Time constant
  summary: Washout 时间常数 0.1（默认）| 正数
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

### **Time constant** — Washout 时间常数 `0.1`（默认）| 正数

Washout 时间常数。将此值设置为小于 **Sample time** 以绕过滤波器动态。

### **Initialization** — 初始状态指定 `Inherited from block input`（默认）| `Specify as parameter`

指定此模块的初始状态条件。有关详细信息，请参阅初始条件。

### **Initial state** — 初始状态 `0`（默认）| 实数

模块初始状态。

#### 依赖关系

要启用此参数，请将 **Initialization** 设置为 `Specify as parameter`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续和离散实现之间正确切换。有关详细信息，请参阅提升掩码上的模块参数。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

离散时间或连续时间 Washout 或高通滤波器

Washout (Discrete or Continuous) 模块实现符合 IEEE 421.5-2016[1] 的 washout 滤波器。Washout 也称为高通滤波器。

您可以使用 **Sample time** 参数在积分器的连续和离散实现之间切换。

### 方程

**连续**

要将 Washout (Discrete or Continuous) 模块配置为连续时间，请将 **Sample time** 属性设置为 `0`。此表示等效于以下连续传递函数：

G(s)=TsTs+1，

其中 *T* 是时间常数。根据上述传递函数，washout 定义方程为：

{x˙(t)=1T(−x(t)+u(t))y(t)=−x(t)+u(t)  x(0)=u0, y(0)=0，

其中：

- *u* 是 washout 输入。
- *x* 是 washout 状态。
- *y* 是 washout 输出。
- *t* 是仿真时间。
- *u0* 是模块的初始输入。

**离散**

要将 Washout (Discrete or Continuous) 配置为离散时间，请将 **Sample time** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。离散表示等效于以下传递函数：

G(z)=z−1z+Ts/T−1，

其中 *Ts* 是采样时间。根据离散传递函数，washout 定义方程使用前向欧拉方法定义：

{x(n+1)=(1−TsT)x(n)+(TsT)u(n)y(n)=u(n)−x(n)  x(0)=u0, y(0)=0，

其中：

- *u* 是 washout 输入。
- *x* 是 washout 状态。
- *y* 是 washout 输出。
- *n* 是仿真时间步。
- *u0* 是模块的初始输入。

### 初始条件

要指定此模块的初始条件，请将 **Initialization** 设置为：

- `Inherited from block input` — 模块将状态和输出初始条件设置为初始输入。
- `Specify as parameter` — 模块将状态初始条件设置为 **Initial state** 的值。

### 绕过滤波器动态

将时间常数设置为小于或等于采样时间的值，以忽略滤波器的动态。绕过时，模块将输入直接馈送到输出：

T≤Ts→y=u 。

在连续情况下，采样时间和时间常数必须均为零。
