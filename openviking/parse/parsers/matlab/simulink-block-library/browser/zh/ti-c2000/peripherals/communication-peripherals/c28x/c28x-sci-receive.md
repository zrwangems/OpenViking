---
type: simulink-block
title: 'C28x SCI Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xscireceive'
documentation_source_path: 'ref/c28xscireceive.html'
language: zh-CN
chinese_source: official
---

# C28x SCI Receive

## 端口

### 输入

### **Length** — 从输入端口接收到的数据长度 标量

该模块接受要接收的数据长度。

#### 依赖关系

要启用此端口，请将 **Data length option** 参数设置为 `Length via input port`。

**数据类型:** `uint8` | `uint16` | `uint32`
### 输出

### **Data** — 从串行总线接收的数据 标量 | 向量

从串行通信总线接收的数据。

- 当数据长度设置为 `Length via dialog` 时，数据端口配置为 **fixed size signal**。它只输出接收到的数据。
- 当数据长度设置为 `Length via Input port` 或 `Variable Length` 时，数据端口配置为 **variable size signal**。在这种情况下，端口会输出接收到的数据以及接收到的数据的长度。

  当**数据长度**设置为 `Variable Length` 或 `Length via input port` 时，如果未收到数据，则输出数据宽度为 `0`。这与为 **Action taken when connection times out** 参数设置的连接输出类型无关。

  要生成可变大小信号的代码，请转到 **配置参数** > **代码生成** > **接口** 并选择**可变大小信号**。有关更多信息，请参阅

  - 可变大小信号基础知识
  - 可变大小信号长度自适应

**注意**

目前，Monitor & Tune（外部模式）不支持输出可变大小的信号。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single`

### **status** — 串口通信状态 标量

指示接收到的串行数据的状态：

- `0` - 无错误。
- `1` - 模块等待接收数据时发生超时。如果未收到预期标头，则此为默认状态。
- `2` - 接收到的数据包含错误（校验和错误）或未收到所需的尾部。
- `3` - SCI 奇偶校验错误标志：当接收到不匹配的字符时发生。
- `4` - SCI 帧错误标志：当未找到预期的停止位时发生。
- `5` - SCI 溢出错误标志：当在读取前一个字符之前将一个字符传输到接收寄存器时发生。
- `6` - SCI 断路检测标志：当 SCI 接收器数据线 (SCIRXD) 连续保持低电平至少 10 位时发生。
- `7` - 数据不可用标志：在非阻塞模式下，当 FIFO 中没有可用数据时发生。当接收到标头后，数据长度设置为 **Variable length**，并且 FIFO 中没有数据可供读取（作为数据或终止符）时，状态为“数据不可用”。
- `8` - 部分数据可用：部分数据状态表示已接收部分数据，不包括标头。当数据长度设置为 `Variable length` 且预期会收到终止符时，状态设置为 **Partial Data**；否则，状态设置为 `Max data length`。

#### 依赖关系

只有选择 **Output receiving status** 时才会出现此端口。

**数据类型:** `uint16`

## 参数

### **SCI 模块** — SCI 通信模块 **A** (默认) | **B** | **C** | **D**

用于通信的 SCI 模块。不同 C2000™ 处理器支持的 SCI 模块数量各不相同。

### **附加包头** — 表示数据开始 `'S'` (默认) | 字符串 | char | 0 到 255 之间的数字

位于接收到的数据包开头的数据，并非接收到的数据的一部分，它指示数据的开始。附加包头必须使用 ASCII 字符表示。您可以使用字符串或数字 (0–255)。您必须为该参数输入的字符串添加单引号，但引号不会被接收，也不会计入总字节数。要指定空值（无包头），只需输入两个单引号。

头部的数据类型与模块中提到的数据类型无关。

**注意**

- 将附加包头或终止符与主机 SCI Transmit 模块中指定的包头或终止符进行匹配。
- 如果头部为空，则接收缓冲区中存在的任何内容都将被视为接收的起点。如果数据长度选项设置为可变长度，且头部为空，则尾部将从该起始点开始计算。
- 如果模块中未提供预期的头部，则 FIFO 中存在的数据将被视为接收的起点，并从该起点开始，终端将期望检索所需长度的数据。

### **附加包终止符** — 表示数据结尾 `'E'` (默认) | 字符串 | char | 0 到 255 之间的数字

位于接收数据包末尾的数据，并非接收数据的一部分，表示数据结束。附加包终止符必须使用 ASCII 字符表示。使用字符串或数字 (0–255)。您必须为该参数输入的字符串添加单引号，但引号不会被接收，也不会计入总字节数。要指定空值（不带包终止符），只需输入两个单引号。

终止符的数据类型与模块中提到的数据类型无关。

### **标头接收检查的重试次数** — 自定义标头接收检查的重试次数 `16` (默认) | `positive integer, finite` | `scalar`

此参数确保在接收数据时检查预期的头部信息。

当 FIFO 接收到数据时，该模块会逐一检查接收到的数据中的头部信息。如果数据与标头不匹配，则该模块将丢弃该数据，并继续在下一个数据中查找标头，直到重试次数到期。

如果报头在重试次数范围内匹配，则将其视为数据包的开始，并且后续接收到的数据将被视为有效数据。

### **数据类型** — 输出数据类型 **uint8** (默认) | **单精度** | **int8** | **int16** | **uint16** | **int32** | **uint32**

输出数据的数据类型。

如果数据以 `uint8` 格式传输，但 SCI 接收模块输出预期为 `int16/int32`，则假定存在偶数个字节，并且输出格式为不同的数据类型。如果数据字节数为奇数，即使状态显示为**无错误**，格式化时也会丢失最后一个字节。

### **数据长度选项** — 模块接收的数据长度 `Length via dialog` (默认) | `Length via input port` | `Variable length`

选择模块的数据长度选项。

- `Length via dialog` - 要接收的数据长度通过 `Data length` 参数提供。
- `Length via input port` - 该模块接收可变大小的数据，具体取决于输入端口接收到的数据长度。如果输入端口接收到的长度大于最大数据长度参数中规定的长度，则考虑最大数据长度。
- `Variable length` - 在非阻塞模式下接收数据，直到尾部匹配为止。确保数据中不包含尾部。当只有头部和终止符可用而没有数据可用时，状态设置为**无错误**，可变数据长度设置为零。

  - 如果终止符值未达到最大长度，或者中间没有数据，则该模块将输出接收到的数据及其长度，并将状态设置为 `Partial data available`。
  - 如果没有提供终止符值，则该模块尝试接收 **max data length** 的数据。如果读取的数据长度小于最大长度，或者中间没有可用数据，则该模块将输出接收到的数据及其长度，并将状态设置为 `Partial data available`。
  - 如果未读取数据，则状态设置为 **Data not available**。
  - 当收到头部和终止符但没有收到数据时，状态读取为数据不可用。
  - 当使用可变长度的 SCI 数据时，应避免使用尾部，因为尾部的存在被视为数据包的结束。
  - 如果在可变长度模式下没有收到数据，则输出数据端口长度为 0。

要启用输入端口**长度**，请选择数据长度选项为 `Length via input port`。

### **数据长度** — 模块接收的数据类型数量 `1` (默认) | `positive integer, finite` | `scalar`

模块接收到的**数据类型**数量（不是字节数）。如果此参数设置为大于 `1`，则输出将是一个向量。确保指定的数据长度与接收数据的 SCI Transmit 模块的长度相同。

#### 依赖关系

要启用此参数，请将 **Data length option** 参数设置为 `Length via dialog`。

### **最大数据长度** — 模块接收的数据类型最大数量 `1` (默认) | 正整数，有限 | `positive integer, finite`

模块可以接收的最大**数据类型**数（不是字节数）。

如果要接收的数据大小（基于数据长度或最大数据长度、头部、终止符和数据类型）大于 FIFO 大小字节，则会导致数据丢失。

#### 依赖关系

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Variable length`。

### **初始输出** — 模块的默认值输出 `0` (默认) | 标量 | 向量

SCI Receive 模块的默认值输出。例如，当 **Action taken when connection timeout** 参数设置为 **Output the last received value** 且在接收到数据之前发生连接超时时，将输出此值。

#### 依赖关系

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`。

### **Action taken when connection times out** — 连接超时时选择输出类型 **输出上次收到的值** (默认) | **输出自定义值**

指定连接超时时要输出的内容。如果选中 **Output the last received value**，则该模块输出最后接收到的值。如果尚未收到值，则该模块输出**初始输出**值。

如果选择 **Output custom value**，则使用 **Output value when connection times out** 参数设置自定义值。

#### 依赖关系

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`。

### **Output value when connection times out** — 连接超时时，模块的自定义输出值 `0` (默认) | 标量 | 向量

设置自定义超时值。

只有当 **Action taken when connection times out** 参数设置为 **Output custom value** 时，**Output value when connection times out** 参数才可用。

#### 依赖关系

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`。

### **采样时间** — 从 SCI 设备读取数据的频率 `0.1` (默认) | `-1` | 标量

以秒为单位记录该模块的采样时间。要异步执行此模块，请将此参数设置为 `-1`。

#### 依赖关系

要启用此参数，请将 **Data length option** 参数设置为 `Length via dialog` 或 `Variable length`。

当数据长度选项设置为 `Length via input port` 时，采样时间将继承输入端口的属性。

### **等待接收到数据** — 请等待请求的数据可用。 `off` (默认) | `on`

- `on` - 如果启用此选项，系统将等待直到有数据可供读取（达到数据长度时）。读取操作以阻塞模式运行。当模块正在等待请求的数据时，读取操作将被阻塞。如果有数据，该模块将输出数据。如果数据不可用，则该模块等待数据。

  如果在下一次读取操作开始时，目标硬件仍在等待数据，则会发生任务溢出。

  要解决超时问题，请使用**采样时间**参数增加时间步长。
- `off` - 如果禁用此选项，系统将在每个时间步（轮询模式）检查 FIFO 以读取数据。如果数据存在，则该模块读取并输出数据内容。如果没有数据，该模块将输出最后一个值并继续执行。清除此参数后，读取操作将以非阻塞模式运行。

#### 依赖关系

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`。

**注意**

当数据长度选项选择为 **Variable length** 时，模块执行将始终以非阻塞模式进行。

### **超时** — 模块等待接收数据的时间（以秒为单位） `inf` (默认) | `positive value greater than 0`

指定在每个时间步长内，如果接收 FIFO 中没有数据可供读取，则该模块应等待的时间。如果超时，读取操作将中止。

如果该值设置为 `inf`，则该模块将无限期地等待 FIFO 中的数据可用。

**注意**

通过参数**等待数据接收完成**和**超时**可以实现 3 种模式。

- **阻塞模式** - 在阻塞模式下，参数**等待数据接收完成**启用，**超时**设置为 `inf`。

  在这种模式下，如果 FIFO 中没有数据可供读取，它将无限期地等待，直到有数据可供读取为止。
- **Blocking mode with Timeout** - 在阻塞模式下，设置超时，启用参数**等待数据接收完成**，并将**超时**设置为 `any finite value > 0`。

  在此模式下，如果 FIFO 中没有数据可供读取，它将等待检查 FIFO 状态，直到达到设定的超时值。如果在规定时间内 FIFO 中没有数据可供读取，则 SCI Receive 模块将输出状态为 `timeout`。
- **Non-Blocking mode** - 在非阻塞模式下，参数**等待数据接收完成**被禁用。

  在此模式下，如果 FIFO 中存在数据，SCI Receive 模块将读取数据；否则，SCI Receive 模块将输出状态为 `Data not available`。
- 要接收长度超过 FIFO 长度的数据，请使用阻塞模式或带超时的阻塞模式。这样可以确保在读取完整个 FIFO 后，还有额外的时间来获取 FIFO 中的剩余数据。如果在非阻塞模式下尝试接收大于 FIFO 长度的数据，则可能会遇到数据丢失的情况。

  在启用或未启用超时的阻塞模式下，由于需要等待读取数据，可能会遇到任务超时的情况。

#### 依赖关系

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`，并启用参数 `Wait until data received`。

### **输出接收状态** — 串口通信状态 `off` (默认) | `on`

创建一个 **Status** 模块输出，用于提供串行通信的状态。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

通过串行通信接口 (SCI) 从主机接收目标数据

SCI Receive 模块支持处理器与其他异步外设之间的异步串行数字通信。该模块使用指定的 SCI 硬件模块接收标量或向量数据。

每个模块的模型只能包含一个 SCI Receive 模块。C28x 处理器有四个 SCI 模块 - A、B、C 和 D。可用的 SCI 模块数量取决于所选处理器。您可以通过导航到 **硬件实现** > **Target hardware resources** 来配置 SCI 模块。请确认这些设置符合您的应用程序要求。

**注意**

使用类似的 SCI 模块模块进行串行外部模式连接会导致冲突检查错误。

该模块可以以阻塞模式或非阻塞模式输出数据。在阻塞模式下，模型模块执行，等待请求的数据可用。在非阻塞模式下，模型会持续运行。要将模块设置为阻塞模式，请选择**等待数据接收完成**选项。
