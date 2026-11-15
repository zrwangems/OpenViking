---
type: simulink-block
title: 'Puncturer'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Convolutional Coding'
documentation_page: 'puncturer'
documentation_source_path: 'ref/puncturer.html'
language: zh-CN
chinese_source: worker-translation
---

# Puncturer

## 端口

### 输入

### **data** — 输入数据样本 标量 | 大小从 2 到 7 的列向量

输入数据样本，指定为标量或向量。

如果输入为向量类型，则输入数据的大小必须与所选的 **Encoder rate** 参数值匹配。

例如，如果 **Encoder rate** 为 `1/2`，则输入数据大小必须为 2×1。

**数据类型：** `Boolean` | `fixdt(0,1,0)`

### **valid** — 指示有效的输入数据样本 标量

控制信号，指示输入数据是否有效。当该值为 `1`（true）时，模块接受 **data** 输入端口上的值。当该值为 `0`（false）时，模块忽略 **data** 输入端口上的值。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Continuous`。

**数据类型：** `Boolean`

### **puncVector** — 打孔向量 二进制值的列向量

打孔向量，指定为二进制值的列向量。打孔向量的长度必须是 *n* 的整数倍，其中 **Encoder rate** 为 *1/n*。对于编码速率 1/2、1/3、1/5 和 1/6，**puncVector** 的最大长度为 30；对于编码速率 1/4 和 1/7，**puncVector** 的最大长度为 28。

您可以更改 **puncVector** 模式，但其长度必须保持不变。如果提供的最大打孔向量长度为 10，则该模块支持所有小于 10 的向量长度。

**示例：** 对于编码速率 1/2 及其打孔速率 2/3、3/4 和 5/6，相应的向量长度分别为 4、6 和 10。要实现这些多种速率，请将 **Puncture vector source** 参数设置为 `Input port`。为支持最大向量大小，所有速率的向量长度都必须为 10。对于 2/3 和 3/4 速率，请用零填充 **puncVector** 输入以创建 10 元素向量。速率 3/4 的打孔向量为 `[1 1 0 1 1 0]'`。对于长度为 10 的向量，请使用 `[0 0 0 0 1 1 0 1 1 0]'` 作为输入 **puncVector**。

当 **Operation mode** 参数设置为 `Continuous` 时，如果 **syncPunc** 和输入 **valid** 端口信号都为 `1`（true），则该模块捕获 **puncVector** 的值。

当 **Operation mode** 参数设置为 `Frame` 时，如果 `ctrl.start` 和 `ctrl.valid` 信号都为 `1`（true），则该模块捕获 **puncVector** 的值。

#### 依赖关系

要启用此端口，请将 **Puncture vector source** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **syncPunc** — 打孔同步信号 标量

打孔同步信号，指定为 `Boolean` 标量值。此输入是一个控制信号，用于将打孔向量输入与输入样本同步。当 **syncPunc** 和 **valid** 都为 `1`（true）时，模块会对齐打孔向量以开始打孔。模块从 **puncVector** 输入端口或从 **Puncture vector** 参数捕获该向量。

当 **syncPunc** 信号值为 `0`（`false`）时，模块忽略 **puncVector** 信号值。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Continuous`。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` bus

伴随样本流的控制信号，指定为 `samplecontrol` bus。该 bus 包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及输入样本的有效性。

- `start` — 指示输入帧的开始。
- `end` — 指示输入帧的结束。
- `valid` — 指示输入 **data** 端口上的数据有效。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Frame`。在此模式下，模块使用输入 `samplecontrol` bus 中的控制信号来同步打孔向量。

**数据类型：** `bus`

### 输出

### **data** — 打孔后的输出数据 n×1 列向量

打孔后的输出数据，返回为 n×1 列向量，其中 *n* 的取值范围为 1 到 7。

**数据类型：** `Boolean` | `fixdt(0,1,0)`

### **valid** — 输出数据样本的有效性 标量

控制信号，用于指示 **data** 输出端口上的样本何时有效。当输出 **data** 端口上存在有效样本时，模块将 **valid** 端口设置为 `1`（true）。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Continuous`。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` bus

伴随样本流的控制信号，返回为 `samplecontrol` bus。该 bus 包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及样本的有效性。

- `start` — 指示输出帧的开始。
- `end` — 指示输出帧的结束。
- `valid` — 指示输出 **data** 端口上的数据有效。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Frame`。

**数据类型：** `bus`

## 参数

### **Operation mode** — 操作模式 `Continuous`（默认） | `Frame`

操作模式，指定为以下模式之一：

- `Continuous` — 允许随时更改 **puncVector**。要强制模块捕获新的打孔向量，请将 **syncPunc** 参数设置为 `1`（true）。
- `Frame` — 仅允许在帧开始时更改 **puncVector**，由 `ctrl.start` 指示。

### **Encoder rate** — 编码器速率 `1/2`（默认） | 范围从 1/2 到 1/7

选择用于对数据进行打孔的编码器速率。

### **Puncture vector source** — 打孔向量来源 `Input port`（默认） | `Property`

打孔向量来源，指定为：

- `Input port` — 使用 **puncVector** 端口指定打孔向量。
- `Property` — 使用 **Puncture vector** 参数指定打孔向量。

### **Puncture vector** — 要打孔数据的位置 `[1;1;1;0;0;1]`（默认） | 二进制值的列向量

打孔向量的长度必须是 *n* 的整数倍，其中 **Encoder rate** 为 *1/n*。对于编码速率 1/2、1/3、1/5 和 1/6，打孔向量的最大长度为 30；对于编码速率 1/4 和 1/7，打孔向量的最大长度为 28。

#### 依赖关系

要启用此端口，请将 **Puncture vector source** 参数设置为 `Property`。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成
使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

此模块没有任何 HDL Block Properties。

## 版本历史

**在 R2019b 中引入**

## 描述

根据打孔向量对数据进行打孔

Puncturer 模块根据指定的打孔向量对输入数据进行打孔。该模块可以从 `Input port` 或模块的 `Property` 接受打孔向量，并支持 1/2 到 1/7 的编码速率。它提供适用于 HDL 代码生成和硬件部署的架构。

该模块支持 `Continuous` 和 `Frame` 模式操作，并接受标量和向量数据。在 `Continuous` 模式下，模块接受输入数据和打孔向量，以及控制信号 valid 和 syncPunc，并输出带有 valid 信号的打孔数据。在 `Frame` 模式下，模块接受输入数据和打孔向量，以及 `samplecontrol` bus，并输出带有 `samplecontrol` bus 的打孔数据。

该模块支持诸如 Wi-Fi (802.11a/b/g/n/ac)、数字卫星通信、数字视频广播 (DVB)、WiFi (IEEE 802.11a/b/g/n/ac)、WiMax (IEEE 802.16)、IEEE 802.16、HIPERLAN 和 HiperMAN 等通信标准。
