---
type: simulink-block
title: 'CIC Decimation'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'cicdecimation'
documentation_source_path: '../dsp/ref/cicdecimation.html'
language: zh-CN
chinese_source: worker-translation
---

# CIC Decimation

## 端口

### 输入

### **Port\_1** — 输入信号向量 | 矩阵

数据输入，指定为向量或矩阵。输入行数必须是抽取因子的整数倍。

如果输入为 fixed point，则它必须是 signed integer 或具有 2 的幂斜率且零偏置的 signed fixed point 值。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

### 输出

### **Port\_1** — CIC 抽取输出向量 | 矩阵

CIC 抽取输出，以向量或矩阵形式返回。输出的数据类型由模块对话框中的设置决定。输出的复数性与输入匹配。输出行数为
(1/*R*)✕*Num*，其中 *R* 是抽取因子，*Num* 是输入行数。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

## 参数

### **Coefficient source** — 滤波器信息来源 `Dialog parameters`（默认） | `Filter object`

滤波器信息来源，指定为以下之一：

- `Dialog parameters` — 在模块对话框中输入有关滤波器的信息，例如 **Decimation factor (R)**、**Differential delay (M)** 和 **Number of sections (N)**。
- `Filter object` — 使用 `dsp.CICDecimator` System object™ 指定滤波器。

CIC Decimation 模块对话框中显示的项会有所不同，具体取决于您在 **Coefficient source** 参数中选择 `Dialog parameters` 还是 `Filter object`。

### **Decimation factor (R)** — 抽取因子 `2`（默认） | integer

滤波器的抽取因子，指定为大于 1 的 integer。

#### 依赖关系

当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数出现。

### **Differential Delay (M)** — 差分延迟 `1`（默认） | positive integer

将滤波器梳状部分的差分延迟 *M* 指定为 positive integer。有关更多详细信息，请参阅 CIC Decimation Filter。

#### 依赖关系

当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数出现。

### **Number of sections (N)** — 滤波器节数 `2`（默认） | positive integer

指定滤波器节数。您指定的数字决定滤波器梳状部分或积分器部分的节数。此值不表示梳状部分和积分器部分合在一起的总节数。

#### 依赖关系

当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数出现。

### **Data type specification mode** — 指定滤波器节和输出的 fixed-point 字长与小数长度 `Full precision`（默认） | `Minimum section word lengths` | `Specify word lengths` | `Binary point scaling`

选择如何指定滤波器节和/或输出的 fixed-point 字长和小数长度：

- `Full precision` — 自动为您选择滤波器节和输出的字长与小数长度。所有字长 (WL) 设置为：

  WL=ceil(N×log2(M×R))+I

  其中，

  - *I* –– 输入字长
  - *M* –– 差分延迟
  - *N* –– 节数
  - *R* –– 抽取因子

  所有小数长度设置为输入小数长度。
- `Minimum section word lengths` — 在 **Output word length** 参数中指定滤波器输出的字长。模块自动选择滤波器节的字长和所有小数长度，使每个节字长尽可能小。每个滤波器节的精度低于 `Full precision` 模式，但保留每个节的范围。
- `Specify word lengths` — 在 **Section word lengths** 和 **Output word length** 参数中指定滤波器节和输出的字长。模块自动为滤波器节和输出选择小数长度，使得在丢弃最低有效位时保留每个节的范围。
- `Binary point scaling` — 在 **Section word lengths**、**Section fraction lengths**、**Output word length** 和 **Output fraction length** 参数中指定滤波器节和输出的字长与小数长度。

#### 依赖关系

当 **Coefficient source** 设置为 `Dialog parameters` 时，此参数出现。

### **Section word lengths** — 滤波器节的字长 [`16 16 16 16`]（默认） | scalar | row vector

滤波器节的字长，指定为标量或长度等于 2*N* 的向量，其中 *N* 是滤波器节数。节字长必须在 [2, 128] 范围内。

#### 依赖关系

当 **Coefficient source** 设置为 `Dialog parameters`，且 **Data type specification mode** 设置为 `Specify word lengths` 或 `Binary point scaling` 时，此参数出现。

### **Section fraction lengths** — 滤波器节的小数长度 `0`（默认） | integer

滤波器节的小数长度，指定为 integer。

#### 依赖关系

当 **Coefficient source** 设置为 `Dialog parameters`，且 **Data type specification mode** 设置为 `Binary point scaling` 时，此参数出现。

### **Output word length** — 滤波器输出的字长 `32`（默认） | integer

滤波器输出的字长，指定为 [2, 128] 范围内的 integer。

#### 依赖关系

当 **Coefficient source** 设置为 `Dialog parameters`，且 **Data type specification mode** 设置为除 `Full precision` 以外的任何选项时，此参数出现。

### **Output fraction length** — 滤波器输出的小数长度 `0`（默认） | integer

滤波器输出的小数长度，指定为 integer。

#### 依赖关系

当 **Coefficient source** 设置为 `Dialog parameters`，且 **Data type specification mode** 设置为 `Binary point scaling` 时，此参数出现。

### **Rate options** — 速率处理规则 `Enforce single-rate processing`（默认） | `Allow multirate processing`

指定模块的速率处理规则：

- `Enforce single-rate processing` — 模块执行基于帧的处理，并生成与输入具有相同采样率的输出。为了在保持输入采样率的同时对信号进行抽取，模块减小输出帧大小。在此模式下，输入列大小必须是 **Decimation Factor (R)** 的整数倍。
- `Allow multirate processing` — 在此模式下，模块生成采样率比输入采样率慢 `R` 倍的输出。

### **Filter object** — 多速率滤波器对象 `dsp.CICDecimator`

指定希望模块实现的多速率滤波器对象的名称。必须将滤波器指定为 `dsp.CICDecimator` System object。

您可以在模块对话框中或在 MATLAB® 工作区变量中定义 System object。

有关创建 System object 的信息，请参阅 Define Basic System Objects。

#### 依赖关系

当 **Coefficient source** 设置为 `Filter object` 时，此参数出现。

### **View Filter Response** — 查看滤波器响应 `gui button`

此按钮会从 Signal Processing Toolbox™ 产品中打开 Filter Visualization Tool (FVTool)，并显示模块中定义的滤波器的滤波器响应。有关 FVTool 的更多信息，请参阅 Signal Processing Toolbox 文档。

**注意**

如果在 **Filter object** 参数中指定滤波器，则必须先点击 **Apply** 按钮应用滤波器，然后才能使用 **View Filter Response** 按钮。

## 所属库

DSP System Toolbox / Filtering / Multirate Filters DSP System Toolbox HDL Support / Filtering

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `fixed point` | `integer` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖 `memcpy` 或 `memset` 函数 (`string.h`)。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**注意**

对于具有硬件友好控制信号的 HDL 优化滤波器架构，请使用 CIC Decimator (DSP HDL Toolbox) 模块。DSP HDL Toolbox™ 模块在 Simulink® 中模拟 HDL 算法的延迟。

**HDL 架构**

该模块将 `HDLDataPath` 作为默认架构。此架构提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 模块属性**

| HDL 模块属性 | 描述 |
| --- | --- |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **AddPipelineRegisters** | 在滤波器的计算级之间插入一个流水线寄存器。另请参阅 AddPipelineRegisters (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar | Yes | Half  Single  Double | Yes | No | Yes | Yes | Yes |

**模块参数配置**

这些模块参数配置与 HDL 代码生成不兼容。

| 模块参数 | 限制 |
| --- | --- |
| **Rate options** | 不支持参数值 `Enforce single-rate processing`。 |

**优化**

该模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* 是一种面积优化，其中 HDL Coder 识别多个功能等效的资源，并将它们替换为单个资源。 |
| Streaming (HDL Coder) | *Streaming* 是一种面积优化，其中 HDL Coder 将向量数据路径转换为标量数据路径（或转换为多个更小规模的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*（或寄存器重定时）是一种速度优化，它移动设计中的现有延迟以缩短关键路径，同时保持功能行为。 |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* 是 HDL Coder 中的一种优化框架，允许其他速度和面积优化在时钟速率下引入延迟。 |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* 优化通过向设计中的模块插入流水线寄存器，创建带寄存器的模块模式或组合，从而提高可实现的时钟频率并减少 FPGA 板上的面积使用量。 |
| Critical Path Estimation (HDL Coder) | 要快速识别设计中最大可能的关键路径，请使用 *Critical Path Estimation*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中已表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**限制和注意事项**

- HDL 代码生成不支持向量和帧输入。

使用 **AddPipelineRegisters** 时，寄存器会根据滤波器结构放置。流水线寄存器放置位置决定延迟。

| 流水线寄存器放置 | 延迟 (clock cycles) |
| --- | --- |
| 在差分器的梳状级之间添加一个流水线寄存器。 | `NS-1`，其中 `NS` 是节数（在输出侧）。 |

## 版本历史

**在 R2006a 之前引入**

## 描述

使用级联积分梳状滤波器对信号进行抽取

CIC Decimation 模块按整数因子对输入信号执行采样率降低（抽取）。级联积分梳状 (CIC) 滤波器是一类线性相位 FIR 滤波器，由梳状部分和积分器部分组成。

该模块支持实数和复数 fixed-point 输入。在其正常工作模式下，CIC Decimation 模块允许加法器的数值溢出并回绕 [1] [3]。Fixed-Point 基础设施随后会导致命令行上出现溢出警告。此溢出无关紧要。

CIC Decimation 模块需要 Fixed-Point Designer™ 许可证。
