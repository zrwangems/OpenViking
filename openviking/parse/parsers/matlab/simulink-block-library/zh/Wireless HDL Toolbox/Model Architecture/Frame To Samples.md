---
type: simulink-block
title: 'Frame To Samples'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Model Architecture'
documentation_page: 'frametosamples'
documentation_source_path: 'ref/frametosamples.html'
language: zh-CN
chinese_source: worker-translation
---

# Frame To Samples

## 端口

### 输入

### **frame** — 输入样本的帧列向量

输入样本的帧，指定为列向量。向量中的所有样本都被视为有效。每个帧必须具有相同大小。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
### 输出

### **sample** — 输出样本流 标量 | 向量

输出样本流，每次返回 **Output size** 个值。输出流包含由 **Idle cycles between samples** 和 **Idle cycles between frames** 指定的空闲样本。每个输出样本在 **ctrl** 端口上都有对应的一组控制信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，这些信号指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

## 参数

### **Idle cycles between samples** — 每个样本后要插入的空闲周期数 `0`（默认）| integer

每个样本后要插入的空闲周期数，指定为标量整数。对于每个空闲周期，模块返回一个由 **Output size** 个零组成的向量，并将所有控制信号设置为 0（`false`）。

### **Idle cycles between frames** — 每帧末尾要插入的空闲周期数 `0`（默认）| integer

每帧末尾要插入的空闲周期数，指定为标量整数。对于每个空闲周期，模块返回一个由 **Output size** 个零组成的向量，并将所有控制信号设置为 0（`false`）。

### **Output size** — 表示每个样本的值数量 `1`（默认）| positive integer

表示每个样本的值数量，指定为正整数标量。模块输出一个由 **Output size** 个值组成的向量。每个向量都有一组对应的控制信号。例如，您可以使用此参数序列化 turbo 编码样本。在 LTE 标准中，turbo 码率为 1/3，因此每个样本由一个系统值和两个校验值表示：*S\_n*、*P1\_n* 和 *P2\_n*。在这种情况下，将 **Output size** 设置为 `3`。

### **Compose output from interleaved input samples** — 输出样本相对于输入顺序的顺序 off（默认）| on

当多个值表示每个样本时，输出样本相对于输入顺序的顺序。例如，对于 1/3 turbo 编码样本，输入帧可以排序为 `[S_1 P1_1 P2_1 S_2 P1_2 P2_2]` 或 `[S_1 S_2 P1_1 P1_2 P2_1 P2_2]`。在第一种情况下，输出是两个向量：`[S_1 P1_1 P2_1]` 和 `[S_2 P1_2 P2_2]`。要在第二种情况下获得相同的输出，请选择 **Compose output from interleaved input samples**。

#### 依赖关系

当 **Output size** 大于 1 时，此参数适用。

## 所属库

Wireless HDL Toolbox / I/O Interfaces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

## 版本历史

**在 R2017b 中引入**

## 描述

将基于帧的数据转换为样本流

Frame To Samples 模块将基于帧的输入展平为样本流。该模块还返回对应的控制信号流，用于指示样本有效性和帧边界。您可以配置样本之间或帧之间插入的空闲周期，以及表示每个样本的值数量。有关流格式的详细信息，请参阅 Streaming Sample Interface。

使用此模块为面向 HDL 代码生成的子系统生成输入。此模块不支持 HDL 代码生成。
