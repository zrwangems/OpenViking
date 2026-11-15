---
type: simulink-block
title: 'Encoder'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Sensors'
documentation_page: 'encoder'
documentation_source_path: 'beagleboneblue/ref/encoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder

## 端口

### 输入

### **Port\_1** — 用于复位编码器读数的输入信号 标量

当输入端口信号的值为 `0` 时，模块输出从编码器读取的总 tick 计数。模块输出与 `No reset` 模式相同。

当输入端口信号的值为非零值时，模块输出在给定采样时间从编码器读取的 tick 数。模块输出与 `Reset at each sample time` 模式相同。

有关复位模式的详细信息，请参阅参数中的 Reset mode。

#### 依赖项

仅当将 **Reset mode** 参数设置为 `Reset by external signal` 时，此端口才会出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Tick** — 旋转电机的增量位置 标量

该端口输出旋转电机位置的相对变化量，以 ticks 为单位。

**数据类型：** `int16`

## 参数

### **Channel** — 硬件上的通道编号 `1`（默认） | `2` | `3` | `4`

选择编码器所连接硬件上的通道。

### **Reset mode** — 用于复位模块输出的复位模式 `No reset`（默认） | `Reset at each sample time` | `Reset by external signal`

此模块支持三种不同的复位模式。

- `No reset` – 模块输出从编码器读取的总 tick 计数。
- `Reset at each sample time` – 模块输出在给定采样时间从编码器读取的 tick 数。
- `Reset by external signal` – 当将 **Reset mode** 参数设置为 `Reset by external signal` 时，将有一个输入端口可用。在此模式下，当输入端口信号的值为 `0` 时，模块输出与 `No reset` 模式相同。当输入端口信号的值为非零值时，模块输出与 `Reset at each sample time` 模式相同。

例如，假设连接到硬件的编码器轮有 90 个槽。这意味着，每旋转 4 度，编码器 tick 计数为 1。假设模块采样时间为 1 秒，并且在时刻 *T* = 0 时 tick 计数为 0。

- `No reset` – 在 *T* = 0 与 *T* = 1 之间，编码器顺时针旋转 20 度。每个 tick 代表 4 度，因此输出为 20 / 4 = `5`。

  在 *T* = 1 与 *T* = 2 之间，编码器顺时针旋转 40 度，因此在 *T* = 2 时输出为 `15`（来自 *T* = 1 的 5 加上来自 *T* = 2 的 10）。

  在此模式下，任何时刻的模块输出都是先前计数与当前计数之和。
- `Reset at each sample time` – 在 *T* = 0 与 *T* = 1 之间，编码器顺时针旋转 20 度。输出为 `5`。

  在 *T* = 1 与 *T* = 2 之间，编码器顺时针旋转 40 度。输出为 `10`。
- `Reset by external signal` – 从 *T* = 0 到 *T* = 2，输入信号的值为 `0`。在此期间，输出与 `No reset` 模式相同。在 *T* = 3 和 *T* = 4 时，输入信号的值变为非零值。在此期间，输出与 `Reset at each sample time` 模式相同。

  在该表中，在 *T* = 0 与 *T* = 1 之间，编码器顺时针旋转 20 度。在 *T* = 1 时输出为 `5`。

  在 *T* = 1 与 *T* = 2 之间，编码器顺时针旋转 40 度。在 *T* = 2 时输出为 `15`（来自 *T* = 1 的 5 加上来自 *T* = 2 的 10）。

  在 *T* = 2 与 *T* = 3 之间，编码器顺时针方向旋转 60 度。在 *T* = 3 时输出为 `30`（来自 *T* = 2 的 15 加上来自 *T* = 3 的 15）。

  在 *T* = 3 与 *T* = 4 之间，编码器逆时针旋转 20 度。在 *T* = 3 时，输入信号的值变为非零值。在 *T* = 4 时输出为 `–5`（来自 *T* = 3 的 0 加上来自 *T* = 4 的 –5）。

### **Sample time** — 从编码器读取值的频率 `0.1`（默认）

指定模块从编码器读取 tick 计数的频率，以秒为单位。

#### 依赖项

仅当将 **Reset mode** 参数设置为 `No reset` 或 `Reset at each sample time` 时，此参数才会出现。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

测量旋转电机的增量位置和方向

Encoder 模块输出连接到 BeagleBone® Blue 的旋转电机上正交编码器的 tick 计数。编码器 tick 计数的每次递增表示电机正在顺时针旋转。编码器 tick 计数的每次递减表示电机正在逆时针旋转。tick 计数总量表示旋转电机的增量位置。

使用“模块参数”对话框中的 **Reset mode** 参数，可以复位模块输出的编码器读数。有关复位模式的详细信息，请参阅参数中的 Reset mode。

在没有硬件的情况下进行仿真期间，此模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。
