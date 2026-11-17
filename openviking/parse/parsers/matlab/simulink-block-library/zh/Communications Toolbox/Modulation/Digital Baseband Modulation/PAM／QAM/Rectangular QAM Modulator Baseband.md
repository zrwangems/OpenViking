---
type: simulink-block
title: 'Rectangular QAM Modulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / AM'
documentation_page: 'rectangularqammodulatorbaseband'
documentation_source_path: 'ref/rectangularqammodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# Rectangular QAM Modulator Baseband

## 端口
```yaml
ports:
- name: In
  summary: 输入数据 标量 | 列向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out
  summary: 输出数据 标量 | 列向量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **In** — 输入数据 标量 | 列向量

输入数据，指定为标量或列向量。输入数据必须是二进制值或范围在 [0, (*M* – 1)] 内的整数，其中 *M* 是由 **M-ary number** 指定的调制阶数。使用 **Input type** 将输入数据指定为 `Integer` 或 `Bit`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — 输出数据 标量 | 列向量

矩形 QAM 调制基带信号，以标量或向量形式返回。使用 **Output data type** 参数指定输出数据类型。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: M-ary number
  summary: 调制阶数 16（默认）| 正整数
  group: 主要
- name: Input type
  summary: 输入类型 Integer（默认）| Bit
  group: 主要
- name: Constellation ordering
  summary: 符号的映射顺序 Gray（默认）| Binary | User-defined
  group: 主要
- name: Constellation mapping
  summary: 用户定义的星座映射 [0:15]（默认）| 向量
  group: 主要
- name: Normalization method
  summary: 星座图的缩放方法 Min. distance between symbols（默认）| Average Power | Peak Power
  group: 主要
- name: Minimum distance
  summary: 两个最近星座点之间的距离 2（默认）| 正标量
  group: 主要
- name: Average power, referenced to 1 ohm (watts)
  summary: 平均功率 1（默认）| 正标量
  group: 主要
- name: Peak power, referenced to 1 ohm (watts)
  summary: 最大功率 1（默认）| 正标量
  group: 主要
- name: Phase offset (rad)
  summary: 信号星座图的旋转 0（默认）| 数值标量
  group: 主要
- name: View constellation
  summary: 绘制参考星座图的选项 按钮
  group: 主要
- name: Output data type
  summary: '输出数据类型 double（默认）| single | fixdt(1,16) | fixdt(1,16,0) | Inherit: Inherit via back propagation | <data type expression>'
  group: 数据类型
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **M-ary number** — 调制阶数 `16`（默认）| 正整数

调制阶数，指定为 2 的正整数次幂。调制阶数指定信号星座图中的点数。有关详细信息，请参阅星座图大小和缩放。

### **Input type** — 输入类型 `Integer`（默认）| `Bit`

输入类型，指定为 `Integer` 或 `Bit`，以指示输入由整数还是比特组组成。

- 要使用 `Integer`，输入信号必须由范围在 [0, (*M* – 1)] 内的整数组成。*M* 为 **M-ary number**。
- 要使用 `Bit`，输入信号必须包含二进制值，并且行数必须是 log2(*M*) 的整数倍。

有关详细信息，请参阅整数值信号和二值信号。

### **Constellation ordering** — 符号的映射顺序 `Gray`（默认）| `Binary` | `User-defined`

符号的映射顺序，指定为 `Gray`、`Binary` 或 `User-defined`。此参数确定模块如何将每个符号映射到星座点。根据 **Input type** 的设置，模块将输入整数或 log2(*M*) 个输入比特的组映射到一个符号。对于比特，第一个比特表示 MSB，最后一个比特表示 LSB。*M* 为 **M-ary number**。有关详细信息，请参阅整数值信号和二值信号。

### **Constellation mapping** — 用户定义的星座映射 `[0:15]`（默认）| 向量

您定义的星座映射，指定为包含范围在 [0, (*M* – 1)] 内唯一整数值的 *M* 元素向量。*M* 为 **M-ary number**。

此向量的第一个元素对应于星座图最左上角的点，后续元素按列从上到下、从左到右排列。最后一个元素对应于最右下角的点。

#### 依赖关系

当您将 **Constellation ordering** 设置为 `User-defined` 时，此参数出现。

### **Normalization method** — 星座图的缩放方法 `Min. distance between symbols`（默认）| `Average Power` | `Peak Power`

星座图的缩放方法，指定为 `Min. distance between symbols`、`Average Power` 或 `Peak Power`。有关详细信息，请参阅星座图大小和缩放

### **Minimum distance** — 两个最近星座点之间的距离 `2`（默认）| 正标量

两个最近星座点之间的距离，指定为正标量。

#### 依赖关系

当您将 **Normalization method** 设置为 `Min. distance between symbols` 时，此参数出现。

### **Average power, referenced to 1 ohm (watts)** — 平均功率 `1`（默认）| 正标量

星座图中符号的平均功率，以瓦特为单位，指定为正标量。功率值假定标称阻抗为 1 欧姆。

#### 依赖关系

当您将 **Normalization method** 设置为 `Average Power` 时，此参数出现。

### **Peak power, referenced to 1 ohm (watts)** — 最大功率 `1`（默认）| 正标量

星座图中符号的最大功率，以瓦特为单位，指定为正标量。功率值假定标称阻抗为 1 欧姆。

#### 依赖关系

当您将 **Normalization method** 设置为 `Peak Power` 时，此参数出现。

### **Phase offset (rad)** — 信号星座图的旋转 `0`（默认）| 数值标量

信号星座图的旋转，以弧度为单位，指定为数值标量。

### **View constellation** — 绘制参考星座图的选项 按钮

单击模块掩码上的 **View Constellation** 以可视化指定模块参数的信号星座图。在查看星座图之前，请应用参数设置。有关详细信息，请参阅查看调制器模块的星座图。

### 数据类型

### **Output data type** — 输出数据类型 `double`（默认）| `single` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

输出数据类型，指定为 `double`、`single`、`fixdt(1,16)`、`fixdt(1,16,0)`、`Inherit: Inherit via back propagation` 或 `<data type expression>`。

- `fixdt(1,16)`、`fixdt(1,16,0)` 或 `<data type expression>` 会启用可进一步指定详细信息的参数。
- `Inherit: Inherit via back propagation` 将输出数据类型和缩放设置为与下一个模块匹配。

有关指定数据类型的信息，请参阅数据类型助手。
## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / AM Communications Toolbox HDL Support / Modulation / AM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b, c` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 仅方形 QAM。  b 如果 ''input type'' 设置为 ''bit''，则输入为 ufix(1)。如果 ''input type'' 设置为 ''integer'' 以进行 M 进制调制，则输入为 ufix(ceil(log2(M)))。  c 定点输出必须为有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 该模块不支持 `single` 或 `double` 数据类型用于 HDL 代码生成。
- 当 **Input Type** 设置为 `Bit` 时，该模块不支持除 `boolean` 或 `ufix1` 以外的输入类型的 HDL 代码生成。

当输入类型设置为 `Bit`，但模块输入实际上是多比特（例如 `uint16`）时，Rectangular QAM Modulator Baseband 模块不支持 HDL 代码生成。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用矩形正交幅度调制进行调制

Rectangular QAM Modulator Baseband 模块使用矩形格星座图上的 M 进制正交幅度调制对输入信号进行调制。输出是调制信号的基带表示。

**注意**

所有功率值均假定标称阻抗为 1 欧姆。
