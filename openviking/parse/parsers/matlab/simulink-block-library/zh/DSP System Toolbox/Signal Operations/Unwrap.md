---
type: simulink-block
title: 'Unwrap'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'unwrap'
documentation_source_path: 'ref/unwrap.html'
language: zh-CN
chinese_source: worker-translation
---

# Unwrap

## 端口
```yaml
ports:
- name: Port_1
  summary: 信号输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double
- name: Port_1
  summary: 信号输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 信号输入 标量 | 向量 | 矩阵

要解包的信号输入，指定为标量、向量或矩阵。输入必须包含弧度相位值。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 信号输出 标量 | 向量 | 矩阵

解包后的信号输出，以标量、向量或矩阵形式返回。

该模块保持输入的大小和维度，输出端口速率等于输入端口速率。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Tolerance (radians)
  summary: 跳变大小 pi（默认）| 标量值
  group: ''
- name: Input processing
  summary: 处理输入的方法 Columns as channels (frame based)（默认）| Elements as channels (sample based)
  group: ''
- name: Reset initial phase to zero for each input frame
  summary: 检查连续帧 off（默认）| on
  group: ''
```

### **Tolerance (radians)** — 跳变大小 `pi`（默认）| 标量值

模块识别为真实相位不连续的跳变大小。默认值设为 *π*（而非更小的值），以避免改变合法的信号特征。要提高模块的灵敏度，请将 **Tolerance** 设置为略小于 π 的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Input processing** — 处理输入的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定模块应如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`
  （默认）— 选择此选项时，模块将输入的每一列视为一个单独的通道。
- `Elements as channels (sample based)`
  — 选择此选项时，模块将输入的每个元素视为一个单独的通道。

### **Reset initial phase to zero for each input frame** — 检查连续帧 `off`（默认）| `on`

当您清除此参数时，模块忽略输入帧之间的边界，并且不会在每次接收到新输入时将初始相位值重置为零。在此模式下，模块连续地对输入每一列中的数据进行解包。

下图说明了当您清除此参数时模块如何对数据进行解包。

当您选择此参数时，模块独立地处理每一帧输入数据，并为每个新的输入帧重置初始相位值。

下图说明了当您选择此参数时模块如何对数据进行解包。

有关详细信息，请参阅基于帧的处理。

#### 依赖关系

要启用此参数，请将 **Input processing** 参数设置为 `Columns as channels (frame based)`。在基于采样的处理模式下，模块不会为每个新输入将初始相位值重置为零。有关详细信息，请参阅基于采样的处理。
## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

解包信号相位

Unwrap 模块通过对每个通道元素加上或减去适当的 2π 倍数来解包输入的每个通道。该模块识别大于 **Tolerance** 参数值的相位不连续。有关相位解包的详细信息，请参阅相位解包的定义。
