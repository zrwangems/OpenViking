---
type: simulink-block
title: 'Integrator with Wrapped State (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'integratorwithwrappedstatediscreteorcontinuous'
documentation_source_path: 'ref/integratorwithwrappedstatediscreteorcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Integrator with Wrapped State (Discrete or Continuous)

## 端口

### 输入

### **u** — 积分器输入向量

积分器输入。

**数据类型：** `single` | `double`
### 输出

### **y** — 积分器输出向量

积分器输出。

**数据类型：** `single` | `double`

## 参数

### **Wrapped state upper limit** — 状态上限 `2*pi`（默认）| 实数

积分器上限。

### **Wrapped state lower limit** — 状态下限 `0`（默认）| 实数

积分器下限。

### **Initial condition** — 状态初始值 `0`（默认）| 实数

积分器初始状态。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

模块连续执行之间的时间。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

对于继承的离散时间操作，将此参数设置为 `-1`。对于离散时间操作，将此参数设置为正整数。对于连续时间操作，将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅“提升掩码上的模块参数”。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

具有回绕状态的离散时间或连续时间积分器

Integrator with Wrapped State (Discrete or Continuous) 模块实现符合 IEEE 421.5-2016[1] 的回绕状态积分器。

使用此模块生成周期性信号（例如角度）或表示压控振荡器。可以使用 **Sample time** 参数在积分器的连续实现和离散实现之间切换。

### 方程

**连续**

要将积分器配置为连续时间，请将 **Sample time** 属性设置为 `0`。此表示等效于连续传递函数：

G(s)=1s.

根据上述传递函数，积分器定义方程为：

{x˙(t)=u(t)y(t)=x(t)  x(0)=x0,

其中：

- *u* 是积分器输入。
- *x* 是积分器状态。
- *y* 是积分器输出。
- *t* 是仿真时间。
- *x0* 是积分器的初始状态。

**离散**

要将积分器配置为离散时间，请将 **Sample time** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。离散表示等效于传递函数：

G(z)=Tsz−1,

其中 *Ts* 是采样时间。根据离散传递函数，使用前向欧拉法定义积分器方程：

{x(n+1)=x(n)+Tsu(n)y(n)=x(n)  x(0)=x0,

其中：

- *u* 是积分器输入。
- *x* 是积分器状态。
- *y* 是积分器输出。
- *n* 是仿真时间步。
- *x0* 是积分器的初始状态。

### 定义初始条件

可以使用 **Initial condition** 参数定义状态初始条件。

### 回绕循环状态

积分器在指定的下限值和上限值之间回绕其状态。此图显示了恒定输入下回绕状态积分器和非回绕状态积分器的输出。

在图中，下限和上限分别为 *0* 和 *2π*。
