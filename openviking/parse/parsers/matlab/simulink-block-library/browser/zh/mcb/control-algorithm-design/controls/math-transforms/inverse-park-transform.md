---
type: simulink-block
title: 'Inverse Park Transform'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Math Transforms'
documentation_page: 'inverseparktransform'
documentation_source_path: 'ref/inverseparktransform.html'
language: zh-CN
chinese_source: official
---

# Inverse Park Transform

## 端口

### 输入

### **d** — 轴分量 标量

旋转 *dq* 参考系中的直轴分量 *d*。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**二输入**。

**数据类型:** `single` | `double` | `fixed point`

### **q** — 轴分量 标量

旋转 *dq* 参考系中的交轴分量 *q*。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**二输入**。

**数据类型:** `single` | `double` | `fixed point`

### **dq0** — 轴分量 标量

旋转 *dq* 参考系中的多路复用直轴分量 *d*、交轴分量 *q* 和 *0* 分量。

#### 依赖关系

要启用此端口，请将**输入数目**参数设置为**三输入**。

**数据类型:** `single` | `double` | `fixed point`

### **sin θe** — 旋转角度的正弦值 标量

变换角度 *θe* 的正弦值。*θe* 是旋转参考系和 *α* 轴之间的夹角。

**数据类型:** `single` | `double` | `fixed point`

### **cos θe** — 旋转角度的余弦值 标量

变换角度 *θe* 的余弦值。*θe* 是旋转参考系和 *α* 轴之间的夹角。

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

- **二输入** - 将模块配置为接受两个单独的输入信号 *d* 和 *q*。该模块生成两个单独的输出信号 *α* 和 *β*。
- **三输入** - 将模块配置为接受一个包含 *d*、*q* 和 *0* 信号的多路复用输入。该模块生成一个包含 *α*、*β* 和 *0* 信号的多路复用输出。

### **alpha (a 相)轴对齐** — *dq* 参考系对齐 **D 轴** (默认) | **Q 轴**

将旋转参考系的 *d* 或 *q* 轴与静止参考系的 *α* 轴对齐。

### **Theta 输入** — 位置输入的类型 **正弦和余弦电气位置** (默认) | **电气位置**

位置 (theta) 输入的类型：

- **正弦和余弦电气位置** - 将模块配置为直接接受 *sinθe* 和 *cosθe* 输入。
- **电气位置** - 将模块配置为接受电气位置 (*θe*) 输入。该模块根据 *θe* 输入在内部计算 *sinθe* 和 *cosθe* 信号。

### **Theta 单位** — 电气位置输入的单位 **标幺** (默认) | **弧度** | **度**

电气位置输入 (*θe*) 的单位。

#### 依赖关系

要启用此参数，请将**Theta 输入**设置为**电气位置**。

### **查找表的数据点数** — 查找表数组的大小 `1024` (默认) | 标量

模块用于根据 *θe* 输入计算 *sinθe* 和 *cosθe* 信号的查找表数组的大小。您可以指定一个介于 125 和 4095 之间的值。

#### 依赖关系

要启用此参数，请将**Theta 输入**设置为**电气位置**。

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
| **FlattenHierarchy** | 从生成的 HDL 代码中删除 Inverse Park Transform 模块层次结构。默认值为**继承**。另请参阅 FlattenHierarchy (HDL Coder)。  如果您对 Inverse Park Transform 模块使用资源共享优化（通过将 **SharingFactor** 属性设置为大于 0 的值来实现），请将该模块的 **FlattenHierarchy** 属性设置为 `on`。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的功能等效的资源数量。默认值为 0。另请参阅Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中推出**

## 描述

实现 dq 到 αβ 的变换

Inverse Park Transform 模块计算正交直轴 (*d*) 和正交轴 (*q*) 分量或旋转 *dq* 参考系中的多路复用 *dq0* 分量的帕克逆变换。

您可以对该模块进行配置，使 *d* 轴或 *q* 轴在时间 *t* = 0 处与 *α* 轴对齐。

该模块接受以下输入：

- 旋转参考系中的 *d-q* 轴分量或多路复用分量 *dq0*。使用**输入数目**参数以使用两个或三个输入。
- 对应变换角度的正弦值和余弦值。

在使用双输入配置时，该模块输出静止 *αβ* 参考系中的两相正交分量。在使用三输入配置时，它输出多路复用分量 *αβ0*。

对于平衡系统，零分量等于零。

下列各图显示在以下情形下的旋转 *dq* 参考系和 *αβ* 参考系中的 *α-β* 轴分量：

- *d* 轴与 *α* 轴对齐。
- *q* 轴与 *α* 轴对齐。

  在这两种情形下，角度 *θ = ωt*，其中：

  - *θ* 是 *d* 轴对齐时 *α* 轴和 *d* 轴之间的夹角，或是 *q* 轴对齐时 *α* 轴和 *q* 轴之间的夹角。它指示旋转 *dq* 参考系相对于 *α* 轴的角位置。
  - *ω* 是 *d-q* 参考系的转速。
  - *t* 是从初始对齐开始的时间，以秒为单位。

下列各图显示 *αβ* 和 *dq* 参考系的各个分量在以下情形的时间响应：

- *d* 轴与 *α* 轴对齐。
- *q* 轴与 *α* 轴对齐。

### 方程

如果将**输入数目**参数设置为**二输入**，则以下方程描述该模块如何实现帕克逆变换。

- 当 *d* 轴与 *α* 轴对齐时。

  [fαfβ]= [cosθ−sinθsinθcosθ][fdfq]
- 当 *q* 轴与 *α* 轴对齐时。

  [fαfβ]= [sinθcosθ−cosθsinθ][fdfq]

其中：

- fd 和 fq 是旋转 *dq* 参考系中的直轴和交轴正交分量。
- fα 和 fβ 是静止 *αβ* 参考系中的两相正交分量。

如果将**输入数目**参数设置为**三输入**，则以下方程描述该模块如何实现帕克逆变换：

- Inverse Park 模块实现 *a* 相到 *q* 轴对齐的变换，如下所示

  [αβ0]=[sin(θ)cos(θ)0−cos(θ)sin(θ)0001][dq0]

  其中：

  - *d* 和 *q* 是旋转参考系中双轴系统的直轴和交轴分量。
  - *0* 是零分量。
  - *α* 和 *β* 是静止参考系中两相系统的 alpha 轴和 beta 轴分量。
- 对于 *a* 相到 *d* 轴的对齐，该模块使用以下方程实现变换：

  [αβ0]=[cos(θ)−sin(θ)0sin(θ)cos(θ)0001][dq0]
