---
type: simulink-block
title: 'Quadrature Encoder'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'quadratureencoder'
documentation_source_path: 'freescalefrdmk64fboard/ref/quadratureencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Quadrature Encoder

## 端口

### 输入

### **Port\_1** — 指定何时将编码器读数复位的输入信号（标量）

当您将 **Reset mode** 参数设置为 `Reset by external signal` 时，将出现一个输入端口。

tick 计数会根据此端口处的输入值复位为 0。当向模块输入发送非 0 值时，tick 计数复位为 0。对于每个采样周期，模块输出自上次复位以来的编码器读数。

当外部信号为 0 时，tick 计数按与 `No reset` 模式相同的方式计算。当外部信号非零时，tick 计数按与 `Reset at each sample time` 模式相同的方式计算。有关复位模式的详细信息，请参见 **Reset mode** 参数说明。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Tick** — 编码器的角位置，以 ticks 为单位（标量）

该端口输出编码器位置的相对变化量，以 ticks 为单位。当顺时针旋转编码器时，tick 计数增加。当逆时针旋转编码器时，tick 计数减少。

**数据类型：** `int16`

### **Dir** — 编码器的旋转方向（标量）

当顺时针旋转编码器时，该端口输出 1。当逆时针旋转编码器时，该端口输出 0。

#### 依赖项

仅当您选择 **Output encoder direction** 参数时，此端口才会出现。

**数据类型：** `uint8`

## 参数

### **Encoding mode** — 用于计算旋转 tick 计数的编码模式 `Quadrature`（默认） | `Count and Direction`

- 您可以选择编码模式来计算旋转 tick 计数。

  - `Quadrature` – 开发板对编码器执行 X4 编码测量。在此类编码中，会对 Phase A 和 Phase B 信号的每个上升沿和下降沿进行计数。

    当 Phase A 超前 Phase B 信号（编码器顺时针旋转）时，对于两个信号的每个上升沿/下降沿，tick 计数增加。当 Phase A 滞后于 Phase B 信号（编码器逆时针旋转）时，对于两个信号的每个上升沿/下降沿，tick 计数减少。
  - `Count and Direction` – Phase A 信号控制计数速率。Phase B 信号控制计数方向。例如，当 Phase B 信号为 HIGH（编码器顺时针旋转）时，对于 Phase A 信号的每个上升沿，tick 计数增加。当 Phase B 信号为 LOW（编码器逆时针旋转）时，对于 Phase A 信号的每个上升沿，tick 计数减少。

### **Output encoder direction** — 指定模块是否输出编码器方向 on（默认） | off

当您选择此参数时，`Dir` 端口变为可用。

当编码器顺时针旋转时，该端口输出 1。当编码器逆时针旋转时，该端口输出 0。

### **Reset mode** — 用于复位编码器读数的复位模式 `No reset`（默认） | `Reset at each sample time` | `Reset by external signal`

- 此模块支持三种不同的复位模式。复位模式在示例表中描述。

  假设连接到开发板的编码器轮有 90 slots。这意味着，编码器每旋转 4 degrees 对应一个 tick 计数。

  假设模块采样时间为 1 second，并且在时刻 T = 0 时 tick 计数为 0。

  - `No reset` – 编码器读数不复位，模块输出总旋转 ticks。

    例如，在表中，在 T = 0 和 T = 1 之间，编码器顺时针旋转 20 degrees。因此，tick 计数为 5。

    在 T = 1 和 T = 2 之间，编码器顺时针旋转 40 degrees，因此在 T = 2 时 tick 计数为 15（来自 T = 1 的 5 加上来自 T = 2 的 10）。

    在此模式下，任意时刻的输出是先前计数与当前计数的累积和。
  - `Reset at each sample time` – 对于每个采样周期，模块输出编码器读数，然后将其复位为 0。

    例如，在表中，在 T = 0 和 T = 1 之间，编码器顺时针旋转 20 degrees。因此，tick 计数为 5。

    在 T = 1 和 T = 2 之间，编码器顺时针旋转 40 degrees，因此 tick 计数为 10。

    在此模式下，输出为给定采样时间处的 tick 计数。
  - `Reset by external signal` – 当您将 **Reset mode** 参数设置为 `Reset by external signal` 时，将出现一个输入端口。

    对于每个采样周期，模块输出自上次复位以来的编码器读数。编码器读数根据此端口处的输入值复位为 0。当向模块输入发送非 0 值时，模块将编码器读数复位为 0。

    例如，在表中，在 T = 0 和 T = 1 之间，编码器顺时针旋转 20 degrees。因此，在 T=1 时 tick 计数为 5。

    在 T = 1 和 T = 2 之间，编码器顺时针旋转 40 degrees。因此，在 T = 2 时 tick 计数为 15（来自 T = 1 的 5 加上来自 T = 2 的 10）。

    在 T = 2 和 T = 3 之间，编码器顺时针旋转 60 degrees。因此，在 T = 3 时 tick 计数为 30（来自 T = 2 的 15 加上来自 T = 3 的 15）。由于在 T=3 时模块输入值为非零值，模块将编码器读数复位为 0。

    在 T = 3 和 T = 4 之间，编码器逆时针旋转 20 degrees。因此，在 T = 4 时 tick 计数为 -5（来自 T = 3 的 0 加上来自 T = 4 的 -5）。

    在此模式下，当外部信号为 0 时，输出按与 `No reset` 模式相同的方式计算。当外部信号非零时，输出按与 `Reset at each sample time` 模式相同的方式计算。

### **Invert Phase A polarity** — 指定模块是否反转 Phase A 信号 off（默认） | on

当您选中此复选框时，模块会在识别 Phase A 信号的上升沿和下降沿之前反转该信号。根据您使用的编码器，您可以选择反转极性。

### **Invert Phase B polarity** — 指定模块是否反转 Phase B 信号 off（默认） | on

当您选中此复选框时，模块会在识别 Phase B 信号的上升沿和下降沿之前反转该信号。根据您使用的编码器，您可以选择反转极性。

### **Sample time** — 从编码器读取值的频率 `0.1`（默认）

指定此模块读取旋转的频率，以 seconds 为单位。

#### 依赖项

仅当您将 **Reset mode** 参数设置为 `No reset` 或 `Reset at each sample time` 时，此参数才会出现。

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

以 ticks 为单位测量编码器的旋转

Quadrature Encoder 模块读取与开发板连接的编码器的旋转 tick 计数和方向。

当顺时针旋转编码器时，tick 计数增加。当逆时针旋转编码器时，tick 计数减少。

使用此模块的参数，指定编码模式、复位模式和相位极性。

在开发板上，Flexible Timer Module (FTM) 外设提供专用引脚，用于来自编码器的 Phase A 和 Phase B 输出信号。

将编码器上的 Phase A 输出引脚连接到开发板上的 PTB18 引脚。将编码器上的 Phase B 输出引脚连接到开发板上的 PTB19 引脚。
