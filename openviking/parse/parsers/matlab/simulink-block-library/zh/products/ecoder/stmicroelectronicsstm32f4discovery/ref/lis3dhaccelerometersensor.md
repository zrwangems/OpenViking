---
type: simulink-block
title: 'LIS3DH Accelerometer Sensor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Sensors'
documentation_page: 'lis3dhaccelerometersensor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/lis3dhaccelerometersensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LIS3DH Accelerometer Sensor

## 端口

### 输出

### **Acceleration** — 由加速度计向量测量的沿每个轴的加速度

当 FIFO 禁用时，该模块输出加速度，形式为 `1`-by-`3` 向量。当 FIFO 启用时，该模块输出 `n`-by-`3` 向量，其中 `n` 是采样数。每个值表示沿 X、Y 和 Z 轴以 `m/s^2` 为单位的加速度测量值。

#### 依赖关系

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC1 Voltage** — 外部引脚 ADC1 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC1 上的电压。

#### 依赖关系

仅当选择 **Voltage (external input at ADC1)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC2 Voltage** — 外部引脚 ADC2 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC2 上的电压。

#### 依赖关系

仅当选择 **Voltage (external input at ADC2)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC3 Voltage** — 外部引脚 ADC3 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC3 上的电压。

#### 依赖关系

仅当为 **ADC3 input** 参数选择 `Voltage (external input)` 时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **Temperature** — 由 LIS3DH 传感器测量的温度标量

由连接到 STM32 Processors 的 LIS3DH 传感器测量的温度（以 ℃ 为单位）。

#### 依赖关系

仅当为 **ADC3 input** 参数选择 `Temperature` 时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **Acceleration status** — 加速度测量状态 `2` | `0` | `1`

该模块输出加速度测量状态，值为 `0`、`1` 或 `2`。值 `0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`2` 表示数据被覆盖。

如果选择了 **Enable FIFO**，则 `0` 表示已收集指定的样本，`1` 表示未收集指定数量的样本，`2` 表示数据被覆盖。

#### 依赖关系

仅当选择 **Acceleration data ready status** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Samples pending** — 待处理样本数标量

该模块输出要读取的待处理样本数，值范围为 `0-32`。

#### 依赖关系

仅当选择 **Enable FIFO** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Click status [X,Y,Z]** — Click 检测状态 `0` | `1`

该模块将各轴的 Click 状态输出为 `1`-by-`3` 向量（x,y,z），指示在哪个轴上检测到 click。轴值 `1` 表示在该轴上检测到 click，`0` 表示未检测到 click。

#### 依赖关系

仅当选择 **click status** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Inertial wake-up status [X,Y,Z]** — 惯性唤醒中断状态 `0` | `1`

该模块将惯性唤醒状态输出为 `1`-by-`3` 向量。它提供在哪个轴上检测到惯性唤醒的信息。值 `1` 表示在所选轴上检测到惯性唤醒事件，值 `0` 表示未检测到该事件。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `Inertial wake-up`，并选择 **Detection status** 参数。

**数据类型：** `uint8`

### **Free-fall status** — 自由落体状态 `0` | `1`

该模块输出自由落体状态。值 `1` 表示在所选轴上检测到自由落体，`0` 表示未检测到中断。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `Free-fall`，并选择 **Detection status** 参数。

**数据类型：** `uint8`

### **6D position status [X, -X, Y, -Y, Z, -Z]** — 6D 位置状态 `0` | `1`

该模块将 6D 位置状态输出为 `1`-by-`6` 向量。值 `1` 表示在所选轴上检测到 6D 位置中断，`0` 表示未检测到中断。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `6D position`，并选择 **Detection status** 参数。

**数据类型：** `uint8`

### **6D movement status [X, -X, Y, -Y, Z, -Z]** — 6D 移动状态 `0` | `1`

该模块将 6D 移动状态输出为 `1`-by-`6` 向量。值 `1` 表示在所选轴上检测到 6D 移动中断，`0` 表示未检测到中断。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `6D movement`，并选择 **Detection status** 参数。

**数据类型：** `uint8`

### **4D position status [X, -X, Y, -Y]** — 4D 位置状态 `0` | `1`

该模块将 4D 位置状态输出为 `1`-by-`4` 向量。值 `1` 表示在所选轴上检测到 4D 位置中断，`0` 表示未检测到中断。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `4D position`，并选择 **Detection status** 参数。

**数据类型：** `uint8`

### **4D movement status [X, -X, Y, -Y]** — 4D 移动状态 `0` | `1`

该模块将 4D 移动状态输出为 `1`-by-`4` 向量。值 `1` 表示在所选轴上检测到 4D 移动中断，`0` 表示未检测到中断。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `4D movement`，并选择 **Detection status** 参数。

**数据类型：** `uint8`

## 参数

### 主要

### **I2C module** — I2C 通信模块 `I2C1`（默认）| 标量

指定 STM32 Processors 上用于与传感器外设通信的 I2C 模块。

### **I2C address** — 用于与传感器外设通信的 I2C 地址 `0x18`（默认）| `0x19`

用于与 LIS3DH 传感器上的加速度计外设通信的 I2C 地址由硬件板上 SA0 引脚的状态决定。下表提供了与该引脚及其状态对应的 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| SA0 | 0 | 0x18 |
| 1 | 0x19 |

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on`（默认）| `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **ADC3 output** — 选择用于读取温度或电压的输出端口 `None`（默认）| `Temperature` | `Voltage (external input)`

选择 `Temperature` 可将 **Temperature** 设置为输出端口之一，或选择 `Voltage (external input)` 可将 **ADC3 Voltage** 设置为输出端口之一。

### **Voltage (external input at ADC1)** — 选择用于读取电压的输出端口 `off`（默认）| `on`

选择此参数可将 **ADC1 Voltage** 设置为输出端口之一。

### **Voltage (external input at ADC2)** — 选择用于读取电压的输出端口 `off`（默认）| `on`

选择此参数可将 **ADC2 Voltage** 设置为输出端口之一。

### **Acceleration data ready status** — 设置用于获取加速度状态的输出端口 `on`（默认）| `off`

选择此参数可将 **Acceleration status** 设置为输出端口之一。

### **Accelerometer resolution** — 数据寄存器位分辨率 `12bit`（默认）| `10bit` | `8bit`

选择传感器的数据寄存器位分辨率。

### **Accelerometer output data rate (Hz)** — 加速度计数据采样速率 `400 Hz`（默认）| `1 Hz` | `10 Hz` | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `1344 Hz`

选择加速度计数据采样时的输出数据速率。

### **Accelerometer range** — 用于测量线性加速度的满量程 `±2g`（默认）| `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Enable FIFO** — 启用要读取的样本数 `off`（默认）| `on`

选择此选项可启用 **Number of samples to read from FIFO (1-32)** 选项，该选项允许设置要读取的样本数。当 FIFO 启用时，先读取缓冲区中最旧的样本集，最后读取最新的样本集。

### **Number of samples to read from FIFO (1-32)** — 要读取的样本数 `2`（默认）

输入要从 FIFO 读取的样本数（1-32）。

#### 依赖关系

若要启用此参数，请选择 **Enable FIFO** 参数。

**注意**

对于 AVR 目标，如果将 **Number of samples to read from FIFO (1-32)** 参数的值设置为大于 `29`，则 Display Sample 值可能会显示为零。为避免此问题，请将 External Mode 的波特率设置为小于 `921600` 的值。要更改波特率，请选择 **Hardware** > **Hardware Settings** > **Hardware Implementation** > **Target hardware resources** > **Host-board connection**，并将 **External Mode over Serial communication** 下的 **Baudrate** 值更改为 `115200`（推荐值）。

### **Generate FIFO overrun interrupt on INT1 pin** — 当 FIFO 缓冲区满时生成中断 `off`（默认）| `on`

如果 FIFO 缓冲区被填满且第一个样本被覆盖，选择此选项可接收中断。

#### 依赖关系

若要启用此参数，请选择 **Enable FIFO** 参数。

### **Enable high pass filter** — 为加速度计数据启用高通滤波器 `off`（默认）| `on`

启用在读取加速度计值时使用的高通滤波器。

### **HPF cutoff frequency (Hz)** — 高通滤波器的带宽 `100 Hz`（默认）| `12 Hz` | `25 Hz` | `50 Hz`

选择用于读取加速度计值的高通滤波器所需带宽。HPF 截止频率取决于 Accelerometer output data rate (Hz)。所选 Accelerometer output data rate (Hz) 的 HPF 截止频率如下表所示。值 `00`、`01`、`10` 和 `11` 是 HPF 模式配置。

**HPF cutoff frequency**

| HPF 截止频率[2:1] | 加速度输出数据速率 - 1 Hz | 加速度输出数据速率 - 10 Hz | 加速度输出数据速率 - 25 Hz | 加速度输出数据速率 - 50 Hz | 加速度输出数据速率 - 100 Hz | 加速度输出数据速率 - 200 Hz | 加速度输出数据速率 - 400 Hz | 加速度输出数据速率 - 1600 Hz | 加速度输出数据速率 - 5376 Hz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `0.02` | `0.2` | `0.5` | `1` | `2` | `4` | `8` | `32` | `100` |
| `01` | `0.008` | `0.08` | `0.2` | `0.5` | `1` | `2` | `4` | `16` | `50` |
| `10` | `0.004` | `0.04` | `0.1` | `0.2` | `0.5` | `1` | `2` | `8` | `25` |
| `11` | `0.002` | `0.02` | `0.05` | `0.1` | `0.2` | `0.5` | `1` | `4` | `12` |

#### 依赖关系

若要启用此参数，请选择 **Enable high pass filter** 参数。

### **Generate data ready interrupt on INT1 pin** — 当数据就绪时生成中断 `off`（默认）| `on`

如果选择此选项，则当数据就绪时，会在传感器的引脚 INT1 上生成中断，允许您触发其他子系统执行任何操作。

### **Data type** — 来自 lis3dh sensor 的值的输出数据类型 `single`（默认）| `double` | `int16`

指定从 lis3dh sensor 读取的值的输出数据类型。STM32 Processors 的默认数据类型为 `single`。如果需要，使用此参数将值更改为 `double` 或 `int16`。

### **Sample time** — 读取数据的时间间隔 `-1`（默认）| 正整数

指定此模块读取 LIS3DH 传感器数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文为该模块确定最佳采样时间。

### Click 检测

### **Enable click detection** — 用于启用 click 检测的选项 `off`（默认）| `on`

选择此参数以启用 click 检测。

### **Type** — 选择要检测的 click 类型 `Single click`（默认）| `Double click`

选择要检测的 click 类型。可用选项为 `Single click` 和 `Double click`。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数。

### **Threshold (m/s2)** — 用于检测 single click 或 double click 的阈值 `1.5`（默认）

指定用于检测 single click 或 double click 的阈值。当值超过指定阈值时，检测到 click。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数。

### **Time limit (s)** — 时间限制持续时间 `0.3`（默认）| 正整数

指定用于检测 single click 或 double click 的时间限制值，单位为秒。必须在用于检测 single click 或 double click 的指定时间限制内发生 click。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数。

### **Time latency (s)** — 时间延迟持续时间 `0.3`（默认）| 正整数

指定用于检测 double click 的时间延迟值，单位为秒。用于检测 double click 时，第二次 click 必须在指定的时间延迟时段之后发生。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数，并为 **Type** 参数选择 `Double click` 选项。

### **Time window (s)** — 时间窗口持续时间 `0.3`（默认）| 正整数

指定用于检测 double click 的时间窗口值，单位为秒。用于检测 double click 时，第二次 click 必须在时间窗口时段到期之前发生。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数，并为 **Type** 参数选择 `Double click` 选项。

### **X axis** — X 轴中的 Click 检测 `on`（默认）| `off`

选择此选项以启用沿 X 轴的 click 检测。值 `1` 表示检测到 click，`0` 表示未检测到 click。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数。

### **Y axis** — Y 轴中的 Click 检测 `on`（默认）| `off`

选择此选项以启用沿 Y 轴的 click 检测。值 `1` 表示检测到 click，`0` 表示未检测到 click。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数。

### **Z axis** — Z 轴中的 Click 检测 `off`（默认）| `on`

选择此选项以启用沿 Z 轴的 click 检测。值 `1` 表示检测到 click，`0` 表示未检测到 click。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数。

### **Generate click interrupt** — 当检测到 click 时生成中断 `off`（默认）| `on`

如果检测到 click，选择该选项以生成中断。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数。

### **Interrupt pin** — 用于生成 click 中断的引脚 `INT1`（默认）| `INT2`

如果选择此选项，则当数据就绪时，会在传感器的引脚 INT1 或 IN2 上生成中断，允许您触发其他子系统执行任何操作。

#### 依赖关系

若要启用此参数，请选择 **Generate click interrupt** 参数。

### **Click status** — 设置用于获取 click 检测状态的输出端口 `off`（默认）| `on`

选择此参数可将 **Click status [X,Y,Z]** 设置为输出端口之一。

#### 依赖关系

若要启用此参数，请选择 **Enable click detection** 参数。

### 可配置检测

### **Configurable detections** — 设置可配置检测的数量 `0`（默认）| `1` | `2`

选择可配置检测数量所需的选项。

#### 可配置检测 1

### **Detect** — 选择可配置事件 `Inertial wake-up`（默认）| `Free-fall` | `6D position` | `6D movement` | `4D position` | `4D movement`

选择传感器所需的功能。（Inertial wake-up、Free-fall、6D position、6D movement、4D position、4D movement）。

#### 依赖关系

若要启用此参数，请从 **Configurable detections** 参数中选择 `1` 或 `2`。

### **X axis** — X 轴中的可配置检测 `on`（默认）| `off`

选择此选项以启用 X 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `Inertial wake-up` 或 `6D position` 或 `6D movement` 或 `4D position` 或 `4D movement`。

### **Y axis** — Y 轴中的可配置检测 `on`（默认）| `off`

选择此选项以启用 Y 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `Inertial wake-up` 或 `6D position` 或 `6D movement` 或 `4D position` 或 `4D movement`。

### **Z axis** — Z 轴中的可配置检测 `on`（默认）| `off`

选择此选项以启用 Z 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `Inertial wake-up` 或 `6D position` 或 `6D movement`。

### **-X axis** — -X 轴中的可配置检测 `off`（默认）| `on`

选择此选项以启用 -X 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `6D position` 或 `6D movement` 或 `4D position` 或 `4D movement`。

### **-Y axis** — -Y 轴中的可配置检测 `off`（默认）| `on`

选择此选项以启用 -Y 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `6D position` 或 `6D movement` 或 `4D position` 或 `4D movement`。

### **-Z axis** — -Z 轴中的可配置检测 `off`（默认）| `on`

选择此选项以启用 -Z 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

若要启用此参数，请从 **Detect** 参数中选择 `6D position` 或 `6D movement`。

### **Threshold (m/s2** — 用于检测所选可配置检测的加速度阈值 `1.5`（默认）

指定用于检测所选可配置检测的阈值。当加速度值超过指定阈值时，检测到事件。

#### 依赖关系

若要启用此参数，请从 **Configurable detections** 参数中选择 `1` 或 `2`。

### **Duration (s)** — 时间限制持续时间 `0.3`（默认）| 正整数

指定用于检测可配置事件的时间限制。要检测事件，Threshold 条件必须在等于 Duration 的最短时间内得到满足。

#### 依赖关系

若要启用此参数，请从 **Configurable detections** 参数中选择 `1` 或 `2`。

### **Generate interrupt** — 生成中断 `off`（默认）| `on`

如果选择此选项，则将为所选可配置检测生成中断。

#### 依赖关系

若要启用此参数，请从 **Configurable detections** 参数中选择 `1` 或 `2`。

### **Interrupt pin** — 用于生成中断的引脚 `INT1`（默认）| `INT2`

如果选择此选项，则当检测到可配置事件时，会在传感器的引脚 INT1 或 IN2 上生成中断，允许您触发其他子系统执行任何操作。

#### 依赖关系

若要启用此参数，请选择 **Generate interrupt** 参数。

**注意**

**Configuration detections 2** 的参数与 **Configuration detections 1** 类似。有关配置这些参数的信息，请参阅可配置检测。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / Sensors / IMU Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

测量来自 LIS3DH 传感器的线性加速度、电压和温度

LIS3DH Accelerometer Sensor 模块使用与 STM32 Processors 接口的 LIS3DH Accelerometer 传感器，测量线性加速度、传感器外部输入引脚（ADC1、ADC2 和 ADC3）上的电压以及温度。

该模块还提供启用高通滤波器、FIFO 和 FIFO 中断的选项。如果选择了 **Generate data ready interrupt**，则会生成中断。选择 **Generate data ready interrupt** 后，如果 FIFO 禁用，则生成 data ready 中断；如果 FIFO 启用，则生成 FIFO 中断。

该模块输出加速度测量状态，值指定为 `0`、`1` 或 `2`。值 `0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`2` 表示数据被覆盖。

该模块将 single / double click 轴输出为 `1`-by-`3` 向量。click 轴提供在哪个轴上检测到 click 的信息。检测到 click 时，轴值显示 `1`，否则显示 `0`。

该模块支持 inertial wake-up、free-fall、6D position、6D movement、4D position 和 4D movement 识别。该模块将 inertial wake-up 轴输出为 `1`-by-`3` 向量。它提供在哪个轴上检测到 inertial wake-up 的信息。6D position 轴和 6D movement 轴的大小为 `1`-by-`6`。4D position 和 4D movement 轴的大小为 `1`-by-`4`。状态包含在哪个轴上识别到检测的信息。当在所选轴上识别到配置的检测时，状态值显示 `1`，否则显示 `0`。

**注意**

在使用模型中可用的 sensor block 执行 monitor and tune 时，务必确保将传感器连接到板。
