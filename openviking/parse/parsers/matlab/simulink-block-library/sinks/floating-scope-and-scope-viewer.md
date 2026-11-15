---
type: simulink-block
title: 'Floating Scope and Scope Viewer'
family: sinks
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'scopeviewer'
---

# Floating Scope and Scope Viewer

Display signals generated during simulation without signal lines

## 中文

显示仿真过程中生成的信号，无信号线

### 所属库

Simulink / Sinks HDL Coder / Sinks

### 描述

Simulink® 波形查看器和 Floating Scope 模块基于仿真时间显示时域信号。波形查看器和 Floating Scope 模块的功能与 Scope 模块相同，但它们不连接信号线。

**“示波器”选项卡**

此屏幕截图突出显示示波器窗口的重要方面。

**示波器画面支持：**

- 仿真控制 - 从“范围”窗口中使用**运行**、**步进**和**步退**工具栏按钮可以运行和调试模型。
- 多个信号 - 在同一显示画面上绘制多个信号。
- 多个显示画面 - 在多个子图上显示信号。子图的所有 *y* 轴在 *x* 轴上具有共同的时间范围。使用工具条的**示波器**选项卡中的**显示网格**参数控制子图的布局。
- 修改参数 - 在仿真之前和仿真期间修改波形参数值。
- 自动缩放轴范围 - 在仿真期间或仿真结束时自动缩放轴范围。在坐标区的顶部和底部会留有边距。
- 仿真后显示数据 - 仿真期间保存波形数据。如果在仿真开始时波形视图关闭，则当您在仿真后打开波形视图时，波形视图将显示附加的输入信号的仿真结果。

  **注意**

  如果采样率高或仿真时间长，可能会遇到内存或系统性能问题，因为示波器在内部保存数据。要限制为波形可视化保存的数据量，请使用 `Limit data points to last` 属性。
- 示波器窗口管理 - 使用新示波器容器将多个示波器窗口停靠到单个窗口中，并管理和组织示波器。示波器容器还使您能够在单个窗口中查看模型中的所有示波器。

**“测量”选项卡**

此屏幕截图突出显示测量窗口的重要方面。

以下是波形查看器和 Floating Scope 模块支持的所有测量列表：

- 触发器 - 对重复信号设置触发器并在发生指定事件时暂停显示。
- 游标测量 - 使用垂直游标和水平游标测量信号值。
- 信号统计 - 显示所选信号的最大值、最小值、峰间差、均值、中位数和 RMS 值。

  **注意**

  您必须拥有 Simscape™ 或 DSP System Toolbox™ 许可证，才能使用峰值查找器、双电平测量和信号统计这些功能面板。
- 峰值查找器 - 查找最大值，显示出现最大值时的 *x* 轴值。
- 双电平测量 - 测量过渡过程、过冲、下冲和循环。

您必须拥有 Simscape 或 DSP System Toolbox 许可证，才能使用峰值查找器、双电平测量和信号统计这些功能面板。

有关从命令行控制 Floating Scope 模块的信息，请参阅以编程方式控制 Scope 模块。

#### 连接信号

在 Floating Scope 窗口或波形查看器窗口中，使用  按钮连接信号。

要添加具有连接信号的查看器，请在模型中选择一个信号。然后，在**仿真**选项卡的**准备**库中，点击**添加查看器**。

有关详细信息，请参阅将信号添加到现有浮动示波器或波形查看器。

#### 主要功能

- 多个 *y* 轴（显示画面）- 显示多个 *y* 轴。所有 *y* 轴在 *x* 轴上具有共同的时间范围。
- 多个信号 - 在同一 *y* 轴（显示画面）上显示多个信号。
- 修改参数 - 在仿真之前和仿真期间修改波形参数值。
- 在仿真后显示数据 - 如果在仿真开始时关闭了示波器，仿真期间波形数据依然会写入波形视图。如果您在仿真后打开该示波器，波形视图将显示输入信号的仿真结果。

### 端口

#### 输入

#### **Port\_1** — 要可视化的信号 标量 | 向量 | 矩阵 | 数组 | 总线 | 非虚拟总线

连接要可视化的信号。您最多可以有 96 个输入端口。输入信号可以具有以下特性：

- **类型** - 连续（基于采样）或离散（基于采样和基于帧）。
- **数据类型** - Simulink 支持的任何数据类型。请参阅 Simulink 支持的数据类型。

  此模块接受定点输入，但将其转换为 `double` 进行显示。
- **维度** - 标量、一维（向量）、二维（矩阵）或多维（数组）。根据维度在一个信号中显示多个通道。请参阅信号维度和确定信号维度。

##### 输入限制

- 当输入是常量信号时，示波器绘制单个点。
- 当信号值为 `NaN` 时，示波器会在显示画面上显示缺口。
- 当您在示波器内可视化多个基于帧的信号时，部分帧大小为 1 的信号采样可能不会显示。要可视化这些信号，请将帧大小为 1 的信号转移到单独的示波器。

##### 总线支持

可将非虚拟总线和总线信号数组连接到示波器。要显示总线信号，请使用普通或加速仿真模式。示波器按照元素在总线中出现的顺序从上到下显示每个总线元素信号。嵌套的总线元素被展平。

要使用示波器记录非虚拟总线信号，请将**保存格式**参数设置为**数据集**。您可以使用任何**保存格式**记录虚拟总线信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**复数支持:** 是

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

此模块可用于在对要生成代码的系统进行仿真时查看仿真情况，但生成的代码中不会包含此模块。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包括在硬件实现中。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

此模块可用于在对要生成代码的系统进行仿真时查看仿真情况，但生成的代码中不会包含此模块。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块接受定点输入，但将其转换为双精度值进行显示。

### 版本历史记录

**在 R2015b 中推出**

#### R2025a: 改进的示波器和新示波器容器可将所有示波器停靠在后一个窗口中

Simulink Scope、Time Scope (DSP System Toolbox) 和 Floating Scope and Scope Viewer 模块在 Simulink 中具有新用户界面，可用于访问示波器的设置和测量。现在示波器响应更灵敏，性能有所提升。使用新示波器容器将多个示波器窗口停靠到单个窗口中，并管理和组织示波器。示波器容器还使您能够在单个窗口中查看模型中的所有示波器。

Scope、Time Scope 和 Floating Scope and Scope Viewer 模块的主要改进包括：

- 简化的用户界面：可从新示波器工具条的**示波器**选项卡轻松访问所有常规示波器设置，并从**测量**选项卡访问所有测量设置。
- 新示波器容器：单一窗口，为模型中的所有示波器显示画面提供统一视图，使您能够在一个位置集中管理和组织多个示波器。
- 更新后的设置面板：更新后的面板合并了示波器的所有常规和样式设置。要打开该面板，请在工具条的**示波器**选项卡中点击**设置**。

#### R2025a: 浮点信号选择功能已删除

Floating Scope 模块中的浮动信号选择功能 (Lock button used to enable the selection of multiple signals) 已删除。要将信号连接到您的浮动示波器，请改用现有信号选择器 (signal selector icon on floating scope)。有关详细信息，请参阅将 Floating Scope 模块添加到模型和连接信号。

#### R2025a: 将示波器停靠到 MATLAB 桌面的功能已删除

将 Simulink Scope、Time Scope (DSP System Toolbox) 和 Floating Scope and Scope Viewer 停靠到 MATLAB 桌面的功能已删除。请改用新示波器容器。有关详细信息，请参阅示波器窗口管理。

如果您在 R2024b 或更早版本中创建的模型包含四个或更多打开的示波器，并且在 R2025a 中打开该模型，则打开的示波器会自动停靠在示波器容器窗口中。

## Libraries

Simulink / Sinks HDL Coder / Sinks

## Description

The Simulink® Scope Viewer and Floating Scope block display time domain
signals with respect to simulation time. The Scope Viewer and Floating
Scope block have the same functionality as the Scope block, but they are not connected
to signal lines.

**Scope Tab**

This screenshot highlights the important aspects of the scope window.

**Scope display features:**

- Simulation control — Run and debug models from a Scope window using
  **Run**, **Step Forward**, and
  **Step Backward** toolbar buttons.
- Multiple signals — Plot multiple signals on the same display.
- Multiple displays — Display signals on multiple subplots. All the
  *y*-axes of the subplots have a common time range on
  the *x*-axis. Control the layout of the subplots using
  the **Display Grid** parameter in the
  **Scope** tab of the toolstrip.
- Modify parameters — Modify scope parameter values before and during a
  simulation.
- Axis autoscaling — Autoscale axes during or at the end of a simulation.
  Margins are drawn at the top and bottom of the axes.
- Display data after simulation — Scope data is saved during a simulation.
  If a scope is closed at the start of a simulation, when you open the scope
  after a simulation, the scope displays simulation results for attached input signals.

  **Note**

  If you have a high sample rate or long simulation time, you may
  run into issues with memory or system performance because the scope
  saves data internally. To limit the amount of data saved for scope
  visualization, use the `Limit data points to
  last` property.
- Scope window management –– Use the new scope container to dock multiple
  scope windows into a single window and to manage and organize the scopes.
  The scope container also enables you to view all the scopes in the model in
  a single window.

**Measurements Tab**

This screenshot highlights the important aspects of the measurements window.

Here is a list of all the measurements the Scope Viewer and
Floating Scope block supports:

- Triggers — Set triggers on repeating signals and pause the
  display when events occur.
- Cursor
  Measurements — Measure signal values using vertical and
  horizontal cursors.
- Signal
  Statistics — Display the maximum, minimum, peak-to-peak
  difference, mean, median, and RMS values of a selected signal.

  **Note**

  You must have a Simscape™ or DSP System Toolbox™ license to use the Peak Finder, Bilevel Measurements, and
  Signal Statistics.
- Peak
  Finder — Find maxima, showing the *x*-axis
  values at which they occur.
- Bilevel
  Measurements — Measure transitions, overshoots, undershoots, and
  cycles.

You must have a Simscape or DSP System Toolbox license to use the Peak Finder, Bilevel Measurements, and Signal
Statistics.

For information on controlling a Floating Scope block from the command
line, see Control Scope Blocks Programmatically.

### Connect Signals

In the Floating Scope window or Scope viewer window, use the  button to connect signals.

To add a viewer with a connected signal, select a signal in the model. Then, on
the **Simulation** tab, in the **Prepare**
gallery, click **Add Viewer**.

For more details, see Add Signals to Existing Floating Scope or Scope Viewer.

### Key Features

- Multiple *y*-axes (displays) — Display multiple
  *y*-axes. All the *y*-axes have a
  common time range on the *x*-axis.
- Multiple signals — Show multiple signals on the same
  *y*-axis (display).
- Modify parameters — Modify scope parameter values before and during
  a simulation.
- Display data after simulation — If a scope is closed at the start
  of a simulation, scope data is still written to the scope during the
  simulation. If you open the scope after a simulation, the scope displays
  simulation results for input signals.

## Ports

### Input

### **Port\_1** — Signal or signals to visualize scalar | vector | matrix | array | bus | nonvirtual bus

Connect the signals you want to visualize. You can have up to 96 input ports. Input signals can have
these characteristics:

- **Type** — Continuous (sample-based) or discrete (sample-based and
  frame-based).
- **Data type** — Any data type that Simulink supports. See Data Types Supported by Simulink.

  This block accepts fixed-point input, but converts it to
  `double` for display.
- **Dimension** — Scalar, one
  dimensional (vector), two dimensional (matrix), or multidimensional
  (array). Display multiple channels within one signal depending on
  the dimension. See Signal Dimensions and Determine Signal Dimensions.

#### Input Limitations

- When the input is a constant signal, the scope plots a single
  point.
- The scope shows gaps in the display when the signal value is
  `NaN`.
- When you visualize multiple frame-based signals in the scope,
  some samples of signals with a frame size of 1 might not be
  displayed. To visualize these signals, move the signals with
  frame size of 1 to a separate scope.

#### Bus Support

You can connect nonvirtual bus and arrays of bus signals to a scope.
To display the bus signals, use normal or accelerator simulation mode.
The scope displays each bus element signal in the order the elements
appear in the bus, from the top to the bottom. Nested bus elements are
flattened.

To log nonvirtual bus signals with a scope, set the **Save
format** parameter to `Dataset`.
You can use any **Save format** to log virtual bus
signals.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

This block can be used for simulation visibility
in subsystems that generate HDL code, but is not included in the hardware
implementation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

This block accepts fixed-point input, but converts it to double for
display.

## Version History

**Introduced in R2015b**

### R2025a: Improved Scope and new scope container to dock all scopes in one window

The Simulink
Scope, Time Scope (DSP System Toolbox), and Floating Scope and Scope Viewer blocks in Simulink have a new user interface that you can use to access settings and measurements
of the scope. The scope is now more responsive and its performance is improved. Use the new
scope container to dock multiple scope windows into a single window and to manage and
organize the scopes. The scope container also enables you to view all the scopes in the
model in a single window.

Key improvements to the Scope, Time Scope, and
Floating Scope and Scope Viewer blocks are:

- Streamlined user interface: Easy access to all the general scope settings from
  the **Scope** tab and all the measurement settings from the
  **Measurements** tab of the new scope toolstrip.
- New scope container: A single window providing a unified view for all the
  scope displays in the model, enabling you to manage and organize multiple scopes
  in one place.
- Updated settings panel: Updated panel consolidates all general and style
  settings of the scope. To open the panel, click **Settings** in
  the **Scope** tab of the toolstrip.

### R2025a: Floating Signal Selection has been removed

The floating signal selection feature (Lock button used to enable the selection of multiple signals) in the Floating Scope block has been
removed. To connect signals to your floating scope, use the existing signal selector (signal selector icon on floating scope) instead. For more details, see Add Floating Scope Block to Model and Connect Signals.

### R2025a: Ability to dock Scopes to MATLAB desktop has been removed

The ability to dock the Simulink
Scope, Time Scope (DSP System Toolbox), and Floating Scope and Scope Viewer to the MATLAB desktop has been removed. Use the new scope container instead. For more
information, see Scope Window Management.

If you have a model created in R2024b or a previous release with four or more open scopes,
and you open that model in R2025a, the opened scopes automatically dock in the scope
container window.
