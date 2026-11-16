---
type: simulink-block
title: 'Convert 1-D to 2-D'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2023b
official_category: 'Signal Management'
documentation_page: 'convert1dto2d'
documentation_source_path: '../dsp/ref/convert1dto2d.html'
language: zh-CN
chinese_source: worker-translation
---

# Convert 1-D to 2-D

## 端口

### 输入

### **Port\_1** — 输入信号向量 | 矩阵

输入信号，指定为 1-D 向量或 2-D 矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号矩阵

输出信号，以 2-D 矩阵形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **Number of output rows** — 输出矩阵中的行数 `1`（默认）| 正整数

输出矩阵中的行数 *Mo*，指定为正整数。

### **Number of output columns** — 输出矩阵中的列数 `1`（默认）| 正整数

输出矩阵中的列数 *No*，指定为正整数。

### **Frame-based output** — 启用基于帧的输出的选项 `off`（默认）| `on`

选择此参数以创建基于帧的输出。

## 所属库

DSP System Toolbox / Signal Management / Signal Attributes DSP System Toolbox HDL Support / Signal Management

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有直通实现。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持对复信号进行代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

### R2023b：Convert 1-D to 2-D 模块将被移除

Convert 1-D to 2-D 模块将在未来版本中移除。请改用 Reshape (Simulink) 模块。当该模块被移除时，此模块的现有实例将自动替换为 Reshape 模块。

## 描述

（将被移除）将 1-D 或 2-D 输入重塑为具有指定维度的 2-D 矩阵

Convert 1-D to 2-D 模块将长度为 *Mi* 的 1-D 向量或 *Mi*-by-*Ni* 矩阵重塑为 *Mo*-by-*No* 矩阵，其中 *Mo* 由 **Number of output rows** 参数指定，*No* 由 **Number of output columns** 参数指定。

    y = reshape(u,Mo,No)					% Equivalent MATLAB code

输入按 *按列* 重塑，如下面两种情况所示。长度为 6 的向量和 2-by-3 矩阵都被重塑为相同的 3-by-2 输出矩阵。

Convert 1-D to 2-D 模块将长度为 6 的 1-D 向量和 2-by-3 矩阵重塑为 3-by-2 输出矩阵。

当 (*Mo*\**No*)≠(*Mi*\**Ni*) 时会生成错误。换句话说，输入元素的总数必须在输出中保持不变。

当您选中 **Frame-based output** 复选框时，输出基于帧；否则，输出基于样本。
