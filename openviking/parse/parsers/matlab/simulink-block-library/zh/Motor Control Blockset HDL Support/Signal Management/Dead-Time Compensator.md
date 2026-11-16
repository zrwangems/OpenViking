---
type: simulink-block
title: 'Dead-Time Compensator'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'deadtimecompensator'
documentation_source_path: '../mcb/ref/deadtimecompensator.html'
language: zh-CN
chinese_source: worker-translation
---

# Dead-Time Compensator

## 端口

### 输入

### **Vabc** — 参考电压标量

三相参考电压（单位为 volts）。

**数据类型：** `single` | `double` | `fixed point`

### **Iab** — 测得电机电流标量

电机相-*a* 和相-*b* 电流的测量值（单位为 amperes）。

**数据类型：** `single` | `double` | `fixed point`

### **fPWM** — PWM 频率标量

用于执行脉宽调制的载波频率（单位为 hertz）。

**数据类型：** `single` | `double` | `fixed point`

### **Vdc** — 逆变器直流电压标量

逆变器的直流电压供电（单位为 volts）。

**数据类型：** `single` | `double` | `fixed point`

### **Enable** — 使能模块输出的信号标量

使能模块输出的信号：

- `1` — 启用补偿（模块输出补偿后的电压）。
- `0` — 禁用补偿（模块输出输入电压）。

#### 依赖关系

要启用此端口，请选择 **显示使能端口** 参数。

**数据类型：** `single` | `double` | `fixed point`

### 输出

### **Vabc ± Δ** — 补偿后三相电压标量

已针对逆变器死区效应进行补偿的电机三相电压（单位为 volts）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **死区时间 (s)** — 逆变器开关死区时间 `1e-6`（默认） | 标量

逆变器开关中的死区时间（单位为 seconds）。

### **为接近过零的电流启用滞环** — 为接近过零的电流启用滞环算法的选项 `off`（默认） | `on`

选择此参数可在输入电机相电流过零区域附近启用滞环算法。

该模块检测电机电流极性以确定电压补偿。当电机电流有噪声时，在电流过零附近使用滞环带宽有助于更好地检测电流极性。

### **电流滞环带宽 (A)** — 过零附近的电流滞环带宽 `0.1`（默认） | 标量

电流控制器的滞环带宽 *h*。接通点为 *h*，关断点为 *-h*。

#### 依赖关系

要启用此参数，请选择 **为接近过零的电流启用滞环**。

### **电机电流输入** — 电机电流输入的类型 `Two currents (Ia,Ib)`（默认） | `Three currents (Ia,Ib,Ic)`

电机电流输入的数量。您可以选择以下选项之一：

- `Two currents (Ia,Ib)`
- `Three currents (Ia,Ib,Ic)`

### 输入

### **显示使能端口** — 启用输入端口的选项 off（默认） | `on`

选择此参数以显示输入端口 **Enable**。

## 所属库

Motor Control Blockset / Signal Management Motor Control Blockset HDL Support / Signal Management

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

当您选择 **为接近过零的电流启用滞环** 参数时，此模块不支持 HDL 代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

通过修改参考电压来克服死区效应

Dead-Time Compensator 模块补偿逆变器死区。使用此模块补偿三相逆变器的死区效应。

用于电机驱动应用的三相逆变器本质上是非线性的。逆变器中的死区（添加该死区是为了避免逆变器桥臂短路）对这种非线性有很大影响。尽管死区可确保逆变器安全运行，但它可能对逆变器性能产生不利影响。这会导致逆变器输出电压波形偏离其最初预期的形式。

该模块接受三相参考电压、测得电机电流、PWM 频率和逆变器直流电压作为输入。它提供补偿逆变器死区效应的三相电压输出。该补偿有助于降低电机转矩或电流中的噪声或纹波，因此可改善电机驱动性能。

下图显示了该模块在电机控制算法中的位置。
