---
type: simulink-block
title: 'Serial Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'serialreceive'
documentation_source_path: 'freescalefrdmk64fboard/ref/serialreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Receive

## 端口

### 输出

### **Rx** — 从 UART 端口接收的输出数据向量

在每个采样时间，**Rx** 端口输出使用端口上的 Rx 引脚从 UART 端口读取的值。要指定 Rx 引脚，请转到 **配置参数** > **硬件实现窗格** > **UARTx** > **Rx Pin**。

该端口输出大小在 **Data length (N)** 参数中指定的数据向量。有关详细信息，请参阅从 UART 端口接收数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 判断在给定时步是否接收到请求的数据 标量

选择 **Output status** 参数时，`Status` 端口变为可用。当接收的数据长度大于或等于 **Data length (N)** 参数中指定的长度时，该端口输出 `0`。值 `0` 表示读取操作成功。

否则，它输出 `32`，指示没有新数据可用。

#### 依赖关系

只能在非阻塞模式下选择显示读取操作的状态。要启用非阻塞模式，请清除 **Wait until data received** 参数，然后选择 **Output status** 参数。

**数据类型：** `uint8`

## 参数

### **UART** — 用于串行通信的 UART 端口 `0` (默认值) | `1` | `2` | `3`

选择模块从中读取数据的板上的 UART 端口。在每个采样时间，模块上的 `Rx` 端口输出使用端口上的 Rx 引脚从 UART 端口读取的值。要指定 Rx 引脚，请转到 **配置参数** > **硬件实现窗格** > **UARTx** > **Rx Pin**。

### **Data type** — 从 UART 端口读取的数据的数据类型 `uint8` (默认值) | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

选择模块从 UART 端口接收数据时采用的数据类型。

### **Data length (N)** — 从 UART 端口读取的数据长度 `10` (默认值) | 大于或等于 0 的任意整数

指定要在每个采样时间接收的数据长度。

### **Wait until data received** — 等待直到请求的数据可用 off (默认值) | on

- `on` — 选择此参数时，读取操作以 **阻塞模式** 运行。读取操作在等待请求的数据可用时被阻塞。如果数据可用，`Rx` 端口输出数据。如果数据不可用，`Rx` 端口等待数据。`Status` 端口处于隐藏状态。

  如果当下一次读取操作计划开始时，目标硬件仍在等待数据可用，则会发生任务超限。

  要解决超限：

  - 通过使用 **Sample time** 参数增大时间步。
  - 通过使用 **Data length (N)** 参数减少请求的数据长度。
- `off` — 清除此参数时，读取操作以 **非阻塞模式** 运行。读取数据时，如果数据不可用，`Rx` 端口输出零。`Status` 端口输出 `32`，指示没有新数据可用。

### **Output status** — 用于显示读取操作状态的选项 on (默认值) | off

选择此参数时，`Status` 端口变为可用。

当接收的数据长度大于或等于您在 **Data length (N)** 参数中指定的长度时，该端口输出 `0`。值 `0` 表示读取操作成功。

否则，它输出 `32`，指示没有新数据可用。

#### 依赖关系

只能在非阻塞模式下选择显示读取操作的状态。要启用非阻塞模式，请清除 **Wait until data received** 参数，然后选择 **Output status** 参数。

### **Sample time** — 从 UART 端口读取数据的频率 `0.1` (默认值)

指定模块从 UART 端口读取数据的频率。将此参数指定为`-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

### 从 UART 端口接收数据

本节说明输出端口处的值，其中以下模块参数设置为：

| 模块参数 | 值 |
| --- | --- |
| **Data type** | `uint8` |
| **Data length (N)** | `4` |

输出端口处的值取决于接收的数据长度是小于、大于还是等于请求的数据长度。

- 接收的数据长度 = Data length (N)：`Rx` 端口输出大小在 **Data length (N)** 参数中指定的数据向量。

  假设指定的 **Data length (N)** 参数为 4，接收的数据长度也为 4。

  在这种情况下，端口输出大小为 4 的数据向量，其中填充有接收数据中的字节。
- 接收的数据长度 < Data length (N)：`Rx` 端口输出大小在 **Data length (N)** 参数中指定且填充有零的数据向量。

  假设指定的 **Data length (N)** 参数为 4，接收的数据长度为 3 字节。

  在阻塞模式下，读取操作在等待第四个字节可用时被阻塞。

  在非阻塞模式下，端口输出大小为 4 的数据向量。该向量中的所有空位都用零填充。
- 接收的数据长度 > Data length (N)：`Rx` 端口输出大小在 **Data length (N)** 参数中指定的数据向量。该向量仅包含接收数据的前 *N* 个字节。其余数据字节将被丢弃。

  假设指定的 **Data length (N)** 参数为 4，接收的数据长度为 5 字节。在这种情况下，端口输出大小为 4 的数据向量。该向量仅包含接收数据的前 4 个字节。其余数据字节将被丢弃。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

从 UART 端口读取数据

Serial Receive 模块从板上的通用异步收发器 (UART) 端口读取数据。

要选择 UART 端口，请使用 **UART** 参数。

模块使用端口上的 Rx（接收）引脚从 UART 端口读取值。要指定 Rx 引脚，请转到 **配置参数** > **硬件实现窗格** > **UARTx** > **Rx Pin**。

在外部模式仿真期间，模块输出目标硬件上运行的可执行文件的结果。

在所有其他模式的仿真期间，模块输出零。

您可以选择以阻塞或非阻塞模式读取数据。
