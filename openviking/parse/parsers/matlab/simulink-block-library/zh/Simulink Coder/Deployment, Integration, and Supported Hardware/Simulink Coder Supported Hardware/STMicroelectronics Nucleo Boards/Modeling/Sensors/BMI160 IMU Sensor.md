---
type: simulink-block
title: 'BMI160 IMU Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Sensors'
documentation_page: 'bmi160imusensor'
documentation_source_path: 'nucleo/ref/bmi160imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# BMI160 IMU Sensor

## 端口

### 输出

### **Acceleration** — 由 BMI160 传感器测得的线性加速度行向量

线性加速度（以 m/s2 为单位）由连接到 Nucleo 板的 BMI160 传感器沿 x、y 和 z 轴测得，指定为行向量 [x,y,z]。

#### 依赖关系

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Angular Rate** — 由 BMI160 传感器测得的角速率行向量

角速率（以 rad/s 为单位）由连接到 Nucleo 板的 BMI160 传感器沿 x、y 和 z 轴测得，指定为行向量 [x,y,z]。

#### 依赖关系

仅当选择 **Angular rate (rad/s)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Magnetic Field** — 由辅助 BMM150 传感器测得的磁场强度行向量

磁场强度（以 µT 为单位）由作为辅助传感器连接到 BMI160 传感器的 BMM150 传感器沿 x、y 和 z 轴测得，指定为行向量 [x,y,z]。

#### 依赖关系

仅当选择 **Enable secondary magnetometer** 和 **Magnetic Field (µT)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Temperature** — 由 BMI160 传感器测得的温度标量

温度（以 ℃ 为单位）由连接到 Nucleo 板的 BMI160 传感器测得。

#### 依赖关系

仅当选择 **Temperature (℃)** 参数时，此输出端口才会出现。

**数据类型：** `double`

### **Acceleration Status** — 加速度值的状态 `0` | `1`

加速度状态 `0` 表示读取的数据是新的，`1` 表示读取的数据不是新的。

#### 依赖关系

仅当选择 **Acceleration Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

### **Angular Rate Status** — 角速率值的状态 `0` | `1`

角速率状态 `0` 表示读取的数据是新的，`1` 表示读取的数据不是新的。

#### 依赖关系

仅当选择 **Angular Rate Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

### **Magnetic Field Status** — 磁场值的状态 `0` | `1`

磁场状态 `0` 表示读取的数据是新的，`1` 表示读取的数据不是新的。

#### 依赖关系

仅当选择 **Magnetic Field Status** 参数时，此输出端口才会出现。

**数据类型：** `int8`

### **Interrupt Source** — 中断源的状态 `0` | `1` | `-1`

中断源是一个 `1`×`7` 向量，表示 Single tap、Double tap、High g detection、Any motion、Slow motion、Flat detection 和 Data ready 中断。

中断源状态 `1` 表示该中断已使能且它是所生成中断的源，`0` 表示该中断已使能但不是所生成中断的源，`-1` 表示该中断未使能。

#### 依赖关系

仅当选择以下参数之一时，此输出端口才会出现。

- **Single tap**
- **Double tap**
- **High g detection**
- **Any motion**
- **Flat detection**
- **Data ready**

**数据类型：** `double`

### **Tap event Source** — 轻触事件源的状态行向量

轻触事件源是一个 `1`×`4` 向量，表示 Single tap 或 Double tap 中断。前三个元素指示中断是否发生在 X、Y 和 Z 轴，第四个元素指示其位于轴的正方向还是负方向。对于方向，字节 `0` 表示负侧，`1` 表示正侧；对于其他字节，`1` 表示该轴是源，`0` 表示该轴不是源。

#### 依赖关系

仅当选择 **Interrupt source** 参数时，此输出端口才会出现。

**数据类型：** `int8`

### **High g event Source** — 高 g 事件源的状态行向量

高 g 事件源是一个 `1`×`4` 向量，表示 High g 中断。前三个元素指示中断是否发生在 X、Y 和 Z 轴，第四个元素指示其位于轴的正方向还是负方向。对于方向，字节 `0` 表示负侧，`1` 表示正侧；对于其他字节，`1` 表示该轴是源，`0` 表示该轴不是源。

#### 依赖关系

仅当选择 **Interrupt source** 参数时，此输出端口才会出现。

**数据类型：** `int8`

### **Any motion event Source** — Any motion 事件源的状态行向量

Any motion 事件源是一个 `1`×`4` 向量，表示 Any motion 中断。前三个元素指示中断是否发生在 X、Y 和 Z 轴，第四个元素指示其位于轴的正方向还是负方向。对于方向，字节 `0` 表示负侧，`1` 表示正侧；对于其他字节，`1` 表示该轴是源，`0` 表示该轴不是源。

#### 依赖关系

仅当选择 **Interrupt source** 参数时，此输出端口才会出现。

**数据类型：** `int8`

## 参数

### **I2C module** — 用于通信的模块 `I2C_A`（默认）

用于与 BMI160 传感器通信的 I2C 模块。不同 Nucleo 处理器支持的 I2C 模块数量各不相同。您可以通过打开 Configuration Parameters 对话框并检查 **Target hardware resources** 下的 I2C 特定选项卡，找到与处理器对应的受支持 I2C 模块（该处理器是您在 Simulink® 模型中为 Hardware Board 参数选择的处理器）。

### **BMI160 I2C address** — BMI160 传感器的 I2C 地址 `0x69`（默认） | `0x68`

BMI160 传感器与 Nucleo 处理器通信时使用的 I2C 地址。默认参数值（`0x69`）对应于 BOOSTXL-SENSORS BoosterPackTM Plug-in Module User's Guide 的 `Schematics` 一节中提到的值。

### **Enable secondary magnetometer** — 允许从作为 BMI160 辅助传感器连接的 BMM150 读取数据 `on`（默认） | `off`

如果选择此选项，该模块可以从作为 BMI160 辅助传感器连接的 BMM150 传感器读取磁力计数据。

### **BMM150 I2C address** — BMM150 传感器的 I2C 地址 `0x10`（默认） | `0x11` | `0x12` | `0x13`

作为 BMI160 传感器辅助传感器连接的 BMM150 传感器所使用的 I2C 地址。默认参数值（`0x13`）对应于 BOOSTXL-SENSORS BoosterPackTM Plug-in Module User's Guide 的 `Schematics` 一节中提到的值。

#### 依赖关系

仅当选择 **Enable secondary magnetometer** 参数时，此参数才会出现。

#### 选择输出

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on`（默认） | `off`

选择此参数可将 **Acceleration** 设置为输出端口之一。

### **Angular rate (rad/s)** — 设置用于读取角速率的输出端口 `on`（默认） | `off`

选择此参数可将 **Angular Rate** 设置为输出端口之一。

### **Magnetic Field (µT)** — 设置用于读取磁场的输出端口 `on`（默认） | `off`

选择此参数可将 **Magnetic Field** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `off`（默认） | `on`

选择此参数可将 **Temperature** 设置为输出端口之一。

### **Acceleration status** — 设置用于获取加速度状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Acceleration Status** 设置为输出端口之一。

### **Angular rate status** — 设置用于获取角速率状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Angular Rate Status** 设置为输出端口之一。

### **Magnetic Field Status** — 设置用于获取磁场状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Magnetic Field Status** 设置为输出端口之一。

### **Interrupt source** — 设置用于获取中断源状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Interrupt source** 设置为输出端口之一。

### **Tap source** — 设置用于获取轻触事件状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Tap event source** 设置为输出端口之一。

### **High g source** — 设置用于获取高 g 事件状态的输出端口 `off`（默认） | `on`

选择此参数可将 **High g event source** 设置为输出端口之一。

### **Any motion source** — 设置用于获取任意运动事件状态的输出端口 `off`（默认） | `on`

选择此参数可将 **Any motion event source** 设置为输出端口之一。

#### 加速度计设置

### **Accelerometer range** — 用于测量线性加速度的满量程 `±2g`（默认） | `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Accelerometer output data rate** — 加速度计数据的采样速率 `12.5 Hz`（默认） | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz`

选择加速度计数据的输出数据速率，该速率也决定带宽。

### **Enable low pass filter** — 启用低通滤波器以从 BMI160 传感器读取加速度计数据 `off`（默认） | `on`

选择此选项可对从 BMI160 传感器读取的加速度值启用低通滤波器。

### **Accelerometer filter mode** — 选择加速度计值的低通滤波器模式 `Normal`（默认） | `OSR2` | `OSR4`

选择加速度计值的低通滤波器模式。加速度计的 3dB 截止频率取决于此参数的值以及使用 **Accelerometer output data rate** 参数选择的 ODR。

#### 陀螺仪设置

### **Gyroscope range** — 用于测量角速率的满量程 `125 dps`（默认） | `250 dps` | `500 dps` | `1000 dps` | `2000 dps`

选择用于测量角速率的满量程（传感器需要测量的角速率范围）。

### **Gyroscope output data rate** — 陀螺仪数据的采样速率 `25 Hz`（默认） | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz` | `3200 Hz`

选择陀螺仪数据的输出数据速率，该速率也决定带宽。

### **Enable low pass filter** — 启用低通滤波器以从 BMI160 传感器读取陀螺仪数据 `off`（默认） | `on`

选择此选项可对从 BMI160 传感器读取的角速率值启用低通滤波器。

### **Gyroscope filter mode** — 选择陀螺仪值的低通滤波器模式 `Normal`（默认） | `OSR2` | `OSR4`

选择陀螺仪值的低通滤波器模式。陀螺仪的 3dB 截止频率取决于此参数的值以及使用 **Gyroscope output data rate** 参数选择的 ODR。

#### 磁力计设置

### **Magnetometer output data rate** — 磁力计数据的采样速率 `25 Hz`（默认） | `0.78125 Hz` | `1.5625 Hz` | `3.125 Hz` | `6.25 Hz` | `12.5 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz`

选择磁力计数据的输出数据速率。

**注意**

选择这些参数之一（**Single tap**、**Double tap**、**High g detection**、**Any motion**、**Slow motion**、**Flat detection**、**Data ready**）会覆盖输出端其他状态值的可用性。其他状态输出（`Acceleration status`、`Angular rate status` 和 `Magnetic field status`）的参数选择将被禁用。

### **Single tap** — 当触发 single tap 时使能中断 `off`（默认） | `on`

如果选择此选项，则当触发 single tap 且以下条件有效时，会在传感器的 INT1 或 INT2 引脚上生成中断。

- 轻触发生在 Shock Time 阈值期间。
- 在 Quiet Time 阈值期间没有发生轻触。

### **Quiet Time threshold** — 静默时间持续时间 `30 ms`（默认） | `20 ms`

选择用于生成 single tap 或 double tap 中断的静默时间阈值。要生成 single tap 或 double tap 中断，在指定的静默时间阈值期间不得发生轻触。

#### 依赖关系

仅当选择 **Single tap** 参数或 **Double tap** 参数时，此参数才会出现。

### **Shock Time threshold** — 冲击时间持续时间 `50 ms`（默认） | `75 ms`

选择用于 single tap 或 double tap 中断的冲击时间阈值。要生成 single tap 或 double tap 中断，轻触必须发生在指定的冲击时间阈值期间。

#### 依赖关系

仅当选择 **Single tap** 参数或 **Double tap** 参数时，此参数才会出现。

### **Amplitude threshold** — 用于检测轻触的幅度阈值 `0.1`（默认）

指定用于检测 single tap 或 double tap 的幅度阈值，范围为 0.03125g - 1.96875g。当值超过指定的幅度阈值时，会发生轻触。幅度阈值具有最小和最大范围，具体取决于加速度计范围。

#### 依赖关系

仅当选择 **Single tap** 参数或 **Double tap** 参数时，此参数才会出现。

### **Interrupt generate pin** — 用于生成 single tap 中断的引脚 `INT1`（默认） | `INT2`

选择在传感器上生成 single tap 中断的引脚，该中断可供 Nucleo 板使用。

#### 依赖关系

仅当选择 **Single tap** 参数时，此参数才会出现。

### **Double tap** — 当触发 double tap 时使能中断 `off`（默认） | `on`

如果选择此选项，则当触发 double tap 且以下条件有效时，会在传感器的 INT1 或 INT2 引脚上生成中断。

- 第一次轻触发生在 Shock Time 阈值期间。
- 在 Quiet Time 阈值期间没有发生轻触。
- 第二次轻触发生在 Duration Time 阈值期间。

### **Duration Time threshold** — 第二次轻触的时间阈值 `50 ms`（默认） | `100 ms` | `150 ms` | `200 ms` | `250 ms` | `375 ms` | `500 ms` | `700 ms`

选择用于 double tap 中断的持续时间阈值。要生成 double tap 中断，第二次轻触必须发生在指定的持续时间阈值期间。

#### 依赖关系

仅当选择 **Double tap** 参数时，此参数才会出现。

### **Interrupt generate pin** — 用于生成 double tap 中断的引脚 `INT1`（默认） | `INT2`

选择在传感器上生成 double tap 中断的引脚，该中断可供 Nucleo 板使用。

#### 依赖关系

仅当选择 **Double tap** 参数时，此参数才会出现。

### **High g detection** — 当触发 high g detection 时使能中断 `off`（默认） | `on`

如果选择此选项，则当检测到 high g 中断时，会在传感器的 INT1 或 INT2 引脚上生成中断。

### **Time threshold(2.5 ms to 640 ms)** — high g detection 的时间持续时间 `2.5`（默认） |

指定用于 high g 中断的时间阈值，范围为 2.5 ms 到 640 ms。要生成 high g 中断，high g detection 必须发生在指定的时间阈值期间。

#### 依赖关系

仅当选择 **High g detection** 参数时，此参数才会出现。

### **Amplitude threshold** — 用于检测 high g 中断的幅度阈值 `0.1`（默认）

指定用于检测 high g 中断的幅度阈值，范围为 0.00391g - 1.99546g。当值超过指定的幅度阈值时，会检测到 high g 中断。幅度阈值具有最小和最大范围，具体取决于加速度计范围。

#### 依赖关系

仅当选择 **High g detection** 参数时，此参数才会出现。

### **Interrupt generate pin** — 用于生成 high g 中断的引脚 `INT1`（默认） | `INT2`

选择在传感器上生成 high g 中断的引脚，该中断可供 Nucleo 板使用。

#### 依赖关系

仅当选择 **High g detection** 参数时，此参数才会出现。

### **Any motion** — 当触发任意运动中断时启用中断 `off`（默认） | `on`

如果选择此选项，则在检测到任意运动中断时，传感器的 INT1 或 INT2 引脚上会生成中断。

### **Time threshold** — 任意运动检测的时间长度 `1`（默认） | `2` | `3` | `4`

选择任意运动中断的时间阈值。任意运动检测必须在指定的时间阈值内发生。

#### 依赖关系

仅当选择 **Any motion** 参数时，此参数才会出现。

### **Amplitude threshold** — 用于检测任意运动中断的幅度阈值 `0.1`（默认）

指定用于检测任意运动中断的幅度阈值，范围为 0.00195g - 0.999g。当该值越过指定的幅度阈值时，将检测到任意运动中断。幅度阈值具有最小和最大范围，具体取决于加速度计范围。

#### 依赖关系

仅当选择 **Any motion** 参数时，此参数才会出现。

### **Interrupt generate pin** — 用于生成任意运动中断的引脚 `INT1`（默认） | `INT2`

选择在传感器上生成任意运动中断的引脚，该中断可供 Nucleo 板使用。

#### 依赖关系

仅当选择 **Any motion** 参数时，此参数才会出现。

### **Slow motion** — 当慢速运动中断被触发时启用中断 `off`（默认） | `on`

如果选择此选项，则在检测到慢速运动中断时，传感器的 INT1 或 INT2 引脚上会生成中断。

### **Time threshold** — 慢速运动检测的时间长度 `1`（默认） | `2` | `3` | `4`

选择慢速运动中断的时间阈值。慢速运动检测必须在指定的时间阈值内发生。

#### 依赖关系

仅当选择 **Slow motion** 参数时，此参数才会出现。

### **Amplitude threshold** — 用于检测慢速运动中断的幅度阈值 `0.1`（默认）

指定用于检测慢速运动中断的幅度阈值，范围为 0.00195g - 0.999g。当该值越过指定的幅度阈值时，将检测到慢速运动中断。

#### 依赖关系

仅当选择 **Slow motion** 参数时，此参数才会出现。

### **Interrupt generate pin** — 用于生成慢速运动中断的引脚 `INT1`（默认） | `INT2`

选择在传感器上生成慢速运动中断的引脚，该中断可供 Nucleo 板使用。

#### 依赖关系

仅当选择 **Slow motion** 参数时，此参数才会出现。

### **Flat detection** — 当平坦检测中断被触发时启用中断 `-1`（默认） | 正整数

如果选择此选项，则在检测到平坦检测中断时，传感器的 INT1 或 INT2 引脚上会生成中断。

### **Theta threshold (0.7° to 44.8°)** — 用于检测平坦检测中断的 Theta 阈值 `5`（默认）

指定用于检测平坦检测中断的幅度阈值，范围为 0.7° - 44.8°。当该值越过指定的幅度阈值时，将检测到平坦检测中断。

#### 依赖关系

仅当选择 **Flat detection** 参数时，此参数才会出现。

### **Time threshold** — 平坦检测中断的时间长度 `640`（默认） | `0` | `1280` | `2560`

选择平坦检测中断的时间阈值。平坦检测中断必须在指定的时间阈值内发生。

#### 依赖关系

仅当选择 **Flat detection** 参数时，此参数才会出现。

### **Interrupt generate pin** — 用于生成平坦检测中断的引脚 `INT1`（默认） | `INT2`

选择在传感器上生成平坦检测中断的引脚，该中断可供 Nucleo 板使用。

#### 依赖关系

仅当选择 **Flat detection** 参数时，此参数才会出现。

### **Data ready** — 当数据就绪时启用中断 `off`（默认） | `on`

如果选择此选项，则当数据就绪时，传感器的 INT1 或 INT2 引脚上会生成中断，允许您触发其他子系统以执行任意操作。

### **Interrupt generate pin** — 用于生成数据就绪中断的引脚 `INT1`（默认） | `INT2`

选择在传感器上生成数据就绪中断的引脚，该中断可供 Nucleo 板使用。

#### 依赖关系

仅当选择 **Enable data ready interrupt** 参数时，此参数才会出现。

### **Data type** — 来自 BMI160 传感器的值的输出数据类型 `single`（默认） | `double`

指定从 BMI160 传感器读取的值的输出数据类型。Nucleo 板的默认数据类型为 `single`。如果需要，可使用此参数将值更改为 `double`。

### **Sample time** — 读取数据的时间间隔 `-1`（默认） | 正整数

指定此模块从 BMI160 传感器读取数据的频率。将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

测量来自 BMI160 传感器的线性加速度、角速率和温度

BMI160 IMU Sensor 模块输出由连接到 STMicroelectronics® Nucleo 板的 BMI160 传感器测量得到的沿 x、y 和 z 轴的线性加速度和角速率值。该模块还输出 BMI160 传感器读取的温度。如果将 BMM150 作为辅助传感器连接到 BMI160，则 BMI160 模块还会输出由 BMM150 传感器测量得到的沿 x、y 和 z 轴的磁场。

该模块支持单次轻触、双击、高 g 检测、任意运动、慢速运动、平坦检测和数据就绪中断。

Interrupt source output 是一个 `1`-by-`7` 向量，其元素分别对应于单次轻触、双击、高 g 检测、任意运动、慢速运动、平坦检测和数据就绪中断的源。`1` 表示它是源，`0` 表示它不是源，`-1` 表示该中断未激活。

Tap source output 是一个 `1`-by-`4` 向量，其中前三个元素指示单次轻触/双击发生在 X、Y 和 Z 轴中的哪个轴，第四个元素指示它位于该轴的正方向还是负方向。High g source output 是一个 `1`-by-`4` 向量，其中前三个元素指示高 g 中断发生在 X、Y 和 Z 轴中的哪个轴，第四个元素指示它位于该轴的正方向还是负方向。Any motion source output 是一个 `1`-by-`4` 向量，它显示任意运动中断发生在 X、Y 和 Z 轴中的哪个轴，以及它位于该轴的正方向还是负方向。第一个字节表示事件是否发生在 X 轴，第二个字节表示事件是否发生在 Y 轴，第三个字节表示事件是否发生在 Z 轴，第四个字节表示方向。对于方向字节，`0` 表示负侧，`1` 表示正侧；对于其他字节，1 表示该轴是源，`0` 表示该轴不是源。

启用中断时，请使用 External Interrupt 模块并开发相应的函数调用子系统。
