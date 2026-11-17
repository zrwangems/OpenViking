---
type: simulink-block
title: 'Mechanical to Electrical Position'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'mechanicaltoelectricalposition'
documentation_source_path: '../mcb/ref/mechanicaltoelectricalposition.html'
language: zh-CN
chinese_source: worker-translation
---

# Mechanical to Electrical Position

## 端口
```yaml
ports:
- name: θm
  summary: 转子机械位置 标量
  direction: input
  data_types: single | double | fixed point
- name: Npp
  summary: 电机中可用的极对数 标量
  direction: input
  data_types: single | double | fixed point
- name: Offset
  summary: 机械位置偏移 标量
  direction: input
  data_types: single | double | fixed point
- name: θe
  summary: 转子电位置 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **θm** — 转子机械位置 标量

转子的机械位置（由转子位置传感器输出），单位为弧度（0 到 2π）、度（0 到 360）或标幺值（0 到 1）。

**数据类型：** `single` | `double` | `fixed point`

### **Npp** — 电机中可用的极对数 标量

电机中可用的极对数。

#### 依赖关系

要启用此端口，请将 **Pole pairs input** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`

### **Offset** — 机械位置偏移 标量

转子电零点偏离机械零位的量。偏移的单位与机械位置输入的单位相同。

#### 依赖关系

要启用此端口，请将 **Specify offset via** 设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`

**注意**

在所有输入端口指定的值应具有相同的数据类型。
### 输出

### **θe** — 转子电位置 标量

转子的电位置，其范围与机械位置输入的范围相同。电位置的数据类型与输入的数据类型相同。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Pole pairs input
  summary: 指定电机中可用极对数的方法 Specify via dialog（默认）| Input port
  group: ''
- name: Number of pole pairs
  summary: 电机中可用的极对数 4（默认）| 标量
  group: ''
- name: Input mechanical angle unit
  summary: 转子机械位置的单位 Per unit（默认）| Radians | Degrees
  group: ''
- name: Offset input type
  summary: 指定偏移的方法 Input port（默认）| Specify via dialog
  group: ''
- name: Mechanical offset
  summary: 机械位置偏移的值 0（默认）| 标量
  group: ''
- name: Input data type
  summary: 输入端口的数据类型 single（默认）| double | fixed point
  group: ''
```

### **Pole pairs input** — 指定电机中可用极对数的方法 `Specify via dialog`（默认）| `Input port`

用于指定电机中可用极对数的方法。选择 `Input port` 以启用并使用输入端口 **Npp**。选择 `Specify via dialog` 以通过对话框提供极对数。

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

#### 依赖关系

要启用此参数，请将 **Pole pairs input** 参数设置为 `Specify via dialog`。

### **Input mechanical angle unit** — 转子机械位置的单位 `Per unit`（默认）| `Radians` | `Degrees`

转子机械位置的单位。

### **Offset input type** — 指定偏移的方法 `Input port`（默认）| `Specify via dialog`

指定机械位置偏移的方法。

- 选择 `Input port` 以启用并使用输入端口 **Offset**。
- 选择 `Specify via dialog` 以启用 **Mechanical offset** 参数并提供偏移值。

### **Mechanical offset** — 机械位置偏移的值 `0`（默认）| 标量

在此参数中指定机械位置偏移值。偏移的单位必须与机械位置输入的单位相同。

#### 依赖关系

要启用此参数，请将 **Offset input type** 设置为 `Specify via dialog`。

### **Input data type** — 输入端口的数据类型 `single`（默认）| `double` | `fixed point`

要用于输入端口的数据类型。

**注意**

如果选择定点输入数据类型并向输入端口提供定点值，则该模块在硬件上部署时运行更快。
## 所属库

Motor Control Blockset / Sensor Decoders Motor Control Blockset HDL Support / Sensor Decoders

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

根据机械位置计算转子的电位置

Mechanical to Electrical Position 模块通过使用转子的机械位置、机械偏移值和极对数来计算转子的电位置。
