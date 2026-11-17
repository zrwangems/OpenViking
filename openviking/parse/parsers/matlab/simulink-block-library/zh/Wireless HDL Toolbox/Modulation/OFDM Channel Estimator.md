---
type: simulink-block
title: 'OFDM Channel Estimator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ofdmchannelestimator'
documentation_source_path: 'ref/ofdmchannelestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Channel Estimator

## 端口
```yaml
ports:
- name: data
  summary: 输入数据子载波 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: valid
  summary: 指示有效输入数据 标量
  direction: input
  data_types: Boolean
- name: refData
  summary: 参考数据子载波 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: refValid
  summary: 指示有效参考数据 标量
  direction: input
  data_types: Boolean
- name: numScPerSym
  summary: 每个 OFDM 符号的有效子载波数 标量
  direction: input
  data_types: uint8 | uint16 | uint32 | unsigned fixed point
- name: reset
  summary: 清除内部状态 标量
  direction: input
  data_types: Boolean
- name: data
  summary: 输出信道估计 标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: valid
  summary: 指示有效输出数据 标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入数据子载波 标量

输入数据子载波，指定为实数或复数值的标量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输入数据 标量

指示有效输入数据，指定为标量。

此端口是一个控制信号，用于指示 **data** 输入端口的数据何时有效。当该值为 `1` 时，模块采集 **data** 输入端口的数值。当该值为 `0` 时，模块忽略 **data** 输入端口的数值。

**数据类型：** `Boolean`

### **refData** — 参考数据子载波 标量

参考数据子载波，指定为实数或复数值的标量。

参考数据必须是单位模值序列。在数值序列 *r1*、*r2*、*r3*…、*rn* 中，如果 *rj* x *rj*\* = `1`，则这些数值是单位模值，

其中：

- *j* = 1, 2, 3, …, *n*。
- *rj*\* 是 *rj* 的复共轭。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **refValid** — 指示有效参考数据 标量

指示有效参考数据，指定为标量。

此端口是一个控制信号，用于指示 **refData** 输入端口的数据何时有效。当该值为 `1` 时，模块采集 **refData** 输入端口的数值。当该值为 `0` 时，模块忽略 **refData** 输入端口的数值。

**refValid** 端口值必须与 **valid** 端口值同步。

**数据类型：** `Boolean`

### **numScPerSym** — 每个 OFDM 符号的有效子载波数 标量

每个 OFDM 符号的有效子载波数，指定为范围从 2 到 65,536 的标量。

为支持每个符号的最小子载波数，**numScPerSym** 的数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 2。

#### 依赖关系

要启用此端口，请选择 **Enable averaging** 参数或 **Enable interpolation** 参数。

**数据类型：** `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **reset** — 清除内部状态 标量

清除内部状态，指定为标量。当该值为 `1` 时，模块停止当前计算并清除所有内部状态。

#### 依赖关系

要启用此端口，请选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 输出信道估计 标量

输出信道估计，以标量形式返回。输出数据类型与输入数据相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

指示有效输出数据，以标量形式返回。

此端口是一个控制信号，用于指示 **data** 输出端口的数据何时有效。当 **data** 输出端口的数据样本可用时，模块将此值设置为 `1`。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Enable averaging
  summary: 平均 LS 估计 off（默认）| on
  group: ''
- name: Number of symbols to be averaged
  summary: 要平均的符号数 2（默认）| 范围从 2 到 14 的整数
  group: ''
- name: Enable interpolation
  summary: 插值 LS 估计 off（默认）| on
  group: ''
- name: Interpolation factor
  summary: 插值因子 3（默认）| 范围从 2 到 12 的整数
  group: ''
- name: Maximum number of subcarriers per symbol
  summary: 每个符号的最大子载波数 52（默认）| 范围从 2 到 65, 536 的整数
  group: ''
- name: Enable reset input port
  summary: 复位信号 off（默认）| on
  group: ''
```

### **Enable averaging** — 平均 LS 估计 `off`（默认）| `on`

选择此参数以启用平均。

### **Number of symbols to be averaged** — 要平均的符号数 `2`（默认）| 范围从 2 到 14 的整数

指定要平均的符号数。

#### 依赖关系

要启用此参数，请选择 **Enable averaging** 参数。

### **Enable interpolation** — 插值 LS 估计 `off`（默认）| `on`

选择此参数以启用插值。

### **Interpolation factor** — 插值因子 `3`（默认）| 范围从 2 到 12 的整数

指定插值因子。

#### 依赖关系

要启用此参数，请选择 **Enable interpolation** 参数。

### **Maximum number of subcarriers per symbol** — 每个符号的最大子载波数 `52`（默认）| 范围从 2 到 65, 536 的整数

指定每个符号的最大子载波数。

#### 依赖关系

要启用此参数，请选择 **Enable averaging** 参数或 **Enable interpolation** 参数。

### **Enable reset input port** — 复位信号 `off`（默认）| `on`

选择此参数以在模块图标上启用 **reset** 端口。
## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2020a 中引入**

## 描述

使用输入数据和参考子载波估计信道

OFDM Channel Estimator 模块使用输入数据和参考子载波估计信道。该模块接受数据子载波、**valid** 控制端口以及 **refData** 和 **refValid** 参考端口。该模块输出信道估计和 **valid** 控制端口。该模块允许您指定每个输出符号要估计的子载波数。

您可以使用此模块在不同通信标准（例如长期演进 (LTE) [1] 和无线局域网 (WLAN) [4]）的接收端估计多径衰落信道。要执行正确的信道估计，**refData** 和 **refValid** 端口必须分别与 **data** 和 **valid** 端口同步。有关信道估计和参考数据的更多信息，请参阅 Channel Estimation (LTE Toolbox)。

此模块提供适用于 HDL 代码生成和硬件部署的接口和架构。
