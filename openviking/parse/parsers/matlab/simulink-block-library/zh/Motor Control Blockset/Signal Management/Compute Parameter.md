---
type: simulink-block
title: 'Compute Parameter'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'computeparameter'
documentation_source_path: 'ref/computeparameter.html'
language: zh-CN
chinese_source: worker-translation
---

# Compute Parameter

## 端口

### 输入

### **Npp** — 电机中可用的极对数 标量

电机中可用的极对数。

#### 依赖

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Flux Observer 或 I-F Controller 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **R** — 定子绕组电阻 标量

电机的定子相绕组电阻（单位：欧姆）。

#### 依赖

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Flux Observer 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **Rs** — 定子绕组电阻 标量

电机的定子相绕组电阻（单位：欧姆）。

#### 依赖

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Extended EMF Observer 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **Ld** — 沿 *d* 轴的定子绕组电感 标量

电机沿 *d* 轴的定子绕组电感（单位：亨利）。

#### 依赖

要启用此端口：

- 将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Flux Observer 模块或 Extended EMF Observer 模块的相对路径。
- 如果兼容模块为 Flux Observer，请将 Flux Observer 模块的**电机选择**参数设置为 `PMSM`。

**数据类型：** `single` | `double` | `fixed point`

### **Lq** — 沿 *q* 轴的定子绕组电感 标量

电机沿 *q* 轴的定子绕组电感（单位：亨利）。

#### 依赖

要启用此端口：

- 将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Extended EMF Observer 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **Lls** — 感应电机的定子漏电感 标量

感应电机定子绕组的漏电感（单位：亨利）。

#### 依赖

要启用此端口：

- 将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Flux Observer 模块的相对路径。
- 将 Flux Observer 模块的**电机选择**参数设置为 `ACIM`。

**数据类型：** `single` | `double` | `fixed point`

### **Llr** — 感应电机的转子漏电感 标量

感应电机转子绕组的漏电感（单位：亨利）。

#### 依赖

要启用此端口：

- 将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Flux Observer 模块的相对路径。
- 将 Flux Observer 模块的**电机选择**参数设置为 `ACIM`。

**数据类型：** `single` | `double` | `fixed point`

### **Lm** — 感应电机的励磁电感 标量

感应电机的励磁电感（单位：亨利）。

#### 依赖

要启用此端口：

- 将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Flux Observer 模块的相对路径。
- 将 Flux Observer 模块的**电机选择**参数设置为 `ACIM`。

**数据类型：** `single` | `double` | `fixed point`

### **fcutoff** — 内部高通滤波器的截止频率 标量

内部高通滤波器的截止频率（以赫兹为单位），该滤波器用于滤除噪声。

Flux Observer 模块使用内部一阶 IIR 高通滤波器。在此端口指定一个频率，该频率应低于电机最低转速对应的最低频率。例如，您可以输入定子电压和电流最低电气频率的十分之一值。您可以调整在此端口指定的值，以确定能生成所需模块输出的更精确截止频率。

#### 依赖关系

要启用此端口，请将 **Relative path of compatible block that needs functional extension** 参数设置为指示当前模型中 Flux Observer 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **NumSlits** — 每相狭缝数 标量

正交编码器每相可用的狭缝数。

#### 依赖关系

要启用此端口，请将 **Relative path of compatible block that needs functional extension** 参数设置为指示当前模型中 Quadrature Decoder 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **CountsPerSlit** — 每个狭缝生成的计数数 标量

正交编码器为每个狭缝生成的计数数。一个计数表示一个狭缝位置。例如，如果您希望编码器生成对应于 00、10、11 和 01 狭缝位置或值的四个计数，请将此端口设置为 4（正交模式）。如果您选择正交模式：

每转编码器计数（正交后）= **Encoder counts per slit** ✖ **Encoder slits**

#### 依赖关系

要启用此端口，请将 **Relative path of compatible block that needs functional extension** 参数设置为指示当前模型中 Quadrature Decoder 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **ω1 (RPM)** — I-F 控制停止时的速度（电机启动后） 标量

I-F 控制器保持激活状态的速度（电机启动后，以 RPM 为单位）。当电机速度超过此值时，I-F 控制器变为非激活状态，**Status** 模块输出变为 true。

#### 依赖关系

要启用此端口，请将 **Relative path of compatible block that needs functional extension** 参数设置为指示当前模型中 I-F Controller 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **ω2 (RPM)** — 重新进入 I-F 控制所需的速度 标量

退出 I-F 控制（并进入闭环控制）后，重新激活 I-F 控制器所需的速度（以 RPM 为单位）。当电机速度降至该值以下时，I-F 控制器再次变为激活状态，**Status** 模块输出变为 false。

#### 依赖关系

要启用此端口，请将 **Relative path of compatible block that needs functional extension** 参数设置为指示当前模型中 I-F Controller 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **ωmax** — 支持的最大机械速度 标量

该模块可支持的最大机械速度（以 RPM 为单位）。如果您将速度设置为高于此值的值，模块将生成不正确的输出。

#### 依赖关系

要启用此端口，请将 **Relative path of compatible block that needs functional extension** 参数设置为指示当前模型中 Extended EMF Observer 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **Imax (A)** — I-F 控制期间的最大电机电流 标量

I-F 控制激活时提供给电机的最大电流（以安培为单位）。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 I-F Controller 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **Max(Δω/Δt) (RPM/s)** — I-F 控制期间的最大速度变化率 标量

I-F 控制激活时电机速度可以变化的最大速率（以 RPM/s 为单位）。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 I-F Controller 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **IDecayRate (A/s)** — I-F 控制期间的最大电流衰减率 标量

I-F 控制激活时电机电流可以衰减的最大速率（以安培/秒为单位）。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 I-F Controller 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **ζ** — 速度振荡阻尼系数值 标量

I-F Controller 模块应使用的速度振荡阻尼系数值。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 I-F Controller 模块的相对路径。I-F Controller 模块还必须配置为启用速度阻尼。

**数据类型：** `single` | `double` | `fixed point`

### **TIdle (s)** — 恒定速度和电流的时间 标量

I-F 控制激活时电机速度和电流均保持恒定的时间（以秒为单位）。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 I-F Controller 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **KEEMF** — 扩展 EMF 观测器增益 标量

线性扩展 EMF 状态观测器的增益。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Extended EMF Observer 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **fEEMFcutoff** — EEMF 滤波器截止频率 标量

模块用于去除估计反电动势值中噪声的低通滤波器的截止频率（以 Hz 为单位）。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Extended EMF Observer 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **fSpdcutoff** — 速度滤波器截止频率 标量

模块用于去除估计速度中噪声的低通滤波器的截止频率（以 Hz 为单位）。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 Extended EMF Observer 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **fcutoff** — 低通滤波器截止频率 标量

模块用于对估计角频率进行滤波的低通滤波器的截止频率（以 Hz 为单位）。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中 PLL with Feed Forward 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **KSpdp** — 速度观测器的比例增益 标量

速度观测器的比例增益。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中扩展 EMF 观测器模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **KSpdi** — 速度观测器的积分增益 标量

速度观测器的积分增益。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中扩展 EMF 观测器模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **Kp** — 比例控制器增益 标量

模块用于计算角频率的 PID 控制器的比例增益。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中带前馈的 PLL 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **Ki** — 控制器的积分增益 标量

模块用于计算角频率的 PID 控制器的积分增益。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中带前馈的 PLL 模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`

### **UseInternalKpKi** — 使用控制器内部增益 `0` | `1`

选择使用控制器的内部增益，而不是来自此模块输入端口的 Kp 和 Ki 增益。如果希望使用从带前馈的 PLL 模块计算得到的 Kp 和 Ki 值，请将此端口设置为接受 `1`。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中带前馈的 PLL 模块的相对路径。

**数据类型：** `Boolean`

### **fmax** — 最大适用输入频率 标量

输入信号的最大可能频率（单位：Hz）。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中扩展 EMF 观测器模块的相对路径。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **ParameterBus** — 兼容模块的计算参数 总线

磁通观测器、I-F 控制器、扩展 EMF 或带前馈的 PLL 模块的计算参数。

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中磁通观测器、I-F 控制器、扩展 EMF 或带前馈的 PLL 模块的相对路径。

**数据类型：** `single`

### **CountsPerRev** — 每转计数数 标量

正交编码器每转生成的计数数。

**CountsPerRev** = **编码器狭缝数** ⨯ **每狭缝编码器计数数**

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中正交解码器模块的相对路径。

**数据类型：** `single`

### **1/CountsPerRev** — 每转计数数的倒数 标量

模块在此端口输出正交编码器每转生成的计数数的倒数。

**1/CountsPerRev** = 1/(**编码器狭缝数** ⨯ **每狭缝编码器计数数**)

#### 依赖关系

要启用此端口，请将**需要功能扩展的兼容模块的相对路径**参数设置为指示当前模型中正交解码器模块的相对路径。

**数据类型：** `single`

## 参数

### **需要功能扩展的兼容模块的相对路径** — 兼容模块的相对路径 空白（默认）| 字符串

需要功能扩展的兼容模块相对于当前模型的相对路径。

### **获取模型中支持的模块路径列表** — 获取兼容模块路径列表 按钮

点击此按钮可获取当前模型中所有兼容模块的相对路径列表。该模块会在**支持的模块路径**部分显示此列表。

从列表中复制相关路径并粘贴到**需要功能扩展的兼容模块的相对路径**参数中，以配置此模块。

### **支持的模块路径** — 兼容模块路径列表 显示单元格

此部分显示当前模型中兼容模块的相对路径列表。

## 所属库

Motor Control Blockset / Signal Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

通过启用附加输入来扩展模块的功能

Compute Parameter 模块扩展当前模型中可用的兼容模块的功能。该模块根据兼容模块的设置进行自定义，并通过输出总线或多个输出信号提供兼容模块所需的参数。

您可以使用 Compute Parameter 模块参数对话框，通过提供兼容模块的相对路径来选择兼容模块。该对话框列出当前模型中所有可用兼容模块的相对路径，您可以将其复制到对话框中的**需要功能扩展的兼容模块的相对路径**字段中。

例如，当您将 Compute Parameter 模块配置为与 Flux Observer 模块连接时，Compute Parameter 模块以总线形式提供输出。然后，您可以将此总线连接到 Flux Observer 模块中可用的附加输入端口 **ParameterBus**。

对于其他兼容模块，您可以将 Compute Parameter 输出信号连接到兼容模块中相应的附加输入端口。

因此，该模块通过使兼容模块能够在运行时接受参数值，为其提供功能扩展。该模块支持以下兼容模块：

- Flux
  Observer
- Quadrature
  Decoder
- I-F
  Controller
- Extended EMF
  Observer
- PLL with Feed
  Forward

建议以低于兼容模块任务速率的速率运行此模块，以最大限度地减少硬件目标中的计算负载。
