---
type: simulink-block
title: 'HDL Cosimulation'
family: 'hdlverifier'
product_id: 'hdlverifier'
product_name: 'HDL Verifier'
documentation_release: R2025b
official_category: 'For Use with AMD Vivado Simulator'
documentation_page: 'hdlcosimulation'
documentation_source_path: 'ref/hdlcosimulation.html'
language: zh-CN
chinese_source: worker-translation
---

# HDL Cosimulation

## 端口

### 输入

### **HDL\_input\_port\_name** — 从 Simulink 传递到 HDL 仿真器的信号 标量 | 向量

模块上的端口与 HDL 设计上的端口相对应。在 **端口** 选项卡上添加或删除端口。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`
### 输出

### **HDL\_output\_port\_name** — 从 HDL 仿真器传递到 Simulink 的信号 标量 | 向量

模块上的端口与 HDL 设计上的端口相对应。在 **端口** 选项卡上添加或删除端口。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`

## 参数

### **Block Info** — Vivado 协同仿真的模块信息 只读：模块生成设置

此参数为只读。

此部分显示使用协同仿真向导生成此模块后的信息。它显示以下各项：

- HDL Simulator – Vivado 仿真器
- HDL Design Library – HDL 库文件的位置
- HDL Language – VHDL 或 Verilog
- HDL Time Precision – HDL 设计的时间精度
- HDL Waveform File – 波形文件的名称和路径

为 Vivado 仿真器生成协同仿真模块时，无法使用模块封装更改端口、时钟、复位或时间精度的名称和方向。要更改这些项，请打开协同仿真向导并重新生成模块。

#### 依赖项

此参数仅在使用 Vivado 协同仿真时可见。

### 端口

### **Enable direct feedthrough** — 解决代数环警告 `true`（默认）| `false`

消除当模型包含纯组合路径时协同仿真与 Simulink 之间出现的一个输出采样延迟差异。如果 HDL Cosimulation 模块位于反馈环路中并产生代数环警告或错误，请清除此复选框。当您仿真数据路径上带有寄存器的时序电路时，指定直接馈通不会影响该数据路径的时序。

#### 依赖项

### **Full HDL Name** — 信号路径名称 字符串

使用 HDL 仿真器路径名称语法指定信号路径名称。例如，对于 Xcelium HDL 仿真器，使用 `manchester.samp`。该信号可以位于 HDL 设计层次的任何级别。与该信号对应的 HDL Cosimulation 模块端口以此名称标记。

有关在 Simulink 中指定端口和模块路径名称的规则，请参阅 Specify HDL Signal/Port and Module Paths for Simulink Testbench Cosimulation。

您可以直接从 HDL 仿真器 **wave** 窗口复制信号路径名称，并将其粘贴到 **Full HDL Name** 字段中。使用 *`Path.Name`* 视图，而不是 *`Db::Path.Name`* 视图。将信号路径名称粘贴到 **Full HDL Name** 后，点击 **Apply** 以完成粘贴操作并更新信号列表。

#### 依赖项

如果该模块是从协同仿真向导生成的，则不应更改此值。对于 Vivado HDL Cosimulation 模块，该参数为只读。

### **I/O Mode** — 端口方向 `Input` | `Output`

要添加双向端口，请将该端口作为输入和输出两次添加到列表中。

`Input` — Simulink 驱动的 HDL 信号。Simulink 以指定的采样率将值写入指定的 HDL 仿真器信号。

**注意**

当您定义模块输入端口时，请确保只有一个源被设置为驱动该信号的输入。例如，避免定义具有多个实例的输入端口。如果多个源驱动单个信号的输入，您的仿真模型将产生意外结果。

`Output` — Simulink 读取的 HDL 信号。对于输出信号，您必须指定显式采样时间。您也可以指定数据类型，但宽度必须与 HDL 中信号的宽度匹配。有关指定数据类型的详细信息，请参阅 **Data Type** 和 **Fraction Length** 参数。

Simulink 信号没有三态语义，因为不存在 `'Z'` 值。要与双向信号进行接口，请连接到输出驱动器和输入驱动器的输出信号的输入和使能信号。此方法将实际的三态缓冲器保留在 HDL 中，在那里解析函数可以处理与其他三态缓冲器的接口。

#### 依赖关系

如果该模块是由 Cosimulation Wizard 生成的，则不应更改此值。对于 Vivado HDL Cosimulation 模块，该参数为只读。

### **HDL Type** — HDL 端口信号类型 只读：`Logic`（默认）| `Vector`

此参数为只读。

显示 HDL 端口信号的类型，由 Cosimulation Wizard 配置。

#### 依赖关系

仅当该模块为与 Vivado 协同仿真配合使用而生成时，此参数才可见。

### **HDL Dims** — HDL 端口信号维度 只读：标量 | 向量

此参数为只读。

显示 HDL 端口信号的维度，由 Cosimulation Wizard 配置。

#### 依赖关系

仅当该模块为与 Vivado 协同仿真配合使用而生成时，此参数才可见。

### **Sample Time** — 输出端口上读取采样之间的时间 1（默认）| 整数

应用于输出端口的连续采样之间的时间间隔。

Simulink 以此处指定的采样率从关联的 HDL 仿真器信号读取值。

通常，Simulink 按如下方式处理端口采样周期：

- 如果您将输入端口连接到具有显式采样周期的信号，基于前向传播，Simulink 将该速率应用于该端口。
- 如果您将输入端口连接到不具有显式采样周期的信号，Simulink 将分配一个采样周期，该周期等于模型中所有已识别输入端口采样周期的最小公倍数（LCM）。
- 您必须为每个输出端口指定显式采样时间。

与 Simulink 采样时间命中对应的 HDL 时间取决于 **Timescales** 设置。请参阅 Simulation Timescales。

#### 依赖关系

要启用此参数，请将 **I/O Mode** 设置为 `Output`。

### **Data Type** — 输出信号 `Inherit`（默认）| `Fixedpoint` | `Double` | `Single` | `Half` 的 Simulink 数据类型

选择 `Inherit` 以自动确定数据类型。该模块会检查继承的字长是否与从 HDL 仿真器查询到的字长匹配。如果它们不匹配，Simulink 会生成错误消息。例如，如果你将一个 Signal Specification 模块连接到输出，`Inherit` 会强制将 Signal Specification 模块指定的数据类型应用于输出端口。

如果 Simulink 无法确定连接到输出端口的信号的数据类型，它会向 HDL 仿真器查询该端口的数据类型。例如，如果 HDL 仿真器为大小为 `N` 位的信号返回 VHDL® 数据类型 `STD_LOGIC_VECTOR`，则数据类型 `ufixN` 会被强制应用于输出端口。隐式小数长度为 0。

你也可以分配显式数据类型，并可选择 **Fraction Length**。通过显式分配数据类型，你可以将定点数据类型强制应用于 HDL Cosimulation 模块的输出端口。例如，对于一个 8 位输出端口，将 **Sign** 设置为 `Signed` 并将 **Fraction Length** 设置为 `5`，会将数据类型强制为 `sfix8_En5`。你不能强制宽度。宽度始终从 HDL 仿真器继承。

**Data Type** 和 **Fraction Length** 属性仅适用于以下类型的 HDL 信号：

- 任意逻辑类型的 VHDL 信号，例如 `STD_LOGIC` 或 `STD_LOGIC_VECTOR`
- `wire` 或 `reg` 类型的 Verilog® 信号

#### 依赖关系

要启用此参数，请将 **I/O Mode** 设置为 `Output`。

在与 Vivado 仿真器进行协同仿真期间，此参数显示为 **Simulink Data Type**。

### **Sign** — 输出数据类型的符号分量 `Unsigned`（默认）| `Signed`

显式输出端口数据类型的符号指定。

#### 依赖关系

要启用此参数，请将 **I/O Mode** 设置为 `Output`，并将 **Data Type** 设置为 `Fixedpoint`。

### **Fraction Length** — 输出数据类型整数中的小数位数

定点输出信号小数部分的位数。例如，对于一个 8 位输出端口，将 **Sign** 设置为 `Signed` 并将 **Fraction Length** 设置为 `5`，会将数据类型强制为 `sfix8_En5`。你不能强制宽度；宽度始终从 HDL 仿真器继承。

#### 依赖关系

要启用此参数，请将 **I/O Mode** 设置为 `Output`，并将 **Data Type** 属性设置为 `Fixedpoint`。

**Data Type** 和 **Fraction Length** 属性仅适用于以下类型的 HDL 信号：

- 任意逻辑类型的 VHDL 信号，例如 `STD_LOGIC` 或 `STD_LOGIC_VECTOR`
- `wire` 或 `reg` 类型的 Verilog 信号

### **Simulink Word Length** — Simulink 端口整数的位宽 <129 | `inherit`

Simulink 端口的大小，指定为小于 129 的正整数。

**对于输入端口** — 此值设置为 `inherit`（只读）。

当 **HDL Word Length** 参数大于 128 位时，Simulink 端口维度在编译时由驱动信号的数据类型决定。例如：

- 当 **HDL Word Length** = 150 且 **Simulink Word Length** = 50 时，HDL Verifier™ 允许数据宽度为 50 位、维度大小为 3 的 Simulink 端口，例如 `sfix50(3)` 或 `ufix50(3)`。
- 当 **HDL Word Length** = 140 且 **Simulink Word Length** = 50 时，HDL Verifier 将 150 位的 Simulink 打包为 140 位的 HDL。HDL Verifier 忽略最后一个字的 10 个最高有效位（MSB）。

  三个各 50 位的 Simulink 输入字被打包为一个 140 位的 HDL 输入信号。最后一个 Simulink 字的 10 个 MSB 被 HDL 服务器忽略

**对于输出端口** — 有 2 种情况。

- 当 **HDL Word Length** 参数小于 129 位时，此参数与 HDL 端口的宽度匹配，且为只读。
- 当 **HDL Word Length** 参数大于 128 位时，HDL Verifier 创建一个端口向量来表示此端口。例如：

  - 当 **HDL Word Length** = 150 且 **Simulink Word Length** = 50 时，HDL Verifier 创建一个数据宽度为 50 位的 Simulink 端口。例如 `sfix50(3)` 或 `ufix50(3)`。
  - 当 **HDL Word Length** = 150 且 **Simulink Word Length** = 60 时，HDL Verifier 创建一个数据宽度为 60 的 Simulink 端口，例如 `sfix60(3)` 或 `ufix60(3)`。由于 HDL 字只有 150 位，而 Simulink 端口需要 180 位，因此 30 位被填充或符号扩展。
  - 当 **HDL Word Length** = 140 且 **Simulink Word Length** = 50 时，HDL 输出的每 50 位被表示为一个 Simulink 字。最后一个 Simulink 字的 10 个 MSB 未使用，并根据 **Sign** 参数进行扩展。

    140 位的 HDL 输出信号被打包为三个各 50 位的 Simulink 字。最后一个字仅使用 40 位，10 位被扩展

#### 依赖关系

当 **HDL Word Length** 小于 129 时，此参数为只读。

### **HDL Word Length** — HDL 端口的位宽 只读：整数

此参数为只读。

HDL 端口的大小，以位为单位。

**Verilog 或 SystemVerilog 示例**：在下面的代码中，输入 `In1` 的 HDL 字长为 140 位，输出 `Out1` 的 HDL 字长为 160 位。

```
input [1:0][69:0] In1;
output [159:0] Out1;
```

**VHDL 示例**：在下面的代码中，`In1` 的 HDL 字长为 120 位，`In2` 的 HDL 字长为 1200 位。

```
TYPE matrix_of_std_logic_vector120 IS ARRAY (NATURAL RANGE <>, NATURAL RANGE <>) OF std_logic_vector(119 DOWNTO 0);
In1: IN matrix_of_std_logic_vector120(0 TO 4, 0 TO 1);
In2: IN std_logic_vector(1199 DOWNTO 0);
```

### Clocks

**Note**

- 在与 Vivado 仿真器进行协同仿真时，此选项卡名为 **Clocks, Resets, Enables**。
- 在与 VCS 仿真器进行协同仿真时，此选项卡不可用。使用 `launchVCS` 函数的 `PreSimulationTcl` 属性来定义时钟和复位信号。

创建可选的上升沿和下降沿时钟，为您的协同仿真模型施加激励。滚动列表显示驱动 HDL 信号值的 HDL 时钟，使用 deposit 方法对您正在建模的信号进行操作。时钟信号必须是单比特信号。不支持向量信号。有关添加和编辑时钟信号的说明，请参阅 Creating Optional Clocks with the Clocks Pane of the HDL Cosimulation Block。

### **Time to run HDL simulator before cosimulation starts** — 协同仿真开始前运行 HDL 仿真所需的时间 `0`（默认）| 非负整数

指定在开始协同仿真之前运行 HDL 仿真所需的时间。指定一个非负整数，并从菜单中选择时间单位。

- `fs` – 飞秒
- `ps` – 皮秒
- `ns` – 纳秒
- `us` – 微秒
- `ms` – 毫秒
- `s` – 秒

#### 依赖关系

要启用此参数，请为 Vivado 协同仿真生成此模块。

### **Full HDL Name** — 信号路径名称字符串

使用 HDL 仿真器路径名称语法，将每个时钟指定为信号路径名称。例如：`/manchester/clk` 或 `manchester.clk`。

有关 Simulink 中路径规范的信息和要求，请参阅 Specify HDL Signal/Port and Module Paths for Simulink Testbench Cosimulation。

您可以直接从 HDL 仿真器 **wave** 窗口复制信号路径名称，并将其粘贴到 **Full HDL Name** 字段中。请使用 *`Path.Name`* 视图，而不是 *`Db::Path.Name`* 视图。将信号路径名称粘贴到 **Full HDL Name** 后，点击 **Apply** 以完成粘贴操作并更新信号列表。

#### 依赖关系

如果该模块是从 Cosimulation Wizard 生成的，则不应更改此值。对于 Vivado HDL Cosimulation 模块，该参数为只读。

### **Active Clock Edge** — 用于采样信号的 HDL 时钟边沿 `Rising`（默认）| `Falling`

选择以下选项之一。

- `Rising` – 指定上升沿时钟。
- `Falling` – 指定下降沿时钟。

周期和持续时间均为 Simulink 时间。要将 Simulink 时间与 HDL 时间关联，请转到 **Timescales** 选项卡，然后点击 **Determine Timescale Now**。

#### 依赖关系

此参数仅对 ModelSim 或 Xcelium 协同仿真可见。

### **Waveform Type** — 生成用于驱动 HDL 设计的时钟、复位或使能的波形 `Rising`（默认）| `Falling` | `Step 1 to 0` | `Step 0 to 1`

对于 Vivado 协同仿真，选择以下选项之一。

- `Active Rising Edge Clock` – 创建一个占空比为 50% 的周期信号，其上升沿相对于 Simulink 驱动输入的时刻有偏移。
- `Active Falling Edge Clock` – 创建一个占空比为 50% 的周期信号，其下降沿相对于 Simulink 驱动输入的时刻有偏移。
- `Step 0 to 1` – 创建一个阶跃函数，在指定持续时间内先驱动 0，然后转换为 1。
- `Step 1 to 0` – 创建一个阶跃函数，在指定持续时间内先驱动 1，然后转换为 0。

周期和持续时间均为 Simulink 时间。要将 Simulink 时间与 HDL 时间关联，请转到 **Timescales** 选项卡，然后点击 **Show Times and Suggest Timescale**。

#### 依赖关系

此参数仅对 Vivado 协同仿真可见。

### **Period/Duration** — 时钟周期 2（默认）| 整数

要指定显式时钟周期，请输入等于或大于两个分辨率单位（ticks）的采样时间。

如果时钟周期不是偶数整数，Simulink 无法创建 50% 占空比。此时，HDL Verifier 软件会在 `clockperiod/2`（向下取整到最接近的整数）处创建下降沿。

对于 ModelSim 或 Xcelium，周期和持续时间指定为 Simulink 时间；对于 Vivado，它们指定为 HDL 时间。

#### 依赖关系

此属性不适用于与 VCS 的协同仿真。

### 时间尺度

手动或自动选择 Simulink 与 HDL 仿真器之间的时序关系。这些参数指定 Simulink 时间的一秒与 HDL 仿真器时间的某个量之间的对应关系。这个 HDL 仿真器时间的量可以用以下方式之一表示：

- *相对*时序关系（Simulink 秒对应于 HDL 仿真器精度，即
  “tick”。
- *绝对*时序关系（Simulink 秒对应于 HDL 仿真器时间的绝对单位）

有关计算相对和绝对时序模式的更多信息，请参阅 Defining the Simulink and HDL Simulator Timing Relationship。

有关协同仿真期间 Simulink 与 HDL 仿真器之间关系的详细信息，以及相对和绝对时序模式操作的详细信息，请参阅 Simulation Timescales。

要查看所有端口、时钟、复位和使能的 Simulink 时间与 HDL 时间之间的关系，
请点击 **Show Times and Suggest Timescale**。如有需要，此操作还会
自动确定可用的时间尺度。

### **Automatically determine timescale at start of simulation** — 何时计算自动时间尺度 `true`（默认）| `false`

如果选择此选项，HDL Verifier 会在您启动 Simulink 仿真时计算时间尺度。如果未选择此选项，请点击
**Determine Timescale Now** 以立即计算
时间尺度，而无需启动仿真。对于 Vivado 协同仿真，此按钮显示为 **Show Times
and Suggest Timescale**。或者，您也可以手动
选择时间尺度。有关自动时间尺度
计算的指导，请参阅 Specify Timing Relationship Automatically。

#### 依赖关系

对于 VCS 协同仿真，此参数被禁用。您可以在建立 VCS 与 Simulink 之间的
连接后点击 **Show Timescale**，以打开一个包含端口时间映射
信息的对话框。有关启动 VCS 协同仿真的更多信息，请参阅 Start VCS from MATLAB。

### **1 second in Simulink corresponds to {} in the HDL simulator** — Simulink 与 HDL 仿真器之间的时序关系 整数和时间单位

此参数由一个 *Time* 值和一个
*TimeUnit* 值组成。

要为协同仿真配置相对时序模式：

1. 确认已选择 `Tick`，即 *TimeUnit* 的默认
   设置。如果未选择，则从右侧列表中选择它。
2. 在左侧的 *Time* 文本框中输入比例因子。默认比例因子为 1。

要为协同仿真配置绝对时序模式：

1. 将 *TimeUnit* 设置为绝对时间单位：
   `fs`（飞秒）、`ps`
   （皮秒）、`ns`（纳秒）、
   `us`（微秒）、`ms`
   （毫秒）或 `s`（秒）。
2. 在左侧的 *Time* 文本框中输入比例因子。默认比例因子为 1。

### 连接

在与 Vivado 仿真器进行协同仿真期间，此选项卡不可见。

### **Connection mode** — Simulink 与 HDL 仿真器之间的连接 `Full Simulation`（默认）| `Confirm Interface Only` | `No Connection`

Simulink 与 HDL 仿真器之间的连接类型。

- `Full Simulation`：确认
  接口并运行 HDL 仿真。
- `Confirm Interface Only`：连接到
  HDL 仿真器并检查信号名称、维度和
  数据类型，但不运行 HDL 仿真。在
  Simulink 仿真期间，不与 HDL
  仿真器联系。
- `No Connection`：不与
  HDL 仿真器通信。无需启动 HDL 仿真器。

### **HDL simulator is running on this computer** — HDL 仿真器和 Simulink 位于同一主机 `true`（默认）| `false`

当两个应用程序运行在同一台计算机上时，您可以为应用程序之间的通信通道选择共享
内存或 TCP 套接字。如果未选择此选项，则仅
TCP/IP 套接字模式可用，并且 **Connection method** 列表
将不可用。

#### 依赖项

对于 VCS 协同仿真，此参数被禁用。

### **Connection method** — HDL 仿真器与 Simulink 之间的连接 `Socket`（默认）| `Shared memory`

- `Socket`：Simulink 与 HDL 仿真器通过指定的 TCP/IP 套接字进行通信。TCP/IP 套接字模式更加通用。您可将其用于单系统和网络配置。此选项提供最大的可扩展性。有关 TCP/IP 套接字通信的更多信息，请参阅 TCP/IP Socket Ports。
- `Shared memory`：Simulink 与 HDL 仿真器通过共享内存进行通信。共享内存通信提供最佳性能，是默认的通信模式。

#### 依赖项

- 当您选择 **HDL Simulator is running on this computer** 时，此参数显示。
- VCS 协同仿真仅支持套接字通信。

### **Host name** — HDL 仿真器主机名字符串

如果您在不同于 HDL 仿真器的计算机上运行 Simulink，则此参数适用。

#### 依赖项

对于 VCS 协同仿真，此参数为只读。

### **Port number or service** — 套接字端口号字符串

如果您未使用共享内存，请为您的计算机系统指定有效的 TCP 套接字端口号或服务。有关选择 TCP 套接字端口的信息，请参阅 TCP/IP Socket Ports。

### **Show connection info on icon** — 在模块图标上添加连接参数 `true`（默认）| `false`

当您选择此选项时，HDL Cosimulation 模块图标会显示当前的通信参数设置。如果您选择共享内存，图标将显示 `SharedMem`。如果您选择 TCP 套接字通信，图标将显示 `Socket`，并以 `hostname:port` 格式显示主机名和端口号。

此信息可帮助您区分多个 HDL Cosimulation 模块，其中每个模块与 HDL 仿真器的不同实例进行通信。

### 仿真

在与 Vivado 仿真器进行协同仿真期间，此选项卡不可见。

### **Time to run HDL simulator before cosimulation starts** — 使 Simulink 与 HDL 仿真器整数和时间单位对齐的偏移量

指定在 Simulink 中开始仿真之前运行 HDL 仿真器的时间量。正确指定此时间可使 Simulink 模块的信号与 HDL 信号对齐，从而可以直接进行比较和验证，而无需额外的延迟。

此设置由 *PreRunTime* 值和 *PreRunTimeUnit* 值组成。

- *PreRunTime*：任何有效的时间值。默认值为 0。
- *PreRunTimeUnit*：指定 *PreRunTime* 的时间单位。

  - `Tick`
  - `s`
  - `ms`
  - `us`
  - `ns`
  - `ps`
  - `fs`

### **Pre-simulation Tcl commands** — 在协同仿真之前在 HDL 仿真器中运行的命令字符串

协同仿真工具在仿真 Simulink 模型的 HDL 组件之前，会在 HDL 仿真器中执行这些命令。如果您在一行中输入多个命令，请在每个命令后附加分号（;），即标准 Tcl 连接运算符。

例如，使用此参数生成单行 echo 命令以确认仿真正在运行，或生成执行大量仿真初始化和启动序列的复杂脚本。您不能使用这些命令更改仿真状态。

您可以指定任何有效的 Tcl 命令。您指定的 Tcl 命令不能包含加载 HDL 仿真器项目或修改仿真器状态的命令。例如，字符向量不能包含 `start`、`stop` 或 `restart`（对于 ModelSim）或 `run`、`stop` 或 `reset`（对于 Xcelium）等命令。

#### 依赖项

对于 VCS 协同仿真，此参数被禁用。请使用 `launchVCS` 函数的 `PreSimulationTcl` 属性来定义预仿真 Tcl 命令。

### **Post-simulation Tcl commands** — 在协同仿真字符串之后于 HDL 仿真器中运行的命令

协同仿真工具在仿真 Simulink 模型的 HDL 组件之后，会在 HDL 仿真器中执行这些命令。

您可以指定任何有效的 Tcl 命令。您指定的 Tcl 命令不能包含加载 HDL 仿真器项目或修改仿真器状态的命令。例如，该字符串不能包含 `start`、`stop` 或 `restart`（用于 ModelSim）或 `run`、`stop` 或 `reset`（用于 Xcelium）等命令。

**注意**

每次 ModelSim 仿真后，仿真器需要时间更新覆盖率结果。为防止此过程与下一次协同仿真会话之间可能发生冲突，请在每次连续仿真之间添加短暂暂停。

#### 依赖关系

对于 VCS 协同仿真，此参数被禁用。请使用 `launchVCS` 函数的 `PostSimulationTcl` 属性来定义仿真后 Tcl 命令。

## 所属库

HDL Verifier / For Use with AMD Vivado Simulator HDL Verifier / For Use with Cadence Xcelium HDL Verifier / For Use with Siemens ModelSim/Questa HDL Verifier / For Use with Synopsys VCS

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的附加配置选项。您可以为与 Siemens® ModelSim、Cadence® Xcelium 或 AMD® Vivado 仿真器一起使用的协同仿真模块生成 HDL 代码。

每个 HDL Cosimulation 模块通过向在 HDL 仿真器下执行的 HDL 模型施加输入信号并从中读取输出信号，来协同仿真一个硬件组件。请参阅 Generate Cosimulation Model (HDL Coder)。

有关设置 HDL 协同仿真时的时序、延迟、数据类型、基于帧的处理及其他问题的信息，请参阅 Define HDL Cosimulation Block Interface。

您可以将 HDL Cosimulation 模块与 HDL Coder 一起使用，为您手写或遗留的 HDL 代码生成接口。当模型中包含 HDL Cosimulation 模块时，代码生成器会根据所选目标语言生成 VHDL 或 Verilog 接口。

当目标语言为 VHDL 时，生成的接口包括：

- 一个实体定义。该实体定义与 HDL Cosimulation 模块上配置的端口在名称和数据类型上对应的端口（输入、输出和时钟）。还会声明时钟使能和复位端口。
- 一个 RTL 架构，包括组件声明、声明与连接到 HDL Cosimulation 端口的信号相对应信号的组件配置，以及组件实例化。
- 模型所需的端口赋值语句。

当目标语言为 Verilog 时，生成的接口包括：

- 一个模块，定义与 HDL Cosimulation 模块上配置的端口在名称和数据类型上对应的端口（输入、输出和时钟）。该模块还定义时钟使能和复位端口，以及与连接到 HDL Cosimulation 端口的信号相对应的 `wire` 声明。
- 一个模块实例。
- 模型所需的端口赋值语句。

在启动代码生成之前，请检查模型是否满足代码生成要求。要检查代码生成要求，请选择 **Debug** 选项卡，然后单击 **Update Model**。

**HDL Architecture**

此模块有一个默认 HDL 架构。

**HDL Block Properties**

有关实现参数说明，请参阅 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

## 版本历史

**在 R2008a 中引入**

### R2024b: Support added for VCS simulator

要为 Synopsys VCS 仿真器创建 HDL Cosimulation 模块，请将此模块添加到 Simulink 测试平台，并配置参数以匹配您的 HDL DUT：指定端口名称和属性、时间尺度、连接和仿真选项。

### R2022a：新增对 Vivado 仿真器的支持

要为 Vivado 仿真器创建 HDL Cosimulation 模块，请使用 Cosimulation Wizard 生成并配置 HDL Cosimulation 模块。然后，在 Simulink 测试平台中使用生成的模块。

## 描述

通过将 Simulink 与 HDL 仿真器连接来协同仿真 HDL 设计

HDL Cosimulation 模块通过向 HDL 仿真器中正在仿真的 HDL 模型施加输入信号并读取输出信号，来协同仿真硬件组件。使用 Cosimulation Wizard 配置并生成此模块。

- 使用 Vivado® 仿真器进行协同仿真时，必须首先使用 Cosimulation Wizard 生成此模块。
- 使用 VCS®、ModelSim™ 或 Xcelium™ 进行协同仿真时，可以选择绕过该向导并直接配置模块。

您可以在模块上配置以下选项：

- 将模块的输入和输出端口映射为与 HDL 模块的信号（包括内部信号）相对应。必须为每个输出端口指定采样时间。可以选择为每个输出端口指定数据类型。Vivado 协同仿真不支持内部信号映射。
- 用于在仿真器之间交换数据的通信类型和通信设置。
- Simulink® 中的仿真时间单位与 HDL 仿真器中的仿真时间单位之间的时序关系。
- 要施加到模型的上升沿或下降沿时钟。可以为每个时钟信号指定周期。
- 在仿真之前和之后运行的 Tcl 命令。

您可以通过仅使用输入端口或仅使用输出端口配置该模块，从而使用它来建模源设备或接收设备。

**与 Simulink 代码生成的兼容性**

- 此模块参与 HDL Coder™ 的 HDL 代码生成。代码生成器会为您手写或遗留的 HDL 代码生成接口。它不参与 Simulink Coder™ 的 C 代码生成。
