---
type: simulink-block
title: 'Interface (2P-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces'
documentation_page: 'interface2pma'
documentation_source_path: 'ref/interface2pma.html'
language: zh-CN
chinese_source: worker-translation
---

# Interface (2P-MA)

## 端口

### 输入

### **W** — 湿度，无量纲物理信号

与界面处湿度含量关联的物理信号端口。

#### 依赖关系

要启用此端口，请选择 **Provide input signal for
interface humidity** 并将 **Interface
humidity specification** 设置为 `Relative
humidity`、`Specific
humidity`、`Mole
fraction` 或 `Humidity
ratio`。

### **Tw** — 温度，K 物理信号

与界面处湿球温度关联的物理信号端口，单位为
K。

#### 依赖关系

要启用此端口，请选择 **Provide input signal for interface
humidity** 并将 **Interface humidity
specification** 设置为 `Wet-bulb
temperature`。

### **TG** — 示踪气体，无量纲物理信号

与界面处示踪气体关联的物理信号端口。

#### 依赖关系

要启用此端口，请选择 **Provide input signal for interface trace
gas**。

### **D** — 水滴质量比，无量纲物理信号

与界面处水滴与湿空气的质量比关联的物理信号端口。

#### 依赖关系

要启用此端口，请选择 **Provide input signal for
interface water droplets**。
### 守恒

### **2P** — 两相端口 两相流体

与界面处两相流体关联的两相流体守恒端口。

### **MA** — 湿空气端口 湿空气

与界面处湿空气关联的湿空气守恒端口。

## 参数

### **Provide input signal for interface humidity** — 界面湿度控制选项 `off`（默认）| `on`

用于指定界面湿度的选项。如果选中此复选框，模块将启用端口 **W**。如果清除此复选框，则可以指定恒定湿度条件。

### **Interface humidity specification** — 湿度参数化选项 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、摩尔分数、湿度比或湿球温度来计算湿度。

### **Interface relative humidity** — 界面处相对湿度 `0.5`（默认）| 正标量

界面处的相对湿度。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface
humidity** 复选框并将 **Interface humidity
specification** 设置为 `Relative
humidity`。

### **Interface specific humidity** — 界面处比湿度 `0.01`（默认）| 正标量

界面处的比湿度。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface
humidity** 复选框并将 **Interface humidity
specification** 设置为 `Specific
humidity`。

### **Interface water vapor mole fraction** — 界面处水蒸气摩尔分数 `0.01`（默认）| 正标量

界面处的水蒸气摩尔分数。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface
humidity** 复选框并将 **Interface humidity
specification** 设置为 `Mole
fraction`。

### **Interface humidity ratio** — 界面处湿度比 `0.01`（默认）| 正标量

界面处的湿度比。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface
humidity** 复选框并将 **Interface humidity
specification** 设置为 `Humidity
ratio`。

### **Interface wet-bulb temperature** — 界面处湿球温度 `287 K`（默认）| 正标量

界面处的湿球温度。模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface
humidity** 复选框并将 **Interface humidity
specification** 设置为 `Wet-bulb
temperature`。

### **Provide input signal for interface trace gas** — 界面痕量气体控制选项 `off`（默认）| `on`

用于指定痕量气体分数的选项。如果选中此复选框，模块将启用端口 **TG**。如果清除此复选框，则可以指定恒定痕量气体条件。

### **Interface trace gas specification** — 痕量气体参数化 `Mass fraction`（默认）| `Mole fraction`

是否使用质量分数或摩尔分数对界面处的痕量气体进行参数化。

### **Interface trace gas mass fraction** — 界面处的痕量气体质量分数 `0.001`（默认）| 正标量

界面处痕量气体的质量分数。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface trace gas** 复选框，并将 **Interface trace gas specification** 设置为 `Mass fraction`。

### **Interface trace gas mole fraction** — 界面处的痕量气体摩尔分数 `0.001`（默认）| 正标量

界面处痕量气体的摩尔分数。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface trace gas** 复选框，并将 **Interface trace gas specification** 设置为 `Mole fraction`。

### **Provide input signal for interface water droplets** — 界面水滴控制选项 `off`（默认）| `on`

用于指定水滴与湿空气质量比的选项。如果选中此复选框，模块将启用端口 **D**。如果清除此复选框，则可以使用 **Interface mass ratio of water droplets to moist air** 参数指定恒定水滴条件。

### **Interface mass ratio of water droplets to moist air** — 界面处水滴与湿空气的质量比 `0`（默认）| 正标量

界面处水滴与湿空气的质量比。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface water droplets** 复选框。

### **Relative humidity at saturation** — 饱和点相对湿度 `1`（默认）| 正标量

饱和点的相对湿度。

### **Cross-sectional area at ports 2P and MA** — 端口面积 `0.01` `m^2`（默认）| 正标量

两相流体端口和湿空气端口的横截面积。

### **Two-phase fluid superheated vapor check** — 两相流体过热条件检查 `None`（默认）| `Warning` | `Error`

当界面处的流体不满足过热条件时要执行的操作。

### **Inputs outside valid range** — 监视或控制无效输入的选项 `Limit to valid values`（默认）| `Warn and limit to valid values` | `Error`

监视或控制无效输入。当选择 `Limit to valid values` 时，模块会将输入饱和限制在边界内。您可以选择让模块在限制输入时发出警告，方法是选择 `Warn and limit to valid values`；或者，您可以选择在模块接收到无效输入时停止仿真，方法是选择 `Error`。

## 所属库

Simscape / Fluids / Fluid Network Interfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024b：对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要启用液滴跟踪，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

不再使用 **Moisture and trace gas specification** 参数来指定界面是恒定的还是受控的，而是使用新的 **Provide input signal for interface humidity**、**Provide input signal for interface trace gas** 和 **Provide input signal for interface water droplets** 参数来启用物理信号输入端口。

## 描述

两相流体与湿空气网络接口

Interface (2P-MA) 模块表示两相流体网络与湿空气网络之间的流动连接。压力、温度和质量流量在接口处相等。该模块不在接口处传递各流体网络的流体属性。当湿空气离开端口 **MA** 时，该模块将 **Interface relative humidity**、**Interface trace gas mass fraction** 和 **Interface mass ratio of water droplets to moist air** 参数的值，或输入信号的值赋给信号。然而，当湿空气进入端口 **MA** 时，该模块保留上游值。

您可以选择在接口处保持恒定的湿度、水滴量和微量气体量，或者分别使用 **W** 或 **Tw**、**D** 和 **TG** 端口来指定它们。**2P** 端口处的流体必须保持过热状态。您可以使用 **Two-phase fluid superheated vapor check** 参数来选择当流体不满足此条件时模块执行的操作。

### 方程

该模块守恒质量，使得

m˙2P+m˙MA=0,

其中：

- *ṁ2P* 是流入端口 **2P** 的质量流量。
- *ṁMA* 是流入端口 **MA** 的质量流量。

该模块保持端口压力和温度相等，使得

p2P=pMAT2P=TMA

该模块计算接口处的能量平衡为

Φ2P+ΦMA=m˙2P(h2P+w2P22)+m˙MA(hMA+wMA22),

其中：

- *Φ2P* 是流入端口 **2P** 的能量流量。
- *ΦMA* 是流入端口 **MA** 的能量流量。
- *h2P* 是端口 **2P** 处的比焓。
- *hMA* 是端口 **MA** 处的比焓。
- *v2P* 是端口 **2P** 处的比体积。
- *vMA* 是端口 **MA** 处的比体积。
- *w2P* 是端口 **2P** 处的流速。
- *wMA* 是端口 **MA** 处的流速。

对于给定的横截面积 *S*，该模块将 *w2P* 定义为

w2P=m˙2Pv2PS,

并将 *wMA* 定义为

wMA=m˙MAvMAS,

其中

vMA=RITMApMA.

您使用 **Cross-sectional area at ports 2P and MA** 参数指定 *S*。该模块将接口混合物的比气体常数 *RI* 计算为两侧流体的函数，使得

RI=f(RA,RW,RG,xWI,xGI),

其中：

- *RA* 是干空气比气体常数。
- *RW* 是水蒸气比气体常数。
- *RG* 是微量气体比气体常数。
- *xWI* 是接口比湿度。当流动离开端口 **MA** 时，该模块根据您的参数设置确定此值：

  - 当您清除 **Provide input signal for interface humidity** 复选框时，该模块根据 **Interface humidity specification** 参数指定的方法计算 *xWI*。
  - 当您选择 **Provide input signal for interface humidity** 时，该模块根据您在端口 **W** 或端口 **Tw** 处提供的输入确定 *xWI*。
- *xGI* 是接口微量气体质量分数。当流动离开端口 **MA** 时，该模块根据您的参数设置确定此值：

  - 当您清除 **Provide input signal for interface trace gas** 复选框时，该模块根据 **Interface trace gas mass fraction** 或 **Interface trace gas mole fraction** 参数的值计算 *xGI*。
  - 当您选择 **Provide input signal for interface trace gas** 时，该模块根据您在端口 **TG** 处提供的输入确定 *xGI*。
