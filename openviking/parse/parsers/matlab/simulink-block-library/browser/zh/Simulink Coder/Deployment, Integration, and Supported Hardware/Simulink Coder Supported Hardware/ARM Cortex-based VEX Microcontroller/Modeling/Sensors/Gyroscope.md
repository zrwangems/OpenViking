---
type: simulink-block
title: 'Gyroscope'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'gyroscope'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/gyroscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Gyroscope

## 端口

### 输入

### **Rst** — 重置模式标量

当您将 **Reset mode** 参数设置为 `Reset by external signal` 时，`Rst` 端口变为可用。

模块输出根据此端口处的输入值重置为 0。当您向模块输入发送非 0 值时，模块输出重置为 0。对于每个采样周期，模块输出自上次重置以来的陀螺仪读数。

当外部信号为 0 时，输出计算方式与 `No reset` 模式相同。当外部信号非零时，输出计算方式与 `Reset at each sample time` 模式相同。有关重置模式的详细信息，请参阅 **Reset mode** 参数描述。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Sim** — 用于仿真目的的陀螺仪读数标量

当您选择 **Add input port for simulation** 参数时，`Sim` 端口变为可用。

对于仿真行为，请通过源模块从此端口提供陀螺仪读数

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Port\_1** — 自上次启动或重置以来的偏航旋转标量

沿陀螺仪传感器轴的偏航旋转，以 degrees 为单位。当您沿顺时针方向旋转陀螺仪传感器时，滴答计数会减少。当您沿逆时针方向旋转编码器时，滴答计数会增加。

**数据类型：** `double`

## 参数

### **Analog port** — 模拟端口号 `1`（默认）| `2` | `3` | `4` | `5` | `6` | `7` | `8`

选择微控制器上连接陀螺仪传感器的模拟端口号。

### **Calibration multiplier** — 用于调整模块读数的常量 `196`（默认）| `Any value between 0 and 65535`

指定一个值以消除模块读数输出中的正偏置或负偏置。要校准传感器，请尝试不同的范围，直到达到可接受的精度范围。

当陀螺仪读数大于实际旋转时，减小 **Calibration multiplier** 值。当陀螺仪读数小于实际旋转时，增大 **Calibration multiplier** 值。

### **Reset mode** — 用于重置陀螺仪传感器读数的重置模式 `No reset`（默认）| `Reset at each sample time` | `Reset by external signal`

- 在示例表中，假设模块采样时间为 1 second。在时间点 T = 0 时的旋转角度为 0 degrees。

  此模块支持的不同重置模式包括：

  - `No reset` – 陀螺仪读数不会重置，并且模块输出总旋转角度。

    例如，在表中，T = 1 时，陀螺仪传感器沿逆时针方向旋转 20 degrees，因此输出为 20。

    在 T = 1 和 T = 2 之间，陀螺仪传感器沿逆时针方向旋转 10 degrees。因此，T = 2 时的偏航旋转为 30（来自 T = 1 的 20 和来自 T = 2 的 10）。

    在此重置模式下，任意时间点的输出是先前偏航旋转和当前偏航旋转的累积和。
  - `Reset at each sample time`  – 对于每个采样周期，模块输出陀螺仪读数，然后将其重置为 0。

    例如，在表中，T = 1 时，陀螺仪传感器沿逆时针方向旋转 20 degrees，因此输出为 20。

    在 T = 1 和 T = 2 之间，陀螺仪传感器沿逆时针方向旋转 10 degrees，因此输出为 10。

    在此重置模式下，输出是特定时间点的偏航旋转。
  - `Reset by external signal`  – 陀螺仪读数根据 `Rst` 端口的输入值重置为 0。当您向模块输入发送非 0 值时，陀螺仪读数重置为 0。对于每个采样周期，模块输出自上次重置以来的陀螺仪读数。

    例如，在表中，当外部信号为 0 时，输出计算方式与 `No reset` 模式相同。当外部信号非零时，输出计算方式与 `Reset at each sample time` 模式相同。

### **Add input port for simulation** — 指定是否要运行普通模式仿真 off（默认）| on

如果要使用提供输入值的源模块进行普通模式仿真，请选择此参数。

### **Sample time** — 指定模块读取旋转的频率 `0.2`（默认）

指定模块读取旋转的频率，以 seconds 为单位。

#### 依赖项

如果您将 **Reset mode** 参数设置为 `Reset by external signal`，或选择 **Add input port for simulation** 参数，则 **Sample time** 参数将被隐藏，并且该值被继承（Sample time = -1）。

## 所属库

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller/Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

测量以 degrees 为单位的偏航旋转

Gyroscope 模块测量沿陀螺仪传感器单轴的旋转角度（偏航）。在图中，垂直轴上方的箭头表示偏航。箭头方向表示陀螺仪传感器读数的正方向。

该模块将角度（以 degrees 为单位）输出为双精度标量值。当您沿顺时针方向旋转陀螺仪传感器时，滴答计数会减少。当您沿逆时针方向旋转编码器时，滴答计数会增加。

使用 **Calibration multiplier** 参数，校准陀螺仪并减少陀螺仪传感器读数中的漂移。漂移是由于温度、机械振动和电机磁场影响等外部因素引入到读数中的正偏置或负偏置。已校准的传感器有助于减少漂移，并在传感器读数中获得可接受的精度范围。要了解如何校准陀螺仪传感器，请参阅 Turn Robot Using LCD Button Press and Display Gyroscope Reading on LCD Screen。

在仿真期间，无硬件时，如果没有源模块连接到仿真输入端口，此模块将发出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。要实现仿真行为，请从 VEX microcontroller library 中的 Utilities library 连接一个源模块。

在代码生成期间，任何连接到 Gyroscope 模块输入端口的仿真模块都会被忽略，并且对生成的代码没有影响。

为使此模块生成的代码能与陀螺仪传感器正常工作，请将 VEX 7.2 volt 电池连接到微控制器。在将程序下载到 VEX 微控制器之前，请开启电池。开启电池后，为了正确初始化陀螺仪，不要移动安装有陀螺仪传感器的机器人。
