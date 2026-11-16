---
type: simulink-block
title: 'Clarke Transform'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'clarketransform'
documentation_source_path: '../mcb/ref/clarketransform.html'
language: zh-CN
chinese_source: official
---

# Clarke Transform

## 端口

### 输入

### **a** — 相分量 标量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**二输入**。

**数据类型:** `single` | `double` | `fixed point`

### **b** — 相分量 标量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**二输入**。

**数据类型:** `single` | `double` | `fixed point`

### **abc** — 相分量 标量

*abc* 参考系中三相系统的多路复用相分量 *a*、*b* 和 *c*。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**三输入**。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **α** — 轴分量 标量

静止 *αβ* 参考系中的 alpha 轴分量 *α*。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**二输入**。

**数据类型:** `single` | `double` | `fixed point`

### **β** — 轴分量 标量

静止 *αβ* 参考系中的 beta 轴分量 *β*。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**二输入**。

**数据类型:** `single` | `double` | `fixed point`

### **αβ0** — 轴分量 标量

静止 *αβ* 参考系中多路复用 alpha 轴分量 *α* 和 beta 轴分量 *β* 以及 `0` 分量。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**三输入**。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **输入数目** — 模块输入的数目 **二输入** (默认) | **三输入**

选择您可以指定的输入数目：

- **二输入** - 将模块配置为接受两个单独的输入信号 *a* 和 *b*。该模块生成两个单独的输出信号 *α* 和 *β*。
- **三输入** - 将模块配置为接受包含 *a*、*b* 和 *c* 信号的多路复用输入。该模块生成一个包含 *α*、*β* 和 *0* 信号的多路复用输出。

### **功率不变** — 启用功率不变性 `off` (默认) | `on`

要在模块输出中启用功率不变性属性，请选择此参数。要在模块输出中禁用功率不变性（启用振幅不变性），请不要选择此参数。

## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

实现 ab 到 αβ 的变换

Clarke Transform 模块计算 *abc* 参考系中平衡三相分量的克拉克变换，并输出静止 *αβ* 参考系中平衡两相正交分量。该模块也可以计算三相分量 *a*、*b* 和 *c* 的克拉克变换，并输出分量 *α*、*β* 和 `0`。对于平衡系统，零分量等于零。使用**输入数目**参数以使用两个或三个输入。

使用双输入配置时，该模块接受三相 (*abc*) 中的两个信号，自动计算第三个信号，并输出 *αβ* 参考系中的对应分量。

例如，该模块接受 *a* 和 *b* 输入值或多路复用输入值 *abc*，其中相位 *a* 轴与 *α* 轴对齐。

- 下图显示了定子绕组在 *abc* 参考系和静止 *αβ* 参考系中的磁轴方向。
- 下图显示了静止 *αβ* 参考系中的等效 *α* 和 *β* 分量。
- 等效平衡的 *abc* 和 *αβ* 系统的单个分量的时间响应。

### 方程

以下方程描述克拉克变换计算：

[fαfβf0]=(23)×[1−12−120 32−3212 12 12][fafbfc]

对于电机等平衡系统，零序分量计算始终为零。例如，电机的电流可以表示为，

ia+ib+ic=0

因此，在三相电机驱动中可以只使用两个电流传感器，您可以将其中的第三相计算为，

ic=−(ia+ib)

通过使用以下方程，该模块将克拉克变换实现为，

[fαfβ]= [1013  23][fafb]

其中：

- fa、fb 和 fc 是 *abc* 参考系中的平衡三相分量。
- fα 和 fβ 是静止 *αβ* 参考系中的平衡两相正交分量。
- f0 是静止 *αβ* 参考系中的零分量。
