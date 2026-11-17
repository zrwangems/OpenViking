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
chinese_source: worker-translation
---

# ACIM Feed Forward Control

## 端口

### 输入

### **Isd** — *d* 轴定子电流标量

沿旋转 *dq* 参考坐标系 *d* 轴的定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **Isq** — *q* 轴定子电流标量

沿旋转 *dq* 参考坐标系 *q* 轴的定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 转子机械转速标量

转子的机械转速。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **VsdFF** — *d* 轴前馈电压标量

沿旋转 *dq* 参考坐标系 *d* 轴的前馈电压。

**数据类型：** `single` | `double` | `fixed point`

### **VsqFF** — *q* 轴前馈电压标量

沿旋转 *dq* 参考坐标系 *q* 轴的前馈电压。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Number of pole pairs** — 电机中可用的极对数 `2`（默认）| 标量

感应电机中可用的极对数。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters`（默认）| `Non-linear model with D,Q-flux linkage LUTs`

*自 R2025a 起*

模块用于生成前馈电压增益的电机参数。将参数设置为以下值之一：

- `Linear model with lumped parameters` — 使用电机电感 *Ls*、*Lr*、*Lm* 的集中电路值和额定磁通生成电压增益。
- `Non-linear model with D,Q-flux linkage LUTs` — 使用 *d* 轴和 *q* 轴磁链查找表生成电压增益。

### **Stator leakage inductance (H)** — 定子绕组漏电感 `6.81e-3`（默认）| 标量

与定子绕组交链的漏磁通引起的电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Linear model with lumped parameters`。

### **Rotor leakage inductance (H)** — 转子绕组漏电感 `6.81e-3`（默认）| 标量

与转子绕组交链的漏磁通引起的电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Linear model with lumped parameters`。

### **Magnetizing Inductance (H)** — 感应电机的励磁电感 `30e-3`（默认）| 标量

励磁磁通引起的电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Linear model with lumped parameters`。

### **Rated Flux (Wb)** — 电机额定磁通 `38.2e-3`（默认）| 标量

感应电机的额定磁通（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Linear model with lumped parameters`。

### **D-axis current breakpoint vector, id (A)** — *d* 轴电流查找向量 `[0, 150, 350, 500]`（默认）| 向量

*自 R2025a 起*

用于磁链查找表的 *d* 轴电流查找向量（以百分比表示）。该向量可包含任意数量的元素。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q-axis current breakpoint vector, id (A)** — *q* 轴电流查找向量 `[0, 250, 500]`（默认）| 向量

*自 R2025a 起*

用于磁链查找表的 *q* 轴电流查找向量（以百分比表示）。该向量可包含任意数量的元素。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **D-axis flux linkage LUT, FluxD (id,iq) (Wb)** — 参考 *d* 轴磁链查找数据 `4.4e-2 * repmat([0, 150, 350, 500]', 1, 3)`（默认）| 向量

*自 R2025a 起*

*d* 轴磁链查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q-axis flux linkage LUT, FluxD (id,iq) (Wb)** — 参考 *q* 轴磁链查找数据 `2.1e-3 * repmat([0, 250, 500], 4, 1)`（默认）| 向量

*自 R2025a 起*

*q* 轴磁链查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Output Saturation (V)** — 输出值的饱和限值 `24/sqrt(3)`（默认）| 标量

模块输出 `VsdFF` 和 `VsqFF` 的饱和限值（单位：伏特）。

### **Input units** — 输入值的单位 `Per-Unit (PU)`（默认）| `SI Units`

输入值的单位。

### **Base Voltage (V)** — 标幺制系统的基准电压 `24/sqrt(3)`（默认）| 标量

标幺制系统的基准电压（单位：伏特）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base Current (A)** — 标幺制系统的基准电流 `5.3611`（默认）| 标量

标幺制系统的基准电流（单位：安培）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base Speed (rpm)** — 标幺制系统的基准转速 `1500`（默认）| 标量

标幺制系统的基准转速（单位：rpm）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中引入**

### R2025a：使用新的模块参数计算前馈电压增益

模块参数对话框现在包含一些参数，使您能够根据磁链查找表数据计算前馈电压增益。

## 描述

解耦 d 轴和 q 轴电流以消除扰动

ACIM Feed Forward Control 模块解耦 *d* 轴和 *q* 轴电流控制，并为感应电机的磁场定向控制生成相应的前馈电压增益。

该模块接受 *d* 轴和 *q* 轴电流的反馈值以及转子的机械转速。

### 方程

如果在 **Input units** 参数中选择 `Per-Unit (PU)`，则模块在执行任何计算之前会将输入转换为 SI 单位。计算输出后，模块会将值转换回标幺值（PU）。

电机电感和定子磁链表示为：

Ls= Lls+ Lm

Lr= Llr+ Lm

σ=1−(Lm2Ls⋅Lr)

λsd= LmLrλrd+σLsisd

λsq= σLsisq

这些方程描述了模块如何计算前馈增益。

VsdFF=−ωeλsq

VsqFF=ωeλsd

有关详细的方程组和假设，请参阅感应电机的数学模型。

其中：

- ωe 是对应于定子电压频率的电角速度（弧度/秒）。
- Lls 是定子漏电感（亨利）。
- Llr 是转子漏电感（亨利）。
- Ls 是定子电感（亨利）。
- Lr 是转子电感（亨利）。
- Lm 是电机的励磁电感（亨利）。
- σ 是感应电机的总漏磁系数。
- λsd 是定子的 *d* 轴磁链（韦伯）。
- λsq 是定子的 *q* 轴磁链（韦伯）。
- λrd 是转子的 *d* 轴磁链（韦伯）。
- isd 和 isq 是定子 *d* 轴和 *q* 轴电流（安培）。
