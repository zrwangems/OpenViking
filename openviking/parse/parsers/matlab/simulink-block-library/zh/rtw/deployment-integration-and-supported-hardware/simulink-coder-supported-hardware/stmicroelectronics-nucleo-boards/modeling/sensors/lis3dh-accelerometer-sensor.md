---
type: simulink-block
title: 'LIS3DH Accelerometer Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'lis3dhaccelerometersensor'
documentation_source_path: 'nucleo/ref/lis3dhaccelerometersensor.html'
language: zh-CN
chinese_source: worker-translation
---

# LIS3DH Accelerometer Sensor

## 端口

### 输出

### **Acceleration** — 由加速度计向量测量的沿各轴的加速度

当 FIFO 禁用时，该模块将加速度输出为 `1`-by-`3` 向量。
当 FIFO 启用时，该模块输出 `n`-by-`3` 向量，其中 `n` 是样本数。每个值表示沿 X、Y 和 Z 轴的加速度测量值，单位为 `m/s^2`。

#### 依赖项

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC1 Voltage** — 外部引脚 ADC1 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC1 上的电压。

#### 依赖项

仅当选择 **Voltage (external input at ADC1)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC2 Voltage** — 外部引脚 ADC2 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC2 上的电压。

#### 依赖项

仅当选择 **Voltage (external input at ADC2)** 参数时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **ADC3 Voltage** — 外部引脚 ADC3 上的电压向量

该模块输出施加在 LIS3DH 传感器外部引脚 ADC3 上的电压。

#### 依赖项

仅当为 **ADC3 input** 参数选择 `Voltage (external input)` 时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **Temperature** — 由 LIS3DH 传感器测量的温度标量

连接到 Arduino 板的 LIS3DH 传感器测量得到的温度（单位：℃）。

#### 依赖项

仅当为 **ADC3 input** 参数选择 `Temperature` 时，此输出端口才会出现。

**数据类型：** `single` | `double` | `int16`

### **Acceleration status** — 加速度测量状态 `2` | `0` | `1`

该模块将测量得到的加速度状态输出为值 `0`、`1` 或 `2`。值 `0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据，`2` 表示数据被覆盖。

如果选择了 **Enable FIFO**，则 `0` 表示已收集指定样本，`1` 表示未收集指定数量的样本，`2` 表示数据被覆盖。

#### 依赖项

仅当选择 **Acceleration data ready status** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Samples pending** — 待处理样本数标量

该模块将待读取的待处理样本数输出为范围 `0-32` 内的值。

#### 依赖项

仅当选择 **Enable FIFO** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Click status [X,Y,Z]** — 点击检测状态 `0` | `1`

该模块将各轴的 Click status 输出为 `1`-by-`3` 向量 (x,y,z)，指示在哪个轴上检测到点击。轴值 `1` 表示在该轴上检测到点击，`0` 表示未检测到点击。

#### 依赖项

仅当选择 **click status** 参数时，此输出端口才会出现。

**数据类型：** `uint8`

### **Inertial wake-up status [X,Y,Z]** — 惯性唤醒中断状态 `0` | `1`

该模块将惯性唤醒状态输出为 `1`-by-`3` 向量。这提供检测到惯性唤醒的轴的信息。值 `1` 表示在所选轴上检测到惯性唤醒事件，值 `0` 表示未检测到该事件。

#### 依赖项

仅当从 **Detect** 参数中选择 `Inertial wake-up` 并选择 **Detection status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **Free-fall status** — 自由落体状态 `0` | `1`

该模块输出自由落体状态。值 `1` 表示在所选轴上检测到自由落体，`0` 表示未检测到中断。

#### 依赖项

仅当从 **Detect** 参数中选择 `Free-fall` 并选择 **Detection status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **6D position status [X, -X, Y, -Y, Z, -Z]** — 6D 位置状态 `0` | `1`

该模块将 6D 位置状态输出为 `1`-by-`6` 向量。值 `1` 表示在所选轴上检测到 6D 位置中断，`0` 表示未检测到中断。

#### 依赖项

仅当从 **Detect** 参数中选择 `6D position` 并选择 **Detection status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **6D movement status [X, -X, Y, -Y, Z, -Z]** — 6D 移动状态 `0` | `1`

该模块将 6D 移动状态输出为 `1`-by-`6` 向量。值 `1` 表示在所选轴上检测到 6D 移动中断，`0` 表示未检测到中断。

#### 依赖项

仅当从 **Detect** 参数中选择 `6D movement` 并选择 **Detection status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **4D position status [X, -X, Y, -Y]** — 4D 位置状态 `0` | `1`

该模块将 4D 位置状态输出为 `1`-by-`4` 向量。值 `1` 表示在所选轴上检测到 4D 位置中断，`0` 表示未检测到中断。

#### 依赖项

仅当从 **Detect** 参数中选择 `4D position` 并选择 **Detection status** 参数时，此参数才会出现。

**数据类型：** `uint8`

### **4D movement status [X, -X, Y, -Y]** — 4D 移动状态 `0` | `1`

该模块将 4D 移动状态输出为 `1`-by-`4` 向量。值 `1` 表示在所选轴上检测到 4D 移动中断，`0` 表示未检测到中断。

#### 依赖项

仅当从 **Detect** 参数中选择 `4D movement` 并选择 **Detection status** 参数时，此参数才会出现。

**数据类型：** `uint8`

## 参数

### 主设置

### **I2C address** — 用于与传感器外设通信的 I2C 地址 `0x18`（默认） | `0x19`

用于与 LIS3DH 传感器上的加速度计外设通信的 I2C 地址由硬件板上 SA0 引脚的状态决定。下表提供了与该引脚及其状态对应的 I2C 地址。

| 引脚名称 | 引脚状态 | I2C 地址 |
| --- | --- | --- |
| SA0 | 0 | 0x18 |
| 1 | 0x19 |

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on`（默认） | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **ADC3 input** — 选择用于读取温度或电压的输出端口 `None`（默认） | `Temperature` | `Voltage (external input)`

选择 `Temperature` 可将 **Temperature** 设置为输出端口之一，或选择 `Voltage (external input)` 可将 **ADC3 Voltage** 设置为输出端口之一。

### **Voltage (external input at ADC1)** — 选择用于读取电压的输出端口 `off`（默认） | `on`

选择此参数可将 **ADC1 Voltage** 设置为输出端口之一。

### **Voltage (external input at ADC2)** — 选择用于读取电压的输出端口 `off`（默认） | `on`

选择此参数可将 **ADC2 Voltage** 设置为输出端口之一。

### **Acceleration data ready status** — 设置用于获取加速度状态的输出端口 `on`（默认） | `off`

选择此参数可将 **Acceleration status** 设置为输出端口之一。

### **Accelerometer resolution** — 数据寄存器位分辨率 `12bit`（默认） | `10bit` | `8bit`

选择传感器的数据寄存器位分辨率。

### **Accelerometer output data rate (Hz)** — 加速度计数据的采样速率 `400 Hz`（默认） | `1 Hz` | `10 Hz` | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `1344 Hz`

选择加速度计数据的采样输出数据速率。

### **Accelerometer range** — 测量线性加速度的满量程 `±2g`（默认） | `±4g` | `±8g` | `±16g`

选择测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Enable FIFO** — 启用要读取的样本数 `off`（默认） | `on`

选择此选项可启用 **Number of samples to read from FIFO (1-32)** 选项，从而允许您设置要读取的样本数。当 FIFO 启用时，首先读取缓冲区中最旧的样本集，最后读取最新的样本集。

### **Number of samples to read from FIFO (1-32)** — 要读取的样本数 `2`（默认）

输入要从 FIFO 读取的样本数 (1-32) 的值。

#### 依赖项

仅当选择 **Enable FIFO** 参数时，此参数才会出现。

**注意**

对于 AVR 目标，如果 **Number of samples to read from FIFO (1-32)** 参数的值设置为大于 `29`，则 Display Sample 值可能会显示为零。为避免此问题，请将 External Mode 的波特率设置为小于 `921600` 的值。要更改波特率，请选择 **Hardware** > **Hardware Settings** > **Hardware Implementation** > **Target hardware resources** > **Host-board connection**，并将 **External Mode over Serial communication** 下 **Baudrate** 的值更改为 `115200`（推荐值）。

### **Generate FIFO overrun interrupt on INT1 pin** — 当 FIFO 缓冲区已满时生成中断 `off`（默认） | `on`

选择此选项可在 FIFO 缓冲区被填满且第一个样本被覆盖时接收中断。

#### 依赖项

仅当选择 **Enable FIFO** 参数时，此参数才会出现。

### **Enable high pass filter** — 为加速度计数据启用高通滤波器 `off`（默认） | `on`

启用高通滤波器以读取加速度计值。

### **HPF cutoff frequency (Hz)** — 高通滤波器的带宽 `100 Hz`（默认） | `12 Hz` | `25 Hz` | `50 Hz`

选择读取加速度计值所需的高通滤波器带宽。HPF 截止频率取决于 Accelerometer output data rate (Hz)。所选 Accelerometer output data rate (Hz) 对应的 HPF 截止频率如下表所示。值 `00`、`01`、`10` 和 `11` 是 HPF 模式配置。

**HPF 截止频率**

| HPF 截止频率[2:1] | 加速度输出数据速率 - 1 Hz | 加速度输出数据速率 - 10 Hz | 加速度输出数据速率 - 25 Hz | 加速度输出数据速率 - 50 Hz | 加速度输出数据速率 - 100 Hz | 加速度输出数据速率 - 200 Hz | 加速度输出数据速率 - 400 Hz | 加速度输出数据速率 - 1600 Hz | 加速度输出数据速率 - 5376 Hz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `00` | `0.02` | `0.2` | `0.5` | `1` | `2` | `4` | `8` | `32` | `100` |
| `01` | `0.008` | `0.08` | `0.2` | `0.5` | `1` | `2` | `4` | `16` | `50` |
| `10` | `0.004` | `0.04` | `0.1` | `0.2` | `0.5` | `1` | `2` | `8` | `25` |
| `11` | `0.002` | `0.02` | `0.05` | `0.1` | `0.2` | `0.5` | `1` | `4` | `12` |

#### 依赖项

仅当选择 **Enable high pass filter** 参数时，此参数才会出现。

### **Generate data ready interrupt on INT1 pin** — 当数据就绪时生成中断 `off`（默认） | `on`

如果选择此选项，则当数据就绪时会在传感器的 INT1 引脚上生成中断，从而允许您触发其他子系统执行任何操作。

### **Data type** — 来自 lis3dh 传感器的值的输出数据类型 `single`（默认） | `double` | `int16`

指定从 lis3dh 传感器读取的值的输出数据类型。Arduino 硬件的默认数据类型为 `single`。如果需要，可使用此参数将值更改为 `double` 或 `int16`。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 LIS3DH 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 点击检测

### **Enable click detection** — 用于启用点击检测的选项 `off`（默认） | `on`

选择此参数以启用点击检测。

### **Type** — 选择要检测的点击类型 `Single click`（默认） | `Double click`

选择要检测的点击类型。可用选项为 `Single click` 和 `Double click`。

#### 依赖项

仅当选择 **Enable click detection** 参数时，此参数才会出现。

### **Threshold (m/s2)** — 用于检测单击或双击的阈值 `1.5`（默认）

指定用于检测单击或双击的阈值。当值超过指定阈值时，检测到点击。

#### 依赖项

仅当选择 **Enable click detection** 参数时，此参数才会出现。

### **Time limit (s)** — 时间限制持续时间 `0.3`（默认） | `positive integer`

指定用于检测单击或双击的时间限制值（以秒为单位）。点击必须发生在指定的时间限制内，才能检测到单击或双击。

#### 依赖项

仅当选择 **Enable click detection** 参数时，此参数才会出现。

### **Time latency (s)** — 时间延迟持续时间 `0.3`（默认） | `positive integer`

指定用于检测双击的时间延迟值（以秒为单位）。第二次点击必须发生在指定的时间延迟时间段之后，才能检测到双击。

#### 依赖项

仅当选择 **Enable click detection** 参数并为 **Type** 参数选择 `Double click` 选项时，此参数才会出现。

### **Time window (s)** — 时间窗口持续时间 `0.3`（默认） | `positive integer`

指定用于检测双击的时间窗口值（以秒为单位）。第二次点击必须在时间窗口时间段到期之前发生，才能检测到双击。

#### 依赖项

仅当选择 **Enable click detection** 参数并为 **Type** 参数选择 `Double click` 选项时，此参数才会出现。

### **X axis** — X 轴上的点击检测 `on`（默认） | `off`

选择此选项以启用沿 X 轴的点击检测。值 `1` 表示检测到点击，`0` 表示未检测到点击。

#### 依赖项

仅当选择 **Enable click detection** 参数时，此参数才会出现。

### **Y axis** — Y 轴上的点击检测 `on`（默认） | `off`

选择此选项以启用沿 Y 轴的点击检测。值 `1` 表示检测到点击，`0` 表示未检测到点击。

#### 依赖项

仅当选择 **Enable click detection** 参数时，此参数才会出现。

### **Z axis** — Z 轴上的点击检测 `off`（默认） | `on`

选择此选项以启用沿 Z 轴的点击检测。值 `1` 表示检测到点击，`0` 表示未检测到点击。

#### 依赖项

仅当选择 **Enable click detection** 参数时，此参数才会出现。

### **Generate click interrupt** — 当检测到点击时生成中断 `off`（默认） | `on`

如果检测到点击，请选择此选项以生成中断。

#### 依赖项

仅当选择 **Enable click detection** 参数时，此参数才会出现。

### **Interrupt pin** — 用于生成点击中断的引脚 `INT1`（默认） | `INT2`

如果选择此选项，则当数据就绪时会在传感器的 INT1 或 IN2 引脚上生成中断，从而允许您触发其他子系统执行任何操作。

#### 依赖项

仅当选择 **Generate click interrupt** 参数时，此参数才会出现。

### **Click status** — 设置用于获取点击检测状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Click status [X,Y,Z]** 设置为输出端口之一。

#### 依赖项

仅当选择 **Enable click detection** 参数时，此参数才会出现。

### 可配置检测

### **Configurable detections** — 设置可配置检测的数量 `0`（默认） | `1` | `2`

选择可配置检测数量所需的选项。

#### 可配置检测 1

### **Detect** — 选择可配置事件 `Inertial wake-up`（默认） | `Free-fall` | `6D position` | `6D movement` | `4D position` | `4D movement`

选择所需的传感器功能。（Inertial wake-up、Free-fall、6D
position、6D movement、4D position、4D movement）。

#### 依赖项

仅当从 **Configurable detections**
参数中选择 `1` 或
`2` 时，此参数才会显示。

### **X axis** — X 轴上的可配置检测 `on`（默认） | `off`

选择此选项可启用 X 轴上的可配置事件检测状态。
值 `1` 表示检测到事件，
`0` 表示未检测到事件。

#### 依赖项

仅当从 **Detect**
参数中选择 `Inertial
wake-up` 或 `6D position` 或 `6D
movement` 或 `4D position` 或
`4D movement` 时，此参数才会显示。

### **Y axis** — Y 轴上的可配置检测 `on`（默认） | `off`

选择此选项可启用 Y 轴上的可配置事件检测状态。
值 `1` 表示检测到事件，
`0` 表示未检测到事件。

#### 依赖项

仅当从 **Detect**
参数中选择 `Inertial
wake-up` 或 `6D position` 或 `6D
movement` 或 `4D position` 或
`4D movement` 时，此参数才会显示。

### **Z axis** — Z 轴上的可配置检测 `on`（默认） | `off`

选择此选项可启用 Z 轴上的可配置事件检测状态。
值 `1` 表示检测到事件，
`0` 表示未检测到事件。

#### 依赖项

仅当从 **Detect** 参数中选择 `Inertial
wake-up` 或 `6D position` 或 `6D
movement` 时，此参数才会显示。

### **-X axis** — -X 轴上的可配置检测 `off`（默认） | `on`

选择此选项可启用 -X 轴上的可配置事件检测状态。
值 `1` 表示检测到事件，
`0` 表示未检测到事件。

#### 依赖项

仅当从 **Detect**
参数中选择 `6D position`
或 `6D movement` 或 `4D position`
或 `4D movement` 时，此参数才会显示。

### **-Y axis** — -Y 轴上的可配置检测 `off`（默认） | `on`

选择此选项可启用 -Y 轴上的可配置事件检测状态。
值 `1` 表示检测到事件，
`0` 表示未检测到事件。

#### 依赖项

仅当从 **Detect**
参数中选择 `6D position`
或 `6D movement` 或 `4D position`
或 `4D movement` 时，此参数才会显示。

### **-Z axis** — -Z 轴上的可配置检测 `off`（默认） | `on`

选择此选项可启用 -Z 轴上的可配置事件检测状态。
值 `1` 表示检测到事件，
`0` 表示未检测到事件。

#### 依赖项

仅当从 **Detect**
参数中选择 `6D position`
或 `6D movement` 时，此参数才会显示。

### **Threshold (m/s2** — 用于检测所选可配置检测的加速度阈值 `1.5`（默认）

指定用于检测所选可配置检测的阈值。当
加速度值越过指定阈值时，即检测到事件。

#### 依赖项

仅当从 **Configurable detections**
参数中选择 `1` 或
`2` 时，此参数才会显示。

### **Duration (s)** — 时间限制持续时间 `0.3`（默认） | `positive integer`

指定用于检测可配置事件的时间限制。要检测事件，
Threshold 条件必须在等于 Duration 的最短时间内得到满足。

#### 依赖项

仅当从 **Configurable detections**
参数中选择 `1` 或
`2` 时，此参数才会显示。

### **Generate interrupt** — 生成中断 `off`（默认） | `on`

如果选择此选项，则为所选
可配置检测生成中断。

#### 依赖项

仅当从 **Configurable detections**
参数中选择 `1` 或
`2` 时，此参数才会显示。

### **Interrupt pin** — 用于生成中断的引脚 `INT1`（默认） | `INT2`

如果选择此选项，则在检测到可配置事件时，会在传感器的引脚 INT1 或 IN2 上
生成中断，从而允许您触发其他
子系统以执行任何操作。

#### 依赖项

仅当选择 **Generate
interrupt** 参数时，此参数才会显示。

**注意**

**Configuration detections 2** 的参数与
**Configuration detections 1** 类似。有关配置
这些参数的信息，请参阅 Configurable detections。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

测量来自 LIS3DH 传感器的线性加速度、电压和温度

LIS3DH Accelerometer Sensor 模块使用与 Arduino® 硬件连接的 LIS3DH Accelerometer sensor 测量线性加速度、
传感器外部输入引脚（ADC1、ADC2 和 ADC3）上的电压以及温度。

该模块还提供启用高通滤波器、FIFO 和 FIFO
中断的选项。如果选择 **Generate data ready interrupt**，
则生成中断。选择 **Generate data ready interrupt** 后，如果禁用 FIFO，
则生成 data ready 中断；如果启用 FIFO，则生成 FIFO 中断。

该模块输出加速度测量状态，指定为值
`0`、`1` 或 `2`。值
`0` 表示读取的数据是新数据，`1` 表示
读取的数据不是新数据，`2` 表示数据已
被覆盖。

该模块将 single / double click axis 输出为
`1`×`3` 向量。click axis 提供检测到
click 的轴的信息。检测到 click 时，轴值显示 `1`，
否则显示 `0`。

该模块支持 inertial wake-up、free-fall、6D position、6D movement、4D position 和
4D movement 识别。该模块将 inertial wake-up axis 输出为
`1`×`3` 向量。这提供检测到 inertial wake-up 的轴
的信息。6D position axis 和 6D movement axis 的大小为
`1`×`6`。4D position 和 4D movement axis 的大小为
`1`×`4`。status 包含识别到检测的轴的信息。
在所选轴上识别到配置的检测时，status 值显示 `1`，
否则显示 `0`。

**注意**

在使用模型中可用的传感器模块执行监视和调优时，
请始终确保将传感器连接到开发板。
