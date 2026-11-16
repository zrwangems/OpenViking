---
type: simulink-block
title: 'Passive Interface'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Deployment and Hardware-in-the-Loop Simulation'
documentation_page: 'passiveinterface'
documentation_source_path: 'ref/passiveinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Passive Interface

## 端口

### 输入

### **Icsc\_discharge** — 来自电芯监控电路的放电电流，A physical signal | scalar

来自电芯监控电路的放电电流，单位为 ampere。

### **SOC** — 电池荷电状态，unitless physical signal | scalar

电池的荷电状态，以 percent 表示。

#### 依赖关系

要启用此端口，请将 **Expose SOC input port** 参数设置为 `Yes`。

### 输出

### **Vbat** — 电池电压，V physical signal

电池两端的电压，单位为 volt。

### **Icsc** — 电芯监控电路电流，A physical signal

流经电芯监控电路的电流，单位为 ampere。

此端口的值在数值上始终与 **Icsc\_discharge** 端口的值相同。此端口只是为了与 Active Interface 模块或任何需要它的硬件保持一致。

#### 依赖关系

要启用此端口，请将 **Expose cell supervisory circuit current measurement port** 参数设置为 `Yes`。

### **SOC** — 电池荷电状态，unitless physical signal

电池的荷电状态，以 percent 表示。

#### 依赖关系

要启用此端口，请将 **Expose SOC output port** 参数设置为 `Yes`。

### **T** — 温度测量，K physical signal

电池的温度，单位为 kelvin。

#### 依赖关系

要启用此端口，请将 **Expose temperature measurement port** 参数设置为 `Yes`。

### 守恒

### **+** — 正极端子 electrical

与接口正极端子关联的电气守恒端口。

### **-** — 负极端子 electrical

与接口负极端子关联的电气守恒端口。

### **H** — 热端口 thermal

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Thermal port** 参数设置为 `Model`。

## 参数

### **Expose cell supervisory circuit current measurement port** — 电芯监控电路电流的测量端口可见性 `Yes` (默认) | `No`

用于公开测量电芯监控电路电流的端口的选项。

### **Expose SOC input port** — SOC 输入端口可见性 `No` (默认) | `Yes`

用于公开电池 SOC 输入端口的选项。

### **Expose SOC output port** — SOC 输出端口可见性 `Yes` (默认) | `No`

用于公开电池 SOC 输出端口的选项。

#### 依赖关系

要启用此参数，请将 **Expose SOC input port** 设置为 `Yes`。

### **Thermal port** — 热端口可见性 `Omit` (默认) | `Model`

用于对无源接口的热端口建模的选项。

### **Expose temperature measurement port** — 温度测量端口可见性 `Yes` (默认) | `No`

用于公开测量电池温度的端口的选项。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为 `Model`。

## 所属库

Simscape / Battery / HIL

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

电池与电芯监控电路之间的无源接口

Passive Interface 模块提供电池与电芯监控电路之间的抽象无源接口。可将此模块用于桌面仿真和硬件在环电池仿真硬件。

电芯监控电路是一种电子电路，连接到电芯或并联组件。可使用此电路来归一化模组或电池包内部的电压或荷电状态（SOC）。在现实世界中，您将此设备实现在电池与电池管理系统（BMS）控制之间。

在此图中，蓝色项表示现实世界中的设备、电压和电流。

为避免损坏电池，并在标准运行条件和故障条件下测试电芯均衡算法，可使用硬件在环电池仿真硬件。抽象接口有助于将无源均衡 BMS 连接、设置和配置到仿真电池。

在此图中：

- 蓝色表示现实世界中的设备、电压和电流。
- 绿色表示现实世界中的设备、电压和电流与仿真设备、电压和电流之间的接口。
- 橙色表示仿真设备、电压和电流。

Passive Interface 模块提供电力电子设备的抽象表示，而无需对其进行详细建模。例如，如果电池包的各组成部分具有不同的温度或电压水平，可使用此模块检查 BMS 在各种运行场景之后是否正确均衡电池包。

### SOC 可选端口

使用 Passive Interface 模块的可选 SOC 端口可避免在 BMS 中实现 SOC 估计算法，根据仿真 SOC 验证和确认 SOC 估计算法，或表示现实世界中的电池。

- 如果模型中电池具有 SOC 输出端口，则公开此模块的 SOC 输入端口并适当连接这些端口。要公开此模块的 SOC 输入端口，请将 **Expose SOC input port** 参数设置为 `Yes`。
- 要避免在 BMS 中实现 SOC 估计算法，或根据仿真 SOC 验证和确认 SOC 估计算法，请公开此模块的 SOC 输出端口并将其连接到 BMS。要公开此模块的 SOC 输出端口，请将 **Expose SOC output port** 参数设置为 `Yes`。
- 要表示现实世界中的电池，请不要公开此模块的 SOC 端口。

### 热和温度可选端口

使用 Passive Interface 模块的可选热端口和温度端口来表示带温度传感器的电池，或根据仿真温度验证和确认温度估计算法。

- 如果模型中电池具有温度传感器，则公开此模块的热端口 **H** 并将其连接到热网络。要公开此模块的热端口，请将 **Thermal port** 参数设置为 `Model`。
- 要根据仿真温度验证和确认温度估计算法，请公开此模块的热端口 **H** 和温度测量端口 **T**，并将它们分别连接到热网络和 BMS。要公开此模块的温度测量端口，请将 **Expose temperature measurement port** 参数设置为 `Yes`。
- 如果模型中电池不包含热效应或没有温度传感器，请不要公开此模块的热端口和温度端口。
