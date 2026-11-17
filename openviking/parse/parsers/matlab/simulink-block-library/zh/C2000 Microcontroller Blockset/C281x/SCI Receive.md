---
type: simulink-block
title: 'C28x SCI Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xscireceive'
documentation_source_path: 'ref/c28xscireceive.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x SCI Receive

## 端口

### 输入

### **Length** — 从输入端口接收的数据长度 标量

该模块接受要接收的数据的长度。

#### 依赖

要启用此端口，请将 **Data length option** 参数设置为 `Length via input port`。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Data** — 从串行总线接收的数据 标量 | 向量

从串行通信总线接收的数据。

- 当数据长度设置为 `Length via dialog` 时，数据端口配置为**固定大小信号**。它仅输出接收到的数据。
- 当数据长度设置为 `Length via Input port` 或 `Variable Length` 时，数据端口配置为**可变大小信号**。在这种情况下，端口输出接收到的数据以及接收数据的长度。

  当 **Data length** 设置为 `Variable Length` 或 `Length via input port` 时，如果未接收到数据，则输出数据宽度为 `0`。这与为 **Action taken when connection times out** 参数设置的连接输出类型无关。

  要为可变大小信号生成代码，请转到 **Configuration Parameters** > **Code Generation** > **Interface** 并选择 **Variable-size signals**。有关更多信息，请参阅

  - Variable-Size Signal Basics
  - Variable-Size Signal Length Adaptation

**注意**

目前，Monitor & Tune（外部模式）不支持输出可变大小信号。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single`

### **status** — 串行通信状态 标量

指示接收到的串行数据的状态：

- `0` - 无错误。
- `1` - 模块在等待接收数据时发生超时。如果未接收到预期的包头，这是默认状态。
- `2` - 接收到的数据包含错误（校验和错误）或未接收到所需的包尾。
- `3` - SCI 奇偶校验错误标志：当接收到的字符存在不匹配时发生。
- `4` - SCI 帧错误标志：当未找到预期的停止位时发生。
- `5` - SCI 溢出错误标志：当在读取前一个字符之前将字符传输到接收寄存器时发生。
- `6` - SCI 间隔检测标志：当 SCI 接收器数据线（SCIRXD）连续保持低电平至少十位时发生。
- `7` - 数据不可用标志：在非阻塞模式下，当 FIFO 中没有可用数据时发生。当数据长度设置为 **Variable length** 时，在接收到包头后，如果 FIFO 中没有可用数据作为数据或终止符读取，则状态为 Data not available。
- `8` - 部分数据可用：部分数据状态表示部分接收的数据（不包括包头）。当数据长度设置为 `Variable length` 时，如果预期接收终止符但未接收到直到 `Max data length`，则状态设置为 **Partial Data**。

#### 依赖

此端口仅在您选择 **Output receiving status** 时出现。

**数据类型：** `uint16`

## 参数

### **SCI module** — 用于通信的 SCI 模块 `A`（默认） | `B` | `C` | `D`

用于通信的 SCI 模块。支持的 SCI 模块数量因不同的 C2000™ 处理器而异。

### **Additional package header** — 指示数据起始 `'S'`（默认） | 字符串 | 字符 | 0 到 255 的数字

位于接收数据包前面的数据，不属于正在接收的数据，用于指示数据的起始。附加包头必须使用 ASCII 字符表示。您可以使用字符串或数字（0–255）。必须为此参数输入的字符串添加单引号，但引号不会被接收或计入总字节数。要指定空值（无包头），仅输入两个单引号。

包头的数据类型与模块上提到的数据类型无关。

**注意**

- 将附加包头或终止符与主机 SCI Transmit 模块中指定的内容匹配。
- 如果包头为空，则接收缓冲区中存在的任何内容都将被视为接收的起始点。在数据长度选项为 Variable length 的情况下，如果包头为空，则包尾将从此起始点本身开始计算。
- 如果模块上未提供预期的包头，则 FIFO 中存在的数据被视为接收的起始点，从该点开始将预期检索所需长度的数据和终止符。

### **Additional package terminator** — 指示数据结束 `'E'`（默认） | 字符串 | 字符 | 0 到 255 的数字

位于接收数据包末尾的数据，不属于正在接收的数据，用于指示数据的结束。附加包终止符必须使用 ASCII 字符表示。使用字符串或数字（0–255）。必须为此参数输入的字符串添加单引号，但引号不会被接收或计入总字节数。要指定空值（无包终止符），仅输入两个单引号。

终止符的数据类型与模块上提到的数据类型无关。

### **Number of retries for header receive check** — 包头接收检查的自定义重试次数 `16`（默认） | `正整数，有限` | `标量`

此参数确保检查预期包头作为接收数据的一部分。

当数据接收到 FIFO 中时，模块逐个验证接收数据中的包头。如果数据与包头不匹配，模块将丢弃该数据并继续在下一个数据中查找包头，直到重试次数用完。

如果包头在重试次数内匹配，则将其视为数据包的起始，后续接收的数据被视为有效数据。

### **Data type** — 输出数据的数据类型 `uint8`（默认） | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32`

输出数据的数据类型。

如果数据以 `uint8` 传输，但 SCI receive 模块输出预期为 `int16/int32`，则假定存在偶数个字节，并且输出以不同的数据类型格式化。如果存在奇数个数据字节，则即使状态显示 **No Error**，最后一个字节也会在格式化中丢失。

### **Data length option** — 模块接收的数据长度 `Length via dialog`（默认） | `Length via input port` | `Variable length`

选择模块的数据长度选项。

- `Length via dialog` - 要接收的数据长度通过 `Data length` 参数提供。
- `Length via input port` - 模块根据输入端口接收的长度接收可变大小数据。如果输入端口接收的长度大于最大数据长度参数中提供的长度，则考虑最大数据长度。
- `Variable length` - 在非阻塞模式下，数据接收直到包尾匹配。确保包尾不作为数据的一部分存在。当只有包头和终止符可用而数据不可用时，状态设置为 **No Error**，可变数据长度设置为零。

  - 如果终止符值直到最大长度都不匹配，或者中间数据不可用，则模块将输出接收到的数据及其长度，状态将设置为 `Partial data available`。
  - 如果未提供终止符值，模块尝试接收 **max data length** 的数据。如果读取的数据长度小于最大长度，或者中间数据不可用，则模块将输出接收到的数据及其长度，状态将设置为 `Partial data available`。
  - 如果未读取数据，则状态设置为 **Data not available**。
  - 当包头和终止符已接收但无数据时，状态读取为 data not available。
  - 在可变长度模式下使用时，应避免将包尾作为 SCI 数据的一部分，因为包尾的存在被视为数据包的结束。
  - 在可变长度模式下，如果未接收到数据，输出数据端口长度为 0。

要启用输入端口 **length**，请选择数据长度选项为 `Length via input port`。

### **Data length** — 模块接收的数据类型数量 `1`（默认） | `正整数，有限` | `标量`

模块接收的 **Data type** 数量（不是字节数）。如果此参数设置为大于 `1`，输出将是向量。确保指定的数据长度与接收数据的 SCI Transmit 模块相同。

#### 依赖

要启用此参数，请将 **Data length option** 参数设置为 `Length via dialog`。

### **Max data length** — 模块接收的最大数据类型数量 `1`（默认） | 正整数，有限 | `正整数，有限`

模块可以接收的 **Data type** 的最大数量（不是字节数）。

如果要接收的数据大小（基于数据长度或最大数据长度、包头、终止符和数据类型）大于 FIFO 大小字节，则将导致数据丢失。

#### 依赖

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Variable length`。

### **Initial output** — 模块的默认输出值 `0`（默认） | 标量 | 向量

SCI Receive 模块的默认输出值。例如，当 **Action taken when connection timeout** 参数设置为 `Output the last received value` 且在接收到数据之前发生连接超时时，将输出此值。

#### 依赖

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`。

### **Action taken when connection times out** — 连接超时时选择输出类型 `Output the last received value`（默认） | `Output custom value`

指定连接超时时输出的内容。如果选择 `Output the last received value`，模块输出最后接收的值。如果尚未接收到值，模块输出 **Initial output** 值。

如果选择 `Output custom value`，请使用 **Output value when connection times out** 参数设置自定义值。

#### 依赖

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`。

### **Output value when connection times out** — 连接超时时模块的自定义输出值 `0`（默认） | 标量 | 向量

设置自定义超时值。

**Output value when connection times out** 参数仅在 **Action taken when connection times out** 参数设置为 `Output custom value` 时可用。

#### 依赖

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`。

### **Sample time** — 从 SCI 设备读取数据的频率 `0.1`（默认） | `-1` | 标量

模块的采样时间，以秒为单位。要异步执行此模块，请将此参数设置为 `-1`。

#### 依赖

要启用此参数，请将 **Data length option** 参数设置为 `Length via dialog` 或 `Variable length`。

当数据长度选项设置为 `Length via input port` 时，采样时间将从输入端口继承属性。

### **Wait until data received** — 等待直到请求的数据可用 `off`（默认） | `on`

- `on` — 如果启用此选项，系统等待直到数据可读（当达到数据长度时）。读取操作在阻塞模式下运行。当模块等待请求的数据时，读取操作被阻塞。如果数据可用，模块输出数据。如果数据不可用，模块等待数据。

  如果下一次读取操作开始时目标硬件仍在等待数据，则会发生任务溢出。

  要修复溢出，请使用 **Sample time** 参数增加时间步长。
- `off` — 如果禁用此选项，系统在每个时间步检查 FIFO（轮询模式）以读取数据。如果数据存在，模块读取并输出内容。如果数据不存在，模块输出最后一个值并继续。当您清除此参数时，读取操作在非阻塞模式下运行。

#### 依赖

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`。

**注意**

当数据长度选项选择为 **Variable length** 时，模块执行将始终在非阻塞模式下进行。

### **Timeout** — 模块等待接收数据的时间量（秒） `inf`（默认） | `大于 0 的正值`

指定如果接收 FIFO 中没有可读数据时，模块在每个时间步应等待的时间量。如果超时，读取操作被中止。

如果值设置为 `inf`，模块无限等待数据在 FIFO 中可用。

**注意**

通过 **Wait until data received** 和 **Timeout** 参数可以实现 3 种模式。

- **阻塞模式** - 在阻塞模式下，参数 **Wait until data received** 已启用，**Timeout** 设置为 `inf`。

  在此模式下，如果 FIFO 中没有可读数据，它将无限等待直到数据可读。
- **带超时的阻塞模式** - 在带超时的阻塞模式下，参数 **Wait until data received** 已启用，**Timeout** 设置为 `任何有限值 > 0`。

  在此模式下，如果 FIFO 中没有可读数据，它将检查 FIFO 状态直到提到的超时值。如果在该时间内 FIFO 中没有可读数据，则 SCI Receive 模块将输出状态为 `timeout`。
- **非阻塞模式** - 在非阻塞模式下，参数 **Wait until data received** 已禁用。

  在此模式下，如果 FIFO 中有可用数据，SCI Receive 模块将读取数据，否则 SCI Receive 模块将输出状态为 `Data not available`。
- 要接收长度超过 FIFO 长度的数据，请使用阻塞模式或带超时的阻塞模式。这确保在读取整个 FIFO 后有额外时间获取 FIFO 中的剩余数据。如果在非阻塞模式下尝试接收大于 FIFO 长度的数据，可能会遇到数据丢失。

  在启用和不启用超时的阻塞模式下，由于等待数据读取，可能会遇到任务溢出。

#### 依赖

要启用此参数，请将 **Data length option** 参数设置为 `Length via input port` 或 `Length via dialog`，并启用参数 `Wait until data received`。

### **Output receiving status** — 串行通信状态 `off`（默认） | `on`

创建 **Status** 模块输出，提供串行通信的状态。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

通过串行通信接口 (SCI) 从主机接收目标上的数据

SCI Receive 模块支持处理器与其他异步外设之间的异步串行数字通信。此模块使用指定的 SCI 硬件模块接收标量或向量数据。

一个模型对于每个模块只能包含一个 SCI Receive 模块。C28x 处理器有四个 SCI 模块 — A、B、C 和 D。可用的 SCI 模块数量因所选处理器而异。您可以通过导航到 **Hardware Implementation** > **Target hardware resources** 来配置 SCI 模块。验证这些设置是否满足您的应用需求。

**注意**

使用类似 SCI 模块模块的串行外部模式会导致冲突检查错误。

该模块以阻塞模式或非阻塞模式输出数据。在阻塞模式下，模型在等待所请求的数据可用时阻塞执行。在非阻塞模式下，模型连续运行。要将模块设置为阻塞模式，请选择 **Wait until data received** 选项。
