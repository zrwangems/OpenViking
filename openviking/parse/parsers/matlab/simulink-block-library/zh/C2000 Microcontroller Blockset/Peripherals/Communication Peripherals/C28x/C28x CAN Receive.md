---
type: simulink-block
title: 'C28x CAN Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xcanreceive'
documentation_source_path: 'ref/c28xcanreceive.html'
language: zh-CN
chinese_source: official
---

# C28x CAN Receive

## 端口

### 输出

### **f()** — 函数调用端口 标量

将函数调用子系统连接到此端口。当收到新消息时，子系统将被执行。

### **Msg** — 消息数据端口 向量

接收到的数据以所选数据类型的元素向量的形式输出。向量长度为 8 字节。当以轮询模式使用该模块时，如果在连续执行该模块之间没有创建新消息，则会重复发送现有消息。

要将 CAN Receive 模块与 CAN Unpack 模块一起使用，请在 `canmsglib` 库中将**数据类型**设置为 **CAN\_MESSAGE\_TYPE**。

**数据类型:** `uint8` | `uint16` | `uint32` | `CAN_MESSAGE_TYPE`

### **len** — 输出消息的长度 标量

接收到的输出消息长度（以字节为单位）。

#### 依赖关系

仅当选择了 **Output message length** 参数时才会显示此端口。

**数据类型:** `uint16`

### **ID** — 输出消息标识符 标量

端口输出接收到的消息的消息标识符。

#### 依赖关系

要启用此端口，请选择 **Output message ID** 参数。

**数据类型:** `uint32`

## 参数

### **模块** — 模块配置的 CAN 模块 **CAN\_A** (默认) | **CAN\_B**

确定由 CAN Receive 模块配置的 CAN 模块。

### **邮箱编号(0–31)** — 设置邮箱号码寄存器 (MBNR) 的值 `0` (默认) | [0 31] 范围内的整数

对于标准 CAN 控制器 (SCC) 模式，请输入 `0` 到 `15` 之间的唯一数字。对于高端 CAN 控制器 (HECC) 模式，请输入 `0` 到 `31` 之间的唯一数字。在 SCC 模式下，编号最高的邮箱发送的邮件具有最高优先级。在 HECC 模式下，只有当两个邮箱的传输优先级 (TPL) 相等时，邮箱号码才决定优先级。

**注意**

在模型中，同一个邮箱号码不能被 CAN Transmit 模块或其他 CAN Receive 模块使用。

### **消息标识符** — 设置消息标识符寄存器 (MID) 的值 bin2dec('111000111') (默认) | 长度为 11 位或 29 位的数字标识符

对于标准帧大小，消息标识符长度为 11 位；对于扩展帧大小，消息标识符长度为 29 位，格式可以是十进制、二进制或十六进制。对于二进制和十六进制格式，分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 来转换条目。

### **消息类型** — 消息标识符类型 **标准(11 位标识符)** (默认) | **扩展(29 位标识符)**

消息标识符类型。

### **启用接受过滤器** — 启用以使用 ID 过滤功能 `off` (默认) | `on`

启用此参数可使用 ID 筛选。ID 过滤取决于 **Message type (Standard or extended)**、**消息标识符**和 **Message identifier mask**。

CAN 模块扫描接收到的消息 ID，并将其与过滤掩码进行比较。通过接收过滤的接收消息将被存储到消息 RAM 中。

**注意**

自检模式下的验收筛选仅支持特定处理器。F2805x/F2806x 及更早的处理器在自检模式下不支持接受筛选。

### **消息标识符掩码** — 标识符掩码 `0` (默认) | `1` | 长度为 11 位或 29 位的数字标识符

对于标准帧大小，**Message identifier mask** 的长度为 11 位；对于扩展帧大小，其长度为 29 位，格式可以是十进制、二进制或十六进制。对于二进制和十六进制格式，分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 来转换条目。

- 0 - 如果 **Message identifier mask** 中的位设置为 `0`，则**消息标识符**中的相应位将不被考虑用于接受过滤。
- 1 - 如果 **Message identifier mask** 中的位设置为 `1`，则**消息标识符**中的相应位将被考虑用于接受过滤。

#### 依赖关系

要启用 **Message identifier mask parameter**，请选择 **Enable acceptance filter**。

### **采样时间** — 邮箱轮询新邮件的频率 `1` (默认) | `-1` | 标量

邮箱收到新邮件时，会触发一个函数调用。如果您只想在新消息到达时更新消息输出，则需要异步执行该模块。要异步执行该模块，请将此参数设置为 `-1`，并选择 **Post interrupt when message is received** 选项。

**注意**

有关设置 CAN 模块定时参数的信息，请参阅 Configuring Timing Parameters for CAN Blocks。

### **数据类型** — 输出消息数据类型 **uint16** (默认) | **uint8** | **uint32** | **CAN\_MESSAGE\_TYPE**

可用选项有：

- **uint8**：向量长度 = 8 个元素
- **uint16**：向量长度 = 4 个元素
- **uint32**：向量长度 = 2 个元素
- **CAN\_MESSAGE\_TYPE**：以结构体形式输出数据。使用 CAN Unpack 模块从结构体中提取数据。

接收到的消息向量长度最多为 8 字节。如果消息小于 8 个字节，则数据缓冲区字节在输出中右对齐。使用 8 字节的数据缓冲区，数据按如下方式解包。

对于 **uint8** 数据，CAN Receive 模块读取寄存器中每个 8 字节的单元，并将 8 位数据输出到八个元素（使用 16 位内存的低部分）。

```
Output[0] = data_buffer[0];
Output[1] = data_buffer[1];
Output[2] = data_buffer[2];
Output[3] = data_buffer[3];
Output[4] = data_buffer[4];
Output[5] = data_buffer[5];
Output[6] = data_buffer[6];
Output[7] = data_buffer[7];
```

对于 **uint16** 数据，CAN Receive 模块读取寄存器中每个 8 字节的单元，并将 16 位数据输出到四个元素。

```
Output[0] = data_buffer[1..0];
Output[1] = data_buffer[3..2];
Output[2] = data_buffer[5..4];
Output[3] = data_buffer[7..6];
```

对于 **uint32** 数据，CAN Receive 模块读取寄存器中每个 8 字节的单元，并将 32 位数据输出到两个元素。

```
Output[0] = data_buffer[3..0];
Output[1] = data_buffer[7..4];
```

例如，如果接收到的消息有两个字节：

```
data_buffer[0] = 0x21
data_buffer[1] = 0x43
```

**uint16** 输出为：

```
Output[0] = 0x4321
Output[1] = 0x0000
Output[2] = 0x0000
Output[3] = 0x0000
```

选择 `CAN_MESSAGE_TYPE` 时，该模块会输出以下结构体数据（在 `can_message.h` 中定义）：

```
struct {

  /* Is Extended frame */
  uint8_T Extended;

  /* Length */
  uint8_T Length;

  /* RTR */
  uint8_T Remote;

  /* Error */
  uint8_T Error;

  /* CAN ID */
  uint32_T ID;

  /*
  TIMESTAMP_NOT_REQUIRED is a macro that will be defined by Target teams
  PIL, if they do not require the timestamp field during code
  generation. By default, timestamp is defined. If the targets do not require
  the timestamp field, they should define the macro TIMESTAMP_NOT_REQUIRED before
  including this header file for code generation.
  */
  #ifndef TIMESTAMP_NOT_REQUIRED
    /* Timestamp */
    double Timestamp;
  #endif

  /* Data field */
  uint8_T Data[8];

};
```

#### 限制

当**数据类型**设置为 **CAN\_MESSAGE\_TYPE** 时，存在以下限制。

- 只有当 CAN 解包直接连接到 CAN Receive 模块，而没有 **function trigger** 和 **Action when message not received** 连接到 `Reset all fields to zero` 时，CAN 解包状态才能用于数据有效性。
- 如果 CAN Receive 模块的 **Action when message not received** 设置为 `Output last received values`，则 CAN 解包状态在任何情况下都将无效。
- 无论是否存在 CAN Unpack 模块，始终使用函数触发器作为状态指示。

### **初始输出** — 在接收数据之前设置输出 `0` (默认) | 整数

接收数据之前的输出值。您可以根据所选的**数据类型**指定初始输出值。

### **Action when message not received** — 当未收到新的 CAN 消息时执行的操作 **输出上次收到的消息** (默认) | `Reset all fields to zero`

当未收到新的 CAN 消息时，请选择一个操作。您可以选择 `Output last message received` 或 `Reset all fields to zero`。

### **输出消息 ID** — 输出消息标识符状态 `off` (默认) | `on`

当您选择 **Output message ID** 参数时，该模块会配置一个输出端口 **ID**。该端口输出输出消息标识符的状态。

#### 依赖关系

要启用 **Output message ID**，请选择 **Enable acceptance filter**。

### **输出消息长度** — 输出消息长度（以字节为单位） `off` (默认) | `on`

发送到 **len** 端口的消息长度（以字节为单位）。如果未选中，则不可见 **len** 端口。

### **消息接收时发出中断** — 收到消息时发布异步中断 `off` (默认) | `on`

选中后，当收到消息时，该模块会发出异步中断。

### **中断线** — 异步中断的中断线 **0** (默认) | **1**

异步中断使用的中断线。此参数的值会设置全局中断掩码寄存器 (CANGIM) 中的第 2 位 (GIL)：

- **1** 将全局中断映射到 CAN1INT 线。
- **0** 将全局中断映射到 CAN0INT 线。

#### 依赖关系

此参数仅在选择 **Post interrupt when message is received** 时显示。

## 所属库

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

增强型控制器局域网接收邮箱

CAN Receive 模块生成源代码，用于通过 CAN 邮箱接收增强型控制器局域网 (CAN) 消息。处理器上的 CAN 模块提供串行通信功能，并有 32 个可配置为接收或发送的邮箱。该模块支持标准格式或扩展格式的 CAN 数据帧。

该模块支持 CAN 或 DCAN，具体取决于 C2000 处理器的类型。

要将 CAN Receive 模块与 CAN Pack 模块一起使用，请在 `canmsglib` 库中将**数据类型**设置为 **CAN\_MESSAGE\_TYPE**。

通过导航至 **硬件实现** > **Target hardware resources**，为特定硬件板配置 CAN 模块。请确认这些设置符合您的应用程序要求。
