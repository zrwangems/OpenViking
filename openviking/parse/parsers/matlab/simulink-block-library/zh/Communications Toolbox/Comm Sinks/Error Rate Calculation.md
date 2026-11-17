---
type: simulink-block
title: 'Error Rate Calculation'
family: 'communications-toolbox-hdl-support'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sinks'
documentation_page: 'errorratecalculation'
documentation_source_path: 'ref/errorratecalculation.html'
language: zh-CN
chinese_source: worker-translation
---

# Error Rate Calculation

## 端口

### 输入

### **Tx** — 发送数据 标量 | 列向量

发送数据，指定为标量或列向量。输入信号 **Tx** 和 **Rx** 必须具有相同的数据类型。

- 如果将 **Tx** 或 **Rx** 输入指定为标量，则该模块将此值与另一个输入的所有元素进行比较。
- 如果将 **Tx** 和 **Rx** 输入指定为向量，则它们必须具有相同的大小。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Rx** — 接收数据 标量 | 列向量

接收数据，指定为标量或列向量。输入信号 **Rx** 和 **Tx** 必须具有相同的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Sel** — 样本索引 正整数 | 正整数的列向量

比较数据时要考虑的样本索引，指定为正整数或正整数的列向量。

#### 依赖关系

要启用此输入，请将 **Computation mode** 参数设置为 `Select samples from input port`。

**数据类型：** `double`

### **Rst** — 复位错误计数 标量

复位错误计数，指定为标量。

#### 依赖关系

要启用此输入，请将 **Reset port** 参数设置为 `on`。

**数据类型：** `double` | `Boolean`
### 输出

### **Out** — 发送数据与接收数据之间的差值 列向量

发送数据与接收数据之间的差值，以 `[R; N; S]` 形式的列向量返回，其中：

- *R* 是误码率。
- *N* 是错误数。
- *S* 是比较的样本数。

#### 依赖关系

要启用此端口，请将 **Output data** 参数设置为 `Port`。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Receive delay** — 接收信号延迟 `0`（默认）| 非负整数

接收数据滞后于发送数据的样本数，指定为非负整数。使用此参数可对齐发送和接收输入数据向量中用于比较的样本。

### **Computation delay** — 计算延迟 `0`（默认）| 非负标量

对象在比较开始时忽略的数据样本数，指定为非负整数。使用此参数可忽略两个输入信号的瞬态行为。

### **Computation mode** — 要考虑的样本 `Entire frame`（默认）| `Select samples from mask` | `Select samples from port`

要考虑的样本，指定为以下值之一。

- `Entire frame` — 将接收数据的所有样本与发送帧的样本进行比较。
- `Select samples from mask` — 在 **Selected samples from frame** 参数中设置进行比较时要考虑的样本索引。
- `Select samples from port` — 在 **Sel** 输入端口中设置进行比较时要考虑的样本索引。

### **Selected samples from frame** — 样本索引 `[]`（默认）| 正整数 | 正整数的列向量

比较数据时要考虑的样本索引，指定为正整数或正整数的列向量。默认值为空向量，表示该模块使用接收帧中的所有样本。

#### 依赖关系

要启用此参数，请将 **Computation mode** 参数设置为 `Select samples from mask`。

### **Output data** — 输出数据位置 `Workspace`（默认）| `Port`

输出数据位置，指定为以下选项之一。

- `Workspace` — 将输出数据发送到由 **Variable name** 参数定义的工作区变量。
- `Port` — 向模块添加输出数据端口，并将输出数据发送到该端口。

### **Variable name** — 输出数据变量名 `ErrorVec`（默认）| 字符向量 | 字符串标量

MATLAB® 工作区中的输出数据变量名。

#### 依赖关系

要启用此参数，请将 **Output data** 变量设置为 `Workspace`。

### **Reset port** — 添加 `Rst` 输入端口的选项 `off`（默认）| `on`

启用 `Rst` 输入端口。

### **Stop simulation** — 在指定错误数或比较次数后停止仿真的选项 `off`（默认）| `on`

在该模块检测到 **Target number of errors** 参数中指定的错误数或执行了 **Maximum number of symbols** 参数中指定的比较次数后停止仿真的选项。

### **Target number of errors** — 在指定错误数后停止仿真的选项 `100`（默认）| 正整数

检测到该数量的错误后停止仿真的选项，指定为正整数。

#### 依赖关系

要启用此参数，请将 **Stop simulation** 参数设置为 `on`。

### **Maximum number of symbols** — 在比较指定数量的符号后停止仿真的选项 `1e6`（默认）| 正整数

比较该数量的符号后停止仿真的选项，指定为正整数。

**注意**

如果使用 Simulink Coder™ 快速仿真（RSim）目标构建 RSim 可执行文件，则可以在不重新编译模型的情况下调整 **Target number of errors** 和 **Maximum number of symbols** 参数。这对于蒙特卡洛仿真非常有用，在此类仿真中，您需要以不同的噪声量多次运行仿真（可能在多台计算机上）。

#### 依赖关系

要启用此参数，请将 **Stop simulation** 参数设置为 `on`。

## 所属库

Communications Toolbox / Comm Sinks Communications Toolbox HDL Support / Comm Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当将 **Output data** 参数设置为 `Workspace` 时，该模块不生成代码。同样，如果将 **Simulation mode** 参数设置为 `Accelerator` 或 `Rapid Accelerator`，则不会将数据保存到工作区。如果在这些情况下需要误码率信息，请将 **Output data** 参数设置为 `Port`。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算输入数据的误码率或符号错误率

Error Rate Calculation 模块将来自发送器的输入数据与来自接收器的输入数据进行比较。该模块通过将一个来源的输入数据元素中不相等数据对的总数除以输入数据元素的总数，将错误率作为运行统计量进行计算。

您可以使用此模块计算符号或误码率，因为它不考虑输入数据元素之间差值的大小。如果输入是比特，则该模块计算误码率。如果输入是符号，则该模块计算符号错误率。

此图显示了启用所有端口的模块。启用所有端口的 Error Rate Calculation 模块。
