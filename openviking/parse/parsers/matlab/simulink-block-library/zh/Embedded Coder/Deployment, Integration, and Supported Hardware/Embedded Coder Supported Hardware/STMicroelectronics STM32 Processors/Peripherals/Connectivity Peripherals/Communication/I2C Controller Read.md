---
type: simulink-block
title: 'I2C Controller Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2ccontrollerread.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Read

## 端口

### 输出

### **Data** — 来自 I2C 外设设备的数据向量

该端口从板上的 I2C 设备读取向量数据。数据大小是您在 **Data size** 参数中指定的值。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 读取操作的状态标量

该端口按下表所述输出每个读取请求的状态：

**返回状态代码**

| **Status** | 描述 |
| --- | --- |
| `0` | SUCCESS |
| `1` | BUSY |
| `2` | ARBITRATION\_LOST |
| `4` | NO\_ACKNOWLEDGE |
| `8` | BUS\_ERROR |
| `16` | BUS\_NOT\_IN\_USE |

#### 依赖关系

要启用此端口，请选择 **Output error status** 参数。

**数据类型：** `uint8`

## 参数

### **I2C module** — 用于读取数据的 I2C 模块 `I2C1`（默认） | `I2C2` | `I23C` | `...`

指定板上用于从 I2C 外设设备读取数据的 I2C 模块。

### **Peripheral byte order** — I2C 外设设备支持的字节顺序 `BigEndian`（默认） | `LittleEndian`

2 字节顺序选项包括：

- BigEndian - 最高有效字节先通过 I2C 总线发送。
- LittleEndian - 最低有效字节先通过 I2C 总线发送。

### **Peripheral address via** — I2C 的外设地址来源 `Dialog`（默认） | `Inport`

选择 I2C 控制器的外设地址来源。

### **Peripheral address** — 从中读取数据的 I2C 寄存器外设地址 `10`（默认） | `大于或等于 0 的整数`

指定要读取数据的 I2C 外设地址。您可以使用十六进制格式 `hex2dec()` 指定此地址，例如，‘hex2dec(‘20’)’。

### **Enable register access address mode** — 用于从特定 I2C 外设寄存器读取的选项 on（默认） | off

选择此参数时，模块从您在 **peripheral register address** 参数中指定的 I2C 外设寄存器读取数据。

清除此参数时，将显示 **Send no acknowledgment at the end of the transfer** 和 **Remove stop bit at the end of data transfer (Repeated start)** 参数。使用这些参数，您可以根据需求修改读取操作。

### **Register address via** — I2C 的外设寄存器地址来源 `Dialog`（默认） | `Inport`

选择 I2C 控制器的寄存器地址来源。

#### 依赖关系

要启用此参数，请选择 **Enable register access address mode** 参数。

### **Peripheral register address** — 要读取数据的 I2C 外设寄存器地址 `0`（默认） | `0 到 255 之间的整数`

指定要读取数据的 I2C 寄存器地址。

将此地址指定为整数，或使用 `hex2dec()` 以十六进制格式指定，例如，‘hex2dec(‘20’)’。

有关寄存器读/写的详细信息，请参阅 I2C 寄存器读/写。

#### 依赖关系

要启用此参数，请选择 **Enable register access address mode** 参数。

### **Data type** — 来自 I2C 外设设备的数据的数据类型 `uint8`（默认） | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

选择您要从 I2C 外设设备读取的数据类型。

### **Data size (N)** — 要从 I2C 外设设备读取的数据大小 `1`（默认） | `大于或等于 0 的整数`

指定要针对所选数据类型从 I2C 外设设备读取的数据大小。

### **Remove stop bit at the end of data transfer (Repeated start)** — 用于在数据传输结束时移除 STOP 位的选项 off（默认） | on

未选择该参数时，模块发送 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线空闲，可供任何其他 I2C Controller 模块启动新的读/写操作。

选择此参数时，模块发送另一个 START 条件，后跟地址和读/写位。模块递归发送任意数量的 START 条件。这种重复 START 条件允许在不释放总线的情况下对外设设备执行写操作。没有其他 Controller 模块会中断该操作。

#### 依赖关系

要启用此参数，请取消选择 **Enable register access address mode** 参数。

### **Send no acknowledgment at the end of the transfer** — 用于在数据传输结束时发送 Not Acknowledge 位的选项 off（默认） | on

选择此参数时，I2C Controller Read 模块会随最后一个字节向外设设备发送 NACK（Not Acknowledge）位。

当外设设备收到 NACK 时，它会等待来自 I2C Controller 模块的 STOP 条件。控制器模块会生成 STOP 条件以中止传输，或生成重复 START 条件以启动新传输。

取消选择此参数时，I2C Controller Read 模块会在每个字节结束时向外设设备发送 ACK（Acknowledge）位。ACK 表示 I2C Controller Read 模块已准备好从外设设备读取下一个字节。

#### 依赖关系

要启用此参数，请取消选择 **Enable register access address mode** 参数。

### **Output error status** — 用于在数据传输期间显示错误状态的选项 off（默认） | on

选择此参数时，模块配置一个输出端口。模块上的该端口标记为 `Status`，表示模块在该输出端口输出写操作的状态。

模块将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `I2C_BUS_ERROR` |

### **Sample time** — 从 I2C 外设设备读取数据的频率 `-1`（默认）

指定 I2C Controller Read 模块从 I2C 外设设备读取数据的频率。将此参数指定为 `-1` 时，模块将根据模型内该模块的上下文继承其采样时间。

### **Timeout** — 指定完成读取操作的等待时间 `0.001`（默认）

您将 `Timeout` 配置为等待完成读取操作的最长时间（以秒为单位）。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

未在 R2025b 中记录。

## 描述

从 I2C 外设设备或 I2C 外设设备寄存器读取数据

I2C Controller Read 模块从连接到板上的 I2C 外设设备读取串行数据。使用此模块，您可以从 I2C 外设设备上的特定寄存器读取数据。有关 I2C 通信的详细信息，请参阅支持 I2C 通信。

**注意**

您可以在基于 STM32 处理器的板上以 Connected IO 模式运行包含 I2C Controller Read 模块的 Simulink® 模型。有关详细信息，请参阅使用 Connected IO 与硬件通信。
