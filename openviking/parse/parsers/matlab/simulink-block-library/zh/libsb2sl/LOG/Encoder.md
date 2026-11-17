---
type: simulink-block
title: 'Encoder'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'LOG'
documentation_page: 'encoder'
documentation_source_path: '../simulink/supportpkg/legomindstormsev3_ref/encoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder

## 端口
```yaml
ports:
- name: Port_1
  summary: 用于复位编码器读数的外部信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Tick
  summary: 旋转电机的增量位置 标量
  direction: output
  data_types: int32
```

### 输入

### **Port\_1** — 用于复位编码器读数的外部信号 标量

使用此输入端口复位 Encoder 模块的计数计数器。

当输入端口处的信号值为 `0` 时，模块输出其从编码器读取的总计数。在这种情况下，模块输出与 `No reset` 模式相同。当输入端口处的信号值为非零值时，模块输出其在 **Sample time** 参数中设置的采样时间从编码器读取的计数数。在这种情况下，模块输出与 `Reset at each Sample time` 模式相同。

#### 依赖

要启用此端口，请将 **Reset mode** 设置为 `Reset by external signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Tick** — 旋转电机的增量位置 标量

模块以计数为单位输出旋转电机位置的相对变化。

**数据类型：** `int32`
## 参数
```yaml
parameters:
- name: EV3 brick output port
  summary: EV3 砖的输出端口号 A（默认）| B | C | D
  group: ''
- name: Reset mode
  summary: 复位模块输出 Reset at external signal（默认）| Reset at each sample time | No reset
  group: ''
- name: Sample time
  summary: 模块从编码器读取数据的时间间隔 0.1（默认）| 正整数
  group: ''
```

### **EV3 brick output port** — EV3 砖的输出端口号 `A`（默认）| `B` | `C` | `D`

选择电机所连接的 EV3 砖输出端口。如果您的 Simulink® 模型同时包含 Motor 和 Encoder 模块，请将两个模块中的 **EV3 brick output port** 参数设置为同一端口。

### **Reset mode** — 复位模块输出 `Reset at external signal`（默认）| `Reset at each sample time` | `No reset`

该模块支持三种复位模式。

- `No reset` — 模块输出它从编码器读取的总计数值。
- `Reset at each Sample time` — 模块输出在 **Sample time** 参数中设置的采样时间从编码器读取的计数值。
- `Reset by external signal` — 当您将该参数设置为该模式时，一个输入端口将变为可用。在该模式下，当输入端口处的信号值为 `0` 时，模块输出与 `No reset` 模式相同。当输入端口处的信号值为非零值时，模块输出与 `Reset at each sample time` 模式相同。

假设您连接到 EV3 主机的编码器轮有 90 个槽，这意味着每旋转 4 度编码器计数为 1。假设模块采样时间为 1 秒，且在时刻 *T* = 0 时计数值为 0。下表显示了模块在三种模式下输出的计数值。

LegoEV3 reset mode image

- 在 *T* = 0 和 *T* = 1 之间，假设编码器顺时针旋转 20 度。

  - `No reset` — 输出为 20/4 = 5
  - `Reset at each sample time` — 假设编码器在给定采样时间已旋转 20 度，因此输出为 20/4 = 5
  - `Reset by external signal` — 假设外部信号的值为 0，因此计数按 `No reset` 模式计算，输出为 20/4 = 5
- 在 *T* = 1 和 *T* = 2 之间，假设编码器顺时针旋转 40 度。

  - `No reset` — 在该模式下，模块在任意时刻的输出是先前计数与当前计数之和，因此输出为 5+40/4 = 15
  - `Reset at each sample time` — 假设编码器在给定采样时间已旋转 40 度，因此输出为 40/4 = 10
  - `Reset by external signal` — 假设外部信号的值为 0，因此模块按 `No reset` 模式计算计数，输出为 5+40/4 = 15
- 在 *T* = 3 和 *T* = 4 之间，假设编码器逆时针旋转 20 度。

  - `No reset` — 在该模式下，模块在任意时刻的输出是先前计数与当前计数之和，因此输出为 30–20/4 = 25
  - `Reset at each sample time` — 假设编码器在给定采样时间已逆时针旋转 20 度，因此输出为 – 20/4 = – 5
  - `Reset by external signal` — 假设外部信号的值为非零值，因此模块按 `Reset at each sample time` 模式计算计数，输出为 – 20/4 = – 5

### **Sample time** — 模块从编码器读取数据的时间间隔 `0.1`（默认）| 正整数

指定模块从编码器读取数据的频率。较短的采样时间（例如 `0.01`）可能会产生不可靠的测量结果。

较小的采样时间要求处理器在更短的时间内完成相同数量的指令，这可能导致任务超限。
## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

测量连接到 EV3 砖块的电机的增量位置和方向

使用 Encoder 模块以度为单位测量连接到 EV3 砖块的电机增量车轮旋转。编码器计数值的每次递增表示电机正在顺时针旋转。编码器计数值的每次递减表示电机正在逆时针旋转。总计数表示旋转电机的增量位置。

您可以使用模块参数对话框中的 **Reset mode** 参数从模块重置编码器读数。

您可以将 Motor 模块与 Encoder 模块一起使用。

在没有硬件的仿真期间，此模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。
