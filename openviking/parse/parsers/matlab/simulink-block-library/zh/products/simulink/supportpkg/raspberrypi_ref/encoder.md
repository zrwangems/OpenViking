---
type: simulink-block
title: 'Encoder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'encoder'
documentation_source_path: 'supportpkg/raspberrypi_ref/encoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder

## 端口

### 输入

### **Port\_1** — 用于复位编码器读数的外部信号，标量

使用此输入端口复位 Encoder 模块的 tick 计数器。

当输入端口处的信号值为 `0` 时，模块输出从编码器读取的总 tick 计数。在这种情况下，模块输出与 `No reset` 模式相同。当输入端口处的信号值为非零值时，模块输出在给定采样时间从编码器读取的 tick 数。在这种情况下，模块输出与 `Reset at each Sample time` 模式相同。

#### 依赖关系

要启用此端口，请将 **Reset mode** 设置为 `Reset by external signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Tick** — 旋转电机的增量位置，标量

模块以 tick 为单位输出旋转电机位置的相对变化。您可以根据前一个和当前 tick 计数以及所选的 Reset mode 判断电机的旋转方向。例如，在 `No reset` 模式下，前一个 tick 计数为 `30`、当前 tick 计数为 `20` 时，电机沿逆时针方向运动。

**数据类型：** `int16`

## 参数

### **Board** — Raspberry Pi 硬件板 `Pi 4 Model B`（默认）| `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

选择您的 Raspberry Pi 硬件板。您可以在目标硬件、产品包装或产品文档上找到此信息。

### **Input A** — 硬件的 GPIO 引脚 GPIO 20（默认）| GPIO 引脚 4 – 19 或 GPIO 引脚 21 – 27

选择 Raspberry Pi 硬件板上编码器输出 A 所连接的 GPIO 引脚。

### **Input B** — 硬件的 GPIO 引脚 GPIO 21（默认）| GPIO 引脚 4 – 19 或 GPIO 引脚 21 – 27

选择 Raspberry Pi 硬件板上编码器输出 B 所连接的 GPIO 引脚。

### **Reset mode** — 复位模块输出 `No reset`（默认）| `Reset at each Sample time` | `Reset at external signal`

模块支持三种复位模式。

- `No reset` — 模块输出从编码器读取的总 tick 计数。
- `Reset at each Sample time` — 模块输出在给定采样时间从编码器读取的 tick 数。
- `Reset by external signal` — 当您将参数设置为此模式时，输入端口将变为可用。在此模式下，当输入端口处的信号值为 `0` 时，模块输出与 `No reset` 模式相同。当输入端口处的信号值为非零值时，模块输出与 `Reset at each sample time` 模式相同。

假设连接到硬件的编码器轮有 90 个槽，这意味着每旋转 4 度编码器 tick 计数为 1。假设模块采样时间为 1 秒，并且在时间点 *T* = 0 时的 tick 计数为 0。下表显示了模块在三种模式下输出的 tick 计数。

Raspberry Pi 复位模式图像

- 在 *T* = 0 和 *T* = 1 之间，假设编码器顺时针旋转 20 度。每种模式下的输出为：

  - `No reset` — 输出为 20 / 4 = 5
  - `Reset at each sample time` — 假设编码器在给定采样时间已旋转 20 度，因此输出为 20 / 4 = 5
  - `Reset by external signal` — 假设外部信号的值为 0，因此按 `No reset` 模式计算计数，输出为 20 / 4 = 5
- 在 *T* = 1 和 *T* = 2 之间，假设编码器顺时针旋转 40 度。每种模式下的输出为：

  - `No reset` — 在此模式下，模块在任何时间点的输出都是前一个计数与当前计数之和，因此输出为 5 + 40 / 4 = 15
  - `Reset at each sample time` — 假设编码器在给定采样时间已旋转 40 度，因此输出为 40 / 4 = 10
  - `Reset by external signal` — 假设外部信号的值为 0，因此按 `No reset` 模式计算计数，输出为 5 + 40 / 4 = 15
- 在 *T* = 3 和 *T* = 4 之间，假设编码器逆时针旋转 20 度。每种模式下的输出为：

  - `No reset` — 在此模式下，模块在任何时间点的输出都是前一个计数与当前计数之和，因此输出为 30 – 20 / 4 = 25
  - `Reset at each sample time` — 假设编码器在给定采样时间已逆时针旋转 20 度，因此输出为 – 20 / 4 = – 5
  - `Reset by external signal` — 假设外部信号的值为非零值，因此按 `Reset at each sample time` 模式计算计数，输出为 – 20 / 4 = – 5

### **Sample time** — 模块从编码器读取数据的时间 `-1`（默认）| 标量

输入模块从编码器读取值的时间间隔（秒）。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

测量旋转电机的增量位置和方向

Encoder 模块输出连接到 Raspberry Pi® 硬件板的旋转电机上正交编码器的 tick 计数。编码器 tick 计数的每次递增表示电机正在顺时针旋转。编码器 tick 计数的每次递减表示电机正在逆时针旋转。总 tick 计数表示旋转电机的增量位置。

您可以使用模块参数对话框中的 **Reset mode** 参数复位模块的编码器读数。

在没有硬件的情况下进行仿真时，此模块输出零。有关详细信息，请参阅模块在仿真中产生零或不执行任何操作。
