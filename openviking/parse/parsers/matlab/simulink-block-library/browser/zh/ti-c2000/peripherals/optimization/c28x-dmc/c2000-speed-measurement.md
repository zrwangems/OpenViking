---
type: simulink-block
title: 'C2000 Speed Measurement'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000speedmeasurement'
documentation_source_path: 'ref/c2000speedmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Speed Measurement

## 端口

R2025b 中未记录。

## 参数

**基础速度**
:   要测量的电机的最大速度，单位为 revolutions per minute。

**微分器常数**
:   用于描述转子位置的微分器方程中的常数。

**低通滤波器常数**
:   应用于低通滤波器的常数。此常数为 1/(1+T\*(2πfc))，其中 T 是采样周期，fc 是截止频率。1/(2πfc) 项是低通滤波器时间常数。此模块使用低通滤波器来降低微分器产生的噪声。

**基础速度**
:   要测量的电机的最大速度，单位为 revolutions per minute。

**微分器常数**
:   用于描述转子位置的微分器方程中的常数。

**低通滤波器常数**
:   应用于低通滤波器的常数。此常数为 1/(1+T\*(2πfc))，其中 T 是采样周期，fc 是截止频率。1/(2πfc) 项是低通滤波器时间常数。此模块使用低通滤波器来降低微分器产生的噪声。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

计算电机速度

# C2000 Speed Measurement

计算电机速度

将现有 DMC 模块替换为 MCB 模块，以提高可用性和未来兼容性。建议您使用 Control Algorithm Design (Motor Control Blockset) 中的模块。虽然这些模块不是一对一替换，但它们使您能够实现相同的功能。

| C28x DMC lib | C28x DMC lib 在 MCB 中的等效项 |
| --- | --- |
| C2000 Clarke Transformation | Clarke Transform (Motor Control Blockset) |
| C2000 Inverse Park Transformation | Inverse Park Transform (Motor Control Blockset) |
| C2000 Park Transformation | Park Transform (Motor Control Blockset) |
| C2000 PID Controller | PI Controller (Motor Control Blockset) |
| C2000 Ramp Control | Position Generator (Motor Control Blockset) |
| C2000 Ramp Generator | Position Generator (Motor Control Blockset) |
| C2000 Space Vector Generator | PWM Reference Generator (Motor Control Blockset) |
| C2000 Speed Measurement | Speed Measurement (Motor Control Blockset) |

此模块在方向信息可用时根据转子位置计算电机速度。输入是来自编码器的电角度（`theta`）和旋转方向（`dir`）。输出是 Q format 中从 0 到 1 归一化的速度（`freq`），以及以 revolutions per minute 表示的速度（`rpm`）。

**注意**

- 要从此模块生成优化代码，请启用 `TI C28x` 或 `TI C28x (ISO)` Code Replacement Library。
- 此模块在代码生成期间不调用相应的 Texas Instruments® 库函数。相反，MathWorks® 代码使用 TI 函数的 global Q setting 根据模块输入动态调整 Q format。有关更多信息，请参阅 Using the IQmath Library。

### 理解模块的 Theta 输入

为了指示电机的旋转位置，模块期望一个从 0 到 1 变化的 32-bit、fixed-point 值。

模块输入 theta 由以下关系定义：

- 等于 0 的 theta 输入信号表示 0 degrees 旋转。
- 等于 1 的 theta 输入信号表示 360 degrees 旋转（一整圈）。

当电机以恒定速度旋转时，来自位置传感器（编码器）的 theta（以 counts 为单位）应从 0 线性增加到 1，然后突然返回到 0，类似锯齿形信号。调整编码器输出的 theta 信号，以获得 Speed Measurement 模块的输入信号范围。然后，将编码器信号转换为满足分辨率需求的 32-bit fixed-point Q format。

例如，如果您使用的位置传感器在电机一整圈旋转中生成 8000 counts（0.0450 degrees per count），则需要在计数器达到 8000 后将计数器重置为 0。每次读取编码器位置时，您都需要将位置转换为 32-bit、fixed-point Q format 值，并知道 8000 表示为 1.0。在此示例中，您的格式可以是 Q31。

### 基础速度参数

*基础速度* 是要测量的电机最大旋转速率。此值可能不是电机能够达到的最大速度。

Speed Measurement 模块根据两次连续的电机位置 *theta* 读数（*thetanew* 和 *thetaold*）（电机的基础速度；以及读数之间的时间）计算电机速度。模块能够计算的最大速度发生在两个连续采样之间的差值 [abs(*thetanew*-*thetaold*)] 为 1.0 时——即在 theta 采样之间发生了一整圈电机旋转。

因此，您为基础速度（单位为 revolutions per minute）参数提供的值是电机位置信号在一个采样时间内报告一整圈旋转时的速度（单位为 revolutions per minute）。虽然电机可能旋转得比基础速度快，但模块在此情况下无法计算旋转速率。如果电机在一个采样时间内完成超过一整圈旋转，计算出的速度可能错误。模块不知道在采样 *thetanew* 和 *thetaold* 之间，*theta* 已从 1 回绕到 0 并再次开始递增。

两次 theta 读数之间的时间差是采样时间。Speed Measurement 模块从模型中的上游模块继承采样时间。您在上游模块中设置采样时间，然后 Speed Measurement 模块使用该采样时间来计算电机的旋转速率。

### 采样时间计算

电机速度测量取决于您在模型中设置的采样时间。您的采样时间必须足够短，以测量电机的满速度。

两个参数决定您的采样时间——电机基础速度和编码器 counts per revolution。为了能够测量最大旋转速率，您必须每圈至少采样一次。对于基础速度等于 1000 rpm 的电机，即 16.67 rps，您需要以 1/16.67 s 采样，即 0.06 s/sample。此采样率 16.67 samples per second 是最大采样时间（最低采样率），以便您可以测量电机的满速度。

使用相同的采样率假设，模块能够测量的最小速度取决于编码器 counts per revolution。在可测量的最低电机速度下，编码器每个采样周期生成一个 count——16.67 counts per second。对于生成 8000 counts per revolution 的编码器，这导致能够测量的速度为 [(16.67 counts/s) \* (0.045 degrees/count)] = 0.752 degrees per second，或约 45 degrees per minute——one-eighth RPM。

### 微分器常数

微分器常数是应用于模块输出的标量值。例如，将其设置为 `1` 不会改变输出。将常数设置为 `1/4` 会将频率和 revolutions per minute 输出乘以 0.25。当您的电机具有多个极对，并且一次电气旋转不等于一次机械旋转时，此设置可能有用。该常数让您能够考虑电气旋转速率和机械旋转速率之间的差异。

### 低通滤波器常数

如果位置信号有噪声，此模块包含滤波功能。将滤波器常数设置为 `0` 会禁用滤波器。将滤波器常数设置为 `1` 会滤除整个信号，并导致模块输出等于 0。使用仿真来确定系统的最佳滤波器常数。您的目标是过滤得足以去除信号上的噪声，但不要过滤得太多，以至于速度测量无法对突然的速度变化做出反应。

- C2000 Speed Measurement 模块
