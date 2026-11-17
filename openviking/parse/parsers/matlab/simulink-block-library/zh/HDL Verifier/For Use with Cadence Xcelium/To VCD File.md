---
type: simulink-block
title: 'To VCD File'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'For Use with AMD Vivado Simulator'
documentation_page: 'tovcdfile'
documentation_source_path: 'ref/tovcdfile.html'
language: zh-CN
chinese_source: worker-translation
---

# To VCD File

## 端口
```yaml
ports:
- name: Port_1, Port_2, ..., Port_N
  summary: 要记录到 VCD 文件的信号 标量 | 向量 | 矩阵
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | Fixed-point
```

### 输入

### **Port\_1, Port\_2, ..., Port\_N** — 要记录到 VCD 文件的信号 标量 | 向量 | 矩阵

多维信号在 VCD 文件中会被展平为一维向量。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`
## 参数
```yaml
parameters:
- name: VCD file name
  summary: 生成的 VCD 文件的名称 字符串
  group: ''
- name: Number of input ports
  summary: 要记录的输入信号数量 整数
  group: ''
- name: Timescale
  summary: Simulink 与 HDL 仿真器之间的时间关系 整数和时间单位
  group: ''
```

### **VCD file name** — 生成的 VCD 文件的名称 字符串

生成的 VCD 文件的名称。如果仅指定文件名，Simulink 会将文件放置在当前 MATLAB® 文件夹中。要将生成的文件放置在其他位置，请指定完整路径名。如果为多个 To VCD File 模块指定相同的名称，Simulink 会自动添加数字后缀以唯一标识每个实例。

**注意**

要使用 `.vcd` 文件扩展名保存生成的文件，必须显式指定该扩展名。

### **Number of input ports** — 要记录的输入信号数量 整数

要记录数据的输入信号数量。该模块最多可记录 1000 个信号，其中每个信号映射到 VCD 文件中的唯一符号。要支持超过 1000 个信号，请实例化多个 To VCD File 模块。

在某些情况下，单个输入端口会映射到多个符号。当输入端口接收多维信号时会发生这种多重映射。由于 VCD 规范不包含多维信号，Simulink 会在文件中将其展平为一维向量。

### **Timescale** — Simulink 与 HDL 仿真器之间的时间关系 整数和时间单位

时间关系，定义为一秒 Simulink 时间与一定数量的 HDL 仿真器时间之间的对应关系。您可以通过以下方式之一表示该 HDL 仿真器时间量：

- 以*相对*方式表示，即表示为一定数量的 HDL 仿真器 tick。在这种情况下，协同仿真以*相对时间模式*运行，这是默认的时间模式。

  要使用相对模式，请在 **1 second in Simulink corresponds to {value} {unit} in the HDL simulator** 参数中，将单位设置为 `Tick`，并将值设置为您想要的 tick 数。默认值为 1 tick。
- 以*绝对*单位表示，例如毫秒或纳秒。在这种情况下，协同仿真以*绝对时间模式*运行。

  要使用绝对模式，请在 **1 second in Simulink corresponds to {value} {unit} in the HDL simulator** 参数中，设置分辨率单位的数量和单位类型（`fs`、`ps`、`ns`、`us`、`ms`、`s`）。然后，在 **1 HDL Tick is defined as** 参数中，将 HDL 仿真器 tick 的值设置为 `1`、`10` 或 `100`，并选择分辨率单位。
## 所属库

HDL Verifier / For Use with AMD Vivado Simulator HDL Verifier / For Use with Cadence Xcelium HDL Verifier / For Use with Siemens ModelSim/Questa HDL Verifier / For Use with Synopsys VCS

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2008a 中引入**

### R2024b：新增对 VCS 仿真器的支持

将此模块添加到 Simulink 测试平台，以在 Synopsys® VCS® 协同仿真中生成 VCD 文件。

## 描述

生成值变更转储 (VCD) 文件

To VCD File 模块生成一个 VCD 文件，用于记录其输入端口的变化。您可以在设计验证期间通过以下方式使用 VCD 文件：

- 使用相同或不同的仿真器环境比较多次仿真运行的结果。
- 为仿真后分析工具提供输入。
- 将现有设计的部分移植到新设计中。

您可以指定以下参数：

- 生成的 VCD 文件的名称
- 模块输入端口数量
- 时间尺度，用于将 Simulink® 采样时间与 HDL 仿真器节拍相关联

对于大型设计或仿真运行时间较长的小型设计，VCD 文件可能会变得很大。生成的 VCD 文件中支持的最大信号数为 1000。

您可以在以普通、加速或快速加速仿真模式运行的模型中使用 To VCD File 模块。To VCD File 参数在任何仿真模式下均不可调。有关这些模式的详细信息，请参阅 How Acceleration Modes Work (Simulink)。

To VCD File 模块已集成到 Simulink Viewers and Generators Manager 中。当您使用该管理器将 VCD 模块添加到模型时，VCD 文件中出现的信号名称可能不是您指定的名称。仿真后，打开 VCD 文件并检查信号名称。如果找不到您指定的信号名称，请查找自动生成的信号名称，例如 *`In_1`*。当您直接从 HDL Verifier™ 库中使用 VCD 模块时，信号名称会正确匹配。

### VCD 文件格式

生成的 VCD 文件格式遵循 IEEE® Std 1364-2001。下表描述了该格式。

| VCD 文件内容 | 描述 |
| --- | --- |
| ``` $date 23-Sep-2003 14:38:11 $end ``` | 文件生成的日期和时间。 |
| ``` $version HDL Verifier version 1.0 $ end ``` | 生成该文件的 To VCD File 模块的版本。 |
| ``` $timescale 1 ns $ end ``` | 仿真期间使用的时间尺度。 |
| ``` $scope module manchestermodel $end ``` | 正在转储的模块范围。 |
| ``` $var wire 1 ! Original Data [0] $end $var wire 1 " Recovered Clock [0] $end $var wire 1 # Recovered Data [0] $end $var wire 1 $ Data Validity [0] $end ``` | 变量定义。每个定义将一个信号与一个字符标识代码（符号）相关联。 这些符号派生自 ASCII 字符集中从 `!` 到 `~` 的可打印字符。 变量定义还包括变量类型 (wire) 和以位为单位的大小。 |
| ``` $upscope $end ``` | 标记向 HDL 设计层次结构中下一更高层级的变更。 |
| ``` $enddefinitions $end ``` | 标记头部和定义部分的结束。 |
| ``` #0 ``` | 仿真开始时间。 |
| ``` $dumpvars  0!  0"  0#  0$ $end ``` | 列出时间 0 时所有已定义变量的值。 |
| ``` #630  1! ``` | 在每个仿真时间增量检查变量值时记录的已记录值变更的起始点。 此条目表示在 63 纳秒时，信号 `Original Data` 的值从 0 变为 1。 |
| ``` . . . #1160  1#  1$ ``` | 在 116 纳秒时，信号 `Recovered Data` 和 `Data Validity` 的值从 0 变为 1。 |
| ``` $dumpoff  x!  x"  x#  x$ $end ``` | 通过将所有变量的值转储为值 `x` 来标记文件的结束。 |

### 显示 VCD 文件数据

您可以以图形方式显示 VCD 文件数据，或使用后处理工具分析数据。例如，ModelSim™ `vcd2wlf` 工具将 VCD 文件转换为 `WLF` 文件，您可以在 ModelSim **wave** 窗口中查看该文件。后处理的其他示例包括提取与设计层次结构的特定部分相关的数据，或在特定时间间隔内生成的数据。
