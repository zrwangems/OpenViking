---
type: simulink-block
title: 'Serial Receive'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'serialreceive'
documentation_source_path: 'px4/ref/serialreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Receive

## 端口

### 输出

### **Data** — 从 UART 或 USART 端口接收的数据向量

在每个采样时间，**Data** 端口输出从 UART 或 USART 端口读取的值。

该端口输出大小由 **Data length (N)** 参数指定的数据向量。

有关详细信息，请参阅从串口接收数据

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 确定在给定时步是否接收到请求的数据标量

当接收到的数据长度大于或等于 **Data length (N)** 参数指定的长度时，**Status** 端口输出 `0`。值 `0` 表示读取操作成功。

否则，它输出 `1`，表示没有新数据可用。

#### 依赖项

在非阻塞模式下，如果选中 **Output partially received data** 选项，则 **Status** 端口不可用

**数据类型：** `uint8`

### **Length** — 接收到的数据字节数标量

**Length** 端口输出接收消息中的数据字节数。有关详细信息，请参阅从串口部分接收数据。

#### 依赖项

仅当选中 **Output partially received data** 选项时，此输出才可用。

**数据类型：** `uint8`

## 参数

#### 主选项卡

### **Port** — 用于串行通信的 UART 或 USART 端口 `/dev/ttyACM0`（默认） | `/dev/ttyS1` | `/dev/ttyS2` | `/dev/ttyS3` | `/dev/ttyS5` | `/dev/ttyS6`

输入板子上 UART 或 USART 端口的名称，模块从该端口读取数据。要查看 UART/USART 端口与 Pixhawk 飞行控制器上标签之间的映射，请参阅 Serial Port Names and Corresponding Labels on PX4 Flight Controller Boards。

### **Data type** — 从 UART 或 USART 端口读取的数据的数据类型 `uint8`（默认） | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

选择模块从 UART 或 USART 端口接收数据时使用的数据类型。

### **Data length (N)** — 从 UART 或 USART 端口读取的数据长度 `1`（默认） | 大于或等于 0 的任意整数

指定每个采样时间要接收的数据长度。

### **Sample time** — 从 UART 或 USART 端口读取数据的频率 `0.1`（默认）

指定模块从 UART 端口读取数据的频率。将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

#### 高级选项卡

### **Wait until data received** — 等待直到请求的数据可用 off（默认） | on

- `on` — 选中此参数时，读操作在 **阻塞模式** 中运行。读操作在等待请求的数据可用时被阻塞。如果数据可用，`Data` 端口输出数据。如果数据不可用，`Data` 端口等待数据。

  如果目标硬件在计划开始下一次读操作时仍在等待数据可用，则会发生任务超限。

  要解决超限：

  - 使用 **Sample time** 参数增大时间步长。
  - 使用 **Data length (N)** 参数减少请求的数据长度。
- `off` — 清除此参数时，读操作在 **非阻塞模式** 中运行。读取数据时，如果数据不可用，`Data` 端口输出零。`Status` 端口输出 `32`，指示没有新数据可用。

### **Timeout in seconds** — 等待直到收到数据的时间 `5`（默认） | (0, 2^32/1000]

如果选中 **Wait until data received** 参数，则指定模块在每个时间步等待数据的时间量。如果发生超时，读操作将中止。

#### 依赖项

仅当选中 **Wait until data received** 参数时，此参数才会出现。

### **Output partially received data** — 即使在采样时间没有完整数据可用也输出数据 off（默认） | on

- `on` — 选中此参数时，`Data` 端口在采样时间输出部分接收的数据。
- `off` — 清除此参数时，`Data` 端口等待下一个采样时间，以便接收到整个 Data Length (N) 的数据，然后才提供输出。

#### 依赖项

仅当 **Wait until data received** 选项未选中（非阻塞模式）时，此参数可见。有关详细信息，请参阅从串口部分接收数据。

### 从串口部分接收数据

此示例描述当接收到的消息长度小于、大于或等于请求的数据长度时，`Length` 输出端口的值。本节说明在非阻塞模式下，选中 **Output partially received data** 选项，且 **Data type** 设置为 `uint8`、**Data size (N)** 设置为 `4` 时输出端口的值。

- 接收的数据长度 = Data length (N)：`Data` 端口将消息输出为大小由 **Data size (N)** 参数指定的数据向量。

  假设指定的 **Data size (N)** 参数为 4，并且接收到的消息长度也为 4。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量，其中填充消息的数据字节，`Length` 端口输出 `4`。
- 接收的数据长度 < Data length (N)：`Data` 端口将消息输出为大小由 **Data size (N)** 参数指定的数据向量。向量中的所有空余位置都用零填充。

  假设指定的 **Data size (N)** 参数为 4，接收到的数据长度为 3 字节。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量。向量中的前三个数据字节是来自接收消息的字节；剩余位置用零填充。`Length` 端口输出 `3`。
- 接收的数据长度 > Data length (N)：`Data` 端口输出大小由 **Data size (N)** 参数指定的数据向量。该向量仅包含消息中的前 *N* 个数据字节。剩余数据字节留在缓冲区中。

  假设指定的 **Data length (N)** 参数为 4，接收到的数据长度为 5 字节。在这种情况下，该端口输出大小为 4 的数据向量。向量仅包含接收数据中的前 4 个字节。剩余数据字节留在缓冲区中。`Length` 端口输出 `4`。

### 从串口接收数据

此示例描述当接收到的消息长度小于、大于或等于请求的数据长度时，`Status` 输出端口的值。本节说明在阻塞和非阻塞模式下，**Data type** 设置为 `uint8`、**Data size (N)** 设置为 `4` 时输出端口的值。

- 接收的数据长度 = Data length (N)：`Data` 端口将消息输出为大小由 **Data size (N)** 参数指定的数据向量。

  假设指定的 **Data size (N)** 参数为 4，并且接收到的消息长度也为 4。

  在这种情况下，对于阻塞和非阻塞模式，`Data` 端口输出大小为 4 的数据向量，其中填充消息的数据字节，`Status` 端口输出 `0`。
- 接收的数据长度 < Data length (N)：`Data` 端口将消息输出为大小由 **Data size (N)** 参数指定的数据向量。向量中的所有空余位置都用零填充。

  假设指定的 **Data size (N)** 参数为 4，接收到的数据长度为 3 字节。

  对于非阻塞模式，`Data` 端口输出大小为 4 的数据向量。向量中的前三个数据字节是来自接收消息的字节。剩余位置用零填充。`Status` 端口输出 `1`。

  对于阻塞模式，模块会等待，直到所有数据字节在 `Timeout` 参数指定的时间内被接收。如果在超时时间内未收到第四个数据字节，`Data` 输出零，`Status` 端口输出 `1`。三个已接收的数据字节留在缓冲区中。
- 接收的数据长度 > Data length (N)：`Data` 端口输出大小由 **Data size (N)** 参数指定的数据向量。该向量仅包含消息中的前 *N* 个数据字节。剩余数据字节留在缓冲区中。

  假设指定的 **Data length (N)** 参数为 4，接收到的数据长度为 5 字节。在这种情况下，对于阻塞和非阻塞模式，该端口输出大小为 4 的数据向量。向量仅包含接收数据中的前 4 个字节。剩余数据字节留在缓冲区中。`Status` 端口输出零。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

从 PX4 飞行控制器上的 UART 或 USART 端口读取数据

Serial Receive 模块从 PX4® 飞行控制器上的 Universal Asynchronous Receiver Transmitter (UART) 端口或 Universal Synchronous and Asynchronous Receiver Transmitter (USART) 端口读取数据。

该模块从指定的 UART 或 USART 端口读取值，并将接收到的值输出为 N×1 数组。每个串行通信端口的属性在 Simulink® 的 Configuration Parameters 对话框中说明（转到 **Configuration Parameters**  > **Hardware Implementation** > **/dev/tty**\* 窗格）。

在外部模式仿真期间，该模块输出在目标硬件上运行的可执行文件的结果。

在普通模式仿真期间，该模块输出零。

在 Connected I/O 仿真期间，此模块从硬件的指定串口读取数据。

您可以选择以阻塞或非阻塞模式读取数据。有关详细信息，请参阅从串口部分接收数据和从串口接收数据。

**注意**

如果您使用的是 Cube Orange 自动驾驶仪，则使用 `GPS2` 进行串行数据通信，因为使用 `TELEM1` 或 `TELEM2` 端口可能会出现问题。
