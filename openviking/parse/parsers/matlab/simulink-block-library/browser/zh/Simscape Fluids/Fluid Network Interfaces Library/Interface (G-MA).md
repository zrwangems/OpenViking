---
type: simulink-block
title: 'Interface (G-MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Fluid Network Interfaces Library'
documentation_page: 'interfacegma'
documentation_source_path: 'ref/interfacegma.html'
language: zh-CN
chinese_source: worker-translation
---

# Interface (G-MA)

## 端口

### 输入

### **W** — 湿度，无量纲物理信号

与接口处湿度含量关联的物理信号端口。

#### 依赖关系

要启用此端口，请选中 **Provide input signal for interface humidity** 并将 **Interface humidity specification** 设置为 `Relative humidity`、`Specific humidity`、`Mole fraction` 或 `Humidity ratio`。

### **Tw** — 温度，K 物理信号

与接口处湿球温度关联的物理信号端口，单位为 K。

#### 依赖关系

要启用此端口，请选中 **Provide input signal for interface humidity** 并将 **Interface humidity specification** 设置为 `Wet-bulb temperature`。

### **TG** — 痕量气体，无量纲物理信号

与接口处痕量气体关联的物理信号端口。

#### 依赖关系

要启用此端口，请选中 **Provide input signal for interface trace gas**。

### **D** — 水滴质量比，无量纲物理信号

与接口处水滴与湿空气的质量比关联的物理信号端口。

#### 依赖关系

要启用此端口，请选中 **Provide input signal for interface water droplets**。

### 守恒

### **G** — 流体端口：气体

与接口处气体关联的气体守恒端口。

### **MA** — 湿空气端口：湿空气

与接口处湿空气关联的湿空气守恒端口。

## 参数

### **Provide input signal for interface humidity** — 接口湿度控制选项 `off`（默认）| `on`

用于指定接口湿度的选项。如果选中此复选框，该模块启用端口 **W**。如果清除此复选框，则可以指定恒定湿度条件。

### **Interface humidity specification** — 湿度参数化选项 `Relative humidity`（默认）| `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

是否使用相对湿度、比湿度、摩尔分数、湿度比或湿球温度计算湿度。

### **Interface relative humidity** — 接口处的相对湿度 `0.5`（默认）| 正标量

接口处的相对湿度。该模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface humidity** 复选框，并将 **Interface humidity specification** 设置为 `Relative humidity`。

### **Interface specific humidity** — 接口处的比湿度 `0.01`（默认）| 正标量

接口处的比湿度。该模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface humidity** 复选框，并将 **Interface humidity specification** 设置为 `Specific humidity`。

### **Interface water vapor mole fraction** — 接口处的水蒸气摩尔分数 `0.01`（默认）| 正标量

接口处的水蒸气摩尔分数。该模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface humidity** 复选框，并将 **Interface humidity specification** 设置为 `Mole fraction`。

### **Interface humidity ratio** — 接口处的湿度比 `0.01`（默认）| 正标量

接口处的湿度比。该模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface humidity** 复选框，并将 **Interface humidity specification** 设置为 `Humidity ratio`。

### **Interface wet-bulb temperature** — 接口处的湿球温度 `287 K`（默认）| 正标量

接口处的湿球温度。该模块使用此值计算湿度。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface humidity** 复选框，并将 **Interface humidity specification** 设置为 `Wet-bulb temperature`。

### **Provide input signal for interface trace gas** — 接口痕量气体控制选项 `off`（默认）| `on`

用于指定痕量气体分数的选项。如果选中此复选框，该模块启用端口 **TG**。如果清除此复选框，则可以指定恒定痕量气体条件。

### **Interface trace gas specification** — 痕量气体参数化 `Mass fraction`（默认）| `Mole fraction`

是否使用质量分数或摩尔分数来参数化接口处的痕量气体。

### **Interface trace gas mass fraction** — 接口处的痕量气体质量分数 `0.001`（默认）| 正标量

接口处的痕量气体质量分数。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface trace gas** 复选框，并将 **Interface trace gas specification** 设置为 `Mass fraction`。

### **Interface trace gas mole fraction** — 接口处的痕量气体摩尔分数 `0.001`（默认）| 正标量

接口处的痕量气体摩尔分数。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface trace gas** 复选框，并将 **Interface trace gas specification** 设置为 `Mole fraction`。

### **Provide input signal for interface water droplets** — 接口水滴控制选项 `off`（默认）| `on`

用于指定水滴与湿空气质量比的选项。如果选中此复选框，该模块启用端口 **D**。如果清除此复选框，则可以使用 **Interface mass ratio of water droplets to moist air** 参数指定恒定水滴条件。

### **Interface mass ratio of water droplets to moist air** — 接口处水滴与湿空气的比 `0`（默认）| 正标量

接口处水滴与湿空气的质量比。

#### 依赖关系

要启用此参数，请清除 **Provide input signal for interface water droplets** 复选框。

### **Relative humidity at saturation** — 饱和点相对湿度 `1`（默认）| 正标量

饱和点的相对湿度。

### **Cross-sectional area at ports G and MA** — 端口面积 `0.01` `m^2`（默认）| 正标量

气体端口和湿空气端口的横截面积。

### **Inputs outside valid range** — 用于监测或控制无效输入的选项 `Limit to valid values`（默认）| `Warn and limit to valid values` | `Error`

监测或控制无效输入。当选择 `Limit to valid values` 时，该模块将输入限制在边界内。您可以选择 `Warn and limit to valid values` 让该模块在限制输入时发出警告，也可以选择 `Error` 使该模块在收到无效输入时停止仿真。

## 所属库

Simscape / Fluids / Fluid Network Interfaces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024b：对悬浮在湿空气流中的水滴建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴建模。要启用液滴跟踪，请在连接到您的湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

不再使用 **Moisture and trace gas specification** 参数来指定接口是恒定还是受控，而应使用新的 **Provide input signal for interface humidity**、**Provide input signal for interface trace gas** 和 **Provide input signal for interface water droplets** 参数来启用物理信号输入端口。

### R2023a：新的湿度指定选项

该模块为 **Interface humidity specification** 参数新增了一个选项。此选项称为 `Wet-bulb temperature`，允许以湿球温度形式输入数据。

## 描述

气体和湿空气网络接口

Interface (G-MA) 模块表示气体网络与湿空气网络之间的流动连接。压力、温度和质量流量在接口处相等。该模块不跨接口传递各流体网络的流体属性。为保持流体属性守恒，请确保 Gas Properties (G) 模块和 Moist Air Properties (MA) 模块具有相同设置。当湿空气离开端口 **MA** 时，该模块将 **Interface relative humidity**、**Interface trace gas mass fraction** 和 **Interface mass ratio of water droplets to moist air** 参数的值，或输入信号的值，赋给该信号。但是，当湿空气进入端口 **MA** 时，该模块保留上游值。

您可以选择在接口处保持恒定的湿度、水滴和痕量气体量，还是分别使用 **W** 或 **Tw**、**D** 和 **TG** 端口来指定它们。

### 质量和动量平衡

该模块保持质量守恒，使得

m˙G+m˙MA=0,

其中：

- *ṁG* 是流入端口 **G** 的质量流量。
- *ṁMA* 是流入端口 **MA** 的质量流量。

该模块保持端口压力和温度相等，使得

pG=pMATG=TMA

### 能量平衡

该模块按以下方式计算接口处的能量平衡

ΦG+ΦMA=m˙G(hG+wG22)+m˙MA(hMA+wMA22),

其中：

- *ΦG* 是流入端口 **G** 的能量流量。
- *ΦMA* 是流入端口 **MA** 的能量流量。
- *hG* 是端口 **G** 的比焓。
- *hMA* 是端口 **MA** 的比焓。
- *vG* 是端口 **G** 的比容。
- *vMA* 是端口 **MA** 的比容。
- *wG* 是端口 **G** 的流速。
- *wMA* 是端口 **MA** 的流速。

对于给定的横截面积 *S*，该模块将 *wG* 定义为

wG=m˙GvGS,

并将 *wMA* 定义为

wMA=m˙MAvMAS,

其中：

vMA=RITMApMA.

接口处混合物的比气体常数是两侧流体的函数，使得

RI=f(RA,RWRG,xWI,xGI),

其中：

- *RA* 是干空气比气体常数。
- *RW* 是水蒸气比气体常数。
- *RG* 是痕量气体比气体常数。
- *xWI* 是接口比湿度。当流动离开端口 **MA** 时，该模块根据您的参数设置确定此值：

  - 当清除 **Provide input signal for interface humidity** 复选框时，该模块根据 **Interface humidity specification** 参数指定的方法计算 *xWI*。
  - 当选择 **Provide input signal for interface humidity** 时，该模块根据您在端口 **W** 或端口 **Tw** 提供的输入确定 *xWI*。
- *xGI* 是接口痕量气体质量分数。当流动离开端口 **MA** 时，该模块根据您的参数设置确定此值：

  - 当清除 **Provide input signal for interface trace gas** 复选框时，该模块根据 **Interface trace gas mass fraction** 或 **Interface trace gas mole fraction** 参数的值计算 *xGI*。
  - 当选择 **Provide input signal for interface trace gas** 时，该模块根据您在端口 **TG** 提供的输入确定 *xGI*。
