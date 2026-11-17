---
type: simulink-block
title: 'Current Limiter'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'currentlimiter'
documentation_source_path: 'ref/currentlimiter.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Limiter

## 端口

### 输入

### **Lim** — 可变电流限值，物理信号

*自 R2024a 起*

输入物理信号，用于定义电流限值，单位为 amps。

#### 依赖关系

要启用此端口，请将 **Limiter type** 设置为
`Variable limit`。
### 守恒

### **+** — 正极端子 电气

与正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

与负极端子关联的电气守恒端口。

### **H** — 热端口 热

与热质量关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port` (默认) | `Show thermal port`

是否启用模块的热端口并建模热参数。

### 参数

### **Limiter type** — 限制器类型 `Constant symmetric limits` (默认) | `Constant asymmetric limits` | `Variable limit`

*自 R2024a 起*

限制器类型。请选择以下选项之一：

- `Constant symmetric limits` —
  为电流限值设置恒定幅值。
- `Constant asymmetric limits` —
  为正向电流设置一个限值，为负向电流设置一个限值。
- `Variable limit` — 使用输入物理
  信号指定电流限值的幅值。使用此选项可定义随时间
  变化的电流限值。

### **Current limit** — 正向电流限值 `1` `A` (默认) | 正标量

正向电流方向上的电流限值。

如果将 **Limiter type** 设置为
`Constant asymmetric limits`，则该模块
假定负向电流的电流限值等于正向电流的限值。

#### 依赖关系

要启用此参数，请将 **Limiter type** 设置为
`Constant symmetric limits` 或
`Constant asymmetric limits`。

### **Reverse direction current limit** — 反向电流限值 `1` `A` (默认) | 正标量

*自 R2024a 起*

反向电流方向上的电流限值。

#### 依赖关系

要启用此参数，请将 **Limiter type** 设置为
`Constant asymmetric limits`。

### **Voltage drop when current starts to limit** — 电流开始限制时的电压降 `0.1` `V` (默认) | 正标量

当电流限制生效时，组件两端的近似电压降。当电压降等于此值时，模块
将电流限制为电流限值的 0.9993 倍。

### **Limit-state conductance** — 限制状态电导 `1e-3` `1/Ohm` (默认) | 正标量

大电流幅值下电流相对于电压降的变化率。

### 热端口

### **Thermal mass** — 热质量 `100` `J/K` (默认) | 正标量

使温度升高 1 K 所需的热能。

#### 依赖关系

要启用此参数，请将 **Modeling option**
设置为 `Show thermal port`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

### R2024a：**Initial Temperature** 参数已替换为 **Temperature** 变量

**Initial temperature** 参数已替换为模块对话框或属性检查器中 **初始目标** 部分内的 **Temperature** 变量。

如果较早版本中创建的模型包含此模块，软件会自动将 **初始目标** 部分中 **Temperature** 变量的值设置为 **Initial temperature** 参数指定的值。

### R2024a：指定恒定非对称和可变对称电流限值

现在可以指定正向和反向电流方向上的不同电流限值。要启用此选项，请将 **Limiter type** 参数设置为 `Constant asymmetric limits`。

还可以使用输入物理信号将电流限值的幅值定义为时间的函数。要启用此选项，请将 **Limiter type** 参数设置为 `Variable limit`。

## 描述

电流限制器的行为模型

Current Limiter 模块提供电流限制器的行为模型。使用此模块可对电源和电机驱动器中的电流限制，或对限制浪涌电流的组件进行建模。

该模块使用双曲正切函数限制电流，

i=iLIMtanh(4vvLIM)+gLIMv,

其中：

- *i* 是流过组件的电流。
- *v* 是组件两端的电压降。
- *i*LIM 是电流限值。
- *v*LIM 是当电流限制生效时组件两端的近似电压降。
- *g*LIM 是大电流幅值下电流相对于电压降的变化率。该变量也称为 *limit-state conductance*。

*g*LIM*v* 项表示在任意高电压下无法将电流限制为固定值的情况。该项还可改善仿真期间的数值特性。

选择 *g*LIM 的值，使得当 *v* 等于预期最大电压降时，*g*LIM*v* 相对于 *i*LIM 较小。

该图显示了 Current Limiter 模块的典型 *i*-*v* 特性。当 *i* 低于 *i*LIM 时，器件表现为电阻。电导近似等于 4*v*LIM/*v*LIM。当 *i* 接近 *i*LIM 时，电流随电压的变化率迅速降至限制状态电导 *g*LIM。

显示典型 I-V 特性的图

要为 *v*LIM 选择合适的值，请将 *i*-*v* 特性与数据手册中的图进行比较。较小的值会在低电流下产生更陡的梯度，但求解器需要严格的容差和较小的步长。

当 *v* = *v*LIM 时，

i=iLIMtanh(4)+gLIMvLIM=0.9993iLIM+gLIMvLIM.

因此，流过组件的电流近似等于电流限值。

Current Limiter 模块会限制正向和负向电流。要仅在一个方向上限制电流为 *i*LIM，请将 Current Limiter 模块连接到 Diode 模块。要防止反向偏置方向出现任何电流限制，请将这两个模块串联。要阻断反向偏置方向上的任何电流，请将这两个模块并联。

要对正向和负向电流使用相同的电流限值 *i*LIM，请将 **Limiter type** 参数设置为 `Constant symmetric limits`。**Current limit** 参数定义电流限值的幅值。

要对正向和负向电流使用不同的电流限值，请将 **Limiter type** 参数设置为 `Constant asymmetric limits`。**Current limit** 参数定义正向电流的电流限值，**Reverse direction current limit** 参数定义负向电流的限值。

要使用随时间变化的电流限值，请将 **Limiter type** 参数设置为 `Variable limit`。**Lim** 端口的输入物理信号定义电流限值的幅值。

### 热端口

此模块有一个可选热端口。要控制热端口的可见性，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

热端口模型包含一个热质量。电流限制器耗散的功率加上流入热端口的热流驱动热质量微分方程，

mdTdt=Ploss+QH,

其中：

- *m* 是热质量。
- *T* 是热端口温度。
- *P*loss 是电气损耗，*v*·*i*。
- *Q*H 是从外部网络流入热端口的热流。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅《设置模块变量的优先级和初始目标》。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。可以使用不同来源指定标称值，包括模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅《通过标称值进行系统缩放》。
