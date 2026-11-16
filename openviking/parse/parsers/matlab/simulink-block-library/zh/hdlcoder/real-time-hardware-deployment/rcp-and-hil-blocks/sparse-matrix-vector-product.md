---
type: simulink-block
title: 'Sparse Matrix-Vector Product'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Real-Time Hardware Deployment / RCP and HIL Blocks'
documentation_page: 'sparsematrixvectorproduct'
documentation_source_path: 'ref/sparsematrixvectorproduct.html'
language: zh-CN
chinese_source: worker-translation
---

# Sparse Matrix-Vector Product

## 端口

### 输入

### **x** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。Sparse Matrix-Vector Product 模块支持定点数据类型。输入端口数量取决于 **矩阵 A** 的维度。例如，请参阅 Model 3-D Matrix-Vector Multiplication。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **y** — 输出信号 标量 | 向量

输出信号，以标量或向量形式返回。输出信号是输入信号乘以由 **矩阵 A** 指定的稀疏矩阵。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主

### **矩阵 A** — 稀疏矩阵 `1`（默认）| 实数标量、向量或矩阵

指定用于乘以输入向量的稀疏矩阵。**矩阵 A** 可以是实数标量、向量或矩阵。

#### 编程用法

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `A` |
| **值：** | `"1"` | 实数标量、向量或矩阵 |

### 信号属性

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| 标量

指定软件检查的输出范围的最小值。

软件使用输出最小值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 仿真范围检查（请参阅 Specify Signal Ranges and Enable Simulation Range Checking）
- 定点数据类型的自动定标

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认）| 标量

指定软件检查的输出范围的最大值。

软件使用输出最大值执行：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 仿真范围检查（请参阅 Specify Signal Ranges and Enable Simulation Range Checking）
- 定点数据类型的自动定标

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出数据类型** — 输出数据类型 `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |

### 参数属性

### **参数最小值** — 稀疏矩阵的最小值 `[]`（默认）| 标量

指定 **矩阵 A** 的最小值。默认值为 `[]`（未指定）。软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParamMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **参数最大值** — 稀疏矩阵的最大值 `[]`（默认）| 标量

指定 **矩阵 A** 的最大值。默认值为 `[]`（未指定）。软件使用此值执行：

- 参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）
- 定点数据类型的自动定标

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParamMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **参数数据类型** — 指定稀疏矩阵的数据类型 `'Inherit: Inherit via back propagation'`（默认）| `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'<data type expression>'`

指定 **矩阵 A** 参数的数据类型。

在使用此 **参数数据类型** 设置调节参数时，请指定 **参数最小值** 和 **参数最大值** 参数。这些设置告知软件仿真期间所需的值范围，并允许软件提供具有足够范围的全精度数据类型，以便在指定范围内安全调节。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ParamDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'Enum: <class name>'` | `'<data type expression>'` |

## 所属库

HDL Coder / RCP and HIL

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合后的逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

默认情况下，以下 HDL 模块属性可用。

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定对于浮点运算符，是否将设计中的模块映射到 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy。 |

| 常规 | |
| --- | --- |
| **SharingFactor** | 指定要映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing。 |

## 版本历史

**在 R2024b 中引入**

## 描述

将稀疏矩阵与输入向量相乘

Sparse Matrix-Vector Product 模块将稀疏矩阵 `A` 与输入向量 `x` 相乘。
