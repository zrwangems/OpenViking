---
type: simulink-block
title: 'Serial Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Communication'
documentation_page: 'serialread'
documentation_source_path: 'nvidia/ref/serialread.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Read

## 端口

### 输出

### **Data** — 用于读取数据的输出端口 [Nx1] 数组

该数据端口用于模块从串行设备读取数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — 读取操作的状态 `scalar`

此输出端口显示读取数据的状态。下表列出了可能的状态值及其描述。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `RX_BUSY` |
| `2` | `TX_BUSY` |
| `4` | `PARITY_ERROR` |
| `8` | `FRAME_ERROR` |
| `16` | `BUS_ERROR` |
| `32` | `DATA_NOT_AVAILABLE` |

#### 依赖项

仅当未选中 **Output partially received data** 选项时，此输出端口才可用。

**数据类型：** `uint8`

### **Length** — 接收到的数据字节数 scalar

**Length** 端口输出接收消息中的数据字节数。

#### 依赖项

仅当选中 **Output partially received data** 选项时，此输出才可用。

**数据类型：** `uint8`

## 参数

#### 主选项卡

### **Port** — 将板卡连接到串行设备的端口 `/dev/ttyTHS1`（默认）

将 NVIDIA Jetson 板连接到串行设备的端口。

### **Baudrate (in bits/s)** — 每秒位数 `9600`（默认）| `50` | `75` | `110` | `134` | `150` | `200` | `300` | `600` | `1200` | `1800` | `2400` | `4800` | `19200` | `38400` | `57600` | `115200` | `230400`

选择通过串行线路读取数据的速率。波特率以每秒读取的位数来衡量。

### **Parity** — 添加到数据以检测错误的校验位 `None`（默认）| `Even` | `Odd`

选择要添加到传输数据的校验位。校验位用于检测数据传输中的错误。

- **None** – 此值表示数据传输中不使用校验位进行错误检测。
- **Even** – 如果值为 1 的位数为奇数，则校验位值为 1。如果值为 1 的位数为偶数，则校验位值为 0。
- **Odd** – 如果值为 1 的位数为偶数，则校验位值为 1。如果值为 1 的位数为奇数，则校验位值为 0。

### **Stop bits** — 用于指示数据传输停止的位数 `1`（默认）| `2`

选择用于指示数据传输停止的位数。

### **Data length (N)** — 用于传输的数据长度 `1`（默认）| `scalar`

输入要为所选数据类型从串行设备读取的数据大小。

### **Data type** — 用于传输的数据类型 `uint8`（默认）| `uint16` | `uint32` | `int8` | `int16` | `int32` | `single` | `double`

选择要读取的数据类型。

### **Sample time** — 模块读取数据的时间频率 `0.1`（默认）| `scalar`

指定模块读取串行数据的频率。输入大于零的值。

#### 高级选项卡

### **Wait until data received** — 等待直到请求的数据可用 off（默认）| on

- `on` — 选中此参数时，读取操作以 *阻塞* 模式运行。在等待请求的数据可用期间，读取操作会被阻塞。如果数据可用，`Data` 端口输出数据。如果数据不可用，`Data` 端口等待数据。

  如果在计划开始下一次读取操作时目标硬件仍在等待数据可用，则会发生任务超限。

  要修复超限：

  - 通过使用 **Sample time** 参数增加时间步长。
  - 通过使用 **Data length (N)** 参数减少请求的数据长度。
- `off` — 清除此参数时，读取操作以 *非阻塞* 模式运行。读取数据时，如果数据不可用，`Data` 端口输出零。`Status` 端口输出 `32`，表示没有新数据可用。

### **Timeout in seconds** — 模块等待直到收到数据的时间量 `5`（默认）

如果选中 **Wait until data received** 参数，请指定模块在每个时间步应等待数据的时间量。如果发生超时，读取操作将中止。

#### 依赖项

要启用此参数，请选中 **Wait until data received** 参数。

### **Output partially received data** — 即使在采样时间没有完整数据可用也输出数据 `off`（默认）| `on`

- `on` — 选中此参数时，`Data` 端口在采样时间输出部分接收的数据。
- `off` — 清除此参数时，`Data` 端口在每个采样时间输出零，直到收到请求数量的数据元素。

#### 依赖项

要启用此参数，请清除 **Wait until data received** 参数，以非阻塞模式运行读取操作。有关详细信息，请参阅从串行端口部分接收数据。

### 从串行端口部分接收数据

Serial Read 模块在启用 **Output partially received data** 参数时可以接收部分数据。本节描述当接收到的消息长度小于、大于或等于请求的数据长度时，`Length` 输出端口的值。例如，当 **Data type** 设置为 `uint8` 且 **Data size (N)** 设置为 `4` 时输出端口的值。

- 接收到的数据长度 = Data length (N)：`Data` 端口将消息输出为 **Data size (N)** 参数指定大小的数据向量。

  假设指定的 **Data size (N)** 参数为 `4`，并且接收到的消息长度也为 `4`。

  在这种情况下，`Data` 端口输出大小为 4 的数据向量，其中填充了消息的数据字节，`Length` 端口输出 `4`。

  当接收到的数据长度等于为数据大小 N 指定的值时接收缓冲区
- 接收到的数据长度 < Data length (N)：`Data` 端口将消息输出为 **Data size (N)** 参数指定大小的数据向量。向量中的所有空位都用零填充。

  假设指定的 **Data size (N)** 参数为 `4`，并且接收到的数据长度为 `3` 字节。

  在这种情况下，`Data` 端口输出大小为 `4` 的数据向量。向量中的前三个数据字节是来自接收消息的字节，剩余空间用零填充。`Length` 端口输出 `3`。

  当接收到的数据长度小于为数据大小 N 指定的值时接收缓冲区。缓冲区中的空间用零填充
- 接收到的数据长度 > Data length (N)：`Data` 端口输出 **Data size (N)** 参数指定大小的数据向量。向量仅包含消息中的前 *N* 个数据字节。剩余数据字节留在缓冲区中。

  假设指定的 **Data length (N)** 参数为 `4`，并且接收到的数据长度为 `5` 字节。在这种情况下，该端口输出大小为 `4` 的数据向量。向量仅包含接收数据中的前 `4` 个字节。剩余数据字节留在缓冲区中。`Length` 端口输出 `4`。

  当接收到的数据长度大于为数据大小 N 指定的值时接收缓冲区。额外数据留在缓冲区中

### 从串行端口接收数据

本节描述当接收到的消息长度小于、大于或等于请求的数据长度时，`Status` 输出端口的值。本节说明在阻塞和非阻塞模式下，当 **Data type** 设置为 `uint8` 且 **Data size (N)** 设置为 `4` 时输出端口的值。

- 接收到的数据长度 = Data length (N)：`Data` 端口将消息输出为 **Data size (N)** 参数指定大小的数据向量。

  假设指定的 **Data size (N)** 参数为 `4`，并且接收到的消息长度也为 `4`。

  在这种情况下，对于阻塞和非阻塞模式，`Data` 端口输出大小为 `4` 的数据向量，其中填充了消息的数据字节，并且 `Status` 端口输出 `0`。

  当接收到的数据长度等于为数据大小 N 指定的值时接收缓冲区
- 接收到的数据长度 < Data length (N)：`Data` 端口将消息输出为 **Data size (N)** 参数指定大小的数据向量。向量中的所有空位都用零填充。

  假设指定的 **Data size (N)** 参数为 `4`，并且接收到的数据长度为 `3` 字节。

  对于非阻塞模式，`Data` 端口输出大小为 `4` 的数据向量。向量中的前三个数据字节是来自接收消息的字节。剩余空间用零填充。`Status` 端口输出 `1`。

  对于阻塞模式，模块等待直到在 `Timeout` 参数指定的时间内收到所有数据字节。如果在超时前未收到第四个数据字节，`Data` 输出零，并且 `Status` 端口输出 `1`。接收到的三个数据字节留在缓冲区中。

  接收缓冲区用零填充，直到收到所有数据字节
- 接收到的数据长度 > Data length (N)：`Data` 端口输出 **Data size (N)** 参数指定大小的数据向量。向量仅包含消息中的前 *N* 个数据字节。剩余数据字节留在缓冲区中。

  假设指定的 **Data length (N)** 参数为 4，并且接收到的数据长度为 `5` 字节。在这种情况下，对于阻塞和非阻塞模式，该端口输出大小为 `4` 的数据向量。向量仅包含接收数据中的前 `4` 个字节。剩余数据字节留在缓冲区中。`Status` 端口输出零。

  当接收到的数据长度大于为数据大小 N 指定的值时接收缓冲区。额外数据留在缓冲区中

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从串行端口读取数据

使用 Serial Read 模块从连接到 NVIDIA® Jetson™ 板的串行设备读取数据。

要在 NVIDIA Jetson 板上打开串行引脚映射，请点击 **查看引脚映射** 按钮。有关详细信息，请参阅 NVIDIA Jetson 板的串行端口映射。

在 Monitor and Tune 期间，模块输出目标硬件上运行的可执行文件的结果。在所有其他模式的仿真期间，模块输出零。

您可以选择在阻塞或非阻塞模式下读取数据。有关详细信息，请参阅从串行端口部分接收数据和从串行端口接收数据
