---
type: simulink-block
title: 'CIC Interpolator'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'cicinterpolator'
documentation_source_path: 'ref/cicinterpolator.html'
language: zh-CN
chinese_source: worker-translation
---

# CIC Interpolator

## 端口

### 输入

### **data** — 输入数据 标量 | 列向量

输入数据，指定为标量或长度为 1 到 64 的列向量。
输入数据必须是有符号整数或有符号定点数，字长小于或等于 32。

在处理输入数据时，该模块实现舍入方法
`Floor` 和溢出动作 `Wrap`。有关更
多详细信息，请参阅舍入模式和溢出处理。

**数据类型：** `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输入数据 标量

控制信号，指示输入数据是否有效。当
**valid** 为 `1`（`true`）时，
模块从输入 **data** 端口捕获值。当
**valid** 为 `0`（`false`）时，
模块忽略输入 **data** 端口的值。

**数据类型：** `Boolean`

### **R** — 可变插值率 标量

使用此端口在运行
时动态指定可变插值率。

此值必须具有数据类型 `fixdt(0,12,0)`，并且必须是
范围从 1 到 **Interpolation factor (Rmax)**
参数值的整数。

#### 依赖关系

要启用此端口，请在 **Main** 选项卡上，将
**Interpolation factor source** 参数设置为 `Input
port`。

**数据类型：** `fixdt(0,12,0)`

### **reset** — 清除内部状态 标量

控制信号，用于清除内部状态。当 **reset** 为
`1`（`true`）时，模块停止当前
计算并清除内部状态。当 **reset** 为
`0`（`false`）且输入
**valid** 为 `1`（`true`）时，
模块捕获数据以进行处理。

有关更多复位注意事项，请参阅硬件控制信号页面中的复位信号部分。

#### 依赖关系

要启用此端口，请在 **Control Ports** 选项卡上，选中
**Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — CIC 插值输出数据 标量 | 列向量

CIC 插值输出数据，返回为标量或长度为 1 到 64 的
列向量。您可以通过在 **Data
Types** 选项卡上设置 **Output data type** 参数来定义此输出的数据类型。

**数据类型：** `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

控制信号，指示来自输出
**data** 端口的数据是否有效。当 **valid** 为
`1`（`true`）时，模块从输出 **data**
端口返回有效数据。当 **valid** 为
`0`（`false`）时，输出
**data** 端口的值无效。

**数据类型：** `Boolean`

### **ready** — 指示模块已准备好接收新的输入数据 标量

控制信号，指示模块已准备好在下个周期接收新的输入数据样本。当 **ready** 为 `1`
（`true`）时，您可以为下个时间步指定 **data**
和 **valid** 输入。当
**ready** 为 `0`
（`false`）时，模块在下个时间步忽略任何输入数据。

**数据类型：** `Boolean`

## 参数

### 主要参数

### **Interpolation factor source** — 插值因子的来源 `Property`（默认） | `Input port`

选择模块以固定还是可变插值
率运行。

- `Property` — 使用从 **Interpolation factor (R)** 参数指定的固定插值率。
- `Input port` — 使用从 **R** 输入端口指定的可变插值
  率。

**注意**

该模块不支持以下两种输入和输出组合的可变插值：

- 标量输入和向量输出
- 向量输入和向量输出

### **Interpolation factor (R)** — 插值因子 `2`（默认） | 从 1 到 2048 的整数

指定模块对输入进行插值的插值因子率。
此值必须是整数。可用值的范围取决于输入和输出数据的类型。

| 输入数据 | 输出数据 | Interpolation factor (R) 有效值 |
| --- | --- | --- |
| 标量 | 标量 | 从 1 到 2048 的整数 |
| 标量 | 向量 | 从 1 到 64 的整数 |
| 向量 | 向量 | 从 1 到 64 的整数 |

**注意**

对于向量输入，请选择插值因子率和输入向量长度，
使其乘积值不超过 64。

#### 依赖关系

要启用此参数，请将 **Interpolation factor
source** 参数设置为 `Property`。

### **Interpolation factor (Rmax)** — 可变插值因子的上界 `2`（默认） | 从 1 到 2048 的整数

指定 **R** 输入端口有效值范围的上界。

**注意**

该模块不支持以下两种输入和输出组合的可变插值：

- 标量输入和向量输出
- 向量输入和向量输出

#### 依赖关系

要启用此参数，请将 **Interpolation factor
source** 参数设置为 `Input port`。

### **Differential delay (M)** — 差分延迟 `1`（默认） | `2`

指定模块梳状部分的差分延迟。

### **Number of sections (N)** — 积分器和梳状部分的数量 `2`（默认） | `1` | `3` | `4` | `5` | `6`

指定模块梳状部分或积分器部分的数量。

### **Minimum number of cycles between valid input samples** — 有效输入样本之间的最小周期数 `1`（默认） | *R* 的因子或倍数

根据输入和输出数据的类型，将有效输入样本之间的最小周期数指定为
`1`、*R* 的因子或 *R* 的倍数，其中
*R* 是插值因子。

| 输入数据 | 输出数据 | 有效输入样本之间的最小周期数 |
| --- | --- | --- |
| 标量 | 标量 | 大于或等于 *R* |
| 标量 | 向量 | 小于 R 的因子 |
| 向量 | 向量 | 1 |

#### 依赖关系

要启用此参数，请将 **Interpolation factor
source** 参数设置为 `Property`。

### **Gain correction** — 输出增益补偿 `off`（默认） | `on`

选择此参数以补偿模块的输出增益。

模块的延迟取决于输入类型、您指定的插值、
部分数量以及此参数的值。有关模块延迟的更多
信息，请参阅延迟。

### 数据类型

### **Output data type** — 输出的数据类型 `Full precision`（默认） | `Same word length as input` | `Minimum section word lengths`

选择输出数据的数据类型。

- `Full precision` — 输出数据类型的字长等于输入字长加上增益位。
- `Same word length as input` — 输出数据
  类型的字长等于输入字长。
- `Minimum section word lengths` — 输出
  数据类型使用您在 **Output word
  length** 参数中指定的字长。

### **Output word length** — 输出的字长 `16`（默认） | 从 2 到 104 的整数

将输出的字长指定为从 2 到 104 的整数。

#### 依赖关系

要启用此参数，请将 **Output data type**
参数设置为 `Minimum section word lengths`。

### Control Ports

### **Enable reset input port** — 启用复位输入端口的选项 `off`（默认） | `on`

选择此参数以启用 **reset** 输入端口。复位
信号实现数据路径寄存器的本地同步复位。

有关更多复位注意事项，请参阅提示。

### **Use HDL global reset** — 将数据路径寄存器连接到生成的 HDL 全局复位信号的选项 `off`（默认） | `on`

选择此参数以将生成的 HDL 全局复位信号连接到数据
路径寄存器。此参数不会改变模块的外观或修改 Simulink 中的仿真行为。当您清除此参数时，生成的 HDL 全局复位仅清除
控制路径寄存器。生成的 HDL 全局复位可以是同步或
异步的，具体取决于模型配置参数中的 **HDL Code Generation** > **Global Settings** > **Reset type** 参数。

有关更多复位注意事项，请参阅提示。

## 所属库

DSP HDL Toolbox / Filtering

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和
综合逻辑的附加配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2022a 中引入**

## 描述

使用 CIC 滤波器对信号进行插值

CIC Interpolator 模块使用级联积分梳状（CIC）插值滤波器对输入信号进行插值。CIC 插值滤波器是一类线性
相位有限脉冲响应（FIR）滤波器，由梳状部分和积分器部分组成。
CIC 插值滤波器结构由 *N* 个级联
梳状滤波器部分、速率变化因子 *R* 和 *N* 个
级联积分器组成。有关 CIC 插值滤波器的更多信息，请参阅算法。

该模块支持以下输入和输出数据组合。

- 标量输入和标量输出 — 支持固定和可变插值
  率
- 标量输入和向量输出 — 仅支持固定插值率
- 向量输入和向量输出 — 仅支持固定插值率

该模块提供适用于 HDL 代码生成和硬件
部署的架构。

**注意**

您还可以使用 DSP HDL IP Designer 应用为该硬件优化算法生成 HDL 代码，而无需创建
Simulink® 模型。该应用
提供与 Simulink 模块相同的接口和配置选项。
