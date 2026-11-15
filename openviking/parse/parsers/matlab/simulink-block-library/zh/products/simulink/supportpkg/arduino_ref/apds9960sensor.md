---
type: simulink-block
title: 'APDS9960 Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Proximity Sensors'
documentation_page: 'apds9960sensor'
documentation_source_path: 'supportpkg/arduino_ref/apds9960sensor.html'
language: zh-CN
chinese_source: worker-translation
---

# APDS9960 Sensor

## 端口

### 输出

**Proximity**

### **Proximity** — 邻近数据，范围 [`0`, `255`] 中的正标量

该模块将邻近数据输出为范围 [`0`, `255`] 中的正标量，其中 `0` 表示距离传感器最远的对象，`255` 表示距离传感器最近的对象。

#### 依赖项

要启用此端口：

- 将 **Sensor mode** 设置为 `Proximity`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。

**数据类型：** `uint8`

**Gesture**

### **GFIFO\_U** — 向上方向检测到的手势数据向量

该模块将由传感器检测到的向上方向的手势数据输出为 `1`-by-*N* 向量，其中 *N* 是向上方向手势数量的阈值。

#### 依赖项

要启用此端口：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

**数据类型：** `uint8`

### **GFIFO\_D** — 向下方向检测到的手势数据向量

该模块将由传感器检测到的向下方向的手势数据输出为 `1`-by-*N* 向量，其中 *N* 是向下方向手势数量的阈值。

#### 依赖项

要启用此端口：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

**数据类型：** `uint8`

### **GFIFO\_L** — 向左检测到的手势数据向量

该模块将由传感器检测到的向左方向的手势数据输出为 `1`-by-*N* 向量，其中 *N* 是向左方向手势数量的阈值。

#### 依赖项

要启用此端口：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

**数据类型：** `uint8`

### **GFIFO\_R** — 向右检测到的手势数据向量

该模块将由传感器检测到的向右方向的手势数据输出为 `1`-by-*N* 向量，其中 *N* 是向右方向手势数量的阈值。

#### 依赖项

要启用此端口：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

**数据类型：** `uint8`

**Ambient light and Color**

### **Ambient** — 环境光数据，范围 [`0`, `65535`] 中的正标量

该模块将环境光强度数据输出为范围 [`0`, `65535`] 中的正标量，其中 `0` 表示最低环境光强度，`65535` 表示最高环境光强度。

#### 依赖项

要启用此端口：

- 将 **Sensor mode** 设置为 `Ambient light and Color`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

**数据类型：** `uint16`

### **RGB** — 颜色强度数据向量

该模块将颜色光强度数据输出为 3-by-1 向量。

#### 依赖项

要启用此端口：

- 将 **Sensor mode** 设置为 `Ambient light and Color`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

**数据类型：** `uint16`

**Status**

### **Status** — 输出端口处新数据的可用性，标量

该模块根据您选择的 Sensor mode 将新数据可用性状态输出为标量或值 `0` 和 `1` 的 `1`-by-`2` 向量。

- `0`：表示自上次读取周期以来，传感器的输出端口没有新数据可用。
- `1`：表示自上次读取周期以来，传感器的输出端口有新数据可用。

例如，如果您将 Sensor mode 选择为 `Proximity`，则该模块在端口处输出标量值。类似地，如果您将 Sensor mode 选择为 `Proximity, Ambient light and Color`，则该模块输出 `1`-by-`2` 向量，其中第一个元素对应于 `Proximity` 传感器模式，后一个元素对应于 `Ambient light and Color` 传感器模式。

下表列出了根据您选择的 Sensor mode 在输出端口可用的状态输出。

| 传感器模式 | 状态端口输出 |
| --- | --- |
| `Proximity` | Proximity |
| `Gesture` | Gesture |
| `Ambient light and Color` | Ambient light and Color |
| `Proximity, Ambient light and Color` | - Proximity - Ambient light and Color |
| `Gesture, Ambient light and Color` | - Gesture - Ambient light and Color |

#### 依赖项

要启用此端口，请选择 **Enable status output**。

**数据类型：** `uint8`

## 参数

每个 APDS9960 IMU 传感器模式都有 Basic 和 Advanced 参数。对于您选择的每种传感器模式，您都可以在 **Block Parameters** 对话框的两个选项卡中配置这些参数，以满足您的需求和功能领域。

例如，如果您将 Sensor mode 选择为 `Proximity, Ambient light and Color`，则 **Block Parameters** 对话框的 Basic 和 Advanced 选项卡都将包含适用于 `Proximity, Ambient light and Color` 传感器模式的参数。您可以在两个选项卡中配置这些参数。

### Basic

**通用**

### **I2C module** — I2C 通信模块 `0`（默认）| 标量

指定 Arduino 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的更多信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **Sensor mode** — 传感器模式的类型 `Proximity`（默认）| `Gesture` | `Ambient light and Color` | `Proximity, Ambient light and Color` | `Gesture, Ambient light and Color`

选择传感器的工作模式。

### **Data acquisition mode** — 数据采集模式 `Polling`（默认）| `Interrupt`

选择数据采集模式。

**注意**

在 `Gesture` 模式下，传感器只能以 `Interrupt` 模式采集数据，此时新的手势输入充当中断源。

### **Enable status output** — 输出端口处数据的可用性 off（默认）| on

选择该参数以启用 Status 输出端口。

### **Sample time** — 模块读取数据的时间间隔 `0.1`（默认）| 标量

输入模块从 APDS9960 IMU 传感器读取值的时间间隔，单位为秒。

**Proximity**

### **Interrupt thresholds [low, high]** — 用于生成中断的邻近阈值 `[0, 50]`（默认）| 范围 `[0, 255]` 中的 1-by-2 向量

当邻近值分别高于高中断阈值电平或低于低中断阈值电平时，生成中断。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Proximity`，并将 **Data acquisition mode** 设置为 `Interrupt`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`，并将 **Data acquisition mode** 设置为 `Interrupt`。

### **Interrupt persistence** — 控制邻近中断的速率 `2`（默认）| 正整数

仅当连续的邻近值超出 Interrupt thresholds [low, high] 参数指定的范围时，才置位邻近中断。这可以防止模块生成虚假中断。使用此参数指定在连续多少个超出中断阈值的邻近值之后，模块应生成邻近中断。例如，当您将此参数设置为 `2` 时，当两个连续邻近值超出您在 Interrupt thresholds [low, high] 参数中设置的范围时，模块会生成中断。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Proximity`，并将 **Data acquisition mode** 设置为 `Interrupt`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`，并将 **Data acquisition mode** 设置为 `Interrupt`。

**Gesture**

### **Enter and exit thresholds [enter, exit]** — 用于生成中断的手势阈值 `[40, 30]`（默认）| 范围 `[0, 255]` 中的 1-by-2 向量

设置阈值以确定手势的起点和终点。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

### **FIFO threshold for interrupt** — 手势 FIFO 阈值 `4 datasets`（默认）| `1 dataset` | `8 datasets` | `16 datasets`

当此参数中选择的值等于 FIFO 中可用的数据集数量后，生成手势中断。例如，如果您将此参数设置为 `4 datasets`，则在 FIFO 中有四个数据集可用后，模块会生成手势中断。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

### **Exit persistence** — 控制手势退出的速率 `1st gesture end`（默认）| `2nd gesture end` | `4th gesture end` | `7th gesture end`

仅当连续手势值超出 Enter and exit thresholds [enter, exit] 参数指定的范围时，才置位手势中断。这可以防止模块生成虚假中断。使用此参数指定在连续多少个超出中断阈值的手势值之后，模块应生成手势中断。例如，当您选择 `4th gesture end` 时，在四个连续手势值超出您在 Enter and exit thresholds [enter, exit] 参数中设置的范围后，模块会生成中断。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

**Ambient light and Color**

### **Interrupt thresholds [low, high]** — 用于生成中断的环境光阈值 `[65535, 0]`（默认）| 范围 `[0, 65535]` 中的 1-by-2 向量

当环境光和颜色强度数据分别超过高中断阈值电平或低于低中断阈值电平时，生成中断。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Ambient light and Color`，并将 **Data acquisition mode** 设置为 `Interrupt`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`，将 **Data acquisition mode** 设置为 `Interrupt`，并将 **Interrupt source** 设置为 `Ambient light and Color`。

### **Interrupt persistence** — 控制环境光和颜色中断的速率 `2`（默认）| 正标量

仅当连续超出 Interrupt thresholds [low, high] 的值等于或大于此参数中设置的值时，才向传感器置位环境光和颜色中断。这可以防止模块生成虚假中断。例如，当您将此参数设置为 `2` 时，当两个连续的环境光和颜色值超出您在 Interrupt thresholds [low, high] 参数中设置的范围时，模块会生成中断。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Ambient light and Color`，并将 **Data acquisition mode** 设置为 `Interrupt`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`，将 **Data acquisition mode** 设置为 `Interrupt`，并将 **Interrupt source** 设置为 `Ambient light and Color`。

**Proximity, Ambient light and Color**

### **Interrupt source** — 中断源 `Proximity`（默认）| `Ambient light and Color`

选择传感器的中断源。

#### 依赖项

要启用此参数，请将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`，并将 **Data acquisition mode** 设置为 `Interrupt`。

### Advanced

**Proximity**

### **Gain** — 邻近增益控制 `4x`（默认）| `1x` | `2x` | `8x`

选择邻近数据值的增益。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Proximity`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。

### **Pulse length** — 每个邻近脉冲长度的时间周期 `16 μs`（默认）| `4 μs` | `8 μs` | `32 μs`

选择 IR LED 发射脉冲串中每个脉冲的 ON 时间。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Proximity`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。

### **Pulse count** — 由 LDR 生成的邻近脉冲数量 `8`（默认）| 范围 [`1` 到 `64`] 中的正标量

指定光敏电阻 (LDR) 应生成的脉冲数量。LDR 生成的脉冲数量是脉冲计数值加一。例如，如果您将脉冲计数值设置为 `8`，则 LDR 生成九个脉冲。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Proximity`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。

### **Offsets [UR, DL]** — 右上和左下光电二极管的邻近偏移 `[0, 0]`（默认）| 范围 `[255, 255]` 中的 1-by-2 向量

为右上和左下光电二极管对设置可缩放的内部偏移校正因子。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Proximity`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。

**Proximity, Ambient light and Color**

### **LED drive strength** — 控制 LED IR 发射的强度 `100 mA`（默认）| `50 mA` | `25 mA` | `12.5 mA`

选择 LED IR 发射的电流水平以控制强度水平。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Proximity`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。

**Proximity and Gesture**

### **LED boost current** — LED IR 发射的额外强度升压 `100%`（默认）| `150%` | `200%` | `300%`

指定 LED IR 发射的额外电流升压水平，以检测远距离设备。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Proximity`。
- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Proximity, Ambient light and Color`。

**Gesture**

### **Offsets [U, D, L, R]** — 上、下、左、右光电二极管的手势偏移 `[0, 0, 0, 0]`（默认）| 1-by-4 向量 `[255, 255, 255, 255]`

为上、下、左、右光电二极管设置可缩放的内部偏移校正因子。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

### **LED drive strength** — 控制 LED IR 发射的强度 `100 mA`（默认）| `50 mA` | `25 mA` | `12.5 mA`

选择 LED IR 发射的电流水平以控制强度水平。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

### **Gain** — 手势增益控制 `4x`（默认）| `1x` | `2x` | `8x`

选择手势数据值的增益。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

### **Pulse length** — 每个手势脉冲长度的时间周期 `32 μs`（默认）| `4 μs` | `8 μs` | `16 μs`

选择 IR LED 发射脉冲串中每个脉冲的 ON 时间。

#### 依赖项

要启用此参数，

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

### **Pulse count** — 由 LDR 生成的手势脉冲数量 `10`（默认）| 正标量

指定光敏电阻 (LDR) 应生成的脉冲数量。LDR 生成的脉冲数量是脉冲计数值加一。例如，如果您将脉冲计数值设置为 `10`，则 LDR 生成 `11` 个脉冲。

#### 依赖项

要启用此参数：

- 将 **Sensor mode** 设置为 `Gesture`。
- 将 **Sensor mode** 设置为 `Gesture, Ambient light and Color`。

### **等待时间** — 手势检测周期之间的时间 `2.8 ms`（默认） | `0 ms` | `5.6 ms` | `8.4 ms` | `14 ms` | `22.4 ms` | `30.8 ms` | `39.2 ms`

通过选择手势等待时间来延迟脉冲序列重复。此参数控制传感器在手势检测周期之间处于低功耗模式的时长。加入等待时间可降低传感器的功耗，并使数据采集更高效。

#### 依赖关系

要启用此参数：

- 将 **传感器模式** 设置为
  `Gesture`。
- 将 **传感器模式** 设置为 `Gesture, Ambient light
  and Color`。

**环境光和颜色**

### **增益** — 环境光和颜色增益控制 `4x`（默认） | `1x` | `16x` | `64x`

选择环境光和颜色数据值的增益。

#### 依赖关系

要启用此参数：

- 将 **传感器模式** 设置为 `Ambient light and
  Color`。
- 将 **传感器模式** 设置为 `Proximity, Ambient
  light and Color`。
- 将 **传感器模式** 设置为 `Gesture, Ambient light
  and Color`。

### **ADC 积分时间 (ms)** — 控制环境光和颜色模数转换器的积分时间 `219`（默认） | positive scalar

使用此参数指定颜色和环境光光电二极管的数据累积时间。

#### 依赖关系

要启用此参数：

- 将 **传感器模式** 设置为 `Ambient light and
  Color`。
- 将 **传感器模式** 设置为 `Proximity, Ambient
  light and Color`。
- 将 **传感器模式** 设置为 `Gesture, Ambient light
  and Color`。

### **在环境光感测前启用等待** — 在传感器开始读取环境光和颜色之前激活等待功能 off（默认） | on

在传感器开始读取环境光和颜色之前激活等待功能。

#### 依赖关系

要启用此参数：

- 将 **传感器模式** 设置为 `Ambient light and
  Color`。
- 将 **传感器模式** 设置为 `Proximity, Ambient
  light and Color`。
- 将 **传感器模式** 设置为 `Gesture, Ambient light
  and Color`。

### **等待时间 (ms)** — 传感器开始读取环境光和颜色之前的等待时间 `246`（默认） | positive scalar

输入传感器开始读取环境光和颜色之前的等待时间。

#### 依赖关系

要启用此参数，请选择 **在环境光感测前启用等待**。

### **启用长等待 (12x)** — 将等待时间增加 12x off（默认） | on

启用此参数可将等待时间 (ms) 参数中设置的等待时间增大为原来的 12 倍。

#### 依赖关系

要启用此参数：

- 将 **传感器模式** 设置为 `Ambient light and
  Color`。
- 将 **传感器模式** 设置为 `Proximity, Ambient
  light and Color`。
- 将 **传感器模式** 设置为 `Gesture, Ambient light
  and Color`。

## 所属库

Simulink Support Package for Arduino Hardware / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

从 APDS9960 I2C 传感器读取接近、手势、环境光和 RGB 颜色数据

APDS9960 Sensor 模块检测接近，提供用于解码手势的方向数据，并测量与 Arduino® 硬件连接且采用中断驱动 I2C 通信的 APDS9960 传感器中的环境光和颜色 (RGB) 值。您可以使用轮询模式或中断模式从 APDS9960 I2C 传感器采集数据。

**注意**

对于 `Interrupt` 数据采集模式，请将该模块放置在 External Interrupt block 的函数调用子系统中。

**注意**

如果您使用的是 Arduino Nano 33 BLE Sense 硬件（其始终包含一个嵌入式传感器），则不支持从包含 APDS9960 传感器的转接板读取数据。
