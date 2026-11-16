---
type: simulink-block
title: 'Samples To Frame'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Model Architecture'
documentation_page: 'samplestoframe'
documentation_source_path: 'ref/samplestoframe.html'
language: zh-CN
chinese_source: worker-translation
---

# Samples To Frame

## 端口

### 输入

### **sample** — 样本流 标量 | 向量

样本流，指定为标量或向量。向量输入值表示单个样本，例如由一个系统值和两个校验值表示的 turbo 编码样本。该流可以包括样本之间和帧之间的空闲周期。空闲样本会被丢弃。`double` 和 `single` 支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界以及样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关详细信息，请参阅样本控制总线。

**数据类型：** `bus`

### 输出

### **frame** — 输出样本的帧 列向量

输出样本的帧，以列向量形式返回。每个帧的大小相同。如果输入帧小于 **输出大小**，则该模块用零填充帧。如果输出帧大于 **输出大小**，则该模块使用前 **输出大小** 个样本形成帧。您可以选择在 **len** 端口上输出每个帧中有效样本的数量。

### **valid** — 输出帧的有效性 标量

输出帧的有效性，以 `Boolean` 标量形式返回。当 **frame** 和 **len**（可选）端口上的值有效时，此端口返回 `1`（`true`）。

**数据类型：** `Boolean`

### **len** — 输出帧中有效样本的数量 整数

输出帧中有效样本的数量，以整数形式返回。输入样本流可以具有不同大小的帧。该模块在 **frame** 端口上返回恒定大小的向量；当输入帧小于 **输出大小** 时，用零填充。**len** 端口指示输出帧中有多少个有效样本。如果输出帧大于 **输出大小**，则该模块使用前 **输出大小** 个样本形成帧。

**数据类型：** `double`

## 参数

### **输入大小** — 表示每个样本的值的数量 1（默认）| 正整数

表示每个样本的值的数量，指定为正整数标量。该模块接受包含 **输入大小** 个值的向量。每个向量都有一组对应的控制信号。例如，您可以对此参数使用 turbo 编码样本。在 LTE 标准中，turbo 码率为 1/3，因此每个样本由一个系统值和两个校验值表示：*S\_n*、*P1\_n* 和 *P2\_n*。在这种情况下，将 **输入大小** 设置为 `3`。

### **帧搜索窗口** — 要缓冲的输入周期数量 1（默认）| 正整数

在尝试形成输出帧之前要缓冲的输入周期数量，指定为整数。此参数越大，模块仿真速度越快。但是，该模块从每个搜索窗口中最多返回一个帧。如果此窗口中能容纳多个帧，则该模块返回找到的第一个帧，并丢弃后面的帧。默认设置 1 cycle 从不会丢弃帧，但会导致仿真速度变慢。因此，最佳做法是：将此参数设置为每帧的最小周期数，包括空闲周期。

例如，计算表示每个帧的有效周期和空闲周期。每个周期可能包含多个样本，具体取决于您的 **输入大小**（*samplesize*）设置。

```
% Exact setting: includes idle cycles
totalframesize = ((framesamples/samplesize)*...
    (idlecyclesbetweensamples+1))+idlecyclesbetweenframes;
```

如果帧和样本间距可变或未知，则保守的折中方案是将 **帧搜索窗口** 设置为每帧的最小有效周期数。例如，对于 turbo 编码器模块，输出帧大小取决于编码速率 1/*R* 以及 LTE 标准规定的尾比特。输出数据每个周期有 *R* 个样本。此计算不包括样本之间或帧之间的任何空闲周期。

```
% Conservative setting: number of valid output cycles, without idles
encoderrate = 3;
numtailbits = 12;
framesize = (framesamples+numtailbits)/encoderrate;
```

### **输出大小** — 每帧最大样本数 1024（默认）| 正整数

每帧最大样本数，指定为整数。输入样本流可以具有不同大小的帧。该模块返回恒定大小的向量；如果帧小于 **输出大小**，则用零填充。如果该模块接收到大于 **输出大小** 的帧，则会截断该帧。

### **从交错输入样本组合输出** — 输出样本相对于输入顺序的顺序 off（默认）| on

当多个值表示每个样本时，输出样本相对于输入顺序的顺序。例如，1/3 turbo 编码样本由 `[S_1 P1_1 P2_1]` 和 `[S_2 P1_2 P2_2]` 表示。默认输出顺序为 `[S_1 P1_1 P2_1 S_2 P1_2 P2_2]`。要将样本重新排序，使系统值和校验值分组在一起，请选择 **从交错输入样本组合输出**。输出顺序则为 `[S_1 S_2 P1_1 P1_2 P2_1 P2_2]`。

### **启用帧长度输出端口** — 输出有效样本的数量 off（默认）| on

启用帧长度输出端口。选择此选项可返回每个输出帧中有效样本的数量。长度在 **len** 端口上返回，并由 **valid** 信号限定。当样本流具有可变大小帧，或者下游模块需要将帧大小作为输入（例如 LTE Turbo Decoder）时，请使用此选项。

## 所属库

Wireless HDL Toolbox / I/O Interfaces

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink® 加速模式和快速加速模式以及 DPI 组件生成的 C/C++ 代码生成。

## 版本历史

**在 R2017b 中引入**

## 描述

将样本流转换为基于帧的数据

Samples To Frame 模块从样本流及其对应控制信号重建基于帧的数据。它会从数据中移除任何空闲或无效样本。有关流式格式的详细信息，请参阅流式样本接口。

使用此模块处理面向 HDL 代码生成的子系统的输出。此模块不支持 HDL 代码生成。
