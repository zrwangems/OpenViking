---
type: simulink-block
title: 'Second-Order Low-Pass Filter (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'secondorderlowpassfilterdiscreteorcontinuous'
documentation_source_path: 'ref/secondorderlowpassfilterdiscreteorcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Second-Order Low-Pass Filter (Discrete or Continuous)

## 端口
```yaml
ports:
- name: u
  summary: 滤波器输入标量或向量
  direction: input
  data_types: single | double
- name: y
  summary: 滤波后的输出标量或向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — 滤波器输入标量或向量

滤波器输入。

**数据类型：** `single` | `double`
### 输出

### **y** — 滤波后的输出标量或向量

滤波后的输出。输出的元素数量与输入相同。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Coefficient of s, A1
  summary: '*A1* 系数 0.1（默认）| 正标量'
  group: ''
- name: Coefficient of s^2, A2
  summary: '*A2* 系数 0.2（默认）| 正标量'
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

### **Coefficient of s, A1** — *A1* 系数 `0.1`（默认）| 正标量

*A1*，*s* 的信号调理频率滤波器系数。

### **Coefficient of s^2, A2** — *A2* 系数 `0.2`（默认）| 正标量

*A2*，*s2* 的信号调理频率滤波器系数。

### **Initialization** — 初始状态指定 `Inherited from block input`（默认）| `Specify as parameter`

指定此模块的初始状态条件。有关详细信息，请参阅初始条件。

### **Initial state** — 初始状态 `0`（默认）| 实数

模块初始状态。

#### 依赖关系

要启用此参数，请将 **Initialization** 设置为 `Specify as parameter`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数设置为 `-1`。对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅提升掩码上的模块参数。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

离散时间或连续时间二阶低通滤波器

Second-Order Low-Pass Filter (Discrete or Continuous) 模块实现符合 IEEE Std 421.5-2016[1] 的二阶低通滤波器。在该标准中，该滤波器是用于 Power System Stabilizer PSS1A 的单输入、单输出信号调理器。

在 PSS1A 中，该滤波器考虑了高频扭转滤波器的一些低频效应。它还可以帮助塑造稳定器的增益和相位特性。

要在 Second-Order Low-Pass Filter (Discrete or Continuous) 模块的连续实现和离散实现之间切换，请调整 **Sample time** 参数值。

### 初始条件

要指定此模块的初始条件，请将 **Initialization** 设置为：

- `Inherited from block input` — 模块将状态和输出初始条件设置为初始输入。
- `Specify as parameter` — 模块将状态初始条件设置为 **Initial state** 的值。
