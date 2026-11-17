---
type: simulink-block
title: 'ACIM Feed Forward Control'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'acimfeedforwardcontrol'
documentation_source_path: 'ref/acimfeedforwardcontrol.html'
language: zh-CN
chinese_source: official
---

# ACIM Feed Forward Control

## 端口

### 输入

### **Isd** — D 轴定子电流 标量

沿旋转 *dq* 参考系的 *d* 轴的定子电流。

**数据类型:** `single` | `double` | `fixed point`

### **Isq** — Q 轴定子电流 标量

沿旋转 *dq* 参考系的 *q* 轴的定子电流。

**数据类型:** `single` | `double` | `fixed point`

### **ωm** — 转子的机械转速 标量

转子的机械转速。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **VsdFF** — d 轴前馈电压 标量

沿旋转 *dq* 参考系的 *d* 轴的前馈电压。

**数据类型:** `single` | `double` | `fixed point`

### **VsqFF** — q 轴前馈电压 标量

沿旋转 *dq* 参考系的 *q* 轴的前馈电压。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **极对数** — 电机中可用的极对数 `2` (默认) | 标量

感应电机中可用的极对数。

### **定子泄漏电感(H)** — 定子绕组的泄漏电感 `6.81e-3` (默认) | 标量

与定子绕组相关的泄漏磁通产生的电感（以亨为单位）。

### **转子泄漏电感(H)** — 转子绕组的漏感 `6.81e-3` (默认) | 标量

与转子绕组相关的泄漏磁通产生的电感（以亨为单位）。

### **磁化电感(H)** — 感应电机的磁化电感 `30e-3` (默认) | 标量

由磁化磁通产生的电感（以亨为单位）。

### **额定磁通(Wb)** — 电机的额定磁通 `38.2e-3` (默认) | 标量

感应电机的额定磁通（以韦伯为单位）。

### **输出饱和(V)** — 输出值的饱和界限 `24/sqrt(3)` (默认) | 标量

模块输出 `VsdFF` 和 `VsqFF` 的饱和界限（以伏特为单位）。

### **输入单位** — 输入值的单位 **标幺(PU)** (默认) | **SI 单位**

输入值的单位。

### **基电压(V)** — 标幺制的基电压 `24/sqrt(3)` (默认) | 标量

标幺制的基电压（以伏特为单位）。

#### 依存关系

要启用此参数，请将**输入单位**设置为**标幺(PU)**。

### **基电流(A)** — 标幺制的基电流 `5.3611` (默认) | 标量

标幺制的基电流（以安培为单位）。

#### 依存关系

要启用此参数，请将**输入单位**设置为**标幺(PU)**。

### **基转速(rpm)** — 标幺制的基转速 `1500` (默认) | 标量

标幺制的基转速（以 rpm 为单位）。

#### 依存关系

要启用此参数，请将**输入单位**设置为**标幺(PU)**。

## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置在输出端的寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中推出**

## 描述

解耦 d 轴和 q 轴电流以消除扰动

ACIM Feed Forward Control 模块可以解耦 *d* 轴和 *q* 轴电流控制，并生成对应的前馈电压增益以用于感应电机的磁场定向控制。

该模块接受 *d* 轴和 *q* 轴电流以及转子机械转速的反馈值。

### 方程

如果您在**输入单位**参数中选择**标幺(PU)**，则该模块会在执行任何计算之前将输入转换为 SI 单位。在计算输出后，该模块将这些值转换回标幺 (PU) 值。

电机电感和定子磁通表示为：

Ls= Lls+ Lm

Lr= Llr+ Lm

σ=1−(Lm2Ls⋅Lr)

λsd= LmLrλrd+σLsisd

λsq= σLsisq

下列方程描述模块如何计算前馈增益。

VsdFF=−ωeλsq

VsqFF=ωeλsd

有关详细的方程组和假设，请参阅感应电机的数学模型。

其中：

- ωe 是对应于定子电压频率的电角速度（弧度/秒）。
- Lls 是定子漏感（亨）。
- Llr 是转子泄漏电感（亨）。
- Ls 是定子电感（亨）。
- Lr 是转子电感（亨）。
- Lm 是电机的磁化电感（亨）。
- σ 是感应电机的总漏磁因子。
- λsd 是定子的 *d* 轴磁链（韦伯）。
- λsq 是定子的 *q* 轴磁链（韦伯）。
- λrd 是转子的 *d* 轴磁链（韦伯）。
- isd 和 isq 是定子的 *d* 轴和 *q* 轴电流（安培）。
