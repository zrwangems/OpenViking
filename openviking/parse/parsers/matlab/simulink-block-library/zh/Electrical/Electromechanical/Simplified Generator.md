---
type: simulink-block
title: 'Simplified Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical'
documentation_page: 'simplifiedgenerator'
documentation_source_path: 'ref/simplifiedgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Simplified Generator

## 端口

### 输入

### **Pref** — 参考功率，单位为标幺值的物理信号

物理信号输入端口，用于指定标幺值参考功率。
### 守恒

### **R** — 转子机械旋转

与转子关联的机械旋转守恒端口。

### **C** — 机壳机械旋转

与机壳关联的机械旋转守恒端口。

### **~** — 三相端口 三相电气

复合三相电气守恒端口。

有关复合三相端口和扩展三相端口的详细信息，请参阅 Three-Phase Ports。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为
`Composite three-phase ports`。

### **n** — 中性相电气

与中性相关联的电气守恒端口。

### **a** — *a* 相电气

与 *a* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为
`Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为
`Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为
`Expanded three-phase ports`。

## 参数

要以交互方式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### 常规

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

用于选择复合三相端口或扩展三相端口的选项。有关详细信息，
请参阅 Three-Phase Ports。

### **Rated power** — 额定功率 `100e3` `W`（默认）| 非负标量

额定功率。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）| 正标量

额定电气频率。

### **Internal source voltage (phase-to-phase RMS)** — 内部电源电压 `1485` `V`（默认）| 非负标量

内部电源电压。

### **Source impedance** — 电源阻抗参数化 `X/R Ratio`（默认）| `Series RL`

电源阻抗参数化方法。请选择以下选项之一：

- `X/R Ratio` — 指定串联连接的电抗与电阻之比。
- `Series RL` — 指定电阻和电感。

### **Short circuit power** — 短路功率 `1e6` `A*V`（默认）| 正标量

短路功率。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为
`X/R Ratio`。

### **X/R ratio** — X/R 比 `15`（默认）| 正标量

串联连接的电抗与电阻之比。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为
`X/R Ratio`。

### **Inductance** — 电感 `0.01` `H`（默认）| 正标量

电感。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为
`Series RL`。

### **Resistance** — 电阻 `0.1` `Ohm`（默认）| 正标量

电阻。

#### 依赖关系

要启用此参数，请将 **Source impedance** 设置为
`Series RL`。

### **Source impedance parasitic parallel conductance** — 电源阻抗寄生并联电导 `0` `1/Ohm`（默认）| 非负标量

电源阻抗的寄生并联电导。

### **Percentage mechanical efficiency** — 机械效率百分比 `95`（默认）| 正标量

机械效率，以百分比表示。

### **Active power frequency droop** — 有功功率频率下垂 `0.1` `Hz`（默认）| 非负标量

有功功率的频率下垂。

### **Droop filter time constant** — 下垂滤波器时间常数 `1e-2` `s`（默认）| 标量

下垂滤波器时间常数。

### **Rotor inertia** — 转子惯量 `1` `kg*m^2`（默认）| 正标量

转子对运动变化的阻力。

### **Rotor damping** — 转子阻尼 `0` `N*m*s/rad`（默认）| 非负标量

转子阻尼。

### **Electrical power measurement filter time constant** — 电功率测量滤波器时间常数 `1e-3` `s`（默认）| 非负标量

电功率测量的滤波器时间常数。

## 所属库

Simscape / Electrical / Electromechanical

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

机电发电机的行为模型

Simplified Generator 模块实现机电发电机的行为
模型。使用 **Pref** 端口指定参考功率。该模块向机械网络提供参考功率，
并提供满足机械功率需求并计入损耗所需的电功率。下图显示了该模块的电路配置。该模块
充当带有串联电源阻抗的恒压源。

- *V*ie 是电源电压。
- *I*S 是串联电源电流。
- *R*S 是串联电源电阻。
- *L*S 是串联电源电感。

Simplified Generator 模块可在并网和孤岛两种模式下运行。在并网模式下，机械功率跟踪
参考功率，并且您需要向电网提供电功率以计入损耗。有功功率潮流取决于整个电气网络的
串联连接电抗与电阻之比。为实现预期行为，您需要调节
**Active power frequency droop** 和 **Droop filter time
constant** 参数以及模块阻抗。要选择如何指定模块阻抗，请将 **Source impedance** 参数设置为以下选项之一：

- `X/R Ratio` — 指定串联连接的电抗与电阻之比。
- `Series RL` — 指定电阻和电感。

在孤岛模式下，该模块充当恒压交流电源，因为维持频率优先于机械功率跟踪功率参考值。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，
请使用模块对话框或 Property
Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用
基于标称值的系统缩放可提高仿真鲁棒性。标称值
可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal
Values** 部分。有关更
多信息，请参阅 System Scaling by Nominal Values。

### 假设和限制

此模块要求电气网络具有较高的串联连接
电抗与电阻之比。
