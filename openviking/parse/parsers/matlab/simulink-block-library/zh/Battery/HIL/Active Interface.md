---
type: simulink-block
title: 'Active Interface'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'HIL'
documentation_page: 'activeinterface'
documentation_source_path: 'ref/activeinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Active Interface

## 端口
```yaml
ports:
- name: Vcsc_charge
  summary: 来自电芯监控电路的充电电压，V 物理信号
  direction: input
- name: Icsc_discharge
  summary: 来自电芯监控电路的放电电流，A 物理信号
  direction: input
- name: SOC
  summary: 电池荷电状态，无量纲物理信号
  direction: input
- name: Vbat
  summary: 电池电压，V 物理信号
  direction: output
- name: Icsc
  summary: 电芯监控电路电流，A 物理信号
  direction: output
- name: isCharging
  summary: 充电状态，无量纲物理信号
  direction: output
- name: SOC
  summary: 电池荷电状态，无量纲物理信号
  direction: output
- name: T
  summary: 温度测量，K 物理信号
  direction: output
- name: +
  summary: 正极端子 电气
  direction: output
- name: '-'
  summary: 负极端子 电气
  direction: output
- name: H
  summary: 热端口 热
  direction: output
```

### 输入

### **Vcsc\_charge** — 来自电芯监控电路的充电电压，V 物理信号

来自电芯监控电路的充电电压，单位为伏特。

### **Icsc\_discharge** — 来自电芯监控电路的放电电流，A 物理信号

来自电芯监控电路的放电电流，单位为安培。

### **SOC** — 电池荷电状态，无量纲物理信号

电池的荷电状态，以百分比表示。

#### 依赖关系

要启用此端口，请将 **Expose SOC input
port** 参数设置为
`Yes`。
### 输出

### **Vbat** — 电池电压，V 物理信号

电池两端的电压，单位为伏特。

### **Icsc** — 电芯监控电路电流，A 物理信号

流过电芯监控电路的电流，单位为
安培。

#### 依赖关系

要启用此端口，请将 **Expose cell supervisory
circuit current measurement port** 参数设置为
`Yes`。

### **isCharging** — 充电状态，无量纲物理信号

物理信号输出端口，指示 BMS 正在对电池充电还是放电。如果此输出的值为
`1`，则 BMS 正在对电池充电。如果此输出的值
为 `0`，则 BMS 正在对电池放电。

### **SOC** — 电池荷电状态，无量纲物理信号

电池的荷电状态，以百分比表示。

#### 依赖关系

要启用此端口，请将 **Expose SOC output
port** 参数设置为
`Yes`。

### **T** — 温度测量，K 物理信号

电池的温度，单位为开尔文。

#### 依赖关系

要启用此端口，请将 **Expose temperature
measurement port** 参数设置为
`Yes`。
### 守恒

### **+** — 正极端子 电气

与接口正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

与接口负极端子关联的电气守恒端口。

### **H** — 热端口 热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Thermal port**
参数设置为 `Model`。
## 参数
```yaml
parameters:
- name: Cell supervisory circuit resistance
  summary: 电芯监控电路电阻 1e-6 Ohm（默认值）
  group: ''
- name: Expose SOC input port
  summary: SOC 输入端口可见性 No（默认值）| Yes
  group: ''
- name: Expose SOC output port
  summary: SOC 输出端口可见性 Yes（默认值）| No
  group: ''
- name: Thermal port
  summary: 热端口可见性 Omit（默认值）| Model
  group: ''
- name: Expose temperature measurement port
  summary: 温度测量端口可见性 Yes（默认值）| No
  group: ''
```

### **Cell supervisory circuit resistance** — 电芯监控电路电阻 `1e-6` `Ohm`（默认值）

电芯监控电路的代表性电阻，用于确保在抽象方程中
**Vcsc\_discharge** 和 **Vbat** 端口处的值之间
存在微小差异。此电压差可确保充电和放电模式之间的平滑
过渡。

### **Expose SOC input port** — SOC 输入端口可见性 `No`（默认值）| `Yes`

用于暴露电池 SOC 输入端口的选项。

### **Expose SOC output port** — SOC 输出端口可见性 `Yes`（默认值）| `No`

用于暴露电池 SOC 输出端口的选项。

#### 依赖关系

要启用此参数，请将 **Expose SOC input
port** 设置为 `Yes`。

### **Thermal port** — 热端口可见性 `Omit`（默认值）| `Model`

用于对无源接口的热端口建模的选项。

### **Expose temperature measurement port** — 温度测量端口可见性 `Yes`（默认值）| `No`

用于暴露测量电池温度的端口的选项。

#### 依赖关系

要启用此参数，请将 **Thermal port** 设置为
`Model`。
## 所属库

Simscape / Battery / HIL

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

电池与电芯监控电路之间的主动接口

Active Interface 模块提供电池与电芯监控电路之间的抽象
主动接口。将此模块与
桌面仿真和硬件在环电池仿真硬件一起使用。

电芯监控电路是一种连接到电池电芯或
并联组件的电子电路。您可以使用此电路来归一化模块或电池包内部的电压或荷电状态
（SOC）。在现实世界中，您将此设备实现在
电池与电池管理系统（BMS）控制之间。

在此图中，蓝色项目表示现实世界中的设备、电压和电流。

为避免损坏电池并在
标准运行条件和故障条件下测试您的电芯均衡算法，您可以使用硬件在环
电池仿真硬件。抽象接口有助于将无源均衡 BMS 连接到您的仿真电池，并进行设置和
配置。

在此图中：

- 蓝色表示现实世界中的设备、电压和
  电流。
- 绿色表示现实世界中的设备、
  电压和电流与仿真设备、电压和
  电流之间的接口。
- 橙色表示仿真设备、电压和
  电流。

Active Interface 模块提供功率电子设备的抽象
表示，而无需对其进行详细建模。例如，如果您的电池包在其组成部分内具有不同的温度或电压
水平，您可以使用此模块来检查 BMS 在各种运行场景之后是否正确
均衡您的电池包。

如果输入信号 **Vcsc\_charge** 小于仿真
电池电压 **Vbat**，则：

- 仿真电池正在放电。
- **IsCharging** 输出端口处的值为
  `0`（`false`）。
- **Icsc\_discharge** 输入端口指定
  电芯监控电路中的电流。
- **Icsc** 输出端口处的值在数值上
  与 **Icsc\_discharge** 输入端口处的值相同。
  此输出是提供给电芯监控
  电路的电流的测量值。

如果输入信号 **Vcsc\_charge** 大于或等于
**Vbat**，则：

- 仿真电池正在充电。
- **IsCharging** 输出端口处的值为
  `1`（`True`）。
- **Vcsc\_charge** 输入端口指定
  电池两端的电压减去电芯监控
  电路电阻上的电压降。
- 模块忽略 **Icsc\_discharge** 输入。
- **Icsc** 输出端口是提供给电芯监控
  电路的电流的测量值。因此，当 BMS 正在对
  电池充电时，此电流具有负值。

### SOC 可选端口

使用 Active Interface
模块的可选 SOC 端口可避免在 BMS 中实现 SOC 估计算法、根据仿真 SOC 验证和
确认 SOC 估计算法，或表示
现实世界中的电池。

- 如果在您的模型中，电池具有 SOC 输出端口，请暴露此模块的 SOC
  输入端口并适当连接端口。要暴露
  此模块的 SOC 输入端口，请将 **Expose SOC input
  port** 参数设置为 `Yes`。
- 要避免在 BMS 中实现 SOC 估计算法，或根据仿真 SOC
  验证和确认 SOC 估计算法，
  请暴露此模块的 SOC 输出端口并将其连接到您的 BMS。要
  暴露此模块的 SOC 输出端口，请将 **Expose SOC
  output port** 参数设置为
  `Yes`。
- 要表示现实世界中的电池，请勿暴露此模块的 SOC 端口。

### 热和温度可选端口

使用 Active
Interface 模块的可选热端口和温度端口来表示具有温度传感器的电池，
或根据仿真
温度验证和确认温度估计算法。

- 如果在您的模型中，电池具有温度传感器，请暴露
  此模块的热端口 **H** 并将其连接到
  热网络。要暴露此模块的热端口，请将
  **Thermal port** 参数设置为
  `Model`。
- 要根据仿真温度验证和确认温度估计算法，
  请同时暴露此模块的热端口 **H**
  和温度测量端口 **T**，
  并分别将它们连接到热网络和您的 BMS。要
  暴露此模块的温度测量端口，请将
  **Expose temperature measurement port** 参数设置为
  `Yes`。
- 如果在您的模型中，电池不包含热效应或
  没有温度传感器，请勿暴露此模块的热端口和温度
  端口。
