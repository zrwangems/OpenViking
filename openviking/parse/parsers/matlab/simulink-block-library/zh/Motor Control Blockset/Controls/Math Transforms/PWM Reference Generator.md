---
type: simulink-block
title: 'PWM Reference Generator'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'pwmreferencegenerator'
documentation_source_path: 'ref/pwmreferencegenerator.html'
language: zh-CN
chinese_source: official
---

# PWM Reference Generator

## 端口

### 输入

### **Vα** — *α* 轴定子参考电压分量 标量

沿 *αβ* 参考系的 *α* 轴的定子参考电压分量。

#### 依赖关系

要启用此端口，请将**输入类型**设置为 **Valphabeta**。

**数据类型:** `single` | `double` | `fixed point`

### **Vβ** — *β* 轴定子参考电压分量 标量

沿 *αβ* 参考系的 *β* 轴的定子参考电压分量。

#### 依赖关系

要启用此端口，请将**输入类型**设置为 **Valphabeta**。

**数据类型:** `single` | `double` | `fixed point`

### **Va** — 相分量 标量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请将**输入类型**设置为 **Vabc**。

**数据类型:** `single` | `double` | `fixed point`

### **Vb** — 相分量 标量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请将**输入类型**设置为 **Vabc**。

**数据类型:** `single` | `double` | `fixed point`

### **Vc** — 相分量 标量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请将**输入类型**设置为 **Vabc**。

**数据类型:** `single` | `double` | `fixed point`
### 输出

### **Vao** — *a* 轴定子参考电压分量 标量

沿 *abc* 参考系的 *a* 轴的定子参考电压分量。

**数据类型:** `single` | `double` | `fixed point`

### **Vbo** — *b* 轴定子参考电压分量 标量

沿 *abc* 参考系的 *b* 轴的定子参考电压分量。

**数据类型:** `single` | `double` | `fixed point`

### **Vco** — *c* 轴定子参考电压分量 标量

沿 *abc* 参考系的 *c* 轴的定子参考电压分量。

**数据类型:** `single` | `double` | `fixed point`

## 参数

### **输入类型** — 模块输入类型 **Valphabeta** (默认) | **Vabc** | **度**

模块用作输入的三相定子电压表示的类型。选择 *abc* 或 *αβ* 参考系。

### **调制方法** — 脉冲宽度调制 (PWM) 方法 **SVM: 空间矢量调制** (默认) | **SPWM: 正弦 PWM** | **60 DPWM:60 度不连续 PWM** | **60 DPWM (+30 度相移):从 60 DPWM +30 度相移** | **60 DPWM (-30 度相移):从 60 DPWM -30 度相移** | **30 DPWM:30 度不连续 PWM** | **120 DPWM: 正 DC 分量** | **120 DPWM: 负 DC 分量**

模块用于调制输入定子相位或参考电压的脉冲宽度调制 (PWM) 方法。

## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**支持的模块参数**

要使用 PWM Reference Generator 模块生成 HDL 代码，请将**调制方法**设置为 **SVM: 空间矢量调制**或 **SPWM: 正弦 PWM**。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置在输出端的寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除 PWM Reference Generator 模块层次结构。默认值为**继承**。另请参阅 FlattenHierarchy (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

从相电压生成调制信号

PWM Reference Generator 模块从定子相位或参考电压生成调制电压信号。

该模块接受由 *α-β* 电压分量描述的相电压 (*Vabc*) 或定子参考电压 (*Vαβ*)。

使用此模块执行正弦 PWM (SPWM) 和空间矢量调制 (SVM)，以及降低开关损失的离散脉冲宽度调制 (DPWM) 方法：

**注意**

对于以下 DPWM 方法，该模块仅支持标幺 (PU) 输入信号。有关标幺制的详细信息，请参阅标幺制。

- 60 DPWM - 60 度不连续 PWM
- 60 DPWM (+30 度相移) - 从 60 DPWM +30 度相移
- 60 DPWM (-30 度相移) - 从 60 DPWM -30 度相移
- 30 DPWM - 30 度不连续 PWM
- 120 DPWM - 正 DC 分量
- 120 DPWM - 负 DC 分量

对于不连续 PWM (DPWM)，该模块在每个相位的每个基本周期内将调制波钳制在正或负的 DC 母线（电压）上，钳制时间为 120 度。在每个钳制间隔期间，调制会中断。

下图显示正弦 PWM (SPWM) 波形。

下图显示空间矢量调制 (SVM) 波形。

下图显示每个基本周期内具有两个 60 度钳制间隔的 60 度 DPWM 波形。

下图显示具有正 30 度相移的 60 度 DPWM 波形。

下图显示具有负 30 度相移的 60 度 DPWM 波形。

下图显示每个基本周期内具有四个 30 度钳制间隔的 30 度 DPWM 波形。

下图显示具有正 DC（电压）钳制的 120 度 DPWM 波形。

下图显示具有负 DC（电压）钳制的 120 度 DPWM 波形。
