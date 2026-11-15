---
type: simulink-block
title: 'BMI160 IMU Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sensors / IMU Sensors'
documentation_page: 'bmi160imusensor'
documentation_source_path: 'supportpkg/raspberrypi_ref/bmi160imusensor.html'
language: zh-CN
chinese_source: worker-translation
---

# BMI160 IMU Sensor

## 端口

### 输出

### **Acceleration** — 由 BMI160 传感器测量的线性加速度行向量

由连接到 Raspberry Pi 板的 BMI160 传感器测量的线性加速度（以 m/s2 为单位），沿 x、y 和 z 轴，指定为行向量 [x,y,z]。

#### 依赖项

仅当选择 **Acceleration (m/s2)** 参数时，此输出端口才出现。

**数据类型：** `double`

### **Angular Rate** — 由 BMI160 传感器测量的角速率行向量

由连接到 Raspberry Pi 板的 BMI160 传感器测量的角速率（以 rad/s 为单位），沿 x、y 和 z 轴，指定为行向量 [x,y,z]。

#### 依赖项

仅当选择 **Angular rate (rad/s)** 参数时，此输出端口才出现。

**数据类型：** `double`

### **Magnetic Field** — 由辅助 BMM150 传感器测量的磁场强度行向量

由作为辅助传感器连接到 BMI160 传感器的 BMM150 传感器测量的磁场强度（以 µT 为单位），沿 x、y 和 z 轴，指定为行向量 [x,y,z]。

#### 依赖项

仅当选择 **Enable secondary magnetometer** 和 **Magnetic Field (µT)** 参数时，此输出端口才出现。

**数据类型：** `double`

### **Temperature** — 由 BMI160 传感器测量的温度标量

由连接到 Raspberry Pi 板的 BMI160 传感器测量的温度（以 ℃ 为单位）。

#### 依赖项

仅当选择 **Temperature (℃)** 参数时，此输出端口才出现。

**数据类型：** `double`

### **Acceleration Status** — 加速度值的状态 `0` | `1`

加速度状态 `0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据。

#### 依赖项

仅当选择 **Acceleration Status** 参数时，此输出端口才出现。

**数据类型：** `int8`

### **Angular Rate Status** — 角速率值的状态 `0` | `1`

角速率状态 `0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据。

#### 依赖项

仅当选择 **Angular Rate Status** 参数时，此输出端口才出现。

**数据类型：** `int8`

### **Magnetic Field Status** — 磁场值的状态 `0` | `1`

磁场状态 `0` 表示读取的数据是新数据，`1` 表示读取的数据不是新数据。

#### 依赖项

仅当选择 **Magnetic Field Status** 参数时，此输出端口才出现。

**数据类型：** `int8`

### **Interrupt Source** — 中断源的状态 `0` | `1` | `-1`

中断源是 `1`-by-`7` 向量，表示 Single tap、Double tap、High g detection、Any motion、Slow motion、Flat detection 和 Data ready 中断。

中断源状态 `1` 表示中断已使能且它是所生成中断的源，`0` 表示中断已使能但它不是所生成中断的源，`-1` 表示中断未使能。

#### 依赖项

仅当选择以下参数之一时，此输出端口才出现。

- **Single tap**
- **Double tap**
- **High g detection**
- **Any motion**
- **Flat detection**
- **Data ready**

**数据类型：** `double`

### **Tap event Source** — Tap event source 的状态行向量

Tap event source 是 `1`-by-`4` 向量，表示 Single tap 或 Double tap 中断。前三个元素指示中断是否发生在 X、Y 和 Z 轴，第四个元素指示它位于轴的正方向还是负方向。对于方向，字节 `0` 表示负侧，`1` 表示正侧；对于其他字节，`1` 表示该轴是源，`0` 表示该轴不是源。

#### 依赖项

仅当选择 **Interrupt source** 参数时，此输出端口才出现。

**数据类型：** `int8`

### **High g event Source** — 高 g 事件源的状态行向量

High g event source 是 `1`-by-`4` 向量，表示 High g 中断。前三个元素指示中断是否发生在 X、Y 和 Z 轴，第四个元素指示它位于轴的正方向还是负方向。对于方向，字节 `0` 表示负侧，`1` 表示正侧；对于其他字节，`1` 表示该轴是源，`0` 表示该轴不是源。

#### 依赖项

仅当选择 **Interrupt source** 参数时，此输出端口才出现。

**数据类型：** `int8`

### **Any motion event Source** — 任何运动事件源的状态行向量

Any motion event source 是 `1`-by-`4` 向量，表示 Any motion 中断。前三个元素指示中断是否发生在 X、Y 和 Z 轴，第四个元素指示它位于轴的正方向还是负方向。对于方向，字节 `0` 表示负侧，`1` 表示正侧；对于其他字节，`1` 表示该轴是源，`0` 表示该轴不是源。

#### 依赖项

仅当选择 **Interrupt source** 参数时，此输出端口才出现。

**数据类型：** `int8`

## 参数

### **I2C module** — 用于通信的模块 `1` (默认)

用于与 BMI160 传感器通信的 I2C 模块。

### **BMI160 I2C address** — BMI160 传感器的 I2C 地址 `0x69` (默认) | `0x68`

BMI160 传感器与 Raspberry Pi 板通信所使用的 I2C 地址。

### **Enable secondary magnetometer** — 启用从作为辅助传感器连接到 BMI160 的 BMM150 读取数据 `on` (默认) | `off`

如果选择此选项，该模块可以从作为辅助传感器连接到 BMI160 的 BMM150 传感器读取磁力计数据。

### **BMM150 I2C address** — BMM150 传感器的 I2C 地址 `0x13` (默认) | `0x10` | `0x11` | `0x12`

作为辅助传感器连接到 BMI160 传感器的 BMM150 传感器所使用的 I2C 地址。

#### 依赖项

仅当选择 **Enable secondary magnetometer** 参数时，此参数才出现。

#### 选择输出

### **Acceleration (m/s2)** — 设置用于读取加速度的输出端口 `on` (默认) | `off`

选择此参数以将 **Acceleration** 设置为输出端口之一。

### **Angular rate (rad/s)** — 设置用于读取角速率的输出端口 `on` (默认) | `off`

选择此参数以将 **Angular Rate** 设置为输出端口之一。

### **Magnetic Field (µT)** — 设置用于读取磁场的输出端口 `on` (默认) | `off`

选择此参数以将 **Magnetic Field** 设置为输出端口之一。

### **Temperature (℃)** — 设置用于读取温度的输出端口 `off` (默认) | `on`

选择此参数以将 **Temperature** 设置为输出端口之一。

### **Acceleration status** — 设置用于获取加速度状态的输出端口 `off` (默认) | `on`

选择此参数以将 **Acceleration Status** 设置为输出端口之一。

### **Angular rate status** — 设置用于获取角速率状态的输出端口 `off` (默认) | `on`

选择此参数以将 **Angular Rate Status** 设置为输出端口之一。

### **Magnetic Field Status** — 设置用于获取磁场状态的输出端口 `off` (默认) | `on`

选择此参数以将 **Magnetic Field Status** 设置为输出端口之一。

### **Interrupt source** — 设置用于获取中断源状态的输出端口 `off` (默认) | `on`

选择此参数以将 **Interrupt source** 设置为输出端口之一。

### **Tap source** — 设置用于获取轻触事件状态的输出端口 `off` (默认) | `on`

选择此参数以将 **Tap event source** 设置为输出端口之一。

### **High g source** — 设置用于获取高 g 事件状态的输出端口 `off` (默认) | `on`

选择此参数以将 **High g event source** 设置为输出端口之一。

### **Any motion source** — 设置用于获取任何运动事件状态的输出端口 `off` (默认) | `on`

选择此参数以将 **Any motion event source** 设置为输出端口之一。

#### 加速度计设置

### **Accelerometer range** — 用于测量线性加速度的满量程 `±2g` (默认) | `±4g` | `±8g` | `±16g`

选择用于测量线性加速度的满量程（传感器需要测量的加速度范围）。

### **Accelerometer output data rate** — 加速度计数据的采样速率 `12.5 Hz` (默认) | `25 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz`

选择加速度计数据采样的输出数据率，这也决定带宽。

### **Enable low pass filter** — 启用低通滤波器以从 BMI160 传感器读取加速度计数据 `off` (默认) | `on`

选择此选项以启用从 BMI160 传感器读取的加速度值的低通滤波器。

### **Accelerometer filter mode** — 选择加速度计值低通滤波器的滤波模式 `Normal` (默认) | `OSR2` | `OSR4`

选择加速度计值低通滤波器的滤波模式。加速度计的 3dB 截止频率取决于此参数的值以及您使用 **Accelerometer output data rate** 参数选择的 ODR。

#### 陀螺仪设置

### **Gyroscope range** — 用于测量角速率的满量程 `125 dps` (默认) | `250 dps` | `500 dps` | `1000 dps` | `2000 dps`

选择用于测量角速率的满量程（传感器需要测量的角速率范围）。

### **Gyroscope output data rate** — 陀螺仪数据的采样速率 `25 Hz` (默认) | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz` | `1600 Hz` | `3200 Hz`

选择陀螺仪数据采样的输出数据率，这也决定带宽。

### **Enable low pass filter** — 启用低通滤波器以从 BMI160 传感器读取陀螺仪数据 `off` (默认) | `on`

选择此选项以启用从 BMI160 传感器读取的角速率值的低通滤波器。

### **Gyroscope filter mode** — 选择陀螺仪值低通滤波器的滤波模式 `Normal` (默认) | `OSR2` | `OSR4`

选择陀螺仪值低通滤波器的滤波模式。陀螺仪的 3dB 截止频率取决于此参数的值以及您使用 **Gyroscope output data rate** 参数选择的 ODR。

#### 磁力计设置

### **Magnetometer output data rate** — 磁力计数据的采样速率 `25 Hz` (默认) | `0.78125 Hz` | `1.5625 Hz` | `3.125 Hz` | `6.25 Hz` | `12.5 Hz` | `50 Hz` | `100 Hz` | `200 Hz` | `400 Hz` | `800 Hz`

选择磁力计数据采样的输出数据率。

**在以下项上生成中断**

**注意**

选择这些参数之一（**Single tap**、**Double tap**、**High g detection**、**Any motion**、**Slow motion**、**Flat detection**、**Data ready**）会覆盖输出处其他状态值的可用性。其他状态输出（`Acceleration status`、`Angular rate status` 和 `Magnetic field status`）的参数选择被禁用。

### **Single tap** — 当触发单次轻触时启用中断 `off` (默认) | `on`

如果选择此选项，当触发单次轻触且以下条件有效时，将在传感器的 INT1 或 INT2 引脚上生成中断。

- 轻触发生在 Shock Time threshold 期间。
- 在 Quiet Time threshold 期间没有发生轻触。

### **Quiet Time threshold** — 静默时间持续时间 `30 ms` (默认) | `20 ms`

选择用于生成单次轻触或双击中断的静默时间阈值。在指定的静默时间阈值期间不得发生轻触，才能生成单次轻触或双击中断。

#### 依赖项

仅当选择 **Single tap** 参数或 **Double tap** 参数时，此参数才出现。

### **Shock Time threshold** — 冲击时间持续时间 `50 ms` (默认) | `75 ms`

选择用于单次轻触或双击中断的冲击时间阈值。轻触必须发生在指定的冲击时间阈值期间，才能生成单次轻触或双击中断。

#### 依赖项

仅当选择 **Single tap** 参数或 **Double tap** 参数时，此参数才出现。

### **Amplitude threshold** — 用于检测轻触的幅度阈值 `0.1` (默认)

指定用于检测单次轻触或双击的幅度阈值，范围为 0.03125g - 1.96875g。当该值超过指定的幅度阈值时，会发生轻触。幅度阈值具有最小和最大范围，取决于加速度计范围。

#### 依赖项

仅当选择 **Single tap** 参数或 **Double tap** 参数时，此参数才出现。

### **Interrupt generate pin** — 用于生成单次轻触中断的引脚 `INT1` (默认) | `INT2`

选择在传感器上生成单次轻触中断的引脚，该中断可供 Raspberry Pi 板使用。

#### 依赖项

仅当选择 **Single tap** 参数时，此参数才出现。

### **Double tap** — 当触发双击时启用中断 `off` (默认) | `on`

如果选择此选项，当触发双击且以下条件有效时，将在传感器的 INT1 或 INT2 引脚上生成中断。

- 第一次轻触发生在 Shock Time threshold 期间。
- 在 Quiet Time threshold 期间没有发生轻触。
- 第二次轻触发生在 Duration Time threshold 期间。

### **Duration Time threshold** — 第二次轻触的时间阈值 `50 ms` (默认) | `100 ms` | `150 ms` | `200 ms` | `250 ms` | `375 ms` | `500 ms` | `700 ms`

选择双击中断的持续时间阈值。第二次轻触必须发生在指定的持续时间阈值期间，才能生成双击中断。

#### 依赖项

仅当选择 **Double tap** 参数时，此参数才出现。

### **Interrupt generate pin** — 用于生成双击中断的引脚 `INT1` (默认) | `INT2`

选择在传感器上生成双击中断的引脚，该中断可供 Raspberry Pi 板使用。

#### 依赖项

仅当选择 **Double tap** 参数时，此参数才出现。

### **High g detection** — 当触发高 g 检测时启用中断 `off` (默认) | `on`

如果选择此选项，当检测到高 g 中断时，将在传感器的 INT1 或 INT2 引脚上生成中断。

### **Time threshold(2.5 ms to 640 ms)** — 高 g 检测的时间持续时间 `2.5` (默认) |

指定高 g 中断的时间阈值，范围为 2.5 ms 到 640 ms。高 g 检测必须发生在指定的时间阈值期间，才能生成高 g 中断。

#### 依赖项

仅当选择 **High g detection** 参数时，此参数才出现。

### **Amplitude threshold** — 用于检测高 g 中断的幅度阈值 `0.1` (默认)

指定用于检测高 g 中断的幅度阈值，范围为 0.00391g - 1.99546g。当该值超过指定的幅度阈值时，检测到高 g 中断。幅度阈值具有最小和最大范围，取决于加速度计范围。

#### 依赖项

仅当选择 **High g detection** 参数时，此参数才出现。

### **Interrupt generate pin** — 用于生成高 g 中断的引脚 `INT1` (默认) | `INT2`

选择在传感器上生成高 g 中断的引脚，该中断可供 Raspberry Pi 板使用。

#### 依赖项

仅当选择 **High g detection** 参数时，此参数才出现。

### **Any motion** — 当触发任何运动中断时启用中断 `off` (默认) | `on`

如果选择此选项，当检测到任何运动中断时，将在传感器的 INT1 或 INT2 引脚上生成中断。

### **Time threshold** — 任何运动检测的时间持续时间 `1` (默认) | `2` | `3` | `4`

选择任何运动中断的时间阈值。任何运动检测必须发生在指定的时间阈值期间。

#### 依赖项

仅当选择 **Any motion** 参数时，此参数才出现。

### **幅度阈值** — 用于检测任何运动中断的幅度阈值 `0.1`（默认）

指定用于检测任何运动中断的幅度阈值，范围为 0.00195g - 0.999g。当值超过指定的幅度阈值时，检测到任何运动中断。幅度阈值具有最小和最大范围，该范围取决于加速度计范围。

#### 依赖关系

仅当选择 **任何运动** 参数时，此参数才会显示。

### **中断生成引脚** — 用于生成任何运动中断的引脚 `INT1`（默认）| `INT2`

选择传感器上生成任何运动中断的引脚，该中断可供 Raspberry Pi 板使用。

#### 依赖关系

仅当选择 **任何运动** 参数时，此参数才会显示。

### **慢动作** — 启用慢动作中断触发时的中断 `off`（默认）| `on`

如果选中此选项，则当检测到慢动作中断时，会在传感器的引脚 INT1 或 INT2 上生成中断。

### **时间阈值** — 慢动作检测的时间长度 `1`（默认）| `2` | `3` | `4`

选择慢动作中断的时间阈值。慢动作检测必须在指定的时间阈值内发生。

#### 依赖关系

仅当选择 **慢动作** 参数时，此参数才会显示。

### **幅度阈值** — 用于检测慢动作中断的幅度阈值 `0.1`（默认）

指定用于检测慢动作中断的幅度阈值，范围为 0.00195g - 0.999g。当值超过指定的幅度阈值时，检测到慢动作中断。

#### 依赖关系

仅当选择 **慢动作** 参数时，此参数才会显示。

### **中断生成引脚** — 用于生成慢动作中断的引脚 `INT1`（默认）| `INT2`

选择传感器上生成慢动作中断的引脚，该中断可供 Raspberry Pi 板使用。

#### 依赖关系

仅当选择 **慢动作** 参数时，此参数才会显示。

### **平面检测** — 当平面检测中断触发时启用中断 `-1`（默认）| 正整数

如果选中此选项，则当检测到平面检测中断时，会在传感器的引脚 INT1 或 INT2 上生成中断。

### **Theta 阈值 (0.7° 至 44.8°)** — 用于检测平面检测中断的 Theta 阈值 `5`（默认）

指定用于检测平面检测中断的幅度阈值，范围为 0.7° - 44.8°。当值超过指定的幅度阈值时，检测到平面检测中断。

#### 依赖关系

仅当选择 **平面检测** 参数时，此参数才会显示。

### **时间阈值** — 平面检测中断的时间长度 `640`（默认）| `0` | `1280` | `2560`

选择平面检测中断的时间阈值。平面检测中断必须在指定的时间阈值内发生。

#### 依赖关系

仅当选择 **平面检测** 参数时，此参数才会显示。

### **中断生成引脚** — 用于生成平面检测中断的引脚 `INT1`（默认）| `INT2`

选择传感器上生成平面检测中断的引脚，该中断可供 Raspberry Pi 板使用。

#### 依赖关系

仅当选择 **平面检测** 参数时，此参数才会显示。

### **数据就绪** — 当数据就绪时启用中断 `off`（默认）| `on`

如果选中此选项，则当数据就绪时，会在传感器的引脚 INT1 或 INT2 上生成中断，从而允许您触发其他子系统以执行任何操作。

### **中断生成引脚** — 用于生成数据就绪中断的引脚 `INT1`（默认）| `INT2`

选择传感器上生成数据就绪中断的引脚，该中断可供 Raspberry Pi 板使用。

#### 依赖关系

仅当选择 **启用数据就绪中断** 参数时，此参数才会显示。

### **数据类型** — 来自 BMI160 传感器的值的输出数据类型 `single`（默认）| `double`

指定从 BMI160 传感器读取的值的输出数据类型。Raspberry Pi 板的默认数据类型为 `single`。如果需要，可使用此参数将值更改为 `double`。

### **采样时间** — 读取数据的时间间隔 `-1`（默认）| 正整数

指定此模块从 BMI160 传感器读取数据的频率。将此参数设置为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sensors / IMU Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

从 BMI160 传感器测量线性加速度、角速率和温度

BMI160 模块输出由连接到 Raspberry Pi® 板的 BMI160 传感器测量得到的沿 x、y 和 z 轴的线性加速度和角速率值。该模块还输出 BMI160 传感器读取的温度。如果将 BMM150 作为辅助传感器连接到 BMI160，则 BMI160 模块还输出由 BMM150 传感器测量得到的沿 x、y 和 z 轴的磁场。

该模块支持单次轻触、双击、高 g 检测、任何运动、慢动作、平面检测和数据就绪中断。

Interrupt source output 是一个 `1`-by-`7` 向量，其元素分别对应于单次轻触、双击、高 g 检测、任何运动、慢动作、平面检测和数据就绪中断的来源。`1` 表示它是来源，`0` 表示它不是来源，`-1` 表示该中断未激活。

Tap source output 是一个 `1`-by-`4` 向量，其中前三个元素指示单次轻触/双击发生在 X、Y 和 Z 轴中的哪个轴，第四个元素指示它位于该轴的正方向还是负方向。High g source output 是一个 `1`-by-`4` 向量，其中前三个元素指示 High g 中断发生在 X、Y 和 Z 轴中的哪个轴，第四个元素指示它位于该轴的正方向还是负方向。Any motion source output 是一个 `1`-by-`4` 向量，它显示任何运动中断发生在 X、Y 和 Z 轴中的哪个轴，以及它位于该轴的正方向还是负方向。第一个字节表示事件是否发生在 X 轴，第二个字节表示事件是否发生在 Y 轴，第三个字节表示事件是否发生在 Z 轴，第四个字节表示方向。对于方向字节，`0` 表示负侧，`1` 表示正侧；对于其他字节，1 表示该轴是来源，`0` 表示该轴不是来源。

启用中断时，使用 External Interrupt 模块并开发相应的函数调用子系统。
