---
type: simulink-block
title: 'LIS3DH Accelerometer Sensor'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'lis3dhaccelerometersensor'
documentation_source_path: 'ref/lis3dhaccelerometersensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LIS3DH Accelerometer Sensor

## 端口

### 输出

### **Acceleration** — 由加速度计矢量测量的各轴加速度

当 FIFO 禁用时，该模块输出加速度为 `1`×`3`
向量。当 FIFO 启用时，该模块输出
`n`×`3` 向量，其中
`n` 是样本数。每个值表示沿 X、Y 和 Z
轴以 `m/s^2` 为单位的加速度测量值。

#### 依赖关系

仅当选择 **Acceleration
(m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC1 Voltage** — 外部引脚 ADC1 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC1 上的电压。

#### 依赖关系

仅当选择 **Voltage (external
input at ADC1)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC2 Voltage** — 外部引脚 ADC2 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC2 上的电压。

#### 依赖关系

仅当选择 **Voltage (external
input at ADC2)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC3 Voltage** — 外部引脚 ADC3 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC3 上的电压。

#### 依赖关系

仅当为 **ADC3 input** 参数选择 `Voltage (external
input)` 时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **Temperature** — 由 LIS3DH 传感器测得的温度标量

由连接到 C2000 板的 LIS3DH 传感器测得的温度（单位：℃）。

#### 依赖关系

仅当为 **ADC3 input**
参数选择 `Temperature` 时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **Accelration Status** — 加速度测量状态 `2` | `0` | `1`

加速度测量状态，指定为值 `0`、
`1` 或 `2`。值 `0`
表示读取的数据是新数据，`1` 表示读取的数据
不是新数据，`2` 表示数据被覆盖。

如果选择 **Enable FIFO**，则 `0`
表示已收集指定样本，`1` 表示
未收集指定数量的样本，`2` 表示
数据被覆盖。

#### 依赖关系

仅当选择 **Acceleration data
ready Status** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Samples pending** — 待处理样本数标量

该模块输出要读取的待处理样本数，取值范围为
`0-32`。

#### 依赖关系

仅当选择 **Enable FIFO**
参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Click status [X,Y,Z]** — 单击检测状态 `0` | `1`

该模块输出各轴的 Click status，为
`1`×`3` 向量 (x,y,z)，指示在哪个轴上
检测到单击。轴值 `1` 表示在该轴上
检测到单击，`0` 表示未检测到单击。

#### 依赖关系

仅当选择 **click
status** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Inertial wake-up status [X,Y,Z]** — 惯性唤醒中断状态 `0` | `1`

该模块输出惯性唤醒状态，为
`1`×`3` 向量。这提供检测到惯性唤醒的轴的信息。值 `1`
表示在所选轴上检测到惯性唤醒事件，值
`0` 表示未检测到该事件。

#### 依赖关系

仅当从 **Detect** 参数中选择 `Inertial
wake-up` 并选择
**Detection status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **Free-fall status** — 自由落体状态 `0` | `1`

该模块输出自由落体状态。值 `1` 表示在
所选轴上检测到自由落体，`0` 表示
未检测到中断。

#### 依赖关系

仅当从 **Detect** 参数中选择 `Free-fall`
并选择 **Detection
status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **6D position status [X, -X, Y, -Y, Z, -Z]** — 6D 位置状态 `0` | `1`

该模块输出 6D 位置状态，为
`1`×`6` 向量。值 `1`
表示在所选轴上检测到 6D 位置中断，
`0` 表示未检测到该中断。

#### 依赖关系

仅当从 **Detect** 参数中选择 `6D position`
并选择 **Detection
status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **6D movement status [X, -X, Y, -Y, Z, -Z]** — 6D 运动状态 `0` | `1`

该模块输出 6D 运动状态，为
`1`×`6` 向量。值 `1`
表示在所选轴上检测到 6D 运动中断，
`0` 表示未检测到该中断。

#### 依赖关系

仅当从 **Detect** 参数中选择 `6D movement`
并选择 **Detection
status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **4D position status [X, -X, Y, -Y]** — 4D 位置状态 `0` | `1`

该模块输出 4D 位置状态，为
`1`×`4` 向量。值 `1`
表示在所选轴上检测到 4D 位置中断，
`0` 表示未检测到该中断。

#### 依赖关系

仅当从 **Detect** 参数中选择 `4D position`
并选择 **Detection
status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **4D movement status [X, -X, Y, -Y]** — 4D 运动状态 `0` | `1`

该模块输出 4D 运动状态，为
`1`×`4` 向量。值 `1`
表示在所选轴上检测到 4D 运动中断，
`0` 表示未检测到该中断。

#### 依赖关系

仅当从 **Detect** 参数中选择 `4D movement`
并选择 **Detection
status** 参数时，此参数才会出现。

**数据类型：** `uint8`

## 参数

### 主要

### **I2C Module** — 用于 I2C 通信的特定模块 `I2C_A` (默认)

指定板上用于 I2C 通信的模块。

### **I2C address** — 用于与传感器外设通信的 I2C 地址 `0x18` (默认) | `0x19`

用于与 LIS3DH 传感器上的加速度计外设通信的 I2C 地址由硬件板上 SA0 引脚的状态决定。下表提供与该引脚及其状态对应的 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| SA0 | 0 | 0x18 |
| 1 | 0x19 |

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on` (默认) | `off`

选择此参数以将 **Acceleration** 设置为输出端口之一。

### **ADC3 input** — 选择用于读取温度或电压的输出端口 `None` (默认) | `Temperature` | `Voltage (external input)`

选择 `Temperature` 可将
**Temperature** 设置为输出端口之一，或选择
`Voltage (external input)` 可将 **ADC3
Voltage** 设置为输出端口之一。

### **Voltage (external input at ADC1)** — 选择用于读取电压的输出端口 `off` (默认) | `on`

选择此参数以将 **ADC1 Voltage** 设置为输出端口之一。

### **Voltage (external input at ADC2)** — 选择用于读取电压的输出端口 `off` (默认) | `on`

选择此参数以将 **ADC2 Voltage** 设置为输出端口之一。

### **Acceleration data ready status** — 设置用于获取加速度状态的输出端口 `on` (默认) | `off`

选择此参数以将 **Acceleration status** 设置为输出端口之一。

### **Accelerometer resolution** — 数据寄存器位分辨率 `12bit` (默认) | `10bit` | `8bit`

选择传感器的数据寄存器位分辨率。

### **Accelerometer output data rate (Hz)** — 加速度计数据采样速率 `400 Hz` (默认) | `1 Hz` | `10 Hz` | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `1344 Hz`

选择加速度计数据的采样输出数据速率。

### **Accelerometer range** — 用于测量线性加速度的满量程 `±2g` (默认) | `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Enable FIFO** — 启用要读取的样本数 `off` (默认) | `on`

选择此选项可启用 **Number of samples to read from
FIFO (1-32)** 选项，从而允许您设置要读取的样本数。

### **Number of samples to read from FIFO (1-32)** — 要读取的样本数 `2` (默认)

输入要从 FIFO 读取的样本数 (1-32)。

#### 依赖关系

仅当选择 **Enable FIFO**
参数时，此参数才会出现。

### **Generate FIFO overrun interrupt on INT1 pin** — 当 FIFO 缓冲区已满时生成中断 `off` (默认) | `on`

如果 FIFO 缓冲区被填满且第一个样本被覆盖，选择此选项可接收中断。

#### 依赖关系

仅当选择 **Enable FIFO**
参数时，此参数才会出现。

### **Enable high pass filter** — 为加速度计数据启用高通滤波器 `off` (默认) | `on`

启用在读取加速度计值时使用的高通滤波器。

### **HPF cutoff frequency (Hz)** — 高通滤波器的带宽 `100 Hz` (默认) | `12 Hz` | `25 Hz` | `50 Hz`

选择读取加速度计值时所需的高通滤波器带宽。HPF 截止频率取决于 Accelerometer output data rate (Hz)。所选 Accelerometer output data rate (Hz) 对应的 HPF 截止频率如下表所示。值 `00`、`01`、
`10` 和 `11` 是 HPF 模式配置。

**HPF 截止频率**

| HPF 截止频率[2:1] | 加速度输出数据速率 - 1 Hz | 加速度输出数据速率 - 10 Hz | 加速度输出数据速率 - 25 Hz | 加速度输出数据速率 - 50 Hz | 加速度输出数据速率 - 100 Hz | 加速度输出数据速率 - 200 Hz | 加速度输出数据速率 - 400 Hz | 加速度输出数据速率 - 1600 Hz | 加速度输出数据速率 - 5376 Hz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `0.02` | `0.2` | `0.5` | `1` | `2` | `4` | `8` | `32` | `100` |
| `01` | `0.008` | `0.08` | `0.2` | `0.5` | `1` | `2` | `4` | `16` | `50` |
| `10` | `0.004` | `0.04` | `0.1` | `0.2` | `0.5` | `1` | `2` | `8` | `25` |
| `11` | `0.002` | `0.02` | `0.05` | `0.1` | `0.2` | `0.5` | `1` | `4` | `12` |

#### 依赖关系

仅当选择 **Enable high pass
filter** 参数时，此参数才会出现。

### **Generate data ready interrupt on INT1 pin** — 当数据就绪时生成中断 `off` (默认) | `on`

如果选择此选项，当数据就绪时，传感器的 INT1 引脚上会生成中断，使您可以触发其他子系统执行任意操作。

### **Data type** — 来自 lis3dh 传感器的值的输出数据类型 `single` (默认) | `double` | `int16`

指定从 lis3dh 传感器读取的值的输出数据类型。C2000 板的默认数据类型为 `single`。如果需要，可使用此参数将值更改为 `double` 或 `int16`。

### **Sample time** — 读取数据的时间间隔 `-1` (默认) | 正整数

指定此模块从 LIS3DH 传感器读取数据的频率。当您将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 单击检测

### **Enable click detection** — 用于启用单击检测的选项 `off` (默认) | `on`

选择此参数以启用单击检测。

### **Type** — 选择要检测的单击类型 `Single click` (默认) | `Double click`

选择要检测的单击类型。可用选项为
`Single click` 和 `Double
click`。

#### 依赖关系

仅当选择 **Enable click
detection** 参数时，此参数才会出现。

### **Threshold (m/s2)** — 用于检测单击或双击的阈值 `1.5` (默认)

指定用于检测单击或双击的阈值。当值越过指定阈值时，检测到单击。

#### 依赖关系

仅当选择 **Enable click
detection** 参数时，此参数才会出现。

### **Time limit (s)** — 时间限制持续时间 `0.3` (默认) | 正整数

指定用于检测单击或双击的时间限制值，以 s 为单位。单击必须在指定的时间限制内发生，才能检测到单击或双击。

#### 依赖关系

仅当选择 **Enable click
detection** 参数时，此参数才会出现。

### **Time latency (s)** — 时间延迟持续时间 `0.3` (默认) | 正整数

指定用于检测双击的时间延迟值，以 s 为单位。第二次单击必须在指定的时间延迟时段之后发生，才能检测到双击。

#### 依赖关系

仅当选择 **Enable click
detection** 参数并针对 **Type** 参数选择 `Double click`
选项时，此参数才会出现。

### **Time window (s)** — 时间窗口持续时间 `0.3` (默认) | 正整数

指定用于检测双击的时间窗口值，以 s 为单位。第二次单击必须在时间窗口时段结束之前发生，才能检测到双击。

#### 依赖关系

仅当选择 **Enable click
detection** 参数并针对 **Type** 参数选择 `Double click`
选项时，此参数才会出现。

### **X axis** — X 轴中的单击检测 `on` (默认) | `off`

选择此选项以启用沿 X 轴的单击检测。值
`1` 表示检测到单击，`0`
表示未检测到单击

#### 依赖关系

仅当选择 **Enable click
detection** 参数时，此参数才会出现。

### **Y axis** — Y 轴中的单击检测 `on` (默认) | `off`

选择此选项以启用沿 Y 轴的单击检测。值
`1` 表示检测到单击，`0`
表示未检测到单击

#### 依赖关系

仅当选择 **Enable click
detection** 参数时，此参数才会出现。

### **Z axis** — Z 轴中的单击检测 `off` (默认) | `on`

选择此选项以启用沿 Z 轴的单击检测。值
`1` 表示检测到单击，`0`
表示未检测到单击

#### 依赖关系

仅当选择 **Enable click
detection** 参数时，此参数才会出现。

### **Generate click interrupt** — 当检测到单击时生成中断 `off` (默认) | `on`

如果检测到单击，选择此选项以生成中断。

#### 依赖关系

仅当选择 **Enable click
detection** 参数时，此参数才会出现。

### **Interrupt pin** — 用于生成单击中断的引脚 `INT1` (默认) | `INT2`

如果选择此选项，当数据就绪时，传感器的 INT1 或 IN2 引脚上会生成中断，使您可以触发其他子系统执行任意操作。

#### 依赖关系

仅当选择 **Generate click
interrupt** 参数时，此参数才会出现。

### **Click status** — 设置用于获取单击检测状态的输出端口 `off` (默认) | `on`

选择此参数可将 **Click status [X,Y,Z]** 设置为输出端口之一。

#### 依赖关系

仅当选择 **Enable click
detection** 参数时，此参数才会出现。

### 可配置检测

### **Configurable detections** — 设置可配置检测的数量 `0` (默认) | `1` | `2`

选择可配置检测数量所需的选项。

#### 可配置检测 1

### **Detect** — 选择中断 `Inertial wake-up` (默认) | `Free-fall` | `6D position` | `6D movement` | `4D position` | `4D movement`

选择所需的传感器功能。（Inertial wake-up、Free-fall、6D
position、6D movement、4D position、4D movement）。

#### 依赖关系

仅当从 **Configurable detections**
参数中选择 `1` 或
`2` 时，此参数才会出现。

### **X axis** — X 轴中断检测 `on`（默认） | `off`

选择此选项以启用 X 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

仅当从 **Detect** 参数中选择 `Inertial wake-up` 或 `6D position` 或 `6D movement` 或 `4D position` 或 `4D movement` 时，此参数才会出现。

### **Y axis** — Y 轴中断检测 `on`（默认） | `off`

选择此选项以启用 Y 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

仅当从 **Detect** 参数中选择 `Inertial wake-up` 或 `6D position` 或 `6D movement` 或 `4D position` 或 `4D movement` 时，此参数才会出现。

### **Z axis** — Z 轴中断检测 `on`（默认） | `off`

选择此选项以启用 Z 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

仅当从 **Detect** 参数中选择 `Inertial wake-up` 或 `6D position` 或 `6D movement` 时，此参数才会出现。

### **-X axis** — -X 轴中断检测 `off`（默认） | `on`

选择此选项以启用 -X 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

仅当从 **Detect** 参数中选择 `6D position` 或 `6D movement` 或 `4D position` 或 `4D movement` 时，此参数才会出现。

### **-Y axis** — -Y 轴中断检测 `off`（默认） | `on`

选择此选项以启用 -Y 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

仅当从 **Detect** 参数中选择 `6D position` 或 `6D movement` 或 `4D position` 或 `4D movement` 时，此参数才会出现。

### **-Z axis** — -Z 轴中断检测 `off`（默认） | `on`

选择此选项以启用 -Z 轴上的可配置事件检测状态。值 `1` 表示检测到事件，`0` 表示未检测到事件。

#### 依赖关系

仅当从 **Detect** 参数中选择 `6D position` 或 `6D movement` 时，此参数才会出现。

### **Threshold (m/s2** — 用于检测所选可配置检测的加速度阈值 `1.5`（默认）

指定用于检测所选可配置检测的阈值。当加速度值穿过指定阈值时，检测到事件。

#### 依赖关系

仅当从 **Configurable detections** 参数中选择 `1` 或 `2` 时，此参数才会出现。

### **Duration (s)** — 时间限制持续时间 `0.3`（默认） | `positive integer`

指定用于检测可配置事件的时间限制。要检测事件，Threshold 条件必须在等于 Duration 的最短时间内得到满足。

#### 依赖关系

仅当从 **Configurable detections** 参数中选择 `1` 或 `2` 时，此参数才会出现。

### **Generate interrupt** — 生成中断 `off`（默认） | `on`

如果选择此选项，则会为所选可配置检测生成中断。

#### 依赖关系

仅当从 **Configurable detections** 参数中选择 `1` 或 `2` 时，此参数才会出现。

### **Interrupt pin** — 用于生成中断的引脚 `INT1`（默认） | `INT2`

如果选择此选项，当检测到可配置事件时，会在传感器的 INT1 或 IN2 引脚上生成中断，使您能够触发其他子系统执行任何操作。

#### 依赖关系

仅当选择 **Generate interrupt** 参数时，此参数才会出现。

**注意**

**Configuration detections 2** 的参数与 **Configuration detections 1** 类似。有关配置这些参数的信息，请参见 Configurable detections 1。

## 所属库

C2000 Microcontroller Blockset / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从 LIS3DH 传感器测量线性加速度、电压和温度

LIS3DH Accelerometer Sensor 模块使用与 C2000 板连接的 LIS3DH Accelerometer 传感器，测量线性加速度、传感器外部输入引脚（ADC1、ADC2 和 ADC3）上的电压以及温度。

该模块还提供启用高通滤波器、FIFO 和 FIFO 中断的选项。如果选择 **Generate data ready interrupt**，则会生成中断。选择 **Generate data ready interrupt** 后，如果 FIFO 被禁用，则生成数据就绪中断；如果 FIFO 被启用，则生成 FIFO 中断。

该模块输出加速度测量状态，指定为值 `0`、`1` 或 `2`。值 `0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`2` 表示数据被覆盖。

该模块将 single / double click axis 输出为 `1`-by-`3` 向量。click axis 提供检测到点击的轴的信息。检测到点击时轴值显示 `1`，否则显示 `0`。

该模块支持 inertial wake-up、free-fall、`6D` position、`6D` movement、`4D` position 和 `4D` movement 识别。该模块将 inertial wake-up axis 输出为 `1`-by-`3` 向量。这提供检测到 inertial wake-up 的轴的信息。`6D` position axis 和 `6D` movement axis 的大小为 `1`-by-`6`。`4D` position 和 `4D` movement axis 的大小为 `1`-by-`4`。status 包含识别到检测的轴的信息。当在所选轴上识别到配置的检测时，status 值显示 `1`，否则显示 `0`。
