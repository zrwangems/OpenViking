---
type: simulink-block
title: 'Depuncturer'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'depuncturer'
documentation_source_path: 'ref/depuncturer.html'
language: zh-CN
chinese_source: worker-translation
---

# Depuncturer

## 端口

### 输入

### **data** — 输入样本标量

输入样本，指定为标量。该模块根据输入样本的数据类型在打孔位置插入中性值。

| 输入数据类型 | 插入的中性值 |
| --- | --- |
| - `boolean` - `fixdt(0,1,0)` | 0 |
| `fixdt(0,WL,0)` | 2(WL-1) |
| `uint8` | 128 |
| `uint16` | 32768 |
| - `fixdt(1,WL,0)` - `int8` - `int16` - `single` - `double` | 0 |

当输入类型为 `Boolean` 或 `fixdt(0,1,0)` 时，该模块将输入视为硬判决样本。对于有符号和无符号数值类型，该模块假定为软判决样本。对于 `single` 和 `double` 数据类型，该模块将样本视为有符号整数，但 HDL 代码生成不支持这些数据类型。

输入样本的字长必须小于或等于 16 bits，且小数长度必须为 0 bits。

**数据类型：** `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixdt(0,1,0)` | `fixdt(S,WL,0)` | `single` | `double`

### **puncVector** — 打孔向量，二进制值的列向量

打孔向量，指定为二进制值的列向量。打孔向量的长度必须是范围 [4, 28] 中的偶数。长度必须保持不变。该模块从提供的向量中移除初始零，直到第一个 `1` (`true`)。在第一个 `1` (`true`) 之后，打孔向量不能包含任何匹配 [0 0] 的 [1:0] 子向量。

例如，IEEE 802.11 WLAN 标准 [1] 支持打孔率 2/3、3/4 和 5/6，相应的向量长度分别为 4、6 和 10。要支持这些多个速率，请将 **Puncture vector source** 设置为 `Input port`。要支持最大向量大小，所有速率的向量长度都必须为 10。对于 2/3 和 3/4 速率，用零填充 **puncVector** 输入，以创建 10 元素向量。3/4 速率的打孔向量为 `[1 1 0 1 1 0]'`。对于长度为 10 的向量，请使用 `[0 0 0 0 1 1 0 1 1 0]'` 作为输入 **puncVector**。

当 **Operation mode** 设置为 `Continuous` 时，该模块在 **syncPunc** 和输入 **valid** 端口都为 `1` (`true`) 时捕获 **puncVector** 的值。

当 **Operation mode** 设置为 `Frame` 时，该模块在 **ctrl**`.start` 和 **ctrl**`.valid` 都为 `1` (`true`) 时捕获 **puncVector** 的值。

#### 依赖关系

要启用此端口，请将 **Puncture vector source** 设置为 `Input port`。

**数据类型：** `Boolean`

### **syncPunc** — 打孔同步信号标量

打孔同步信号，指定为 `Boolean` 标量值。此输入是一个控制信号，用于将打孔向量输入与输入样本同步。当 **syncPunc** 和 **valid** 都为 `1` (`true`) 时，该模块对齐打孔向量以开始打孔。该模块从 **puncVector** 输入端口或 **Puncture vector** 参数捕获向量。当 **syncPunc** 为 `0` (`false`) 时，该模块忽略 **puncVector** 端口。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Continuous`。当 **Operation mode** 为 `Frame` 时，该模块使用输入 **ctrl** 总线中的控制信号同步打孔向量。

**数据类型：** `Boolean`

### **valid** — 输入样本的有效性标量

控制信号，指示来自 **data** 输入端口的样本何时有效。当 **valid** 为 1 (`true`) 时，该模块捕获 **data** 输入端口的值。当 **valid** 为 0 (`false`) 时，该模块忽略输入样本。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Continuous`。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Frame`。

**数据类型：** `bus`
### 输出

### **data** — 输出样本 2×1 列向量

输出样本，以 2×1 列向量形式返回。数据类型与输入样本的数据类型相同。

**数据类型：** `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixdt(0,1,0)` | `fixdt(S,WL,0)` | `single` | `double`

### **valid** — 输出数据样本的有效性标量

控制信号，指示来自 **data** 输出端口的样本何时有效。当输出 **data** 端口上存在有效样本时，该模块将 **valid** 端口设置为 `1` (`true`)。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Continuous`。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Frame`。

**数据类型：** `bus`

### **erasure** — 中性符号位置 2×1 列向量

中性符号位置，以对应于输出样本的 2×1 列向量形式返回。当 **erasure** 为 `1` (`true`) 时，对应的输出 **data** 元素是解打孔后的中性值。

**数据类型：** `Boolean`

## 参数

### **Operation mode** — 帧结束行为 `Continuous`（默认）| `Frame`

帧结束行为，指定为以下模式之一：

- `Continuous` – 允许随时更改 **puncVector**。要强制该模块捕获新的打孔向量，请将 **syncPunc** 设置为 `1`(`true`)。此波形显示在 `Continuous` 模式下对 `ufix4` 输入样本进行解打孔。

  显示连续模式下解打孔行为的 Logic Analyzer 波形。
- `Frame` – 只能在帧开始时更改 **puncVector**，由 **ctrl**`.start` 指示。此波形显示在 `Frame` 模式下对 `ufix4` 输入样本进行解打孔。

  显示帧模式下解打孔行为的 Logic Analyzer 波形。

### **Puncture vector source** — 打孔向量的来源 `Input port`（默认）| `Property`

打孔向量的来源，指定为以下之一：

- `Input port` – 使用 **puncVector** 端口指定打孔向量。
- `Property` – 使用 **Puncture vector** 参数指定打孔向量。

### **Puncture vector** — 插入中性值的位置 `[1;1;0;1;1;0]`（默认）| 二进制值的列向量

打孔向量，指定为二进制值的列向量。打孔向量的长度必须是范围 [4, 28] 中的偶数。默认值是 IEEE 802.11 WLAN [1] 的 3/4 码率的打孔向量。

打孔向量不能包含任何匹配 `[0 0]` 的 [1:0] 子向量。

#### 依赖关系

要启用此端口，请将 **Puncture vector source** 设置为 `Property`。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速模式和快速加速模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2018b 中引入**

## 描述

用于准备解码的逆向打孔方案

Depuncturer 模块根据输入打孔向量的指示，用中性值替换打孔符号。该模块返回擦除位，这些位指示输出数据流中中性符号的存在。该模块支持连续和帧操作模式。它提供适用于 HDL 代码生成和硬件部署的接口和架构。

许多无线通信标准通过以基础码率 1/2 进行打孔的模式来实现不同的码率。该模块的输入是一次一个样本的流。您可以提供由硬判决二进制值或软判决对数似然比 (LLR) 表示的样本。该模块以 2×1 向量形式返回输出样本。

插入的中性值取决于输入样本的数据类型。有关详细信息，请参阅输入 **data** 端口。
