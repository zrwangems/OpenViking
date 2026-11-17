---
type: simulink-block
title: 'Floating Scope and Scope Viewer'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'scopeviewer'
documentation_source_path: '../simulink/slref/scopeviewer.html'
language: zh-CN
chinese_source: worker-translation
---

# Floating Scope and Scope Viewer

## 端口
```yaml
ports:
- name: Port_1
  summary: 要可视化的信号 scalar | vector | matrix | array | bus | nonvirtual bus
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus
```

### 输入

### **Port\_1** — 要可视化的信号 scalar | vector | matrix | array | bus | nonvirtual bus

连接要可视化的信号。最多可以有 96 个输入端口。输入信号可以具有以下特征：

- **Type** — 连续（基于采样）或离散（基于采样和基于帧）。
- **Data type** — Simulink 支持的任何数据类型。请参阅 Data Types Supported by Simulink。

  此模块接受定点输入，但会将其转换为 `double` 以进行显示。
- **Dimension** — 标量、一维（向量）、二维（矩阵）或多维（数组）。根据维度在一个信号中显示多个通道。请参阅 Signal Dimensions 和 Determine Signal Dimensions。

#### 输入限制

- 当输入为常量信号时，示波器绘制单个点。
- 当信号值为 `NaN` 时，示波器在显示中显示间隙。
- 当在示波器中可视化多个基于帧的信号时，帧大小为 1 的信号的某些采样可能不会显示。要可视化这些信号，请将帧大小为 1 的信号移到单独的示波器中。

#### 总线支持

可以将非虚拟总线和总线信号数组连接到示波器。要显示总线信号，请使用普通或加速仿真模式。示波器按照元素在总线中出现的顺序从上到下显示每个总线元素信号。嵌套总线元素会被展平。

要使用示波器记录非虚拟总线信号，请将 **Save format** 参数设置为 `Dataset`。可以使用任何 **Save format** 来记录虚拟总线信号。

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink / Sinks HDL Coder / Sinks

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块可用于生成代码的系统中的仿真可视化，但不会包含在生成的代码中。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可视化，但不会包含在硬件实现中。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

此模块可用于生成代码的系统中的仿真可视化，但不会包含在生成的代码中。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块接受定点输入，但会将其转换为 double 以进行显示。

## 版本历史

**在 R2015b 中引入**

### R2025a: 改进的 Scope 和新的示波器容器，可将所有示波器停靠在一个窗口中

Simulink 中的 Scope、Time Scope (DSP System Toolbox) 以及 Floating Scope and Scope Viewer 模块具有新的用户界面，可用于访问示波器的设置和测量。示波器现在响应更快，性能也得到了改进。使用新的示波器容器可将多个示波器窗口停靠到单个窗口中，并管理和组织示波器。示波器容器还使您能够在单个窗口中查看模型中的所有示波器。

Scope、Time Scope 和 Floating Scope and Scope Viewer 模块的主要改进包括：

- 简化的用户界面：可从新示波器工具条的 **Scope** 选项卡轻松访问所有常规示波器设置，并从 **Measurements** 选项卡访问所有测量设置。
- 新的示波器容器：单个窗口为模型中的所有示波器显示提供统一视图，使您能够在一个位置管理和组织多个示波器。
- 更新的设置面板：更新后的面板整合了示波器的所有常规和样式设置。要打开该面板，请单击工具条 **Scope** 选项卡中的 **Settings**。

### R2025a: 浮动信号选择已被移除

Floating Scope 模块中的浮动信号选择功能（用于启用多个信号选择的 Lock 按钮）已被移除。要将信号连接到浮动示波器，请改用现有的信号选择器（浮动示波器上的信号选择器图标）。有关更多详细信息，请参阅 Add Floating Scope Block to Model and Connect Signals。

### R2025a: 将示波器停靠到 MATLAB 桌面的功能已被移除

将 Simulink Scope、Time Scope (DSP System Toolbox) 以及 Floating Scope and Scope Viewer 停靠到 MATLAB 桌面的功能已被移除。请改用新的示波器容器。有关更多信息，请参阅 Scope Window Management。

如果您的模型是在 R2024b 或更早版本中创建的，并且打开了四个或更多示波器，然后在 R2025a 中打开该模型，则已打开的示波器会自动停靠在示波器容器窗口中。

## 描述

显示仿真期间生成的信号，无需信号线

Simulink® Scope Viewer 和 Floating Scope 模块显示相对于仿真时间的时域信号。Scope Viewer 和 Floating Scope 模块具有与 Scope 模块相同的功能，但它们不连接到信号线。

**Scope 选项卡**

此截图突出显示了示波器窗口的重要方面。

**示波器显示功能：**

- 仿真控制 — 使用 **Run**、**Step Forward** 和 **Step Backward** 工具栏按钮从 Scope 窗口运行和调试模型。
- 多个信号 — 在同一显示中绘制多个信号。
- 多个显示 — 在多个子图上显示信号。所有子图的 *y* 轴在 *x* 轴上具有共同的时间范围。使用工具条 **Scope** 选项卡中的 **Display Grid** 参数控制子图的布局。
- 修改参数 — 在仿真之前和期间修改示波器参数值。
- 轴自动缩放 — 在仿真期间或结束时自动缩放轴。边距绘制在轴的顶部和底部。
- 仿真后显示数据 — 示波器数据在仿真期间保存。如果示波器在仿真开始时关闭，当您在仿真后打开示波器时，示波器会显示所连接输入信号的仿真结果。

  **注意**

  如果您的采样率较高或仿真时间较长，可能会遇到内存或系统性能问题，因为示波器会在内部保存数据。要限制为示波器可视化保存的数据量，请使用 `Limit data points to last` 属性。
- 示波器窗口管理 —— 使用新的示波器容器可将多个示波器窗口停靠到单个窗口中，并管理和组织示波器。示波器容器还使您能够在单个窗口中查看模型中的所有示波器。

**Measurements 选项卡**

此截图突出显示了测量窗口的重要方面。

以下是 Scope Viewer 和 Floating Scope 模块支持的所有测量列表：

- Triggers — 在重复信号上设置触发，并在事件发生时暂停显示。
- Cursor Measurements — 使用垂直和水平光标测量信号值。
- Signal Statistics — 显示所选信号的最大值、最小值、峰峰值差、均值、中位数和 RMS 值。

  **注意**

  您必须拥有 Simscape™ 或 DSP System Toolbox™ 许可证才能使用 Peak Finder、Bilevel Measurements 和 Signal Statistics。
- Peak Finder — 查找最大值，显示它们出现的 *x* 轴值。
- Bilevel Measurements — 测量过渡、过冲、下冲和周期。

您必须拥有 Simscape 或 DSP System Toolbox 许可证才能使用 Peak Finder、Bilevel Measurements 和 Signal Statistics。

有关从命令行控制 Floating Scope 模块的信息，请参阅 Control Scope Blocks Programmatically。

### 连接信号

在 Floating Scope 窗口或 Scope viewer 窗口中，使用  按钮连接信号。

要添加带有已连接信号的查看器，请在模型中选择一个信号。然后，在 **Simulation** 选项卡的 **Prepare** 库中，单击 **Add Viewer**。

有关更多详细信息，请参阅 Add Signals to Existing Floating Scope or Scope Viewer。

### 主要功能

- 多个 *y* 轴（显示）— 显示多个 *y* 轴。所有 *y* 轴在 *x* 轴上具有共同的时间范围。
- 多个信号 — 在同一 *y* 轴（显示）上显示多个信号。
- 修改参数 — 在仿真之前和期间修改示波器参数值。
- 仿真后显示数据 — 如果示波器在仿真开始时关闭，示波器数据仍会在仿真期间写入示波器。如果您在仿真后打开示波器，示波器会显示输入信号的仿真结果。
