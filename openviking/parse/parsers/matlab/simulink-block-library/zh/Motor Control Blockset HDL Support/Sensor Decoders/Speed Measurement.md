---
type: simulink-block
title: 'Speed Measurement'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'speedmeasurement'
documentation_source_path: '../mcb/ref/speedmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Speed Measurement

## 端口

### 输入

### **θ** — 转子角位置 标量

转子的角位置，以弧度、度或标幺值指定。

**数据类型：** `single` | `double` | `fixed point`

### **Ts** — 模块再次执行前的采样时间 标量

模块每两次连续执行之间的固定时间间隔（以秒为单位）。

#### 依赖关系

要启用此端口，请选择 **Advanced Options** >
**Use input port for Discrete step size** 参数。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **⍵** — 转子角速度 标量

模块根据角位置输入计算得到的角速度。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Position unit** — 角位置单位 `Radians`（默认）| `Degrees` | `Per unit`

角位置 `θ` 的单位。

### **Position scaling datatype** — 映射输入位置的范围 `uint32`（默认）| `uint16` | `uint64`

用于在内部映射输入位置以适配无符号整数数据类型的范围。
例如，对于 uint32 数据类型，模块将范围 `(0 - 2π)` 内的输入缩放至
`(0 - (232-1))`。

### **Speed calculation criteria** — 速度计算方法 `Maximum application speed`（默认）| `Speed resolution` | `Time interval for speed calculation`

模块中使用的速度计算方法。所选方法决定模块可测量的转子速度范围。

这些参数根据 **Speed calculation
criteria** 参数改变取值：

| 参数名称 | Maximum application speed | Speed Resolution | Time interval for speed calculation |
| --- | --- | --- | --- |
| **Delays for speed calculation (number of samples)** | `299` | `28` | `28` |
| **Maximum measurable speed (RPM)** | `1000` | `10344.8276` | `10713.2857` |
| **Measurable speed resolution (RPM)** | `4.6566e-07` | `4.9892e-06` | `4.9892e-06` |

### **Discrete step size (s)** — 模块再次执行前的采样时间 `100e-6`（默认）| 标量

模块每两次连续执行之间的固定时间间隔（以秒为单位）。

这些参数根据 **Discrete step size
(s)** 参数值改变取值：

- **Delays for speed calculation (number of samples)**
- **Maximum measurable speed (RPM)**
- **Measurable speed resolution (RPM)**

#### 依赖关系

要启用此参数，请清除 **Advanced Options** >
**Use input port for Discrete step size** 参数。

### **Maximum application speed (RPM)** — 最大可测量转子速度 `1000`（默认）| 标量

模块可测量的最大转子速度（以每分钟转数为单位）。

这些参数根据 **Maximum application speed
(RPM)** 参数值改变取值：

- **Delays for speed calculation (number of samples)**
- **Maximum measurable speed (RPM)**
- **Measurable speed resolution (RPM)**

#### 依赖关系

要启用此参数，请将 **Speed calculation criteria** 设置为
`Maximum application speed`。

### **Speed Resolution (RPM)** — 最小可检测速度 `5e-6`（默认）| 标量

模块可检测的 `θ` 输入每单位时间变化的最小值。

这些参数根据 **Speed Resolution
(RPM)** 参数值改变取值：

- **Delays for speed calculation (number of samples)**
- **Maximum measurable speed (RPM)**
- **Measurable speed resolution (RPM)**

#### 依赖关系

要启用此参数，请将 **Speed calculation criteria** 设置为
`Speed resolution`。

### **Delays for speed calculation (number of samples)** — 用于计算速度的延迟（采样数） `299` 或 `28`（默认）| 标量

模块用于计算平均位置值的角位置输入的采样数。

这些参数会根据 **Delays for speed calculation (number of samples)** 参数值改变取值：

- **Maximum measurable speed (RPM)**
- **Measurable speed resolution (RPM)**

**注意**

**Delays for speed calculation (number of samples)** 参数的最大限制设置为 2^30（或 1073741824）。此限制会影响 **Maximum measurable speed (RPM)** 和 **Measurable speed resolution (RPM)** 参数的值，并且它们可能并不总是与所需值匹配。

#### 依赖关系

要启用此参数，请将 **Speed calculation criteria** 设置为 `Time interval for speed calculation`。

### **Maximum measurable speed (RPM)** — 最大可测量速度 `1000` 或 `10344.8276` 或 `10713.2857`（默认）| 标量

模块能够测量的绝对最大速度。

此参数不可配置，并使用由其他参数在内部计算得到的值。

### **Measurable speed resolution (RPM)** — 用于速度计算的最小速度分辨率 `4.6566e-07` 或 `4.9892e-06`（默认）| 标量

模块用于速度计算的最小速度分辨率。它始终小于或等于 **Speed Resolution (RPM)**。

此参数不可配置，并使用由其他参数在内部计算得到的值。

### **Speed unit** — 角速度输出的单位 `RPM`（默认）| `Degrees/Sec` | `Radians/Sec` | `Per unit based on maximum measurable speed` | `Per unit based on dialog`

角速度输出的单位。

### **Per unit speed (RPM)** — 用于标幺值计算的速度（以 RPM 为单位） `1000`（默认）

指定用于标幺值计算的速度，以 RPM 为单位。

#### 依赖关系

仅当 **Speed unit** 选择 `Per unit based on dialog` 时，此参数才会出现。

### **Speed data type** — 角速度输出的数据类型 `single`（默认）| `double` | `fixed point`

角速度输出 `⍵` 的数据类型。

**注意**

Speed Measurement 模块可能偶尔会显示警告消息
`'Wrap on overflow detected`.`'`

### **Use input port for Discrete step size** — 使用输入端口指定采样步长 `off`（默认）| `on`

如果要使用输入端口指定采样步长，请选择此参数。

## 所属库

Motor Control Blockset / Sensor Decoders Motor Control Blockset HDL Support / Sensor Decoders

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成
使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有单一的默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 要映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

### R2025a：新增输入端口和模块参数

模块参数对话框现在包含 **Use input port for Discrete step size** 参数，供您从单独的输入端口 **Ts** 指定离散步长。

## 描述

根据转子角位置计算速度

Speed Measurement 模块通过计算角位置相对于时间的变化，根据转子的角位置计算角速度。
