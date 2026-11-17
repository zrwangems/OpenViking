---
type: simulink-block
title: 'Triggered To Workspace'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'triggeredtoworkspace'
documentation_source_path: 'ref/triggeredtoworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# Triggered To Workspace

## 端口

### 输入

### **Input** — 要记录到工作区的数据 标量 | 向量 | 矩阵 | 总线

指定当模块在 **Trigger** 端口接收到触发时要记录到工作区的数据。Triggered To Workspace 模块支持记录任意内置数据类型或用户定义数据类型（如总线、枚举和定点数据）的实数和复数数据。

#### 提示

记录定点数据需要 Fixed-Point Designer™ 许可证。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `string` | `fixed point` | `enumerated` | `bus` | `image`
**复数支持：** 是

### **Trigger** — 触发信号 标量 | 向量 | 矩阵

指定控制模块执行的触发信号，可以是标量、向量或矩阵。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **Trigger type** — 触发类型 `Rising edge`（默认）| `Falling edge` | `Either edge`

触发模块执行的事件类型。

每当模块被输入 2 处的控制信号触发时，模块从输入 1 获取并缓冲一帧数据。在其他所有时间，模块忽略输入 1。您可以使用 **Trigger type** 参数指定输入 2 处的触发事件：

- `Rising edge` 在触发输入从负值上升到零或正值，或从零上升到正值时触发模块执行。
- `Falling edge` 在触发输入从正值下降到零或负值，或从零下降到负值时触发模块执行。
- `Either edge` 在 `Rising edge` 或 `Falling edge` 时触发模块执行。

### **Variable name** — 工作区变量名称 `yout`（默认）| 字符向量 | 字符串

用于存储数据的工作区变量名称。默认情况下，Triggered To Workspace 模块将记录的数据保存在名为 `yout` 的变量中。当模型包含多个 Triggered To Workspace 模块时，您必须在每个模块的 **Variable name** 参数中指定唯一的值。

### **Decimation** — 抽取因子 `1`（默认）| 标量

指定抽取因子以降低记录数据的有效采样率。对于抽取因子 *D*，Triggered To Workspace 模块记录每第 *D* 个样本的值。例如，当您将 **Decimation** 值指定为 `2` 时，Triggered To Workspace 模块记录每隔一个数据点。

有关在仿真期间控制模块记录哪些样本的详细信息，请参阅 Specify Signal Values to Log (Simulink)。

### **Maximum number of rows** — 要保存的最大行数 `1000`（默认）| 正整数

指定模块保存的最大行数（每个时间步一行）（*P*），为正整数。

### **Save 2-D signals as** — 记录数据中二维样本值的排列方式 `2-D array (concatenate along first dimension)`（默认）| `3-D array (concatenate along third dimension)`

指定模块将二维信号保存为 MATLAB 工作区中的二维数组还是三维数组。

当您选择：

- `2-D array (concatenate along first
  dimension)` — 模块将每个 *M*×*N* 矩阵输入与先前的输入垂直串联，生成二维输出数组。模块将数据保存为 *P*×*N* 矩阵，其中 *P* 是 **Maximum number of rows** 参数的值。

  当仿真运行足够长的时间使模块获取超过 *P* 个样本时，模块仅存储最近的 *P* 个样本。**Decimation factor** *D* 允许您仅存储每第 *D* 个输入矩阵。
- `3-D array (concatenate along third
  dimension)` — 模块将 *M*×*N* 输入保存为三维数组，其中每个 *M*×*N* 页表示来自 *M*\**N* 个通道中每个通道的单个样本（最近的输入矩阵占据最后一页）。此三维数组的最大尺寸限制为 *M*×*N*×*P*，其中 *P* 是 **Maximum number of rows** 参数的值。

  当仿真运行足够长的时间使模块获取超过 *P* 个输入时，模块仅存储最后 *P* 个输入。**Decimation factor** *D* 允许您仅存储每第 *D* 个输入矩阵。

### **Log fixed-point data as a fi object** — 将定点数据记录为 `fi` 对象 `off`（默认）| `on`

指定如何记录定点输入数据。默认情况下，Triggered To Workspace 模块将定点输入数据记录为 `double`。当您选择此参数时，Triggered To Workspace 模块将定点输入记录为 Fixed-Point Designer `fi` (Fixed-Point Designer) 对象。

使用 Triggered To Workspace 模块记录定点数据需要 Fixed-Point Designer 许可证。

## 所属库

DSP System Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2006a 之前引入**

## 描述

触发时将输入样本写入 MATLAB 工作区

Triggered To Workspace 模块在 MATLAB® 工作区中创建一个矩阵或数组变量，并在仿真结束时将获取的输入存储在其中。该模块会覆盖同名的现有变量。

要保存每个样本值对应采样时间的记录，请打开配置参数对话框。要打开配置参数，请在 Simulink® 模型工具条的 **Modeling** 选项卡中，点击 **Model Settings**。在打开的窗口左窗格中，点击 **Data Import/Export** 并选中 **Time** 复选框。

此模块的非触发版本是 To Workspace (Simulink) 模块。
