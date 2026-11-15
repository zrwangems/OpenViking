---
type: simulink-block
title: 'Serial Transmit'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'serialtransmit'
documentation_source_path: 'freescalefrdmk64fboard/ref/serialtransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Transmit

## 端口

### 输入

### **Tx** — 接受数据并发送到 UART 端口向量

该端口从模型中接受 [Nx1] 或 [1xN] 数组形式的值。

该端口使用端口上的 Tx 引脚将这些值发送到 UART 端口。要为 UART 串行接口指定 Tx 引脚，请转到 **配置参数** > **硬件实现窗格** > **UARTx** > **Tx Pin**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### 输出

### **Status** — 确定输入数据在给定时间步是否发送到 UART 标量

当您选择 **Output status** 参数时，`Status` 端口变为可用。

对于成功的发送操作，该端口输出 `0`。值 `0` 表示输入数据在给定时间步发送到 UART 端口。

对于不成功的发送操作，该端口输出 `32`。值 `32` 表示上一时间步接收到的输入数据未发送。

#### 依赖关系

您只能选择在非阻塞模式下显示发送操作的状态。要在非阻塞模式下运行发送操作，请清除 **Wait until data received** 参数。要使 `Status` 端口可用，请选择 **Output status** 参数，然后单击 **应用**。

**数据类型：** `uint8`

## 参数

### **UART** — 用于串行通信的 UART 端口 `0`（默认）| `1` | `2` | `3`

选择模块将数据发送到的板上的 UART 端口。模块上的 `Tx` 端口使用端口上的 Tx 引脚将这些值发送到 UART 端口。要为 UART 串行接口指定 Tx 引脚，请转到 **配置参数** > **硬件实现窗格** > **UARTx** > **Tx Pin**。

### **Wait until data is sent** — 等待上一时间步接收到的输入数据发送完成 off（默认）| on

- `on` — 选择此参数时，发送操作在 **阻塞模式** 中运行。如果上一时间步接收到的数据已发送，则模块从输入端口接受数据。如果发送操作正在进行，则模块等待数据发送完成，然后从输入端口接受数据。

  如果上一时间接收到的输入数据在计划开始下一次发送操作时尚未发送，则会发生任务超限。要修复超限：

  - 增加模块的采样时间。
  - 减少输入端口的数据长度。
- `off` — 清除此参数时，发送操作在 **非阻塞模式** 中运行。发送数据时，如果上一时间步接收到的数据的传输仍在进行，则给定时间步输入端口处的数据将被丢弃。

#### 依赖关系

选择此参数时，`Status` 端口将隐藏。

### **Output status** — 用于显示写操作状态的选项 off（默认）| on

当您选择此参数时，`Status` 端口变为可用。

对于成功的发送操作，该端口输出 `0`。值 `0` 表示输入数据在给定时间步发送到 UART 端口。

对于不成功的发送操作，该端口输出 `32`。值 `32` 表示上一时间步接收到的输入数据未发送。

#### 依赖关系

您只能选择在非阻塞模式下显示发送操作的状态。要在非阻塞模式下运行发送操作，请清除 **Wait until data received** 参数。要使 `Status` 端口可用，请选择 **Output status** 参数，然后单击 **应用**。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

将串行数据发送到 UART 端口

Serial Transmit 模块将串行数据发送到板上的通用异步收发器 (UART) 端口。

要选择 UART 端口，请使用 **UART** 参数。

要将这些值发送到 UART 端口，请使用端口上的 Tx 引脚。要指定 Tx（发送）引脚，请转到 **配置参数** > **硬件实现窗格** > **UARTx** > **Tx Pin**。

该模块从输入端口处的信号继承数据类型。

在外部模式仿真期间，该模块输出在目标硬件上运行的可执行文件的结果。

在所有其他模式下的仿真期间，该模块输出零。
