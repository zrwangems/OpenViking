---
type: simulink-block
title: 'CIC Interpolation'
family: 'filtering'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Filtering / Multirate Filters'
documentation_page: 'cicinterpolation'
documentation_source_path: '../dsp/ref/cicinterpolation.html'
language: zh-CN
chinese_source: worker-translation
---

# CIC Interpolation

## 端口

### 输入

### **Port\_1** — 输入信号向量 | 矩阵

将数据输入指定为向量或矩阵。

如果输入是定点，它必须是有符号整数或具有二的幂斜率且零偏置的有符号定点值。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

### 输出

### **Port\_1** — CIC 插值输出向量 | 矩阵

CIC 插值输出，以向量或矩阵形式返回。输出的数据类型由模块对话框中的设置确定。输出的复数性与输入匹配。输出行数为 *R*✕*Num*，其中 *R* 是插值因子，*Num* 是输入行数。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`
**复数支持：** Yes

## 参数

### **系数源** — 滤波器信息来源 `Dialog parameters` （默认） | `Filter object`

滤波器信息来源，指定为以下项之一：

- `Dialog parameters` — 在模块对话框中输入有关滤波器的信息，例如 **插值因子 (R)**、**差分延迟 (M)** 和 **节数 (N)**。
- `Filter object` — 使用 `dsp.CICInterpolator` System object™ 指定滤波器。

### **插值因子 (R)** — 插值因子 `2` （默认） | 整数

滤波器的插值因子，指定为大于 1 的整数。

#### 依赖关系

当您将 **系数源** 设置为 `Dialog parameters` 时，此参数出现。

### **差分延迟 (M)** — 差分延迟 `1` （默认） | 正整数

将滤波器梳状部分的差分延迟 *M* 指定为正整数。有关详细信息，请参阅 CIC Interpolation Filter。

#### 依赖关系

当您将 **系数源** 设置为 `Dialog parameters` 时，此参数出现。

### **节数 (N)** — 滤波器节数 `2` （默认） | 正整数

指定滤波器节数。您指定的数字确定滤波器梳状部分或积分器部分中的节数。此值不表示梳状部分和积分器部分合计的总节数。

#### 依赖关系

当您将 **系数源** 设置为 `Dialog parameters` 时，此参数出现。

### **数据类型指定模式** — 指定滤波器节和输出的字长与小数长度 `Full precision` （默认） | `Minimum section word lengths` | `Specify word lengths` | `Binary point scaling`

选择如何指定滤波器节和/或输出的定点字长与小数长度：

- `Full precision` — 系统会自动为您选择滤波器节和输出的字长与小数长度。输出和最后一个节的字长 (WL) 设置为：

  WL=ceil(log2((RM)NR))+I

  其中，

  - *I* –– 输入字长
  - *M* –– 差分延迟
  - *N* –– 节数
  - *R* –– 插值因子

  其他节的字长设置为适应位增长，如 Hogenauer 的论文 [1] 中所述。所有小数长度都设置为输入小数长度。
- `Minimum section word lengths` — 在 **输出字长** 参数中指定滤波器输出的字长。滤波器节的字长以与 `Full precision` 模式相同的方式设置。

  节小数长度设置为输入小数长度。输出小数长度设置为输入小数长度减去最后一个节字长与输出字长之间的差。
- `Specify word lengths` — 在 **节字长** 和 **输出字长** 参数中指定滤波器节和输出的字长。滤波器节的小数长度设置为使字长与小数长度之间的差值与全精度模式中相同。输出小数长度设置为输入小数长度减去最后一个节字长与输出字长之间的差。
- `Binary point scaling` — 在 **节字长**、**节小数长度**、**输出字长** 和 **输出小数长度** 参数中指定滤波器节和输出的字长与小数长度。

#### 依赖关系

当您将 **系数源** 设置为 `Dialog parameters`，并将 **数据类型指定模式** 设置为 `Specify word lengths` 或 `Binary point scaling` 时，此参数出现。

### **节字长** — 滤波器节的字长 [`16 16 16 16`] （默认） | 标量 | 行向量

滤波器节的字长，指定为标量或长度等于 2*N* 的向量，其中 *N* 是滤波器节数。节字长必须在范围 [2, 128] 内。

#### 依赖关系

当您将 **系数源** 设置为 `Dialog parameters`，并将 **数据类型指定模式** 设置为 `Specify word lengths` 或 `Binary point scaling` 时，此参数出现。

### **节小数长度** — 滤波器节的小数长度 `0` （默认） | 整数

滤波器节的小数长度，指定为整数。

#### 依赖关系

当您将 **系数源** 设置为 `Dialog parameters`，并将 **数据类型指定模式** 设置为 `Binary point scaling` 时，此参数出现。

### **输出字长** — 滤波器输出的字长 `32` （默认） | 整数

滤波器输出的字长，指定为范围 [2, 128] 内的整数。

#### 依赖关系

当您将 **系数源** 设置为 `Dialog parameters`，并将 **数据类型指定模式** 设置为除 `Full precision` 之外的任何选项时，此参数出现。

### **输出小数长度** — 滤波器输出的小数长度 `0` （默认） | 整数

滤波器输出的小数长度，指定为整数。

#### 依赖关系

当您将 **系数源** 设置为 `Dialog parameters`，并将 **数据类型指定模式** 设置为 `Binary point scaling` 时，此参数出现。

### **输入处理** — 处理输入的方法 `Columns as channels (frame based)` （默认） | `Elements as channels (sample based)`

指定模块应如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)` — 模块将输入的每一列视为单独通道。在此模式下，模块始终执行单速率处理。
- `Elements as channels (sample based)` — 模块将输入的每个元素视为单独通道。在此模式下，模块的输入必须是标量或向量。您可以使用 **速率选项** 参数指定模块执行单速率处理还是多速率处理。

### **速率选项** — 速率处理规则 `Enforce single-rate processing` （默认） | `Allow multirate processing`

指定模块的速率处理规则。您可以选择以下选项之一：

- `Enforce single-rate processing` — 模块保持输入的采样率。
- `Allow multirate processing` — 模块生成的输出采样率比输入采样率快 *R* 倍。要选择此选项，您必须将 **输入处理** 参数设置为 `Elements as channels (sample based)`。

### **滤波器对象** — 多速率滤波器对象 `dsp.CICInterpolator System object`

指定您希望模块实现的多速率滤波器对象的名称。您必须将滤波器指定为 `dsp.CICInterpolator` System object。

您可以在模块对话框中或 MATLAB® 工作区变量中定义 System object。

有关创建 System object 的信息，请参阅 Define Basic System Objects。

#### 依赖关系

当您将 **系数源** 设置为 `Filter object` 时，此参数出现。

### **查看滤波器响应** — 查看滤波器响应按钮

此按钮从 Signal Processing Toolbox™ 产品中打开滤波器可视化工具 (FVTool)，并显示模块中定义的滤波器的滤波器响应。有关 FVTool 的详细信息，请参阅 Signal Processing Toolbox 文档。

**注意**

如果您在 **滤波器对象** 参数中指定滤波器，则必须在使用 **查看滤波器响应** 按钮之前，单击 **应用** 按钮来应用滤波器。

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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供会影响 HDL 实现和综合逻辑的附加配置选项。

**注意**

对于具有硬件友好控制信号的 HDL 优化滤波器架构，请使用 CIC Interpolator (DSP HDL Toolbox) 模块。DSP HDL Toolbox™ 模块在 Simulink® 中模拟 HDL 算法的延迟。

**HDL 架构**

该模块默认架构为 `HDLDataPath`。此架构提供会影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 模块属性**

| HDL 模块属性 | 描述 |
| --- | --- |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **AddPipelineRegisters** | 在滤波器的计算级之间插入流水线寄存器。另请参阅 AddPipelineRegisters (HDL Coder)。 |

**数据类型支持**

该模块支持以下数据类型用于 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 枚举 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量 | Yes | Half  Single  Double | Yes | No | Yes | Yes | Yes |

**模块参数配置**

这些模块参数配置与 HDL 代码生成不兼容。

| 模块参数 | 限制 |
| --- | --- |
| **速率选项** | 不支持参数值 `Enforce single-rate processing`。 |
| **输入处理** | 不支持参数值 `Columns as channels (frame based)`。 |

**优化**

该模块参与以下 HDL 优化，以优化速度和面积。

**面积优化**

| 优化 | 描述 |
| --- | --- |
| 资源共享 (HDL Coder) | *资源共享* 是一种面积优化，其中 HDL Coder 识别多个功能等效的资源，并将它们替换为单个资源。 |
| 流式处理 (HDL Coder) | *流式处理* 是一种面积优化，其中 HDL Coder 将向量数据路径转换为标量数据路径（或转换为若干较小规模的向量数据路径）。 |

**速度优化**

| 优化 | 描述 |
| --- | --- |
| 分布式流水线 (HDL Coder) | *分布式流水线*（或寄存器重定时）是一种速度优化，它在保持功能行为的同时移动设计中的现有延迟，以减少关键路径。 |
| 时钟速率流水线 (HDL Coder) | *时钟速率流水线* 是 HDL Coder 中的一种优化框架，它允许其他速度和面积优化在时钟速率下引入延迟。 |
| 自适应流水线 (HDL Coder) | *自适应流水线* 优化通过向设计中的模块插入流水线寄存器，创建带寄存器的模式或模块组合，从而可提高可实现的时钟频率并减少 FPGA 板上的面积使用量。 |
| 关键路径估计 (HDL Coder) | 要快速识别设计中最可能的关键路径，请使用 *关键路径估计*。关键路径估计可加速查找关键路径的迭代过程。要了解在关键路径估计中表征的模块，请参阅 Characterized Blocks (HDL Coder)。 |

**限制和注意事项**

- HDL 代码生成不支持向量和帧输入。

当您使用 **AddPipelineRegisters** 时，寄存器根据滤波器结构放置。流水线寄存器放置位置决定延迟。

| 流水线寄存器放置 | 延迟（时钟周期） |
| --- | --- |
| 在微分器的梳状级之间添加一个流水线寄存器。 | `NS-1`，其中 `NS` 是节数（在输出侧）。 |

## 版本历史

**在 R2006a 之前引入**

## 描述

使用级联积分梳状滤波器对信号进行插值

CIC Interpolation 模块按整数因子对输入信号执行采样率增加（插值）。级联积分梳状 (CIC) 滤波器是一类线性相位 FIR 滤波器，由梳状部分和积分器部分组成。

CIC Interpolation 模块需要 Fixed-Point Designer™ 许可证。
