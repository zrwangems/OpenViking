---
type: simulink-block
title: 'To VCD File'
family: 'for-use-with-amd-vivado-simulator'
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

### 输入

### **Port\_1, Port\_2, ..., Port\_N** — 要记录到 VCD 文件的信号 scalar | vector | matrix

多维信号会在 VCD 文件中展平为 1-D 向量。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`

## 参数

### **VCD file name** — 生成的 VCD 文件的名称 string

生成的 VCD 文件的名称。如果仅指定文件名，Simulink 会将文件放在当前 MATLAB® 文件夹中。要将生成的文件放在其他位置，请指定完整路径名。如果为多个 To VCD File 模块指定相同名称，Simulink 会自动添加数字后缀以唯一标识每个实例。

**注意**

要使用 `.vcd` 文件扩展名保存生成的文件，必须显式指定它。

### **Number of input ports** — 要记录数据的输入信号数量 integer

要记录数据的输入信号数量。该模块最多可记录 1000 个信号，其中每个信号映射到 VCD 文件中的唯一符号。要支持超过 1000 个信号，请实例化多个 To VCD File 模块。

在某些情况下，单个输入端口会映射到多个符号。当输入端口接收多维信号时会发生这种多重映射。由于 VCD 规范不包含多维信号，Simulink 会在文件中将它们展平为 1-D 向量。

### **Timescale** — Simulink 与 HDL simulator 之间的时序关系 integer and time units

时序关系，定义为 Simulink 时间的 1 秒与 HDL simulator 时间的某个量之间的对应关系。您可以通过以下方式之一表示这个 HDL simulator 时间量：

- 以*相对*项表示，即 HDL simulator 的若干个 tick。在这种情况下，协同仿真在*相对时序模式*下运行，这是时序模式的默认值。

  要使用相对模式，请在 **1 second in Simulink corresponds to {value} {unit} in the HDL simulator** 参数中，将 unit 设置为 `Tick`，并将 value 设置为所需的 tick 数。默认值为 1 tick。
- 以*绝对*单位表示，例如 milliseconds 或 nanoseconds。在这种情况下，协同仿真在*绝对时序模式*下运行。

  要使用绝对模式，请在 **1 second in Simulink corresponds to {value} {unit} in the HDL simulator** 参数中，设置分辨率单位的数量以及单位类型（`fs`、`ps`、`ns`、`us`、`ms`、`s`）。然后，在 **1 HDL Tick is defined as** 参数中，将 HDL simulator tick 的值设置为 `1`、`10` 或 `100`，并选择分辨率单位。

## 所属库

HDL Verifier / For Use with AMD Vivado Simulator HDL Verifier / For Use with Cadence Xcelium HDL Verifier / For Use with Siemens ModelSim/Questa HDL Verifier / For Use with Synopsys VCS

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

此模块可用于生成 HDL 代码的子系统中的仿真可见性，但不包含在硬件实现中。

## 版本历史

**在 R2008a 中引入**

### R2024b：增加了对 VCS simulator 的支持

将此模块添加到 Simulink testbench，以在 Synopsys® VCS® 协同仿真中生成 VCD 文件。

## 描述

生成 value change dump (VCD) 文件

To VCD File 模块生成一个 VCD 文件，用于记录其输入端口的更改。您可以在设计验证期间通过以下方式使用 VCD 文件：

- 使用相同或不同的 simulator 环境比较多次仿真运行的结果。
- 为仿真后分析工具提供输入。
- 将现有设计的某些部分移植到新设计。

您可以指定以下参数：

- 生成的 VCD 文件的名称
- 模块输入端口数
- Timescale，用于将 Simulink® 采样时间与 HDL simulator ticks 关联

对于大型设计或仿真运行时间长的小型设计，VCD 文件可能会变得很大。生成的 VCD 文件中支持的最大信号数为 1000。

您可以在以 normal、accelerator 或 rapid accelerator 仿真模式运行的模型中使用 To VCD File 模块。在任何仿真模式中，To VCD File 参数均不可调。有关这些模式的详细信息，请参阅 How Acceleration Modes Work (Simulink)。

To VCD File 模块集成在 Simulink Viewers and Generators Manager 中。使用该 manager 将 VCD 模块添加到模型时，VCD 文件中出现的信号名可能不是您指定的信号名。仿真后，打开 VCD 文件并检查信号名。如果找不到您指定的信号名，请查找自动信号名，例如 *`In_1`*。当您直接从 HDL Verifier™ 库中使用 VCD 模块时，信号名会正确匹配。

### VCD 文件格式

生成的 VCD 文件的格式遵循 IEEE® Std 1364-2001。下表描述了该格式。

| VCD 文件内容 | 描述 |
| --- | --- |
| ``` $date 23-Sep-2003 14:38:11 $end ``` | 生成文件的日期和时间。 |
| ``` $version HDL Verifier version 1.0 $ end ``` | 生成该文件的 To VCD File 模块的版本。 |
| ``` $timescale 1 ns $ end ``` | 仿真期间使用的 Timescale。 |
| ``` $scope module manchestermodel $end ``` | 正在转储的模块的作用域。 |
| ``` $var wire 1 ! Original Data [0] $end $var wire 1 " Recovered Clock [0] $end $var wire 1 # Recovered Data [0] $end $var wire 1 $ Data Validity [0] $end ``` | 变量定义。每个定义将信号与一个字符标识代码（symbol）关联。这些 symbol 派生自 ASCII 字符集中从 `!` 到 `~` 的可打印字符。变量定义还包括变量类型（wire）和以位为单位的大小。 |
| ``` $upscope $end ``` | 标记 HDL 设计层次结构中转到上一级的更改。 |
| ``` $enddefinitions $end ``` | 标记 header 和 definitions 部分的结束。 |
| ``` #0 ``` | 仿真开始时间。 |
| ``` $dumpvars  0!  0"  0#  0$ $end ``` | 列出时间 0 时所有已定义变量的值。 |
| ``` #630  1! ``` | 记录值变化的起始点，这些变化来自在每个仿真时间增量处对变量值的检查。此条目表示在 63 nanoseconds 时，信号 `Original Data` 的值从 0 变为 1。 |
| ``` . . . #1160  1#  1$ ``` | 在 116 nanoseconds 时，信号 `Recovered Data` 和 `Data Validity` 的值从 0 变为 1。 |
| ``` $dumpoff  x!  x"  x#  x$ $end ``` | 通过将所有变量的值转储为值 `x` 来标记文件结束。 |

### 显示 VCD 文件数据

您可以以图形方式显示 VCD 文件数据，或使用后处理工具分析数据。例如，ModelSim™ `vcd2wlf` 工具将 VCD 文件转换为 `WLF` 文件，您可以在 ModelSim **wave** 窗口中查看该文件。后处理的其他示例包括提取与设计层次结构的特定部分相关的数据，或提取在特定时间间隔内生成的数据。
