---
type: simulink-block
title: 'Encoder'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Motor and Vehicle Sensors'
documentation_page: 'encodersensors'
documentation_source_path: 'supportpkg/arduino_ref/encodersensors.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder

## 端口

### 输入

### **Port\_1** — 用于重置编码器读数的外部信号 scalar

使用此输入端口重置 Encoder 模块的 tick 计数器。

当输入端口处信号的值是 `0` 时，模块输出它从编码器读取的总 tick 计数。在这种情况下，模块输出与 `No reset` 模式下相同。当输入端口处信号的值是非零值时，模块输出它在你在 **Sample time** 参数中设置的采样时间从编码器读取的 tick 数。在这种情况下，模块输出与 `Reset at each Sample time` 模式下相同。

#### 依赖项

要启用此端口，请将 **Reset mode** 设置为 `Reset
by external signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Tick** — 旋转电机的增量位置 scalar

模块以 tick 为单位输出旋转电机位置的相对变化。你可以根据先前和当前 tick 计数以及你在 Reset mode 参数中选择的模式确定旋转方向。例如，在 `No reset` 模式下，先前 tick 计数为 `30`，当前 tick 计数为 `20` 时，电机正在沿逆时针方向运动。

**数据类型：** `int16`

## 参数

### **Input A** — Arduino 硬件的引脚 `2`（默认） | External Interrupt 模块支持的引脚

选择 Arduino 板上已连接编码器输出 A 的引脚。

### **Input B** — Arduino 硬件的引脚 `3`（默认） | External Interrupt 模块支持的引脚

选择 Arduino 板上已连接编码器输出 B 的引脚。

### **Reset mode** — 重置模块输出 `No reset`（默认） | `Reset at each Sample time` | `Reset at external signal`

模块支持三种重置模式。

- `No reset` — 模块输出它从编码器读取的总 tick 计数。
- `Reset at each Sample time`  — 模块输出它在你在 **Sample time** 参数中设置的采样时间从编码器读取的 tick 数。
- `Reset by external signal` — 当你将该参数设置为此模式时，输入端口变为可用。在此模式下，当输入端口处信号的值是 `0` 时，模块输出与 `No reset` 模式下相同。当输入端口处信号的值是非零值时，模块输出与 `Reset at each sample time` 模式下相同。

假设你已连接到 Arduino 硬件的编码器轮有 90 个槽，这意味着编码器每旋转 4 degrees 的 tick 计数为 1。假设模块采样时间为 1 second，并且时间点 *T* = 0 时的 tick 计数为 0。此表显示了模块在三种模式下输出的 tick 计数。

Arduino 重置模式图像

- 在 *T* = 0 和 *T* = 1 之间，假设编码器顺时针旋转 20 degrees。

  - `No reset` — 输出为 20/4 = 5
  - `Reset at each sample time` — 假设编码器在给定采样时间已旋转 20 degrees，因此输出为 20/4 = 5
  - `Reset by external signal` — 假设外部信号的值为 0，因此计数按 `No reset` 模式计算，输出为 20/4 = 5
- 在 *T* = 1 和 *T* = 2 之间，假设编码器顺时针旋转 40 degrees。

  - `No reset` — 在此模式下，模块在任何时间点的输出都是先前计数与当前计数之和，因此输出为 5+40/4 = 15
  - `Reset at each sample time` — 假设编码器在给定采样时间已旋转 40 degrees，因此输出为 40/4 = 10
  - `Reset by external signal` — 假设外部信号的值为 0，因此模块按 `No reset` 模式计算计数，输出为 5+40/4 = 15
- 在 *T* = 3 和 *T* = 4 之间，假设编码器逆时针旋转 20 degrees。

  - `No reset` — 在此模式下，模块在任何时间点的输出都是先前计数与当前计数之和，因此输出为 30–20/4 = 25
  - `Reset at each sample time` — 假设编码器在给定采样时间已逆时针旋转 20 degree，因此输出为 – 20/4 = – 5
  - `Reset by external signal` — 假设外部信号的值为非零值，因此模块按 `Reset at each sample time` 模式计算计数，输出为 – 20/4 = – 5

### **Sample time** — 模块从编码器读取数据的时间 `-1`（默认） | scalar

输入模块从编码器读取值的时间间隔，以 seconds 为单位。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2021b 中引入**

## 描述

测量旋转电机的增量位置和方向

Encoder 模块输出来自连接到 Arduino® 板的旋转电机上正交编码器的 tick 计数。编码器 tick 计数的每次递增表示电机正在顺时针旋转。编码器 tick 计数的每次递减表示电机正在逆时针旋转。总 tick 计数表示旋转电机的增量位置。

你可以使用模块参数对话框中的 **Reset mode** 参数重置来自模块的编码器读数。

在没有硬件的情况下进行仿真时，此模块输出零。有关详细信息，请参阅“在仿真中模块产生零或不执行任何操作”。

**注意**

Encoder 模块目前不支持 Arduino Nano 33 BLE Sense 板上的 connected IO 工作流。
