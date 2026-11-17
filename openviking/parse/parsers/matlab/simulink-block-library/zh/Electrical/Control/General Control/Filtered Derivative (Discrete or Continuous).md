---
type: simulink-block
title: 'Filtered Derivative (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'filteredderivativediscreteorcontinuous'
documentation_source_path: 'ref/filteredderivativediscreteorcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Filtered Derivative (Discrete or Continuous)

## 端口
```yaml
ports:
- name: u
  summary: 微分输入向量
  direction: input
  data_types: single | double
- name: y
  summary: 微分输出向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — 微分输入向量

滤波微分输入信号。该模块使用输入初始值来确定状态初始值。

**数据类型：** `single` | `double`
### 输出

### **y** — 微分输出向量

滤波微分输出信号。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Gain
  summary: 微分增益 1（默认）| 正数
  group: ''
- name: Time constant
  summary: 微分时间常数 0.1（默认）| 正数
  group: ''
- name: Upper saturation limit
  summary: 输出上限 inf（默认）| 实数
  group: ''
- name: Lower saturation limit
  summary: 输出下限 -inf（默认）| 实数
  group: ''
- name: Minimum sample time to time constant ratio
  summary: 离散比值 10（默认）| 实数
  group: ''
- name: Initialization
  summary: 初始状态指定 Inherited from block input（默认）| Specify as parameter
  group: ''
- name: Initial state
  summary: 初始状态 0（默认）| 实数
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 正数
  group: ''
```

### **Gain** — 微分增益 `1`（默认）| 正数

滤波微分增益。

### **Time constant** — 微分时间常数 `0.1`（默认）| 正数

滤波微分时间常数。为获得可接受的精度，请将此值设置为至少比 **Sample time** 大 10 倍。

### **Upper saturation limit** — 输出上限 `inf`（默认）| 实数

滤波微分输出上限。将此值设置为 `inf` 表示无饱和上限。

### **Lower saturation limit** — 输出下限 `-inf`（默认）| 实数

滤波微分输出下限。将此值设置为 `-inf` 表示无饱和下限。

### **Minimum sample time to time constant ratio** — 离散比值 `10`（默认）| 实数

可接受的最小采样时间与时间常数之比。当采样时间接近时间常数时，模块的精度会下降。使用此参数设置该比值的容差。

### **Initialization** — 初始状态指定 `Inherited from block input`（默认）| `Specify as parameter`

指定此模块的初始状态条件。有关详细信息，请参阅初始条件。

### **Initial state** — 初始状态 `0`（默认）| 实数

模块初始状态。

#### 依赖关系

要启用此参数，请将 **Initialization** 设置为 `Specify as parameter`。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请指定 `-1`。对于离散时间操作，请指定正整数。对于连续时间操作，请指定 `0`。

为获得可接受的精度，请将此值设置为至少比 **Time constant** 参数小 10 倍。

如果此模块位于掩码子系统或其他允许连续和离散操作的变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅提升掩码上的模块参数。
## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

离散时间或连续时间滤波微分

Filtered Derivative (Discrete or Continuous) 模块实现符合 IEEE 421.5-2016[1] 的滤波微分。

您可以使用 **Sample time** 参数在微分的连续实现和离散实现之间切换。

### 方程

**连续**

要将滤波微分配置为连续时间，请将 **Sample time** 属性设置为 `0`。此表示形式等效于以下连续传递函数：

G(s)=KsTs+1，

其中：

- *K* 是增益。
- *T* 是时间常数。

根据上述传递函数，定义微分的方程为：

{x˙(t)=1T(Ku(t)−x(t))y(t)=1T(Ku(t)−x(t))   x(0)=u0, y(0)=0，

其中：

- *u* 是模块输入。
- *x* 是状态。
- *y* 是模块输出。
- *t* 是仿真时间。
- *u0* 是模块的初始输入。

**离散**

要将滤波微分配置为离散时间，请将 **Sample time** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。离散表示形式等效于以下传递函数：

(KT)z−1z+Ts/T−1，

其中：

- *K* 是增益。
- *T* 是时间常数。
- *Ts* 是采样时间。

根据离散传递函数，使用前向欧拉法定义微分方程：

{x(n+1)=(1−TsT)x(n)+(TsT)u(n)y(n)=KT(u(n)−x(n))   x(0)=u0, y(0)=0，

其中：

- *u* 是模块输入。
- *x* 是模块状态。
- *y* 是模块输出。
- *n* 是仿真时间步。
- *u0* 是模块的初始输入。

### 初始条件

要指定此模块的初始条件，请将 **Initialization** 设置为：

- `Inherited from block input` — 模块将状态初始条件设置为初始输入，使初始输出为零。
- `Specify as parameter` — 模块将状态初始条件设置为 **Initial state** 的值。

### 限制输出

通过将 **Upper saturation limit** 和 **Lower saturation limit** 参数设置为有限值来限制滤波微分输出。

与 IEEE 421.5-2016 中给出的其他常见模块不同，滤波微分的饱和与抗饱和方法之间没有区别。当输出饱和时，输出可以立即响应输入符号的反转。
