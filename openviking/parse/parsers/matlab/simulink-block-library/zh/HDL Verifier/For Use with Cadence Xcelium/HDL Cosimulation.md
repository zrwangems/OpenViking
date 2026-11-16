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

### **HDL\_input\_port\_name** — 从 Simulink 传递到 HDL 仿真器的信号 scalar | vector

模块上的端口与 HDL 设计上的端口对应。在 **端口** 选项卡上添加或移除端口。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`

### 输出

### **HDL\_output\_port\_name** — 从 HDL 仿真器传递到 Simulink 的信号 scalar | vector

模块上的端口与 HDL 设计上的端口对应。在 **端口** 选项卡上添加或移除端口。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `Fixed-point`

## 参数

### **模块信息** — Vivado 协同仿真的模块信息 只读：模块生成设置

此参数为只读。

在使用 Cosimulation Wizard 生成此模块后，本节显示信息。它显示以下项：

- HDL 仿真器 – Vivado 仿真器
- HDL 设计库 – HDL 库文件的位置
- HDL 语言 – VHDL 或 Verilog
- HDL 时间精度 – HDL 设计的时间精度
- HDL 波形文件 – 波形文件的名称和路径

为 Vivado 仿真器生成协同仿真模块时，不能使用模块掩码更改端口、时钟、复位或时间精度的名称和方向。要更改这些项，请打开 Cosimulation Wizard 并重新生成模块。

#### 依赖关系

此参数仅在使用 Vivado 协同仿真时可见。

### 端口

### **启用直接馈通** — 解决代数环警告 `true` (默认) | `false`

消除当模型包含纯组合路径时协同仿真与 Simulink 之间出现的一个输出采样延迟差异。如果 HDL Cosimulation 模块位于反馈环路中并生成代数环警告或错误，请清除此复选框。当您仿真数据路径上带有寄存器的时序电路时，指定直接馈通不会影响该数据路径的时序。

#### 依赖关系

### **完整 HDL 名称** — 信号路径名称 string

使用 HDL 仿真器路径名称语法指定信号路径名称。例如，对于 Xcelium HDL 仿真器，为 `manchester.samp`。该信号可以处于 HDL 设计层次的任何级别。与该信号对应的 HDL Cosimulation 模块端口使用此名称标记。

有关在 Simulink 中指定端口和模块路径名称的规则，请参阅 Specify HDL Signal/Port and Module Paths for Simulink Testbench Cosimulation。

可以直接从 HDL 仿真器 **wave** 窗口复制信号路径名称，并将其粘贴到 **完整 HDL 名称** 字段中。使用 *`Path.Name`* 视图，而不是 *`Db::Path.Name`* 视图。将信号路径名称粘贴到 **完整 HDL 名称** 后，点击 **Apply** 完成粘贴操作并更新信号列表。

#### 依赖关系

如果该模块是从 Cosimulation Wizard 生成的，则不应更改此值。对于 Vivado HDL Cosimulation 模块，此参数为只读。

### **I/O 模式** — 端口方向 `Input` | `Output`

要添加双向端口，请将该端口两次添加到列表中，分别作为输入和输出。

`Input` — Simulink 驱动的 HDL 信号。Simulink 以指定的采样率在指定的 HDL 仿真器信号上存放值。

**注意**

当您定义模块输入端口时，请确保仅设置一个源来驱动该信号的输入。例如，避免定义具有多个实例的输入端口。如果多个源驱动单个信号的输入，则仿真模型会产生意外结果。

`Output` — Simulink 读取的 HDL 信号。对于输出信号，必须指定显式采样时间。您也可以指定数据类型，但宽度必须与 HDL 中信号的宽度匹配。有关指定数据类型的详细信息，请参阅 **数据类型** 和 **小数长度** 参数。

Simulink 信号不具有三态语义，因为没有 `'Z'` 值。要与双向信号连接，请连接到输出驱动器的输入和使能信号，以及输入驱动器的输出信号。此方法将实际三态缓冲器保留在 HDL 中，在那里分辨率函数可以处理与其他三态缓冲器的连接。

#### 依赖关系

如果该模块是从 Cosimulation Wizard 生成的，则不应更改此值。对于 Vivado HDL Cosimulation 模块，此参数为只读。

### **HDL 类型** — HDL 端口信号的类型 只读：`Logic` (默认) | `Vector`

此参数为只读。

显示 HDL 端口信号的类型，由 Cosimulation Wizard 配置。

#### 依赖关系

仅当该模块为配合 Vivado 协同仿真而生成时，此参数才可见。

### **HDL 维度** — HDL 端口信号的维度 只读：scalar | vector

此参数为只读。

显示 HDL 端口信号的维度，由 Cosimulation Wizard 配置。

#### 依赖关系

仅当该模块为配合 Vivado 协同仿真而生成时，此参数才可见。

### **采样时间** — 在输出端口上读取采样之间的时间 1 (默认) | integer

施加到输出端口的连续采样之间的时间间隔。

Simulink 以此处指定的采样率从关联的 HDL 仿真器信号读取值。

通常，Simulink 按如下方式处理端口采样周期：

- 如果将输入端口连接到具有显式采样周期的信号，则基于前向传播，Simulink 将该速率应用于该端口。
- 如果将输入端口连接到没有显式采样周期的信号，则 Simulink 分配的采样周期等于模型中所有已识别输入端口采样周期的最小公倍数 (LCM)。
- 必须为每个输出端口指定显式采样时间。

与 Simulink 采样时间命中对应的 HDL 时间取决于 **Timescales** 设置。请参阅 Simulation Timescales。

#### 依赖关系

要启用此参数，请将 **I/O 模式** 设置为 `Output`。

### **数据类型** — 输出信号的 Simulink 数据类型 `Inherit` (默认) | `Fixedpoint` | `Double` | `Single` | `Half`

选择 `Inherit` 可自动确定数据类型。该模块会检查继承的字长是否与从 HDL 仿真器查询到的字长匹配。如果它们不匹配，Simulink 会生成错误消息。例如，如果您将 Signal Specification 模块连接到输出，`Inherit` 会将 Signal Specification 模块指定的数据类型强制施加到输出端口。

如果 Simulink 无法确定连接到输出端口的信号的数据类型，它会向 HDL 仿真器查询该端口的数据类型。例如，如果 HDL 仿真器针对大小为 `N` 位的信号返回 VHDL® 数据类型 `STD_LOGIC_VECTOR`，则数据类型 `ufixN` 会被强制施加到输出端口。隐式小数长度为 0。

您还可以分配显式数据类型，并可选择指定 **小数长度**。通过显式分配数据类型，您可以将定点数据类型强制施加到 HDL Cosimulation 模块的输出端口。例如，对于 8 位输出端口，将 **符号** 设置为 `Signed` 并将 **小数长度** 设置为 `5`，会将数据类型强制为 `sfix8_En5`。您不能强制宽度。宽度始终从 HDL 仿真器继承。

**数据类型** 和 **小数长度** 属性仅适用于以下类型的 HDL 信号：

- 任何逻辑类型的 VHDL 信号，例如 `STD_LOGIC` 或 `STD_LOGIC_VECTOR`
- `wire` 或 `reg` 类型的 Verilog® 信号

#### 依赖关系

要启用此参数，请将 **I/O 模式** 设置为 `Output`。

在与 Vivado 仿真器协同仿真期间，此参数显示为 **Simulink Data Type**。

### **符号** — 输出数据类型的符号分量 `Unsigned` (默认) | `Signed`

显式输出端口数据类型的符号指定。

#### 依赖关系

要启用此参数，请将 **I/O 模式** 设置为 `Output`，并将 **数据类型** 设置为 `Fixedpoint`。

### **小数长度** — 输出数据类型中的小数位数 integer

定点输出信号小数部分的大小，以位为单位。例如，对于 8 位输出端口，将 **符号** 设置为 `Signed` 并将 **小数长度** 设置为 `5`，会将数据类型强制为 `sfix8_En5`。您不能强制宽度；宽度始终从 HDL 仿真器继承。

#### 依赖关系

要启用此参数，请将 **I/O 模式** 设置为 `Output`，并将 **数据类型** 属性设置为 `Fixedpoint`。

**数据类型** 和 **小数长度** 属性仅适用于以下类型的 HDL 信号：

- 任何逻辑类型的 VHDL 信号，例如 `STD_LOGIC` 或 `STD_LOGIC_VECTOR`
- `wire` 或 `reg` 类型的 Verilog 信号

### **Simulink 字长** — Simulink 端口的位宽 integer <129 | `inherit`

Simulink 端口的大小，指定为小于 129 的正整数。

**对于输入端口** — 此值设置为 `inherit`（只读）。

当 **HDL 字长** 参数大于 128 位时，Simulink 端口维度在编译时由驱动信号的数据类型确定。例如：

- 当 **HDL 字长** = 150 且 **Simulink 字长** = 50 时，HDL Verifier™ 允许 Simulink 端口的数据宽度为 50 位，维度大小为 3，例如 `sfix50(3)` 或 `ufix50(3)`。
- 当 **HDL 字长** = 140 且 **Simulink 字长** = 50 时，HDL Verifier 将 150 位 Simulink 打包到 140 位 HDL 中。HDL Verifier 忽略最后一个字的 10 个最高有效位 (MSB)。

  三个各为 50 位的 Simulink 输入字被打包成一个 140 位的 HDL 输入信号。最后一个 Simulink 字的 10 个 MSB 被 HDL 服务器忽略

**对于输出端口** — 有 2 种情况。

- 当 **HDL 字长** 参数小于 129 位时，此参数与 HDL 端口的宽度匹配，并且为只读。
- 当 **HDL 字长** 参数大于 128 位时，HDL Verifier 会创建一个端口向量来表示此端口。例如：
  - 当 **HDL 字长** = 150 且 **Simulink 字长** = 50 时，HDL Verifier 创建一个数据宽度为 50 位的 Simulink 端口。例如 `sfix50(3)` 或 `ufix50(3)`。
  - 当 **HDL 字长** = 150 且 **Simulink 字长** = 60 时，HDL Verifier 创建一个数据宽度为 60 的 Simulink 端口，例如 `sfix60(3)` 或 `ufix60(3)`。由于 HDL 字只有 150 位，而 Simulink 端口需要 180 位，因此 30 位被填充或符号扩展。
  - 当 **HDL 字长** = 140 且 **Simulink 字长** = 50 时，HDL 输出的每 50 位表示为一个 Simulink 字。最后一个 Simulink 字的 10 个 MSB 未使用，并根据 **符号** 参数进行扩展。

    HDL 输出信号为 140 位，被打包成三个各为 50 位的 Simulink 字。最后一个字仅使用 40 位，并有 10 位被扩展

#### 依赖关系

当 **HDL 字长** 小于 129 时，此参数为只读。

### **HDL 字长** — HDL 端口的位宽 只读：integer

此参数为只读。

HDL 端口的位大小。

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

### 时钟

**注意**

- 在与 Vivado 仿真器协同仿真期间，此选项卡名为 **Clocks, Resets, Enables**。
- 在与 VCS 仿真器协同仿真期间，此选项卡不可用。使用 `launchVCS` 函数的 `PreSimulationTcl` 属性来定义时钟和复位信号。

创建可选的上升沿和下降沿时钟，以将激励施加到您的协同仿真模型。滚动列表显示 HDL 时钟，这些时钟使用 deposit 方法将值驱动到您正在建模的 HDL 信号。时钟信号必须是单比特信号。不支持向量信号。有关添加和编辑时钟信号的说明，请参阅 Creating Optional Clocks with the Clocks Pane of the HDL Cosimulation Block。

### **协同仿真开始前运行 HDL 仿真器的时间** — 协同仿真开始前所需的 HDL 仿真时间 `0` (默认) | nonnegative integer

指定在开始协同仿真之前 HDL 仿真需要运行的时间。指定一个非负整数，并从菜单中选择时间单位。

- `fs` – Femtoseconds
- `ps` – Picoseconds
- `ns` – Nanoseconds
- `us` – Microseconds
- `ms` – Milliseconds
- `s` – Seconds

#### 依赖关系

要启用此参数，请为 Vivado 协同仿真生成此模块。

### **完整 HDL 名称** — 信号路径名称 string

使用 HDL 仿真器路径名称语法将每个时钟指定为信号路径名称。例如：`/manchester/clk` 或 `manchester.clk`。

有关 Simulink 中路径规范的信息和要求，请参阅 Specify HDL Signal/Port and Module Paths for Simulink Testbench Cosimulation。

可以直接从 HDL 仿真器 **wave** 窗口复制信号路径名称，并将其粘贴到 **完整 HDL 名称** 字段中。使用 *`Path.Name`* 视图，而不是 *`Db::Path.Name`* 视图。将信号路径名称粘贴到 **完整 HDL 名称** 后，点击 **Apply** 完成粘贴操作并更新信号列表。

#### 依赖关系

如果该模块是从 Cosimulation Wizard 生成的，则不应更改此值。对于 Vivado HDL Cosimulation 模块，此参数为只读。

### **有效时钟边沿** — 用于采样信号的 HDL 时钟边沿 `Rising` (默认) | `Falling`

选择以下选项之一。

- `Rising` – 指定上升沿时钟。
- `Falling` – 指定下降沿时钟。

周期和持续时间是 Simulink 时间。要将 Simulink 时间与 HDL 时间关联，请转到 **Timescales** 选项卡，并点击 **Determine Timescale Now**。

#### 依赖关系

此参数仅对 ModelSim 或 Xcelium 协同仿真可见。

### **波形类型** — 生成波形以将时钟、复位或使能驱动到 HDL 设计 `Rising` (默认) | `Falling` | `Step 1 to 0` | `Step 0 to 1`

对于 Vivado 协同仿真，选择以下选项之一。

- `Active Rising Edge Clock` – 创建一个占空比为 50% 的周期信号，其中上升沿相对于 Simulink 驱动输入的时刻偏移。
- `Active Falling Edge Clock` – 创建一个占空比为 50% 的周期信号，其中下降沿相对于 Simulink 驱动输入的时刻偏移。
- `Step 0 to 1` – 创建一个阶跃函数，该函数先在指定持续时间内驱动 0，然后转换为 1。
- `Step 1 to 0` – 创建一个阶跃函数，该函数先在指定持续时间内驱动 1，然后转换为 0。

周期和持续时间是 Simulink 时间。要将 Simulink 时间与 HDL 时间关联，请转到 **Timescales** 选项卡，并点击 **Show Times and Suggest Timescale**。

#### 依赖关系

此参数仅对 Vivado 协同仿真可见。

### **周期/持续时间** — 时钟周期 2 (默认) | integer

要指定显式时钟周期，请输入等于或大于两个分辨率单位 (ticks) 的采样时间。

如果时钟周期不是偶数整数，Simulink 无法创建 50% 占空比。相反，HDL Verifier 软件会在 `clockperiod/2` 处创建下降沿（向下舍入到最接近的整数）。

对于 ModelSim 或 Xcelium，周期和持续时间指定为 Simulink 时间；对于 Vivado，它们指定为 HDL 时间。

#### 依赖关系

此属性不适用于与 VCS 的协同仿真。

### 时间尺度

选择 Simulink 和 HDL 仿真器之间的计时关系，可手动或自动。这些参数指定 Simulink 时间的 1 秒与 HDL 仿真器时间的某个量之间的对应关系。此 HDL 仿真器时间量可以用以下方式之一表示：

- *Relative* 计时关系（Simulink 秒对应于 HDL 仿真器精度，即
  "tick"。
- *Absolute* 计时关系（Simulink 秒对应于 HDL 仿真器时间的绝对单位）

有关计算相对和绝对计时模式的更多信息，请参阅 Defining the Simulink and HDL Simulator Timing Relationship。

有关协同仿真期间 Simulink 与 HDL 仿真器之间关系的详细信息，以及相对和绝对计时模式的操作，请参阅 Simulation Timescales。

要查看所有端口、时钟、复位和使能的 Simulink 时间与 HDL 时间之间的关系，请点击 **Show Times and Suggest Timescale**。如有需要，此操作还会自动确定可用的时间尺度。

### **在仿真开始时自动确定时间尺度** — 何时计算自动时间尺度 `true` (default) | `false`

如果选择此选项，HDL Verifier 会在您启动 Simulink 仿真时计算时间尺度。如果未选择此选项，请点击 **Determine Timescale Now** 立即计算时间尺度而不启动仿真。对于 Vivado 协同仿真，此按钮显示为 **Show Times and Suggest Timescale**。或者，您可以手动选择时间尺度。有关自动时间尺度计算的指导，请参阅 Specify Timing Relationship Automatically。

#### 依赖项

对于 VCS 协同仿真，此参数被禁用。在建立 VCS 与 Simulink 之间的连接后，您可以点击 **Show Timescale**，打开一个包含端口时间映射信息的对话框。有关启动 VCS 协同仿真的更多信息，请参阅 Start VCS from MATLAB。

### **Simulink 中的 1 秒对应于 HDL 仿真器中的 {}** — Simulink 和 HDL 仿真器之间的计时关系 integer 和时间单位

此参数由 *Time* 值和 *TimeUnit* 值组成。

要为协同仿真配置相对计时模式：

1. 验证 *TimeUnit* 的默认设置 `Tick` 已选中。如果未选中，则从右侧列表中选择它。
2. 在左侧的 *Time* 文本框中输入比例因子。默认比例因子为 1。

要为协同仿真配置绝对计时模式：

1. 将 *TimeUnit* 设置为绝对时间单位：`fs`（飞秒）、`ps`（皮秒）、`ns`（纳秒）、`us`（微秒）、`ms`（毫秒）或 `s`（秒）。
2. 在左侧的 *Time* 文本框中输入比例因子。默认比例因子为 1。

### 连接

此选项卡在与 Vivado 仿真器进行协同仿真期间不可见。

### **连接模式** — Simulink 和 HDL 仿真器之间的连接 `Full Simulation` (default) | `Confirm Interface Only` | `No Connection`

Simulink 和 HDL 仿真器之间的连接类型。

- `Full Simulation`：确认接口并运行 HDL 仿真。
- `Confirm Interface Only`：连接到 HDL 仿真器并检查信号名称、维度和数据类型，但不运行 HDL 仿真。在 Simulink 仿真期间，不与 HDL 仿真器接触。
- `No Connection`：不与 HDL 仿真器通信。无需启动 HDL 仿真器。

### **HDL 仿真器正在此计算机上运行** — HDL 仿真器和 Simulink 的主机相同 `true` (default) | `false`

当两个应用程序在同一台计算机上运行时，您可以为应用程序之间的通信通道选择共享内存或 TCP socket。如果未选择此选项，则只有 TCP/IP socket 模式可用，并且 **Connection method** 列表变得不可用。

#### 依赖项

对于 VCS 协同仿真，此参数被禁用。

### **连接方法** — HDL 仿真器和 Simulink 之间的连接 `Socket` (default) | `Shared memory`

- `Socket`：Simulink 和 HDL 仿真器通过指定的 TCP/IP socket 通信。TCP/IP socket 模式更通用。您可以将其用于单系统和网络配置。此选项提供最大的可扩展性。有关 TCP/IP socket 通信的更多信息，请参阅 TCP/IP Socket Ports。
- `Shared memory`：Simulink 和 HDL 仿真器通过共享内存通信。共享内存通信提供最佳性能，并且是默认通信模式。

#### 依赖项

- 当您选择 **HDL Simulator is running on this computer** 时，此参数显示。
- VCS 协同仿真仅支持 socket 通信。

### **主机名** — HDL 仿真器主机机器 string

如果您在不同计算机上运行 Simulink 和 HDL 仿真器，则此参数适用。

#### 依赖项

对于 VCS 协同仿真，此参数为只读。

### **端口号或服务** — Socket 端口号 string

如果您未使用共享内存，请为您的计算机系统指定有效的 TCP socket 端口号或服务。有关选择 TCP socket 端口的信息，请参阅 TCP/IP Socket Ports。

### **在图标上显示连接信息** — 在模块图标上添加连接参数 `true` (default) | `false`

当您选择此选项时，HDL Cosimulation 模块图标显示当前通信参数设置。如果您选择共享内存，图标显示 `SharedMem`。如果您选择 TCP socket 通信，图标显示 `Socket`，并以 `hostname:port` 格式显示主机名和端口号。

此信息可以帮助您区分多个 HDL Cosimulation 模块，其中每个模块正在与 HDL 仿真器的不同实例通信。

### 仿真

此选项卡在与 Vivado 仿真器进行协同仿真期间不可见。

### **协同仿真开始前运行 HDL 仿真器的时间** — 将 Simulink 与 HDL 仿真器对齐的偏移量 integer 和时间单位

指定在 Simulink 中开始仿真之前运行 HDL 仿真器的时间量。指定此时间可正确对齐 Simulink 模块的信号和 HDL 信号，以便可以直接比较和验证它们，而无需额外延迟。

此设置由 *PreRunTime* 值和 *PreRunTimeUnit* 值组成。

- *PreRunTime*：任何有效时间值。默认值为 0。
- *PreRunTimeUnit*：指定 *PreRunTime* 的时间单位。

  - `Tick`
  - `s`
  - `ms`
  - `us`
  - `ns`
  - `ps`
  - `fs`

### **仿真前 Tcl 命令** — 在协同仿真前在 HDL 仿真器中运行的命令 string

协同仿真工具会在仿真 Simulink 模型的 HDL 组件之前，在 HDL 仿真器中执行这些命令。如果在一行中输入多个命令，请在每个命令后附加分号（;），即标准 Tcl 连接运算符。

例如，使用此参数生成一行 echo 命令以确认仿真正在运行，或生成执行大量仿真初始化和启动序列的复杂脚本。您不能使用这些命令更改仿真状态。

您可以指定任何有效的 Tcl 命令。您指定的 Tcl 命令不能包含加载 HDL 仿真器项目或修改仿真器状态的命令。例如，字符向量不能包含 `start`、`stop` 或 `restart`（对于 ModelSim）或 `run`、`stop` 或 `reset`（对于 Xcelium）等命令。

#### 依赖项

对于 VCS 协同仿真，此参数被禁用。使用 `launchVCS` 函数的 `PreSimulationTcl` 属性定义仿真前 Tcl 命令。

### **仿真后 Tcl 命令** — 在协同仿真后在 HDL 仿真器中运行的命令 string

协同仿真工具会在仿真 Simulink 模型的 HDL 组件之后，在 HDL 仿真器中执行这些命令。

您可以指定任何有效的 Tcl 命令。您指定的 Tcl 命令不能包含加载 HDL 仿真器项目或修改仿真器状态的命令。例如，string 不能包含 `start`、`stop` 或 `restart`（对于 ModelSim）或 `run`、`stop` 或 `reset`（对于 Xcelium）等命令。

**注意**

每次 ModelSim 仿真后，仿真器需要时间更新覆盖率结果。为防止此过程与下一个协同仿真会话之间发生潜在冲突，请在每次连续仿真之间添加短暂暂停。

#### 依赖项

对于 VCS 协同仿真，此参数被禁用。使用 `launchVCS` 函数的 `PostSimulationTcl` 属性定义仿真后 Tcl 命令。

## 所属库

HDL Verifier / For Use with AMD Vivado Simulator HDL Verifier / For Use with Cadence Xcelium HDL Verifier / For Use with Siemens ModelSim/Questa HDL Verifier / For Use with Synopsys VCS

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供会影响 HDL 实现和综合逻辑的其他配置选项。您可以为与 Siemens® ModelSim、Cadence® Xcelium 或 AMD® Vivado 仿真器一起使用的协同仿真模块生成 HDL 代码。

每个 HDL Cosimulation 模块通过向在 HDL 仿真器下执行的 HDL 模型施加输入信号并读取输出信号，来协同仿真一个硬件组件。请参阅 Generate Cosimulation Model (HDL Coder)。

有关设置 HDL 协同仿真时的计时、延迟、数据类型、基于帧的处理和其他问题的信息，请参阅 Define HDL Cosimulation Block Interface。

您可以将 HDL Cosimulation 模块与 HDL Coder 一起使用，为您手动编写或遗留的 HDL 代码生成接口。当模型中包含 HDL Cosimulation 模块时，编码器会根据选定的目标语言生成 VHDL 或 Verilog 接口。

当目标语言为 VHDL 时，生成的接口包括：

- 一个 entity 定义。该 entity 定义名称和数据类型与 HDL Cosimulation 模块上配置的端口相对应的端口（输入、输出和时钟）。还声明时钟使能和复位端口。
- 一个 RTL architecture，包括 component 声明、声明与连接到 HDL Cosimulation 端口的信号相对应的信号的 component 配置，以及 component 实例化。
- 模型所需的端口赋值语句。

当目标语言为 Verilog 时，生成的接口包括：

- 一个 module，定义名称和数据类型与 HDL Cosimulation 模块上配置的端口相对应的端口（输入、输出和时钟）。该 module 还定义时钟使能和复位端口，以及与连接到 HDL Cosimulation 端口的信号相对应的 `wire` 声明。
- 一个 module 实例。
- 模型所需的端口赋值语句。

在启动代码生成之前，请检查模型是否满足代码生成要求。要检查代码生成要求，请选择 **Debug** 选项卡，然后点击 **Update Model**。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

有关实现参数说明，请参阅 Customize Black Box or HDL Cosimulation Interface (HDL Coder)。

## 版本历史

**在 R2008a 中引入**

### R2024b：增加了对 VCS 仿真器的支持

要为 Synopsys VCS 仿真器创建 HDL Cosimulation 模块，请将此模块添加到 Simulink 测试平台，并配置参数以匹配您的 HDL DUT：指定端口名称和属性、时间尺度、连接和仿真选项。

### R2022a：增加了对 Vivado 仿真器的支持

要为 Vivado 仿真器创建 HDL Cosimulation 模块，请使用 Cosimulation Wizard 生成并配置 HDL Cosimulation 模块。然后，在 Simulink 测试平台中使用生成的模块。

## 描述

通过将 Simulink 与 HDL 仿真器连接来协同仿真 HDL 设计

HDL Cosimulation 模块通过向在 HDL 仿真器下仿真的 HDL 模型施加输入信号并读取输出信号，来协同仿真一个硬件组件。使用 Cosimulation Wizard 配置并生成此模块。

- 使用 Vivado® 仿真器进行协同仿真时，必须首先使用 Cosimulation Wizard 生成此模块。
- 使用 VCS®、ModelSim™ 或 Xcelium™ 进行协同仿真时，您可以选择绕过向导并直接配置模块。

您可以在该模块上配置以下选项：

- 将模块的输入和输出端口映射为与 HDL 模块的信号（包括内部信号）相对应。必须为每个输出端口指定采样时间。可以选择为每个输出端口指定数据类型。Vivado 协同仿真不支持映射内部信号。
- 用于在仿真器之间交换数据的通信类型和通信设置。
- Simulink® 中的仿真时间单位与 HDL 仿真器之间的计时关系。
- 要施加到模型的上升沿或下降沿时钟。您可以为每个时钟信号指定周期。
- 在仿真之前和之后运行的 Tcl 命令。

您可以通过仅使用输入或输出端口配置该模块，来使用此模块对源或接收器设备建模。

**与 Simulink 代码生成的兼容性**

- 此模块参与使用 HDL Coder™ 的 HDL 代码生成。编码器为您手动编写或遗留的 HDL 代码生成接口。它不参与使用 Simulink Coder™ 的 C 代码生成。
