---
type: simulink-block
title: 'Inverse Clarke Transform'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'inverseclarketransform'
documentation_source_path: '../mcb/ref/inverseclarketransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Clarke Transform

## 端口
```yaml
ports:
- name: α
  summary: 轴分量 标量
  direction: input
  data_types: single | double | fixed point
- name: β
  summary: 轴分量 标量
  direction: input
  data_types: single | double | fixed point
- name: αβ0
  summary: 轴分量 标量
  direction: input
  data_types: single | double | fixed point
- name: a
  summary: 相分量 标量
  direction: output
  data_types: single | double | fixed point
- name: b
  summary: 相分量 标量
  direction: output
  data_types: single | double | fixed point
- name: c
  summary: 相分量 标量
  direction: output
  data_types: single | double | fixed point
- name: abc
  summary: 相分量 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **α** — 轴分量 标量

静止 *αβ* 参考系中的 alpha 轴分量 *α*。

#### 依赖关系

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **β** — 轴分量 标量

静止 *αβ* 参考系中的 beta 轴分量 *β*。

#### 依赖关系

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **αβ0** — 轴分量 标量

静止 *αβ* 参考系中的多路复用 alpha 轴分量 *α*、beta 轴分量 *β* 和 `0` 分量。

#### 依赖关系

要启用此端口，请将 **Number of inputs** 参数设置为 `Three inputs`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **a** — 相分量 标量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **b** — 相分量 标量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **c** — 相分量 标量

*abc* 参考系中三相系统的分量。

#### 依赖关系

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **abc** — 相分量 标量

*abc* 参考系中三相系统的多路复用相分量 *a*、*b* 和 *c*。

#### 依赖关系

要启用此端口，请将 **Number of inputs** 参数设置为 `Three inputs`。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of inputs
  summary: 模块输入数量 Two inputs（默认）| Three inputs
  group: ''
- name: Power invariant
  summary: 启用功率不变性 off（默认）| on
  group: ''
```

### **Number of inputs** — 模块输入数量 `Two inputs`（默认）| `Three inputs`

选择可以指定的输入数量：

- `Two inputs` — 将模块配置为接受两个独立的输入信号 *α* 和 *β*。该模块生成三个独立的输出信号 *a*、*b* 和 *c*。
- `Three inputs` — 将模块配置为接受包含 *α*、*β* 和 *0* 信号的多路复用输入。该模块生成包含 *a*、*b* 和 *c* 信号的多路复用输出。

### **Power invariant** — 启用功率不变性 `off`（默认）| `on`

要启用模块输出中的功率不变性属性，请选中此参数。要禁用模块输出中的功率不变性（启用幅值不变性），请清除此参数。
## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 使用 Fixed-Point Designer™ 进行定点转换设计与仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

实现 αβ 到 abc 变换

Inverse Clarke Transform 模块计算静止 *αβ* 参考系中平衡两相正交分量的 Inverse Clarke 变换，并输出静止 *abc* 参考系中的平衡三相分量。或者，该模块可以计算分量 *α*、*β* 和 `0` 的 Inverse Clarke 变换，以输出三相分量 *a*、*b* 和 *c*。对于平衡系统，零分量等于零。使用 **Number of inputs** 参数选择使用两个或三个输入。

该模块接受 *α-β* 轴分量作为输入，并输出相应的三相信号，其中 phase-*a* 轴与 *α* 轴对齐。

- *αβ* 参考系中的 *α* 和 *β* 输入分量。
- *abc* 参考系和 *αβ* 参考系中等效 *a*、*b* 和 *c* 输出分量的方向。
- 等效平衡 *αβ* 和 *abc* 系统各个分量的时间响应。

### 方程

以下方程描述了 Inverse Clarke 变换计算：

[fafbfc]=[101−12321−12−321][fαfβf0]

对于像电机这样的平衡系统，零序分量计算始终为零：

ia+ib+ic=0

因此，在三相电机驱动中，您可以仅使用两个电流传感器，其中可以计算第三相为，

ic=−(ia+ib)

通过使用这些方程，该模块将 Inverse Clarke 变换实现为，

[fa fb fc ]= [10−1232−12−32][fαfβ]

其中：

- fα 和 fβ 是静止 *αβ* 参考系中的平衡两相正交分量。
- f0 是静止 *αβ* 参考系中的零分量。
- fa、fb 和 fc 是 *abc* 参考系中的平衡三相分量。
