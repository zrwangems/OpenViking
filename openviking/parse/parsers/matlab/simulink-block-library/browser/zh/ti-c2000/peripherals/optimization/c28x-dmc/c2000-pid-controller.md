---
type: simulink-block
title: 'C2000 PID Controller'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000pidcontroller'
documentation_source_path: 'ref/c2000pidcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 PID Controller

## 端口

R2025b 中未记录。

## 参数

**比例增益**
:   要应用于 PID 的比例增益（Kp）大小

**积分增益**
:   要应用于积分方程的增益（Ki）大小

**积分校正增益**
:   要应用于积分方程的校正增益（Kc）大小

**微分增益**
:   要应用于微分方程的增益（Kd）大小。

**最小输出**
:   PID 输出的最小允许值

**最大输出**
:   PID 输出的最大允许值

**比例增益**
:   要应用于 PID 的比例增益（Kp）大小

**积分增益**
:   要应用于积分方程的增益（Ki）大小

**积分校正增益**
:   要应用于积分方程的校正增益（Kc）大小

**微分增益**
:   要应用于微分方程的增益（Kd）大小。

**最小输出**
:   PID 输出的最小允许值

**最大输出**
:   PID 输出的最大允许值

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

数字 PID 控制器

# C2000 PID Controller

数字 PID 控制器

将现有 DMC 模块替换为 MCB 模块，以提高可用性并确保未来兼容性。建议使用 Control Algorithm Design (Motor Control Blockset) 中的模块。虽然这些模块并非一对一替代，但它们使您能够实现相同的功能。

| C28x DMC lib | MCB 中的 C28x DMC lib 等效项 |
| --- | --- |
| C2000 Clarke Transformation | Clarke Transform (Motor Control Blockset) |
| C2000 Inverse Park Transformation | Inverse Park Transform (Motor Control Blockset) |
| C2000 Park Transformation | Park Transform (Motor Control Blockset) |
| C2000 PID Controller | PI Controller (Motor Control Blockset) |
| C2000 Ramp Control | Position Generator (Motor Control Blockset) |
| C2000 Ramp Generator | Position Generator (Motor Control Blockset) |
| C2000 Space Vector Generator | PWM Reference Generator (Motor Control Blockset) |
| C2000 Speed Measurement | Speed Measurement (Motor Control Blockset) |

此模块实现一个带抗积分饱和校正的 32 位数字 PID 控制器。输入为参考输入（`ref`）和反馈输入（`fdb`），输出（`out`）为饱和后的 PID 输出。下图展示了一个带抗积分饱和的 PID 控制器。

此模块中实现的、描述饱和前 PID 控制器的微分方程为

|  |  |
| --- | --- |
| *upresat(t) = up(t) + ui(t) + ud(t)* | **(1)** |

其中 *upresat* 是饱和前的 PID 输出，*up* 是比例项，*ui* 是带饱和校正的积分项，*ud* 是微分项。

比例项为

|  |  |
| --- | --- |
| *up(t) = Kpe(t)* | **(2)** |

其中 *Kp* 是 PID 控制器的比例增益，*e(t)* 是参考输入与反馈输入之间的误差。

带饱和校正的积分项为

其中 *Kc* 是 PID 控制器的积分校正增益。

微分项为

其中 *Td* 是 PID 控制器的微分时间。在离散项中，微分增益定义为 *Kd = Td/T*，积分增益定义为 *Ki = T/Ti*，其中 *T* 是采样周期，*Ti* 是 PID 控制器的积分时间。

使用后向近似，前面的微分方程可转换为以下离散方程。

**注意**

- 要从此模块生成优化代码，请启用 `TI
  C28x` 或 `TI C28x (ISO)` 代码替换库。

  此模块的实现在代码生成期间不会调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关更多信息，请参阅 Using the IQmath Library。

此模块实现一个带抗积分饱和校正的 32 位数字 PID 控制器。输入为参考输入（`ref`）和反馈输入（`fdb`），输出（`out`）为饱和后的 PID 输出。下图展示了一个带抗积分饱和的 PID 控制器。

此模块中实现的、描述饱和前 PID 控制器的微分方程为

|  |  |
| --- | --- |
| *upresat(t) = up(t) + ui(t) + ud(t)* | **(3)** |

其中 *upresat* 是饱和前的 PID 输出，*up* 是比例项，*ui* 是带饱和校正的积分项，*ud* 是微分项。

比例项为

|  |  |
| --- | --- |
| *up(t) = Kpe(t)* | **(4)** |

其中 *Kp* 是 PID 控制器的比例增益，*e(t)* 是参考输入与反馈输入之间的误差

其中 *Kc* 是 PID 控制器的积分校正增益。

微分项为

其中 *Td* 是 PID 控制器的微分时间。在离散项中，微分增益定义为 *Kd = Td/T*，积分增益定义为 *Ki = T/Ti*，其中 *T* 是采样周期，*Ti* 是 PID 控制器的积分时间。

使用后向近似，前面的微分方程可转换为以下离散方程。

**注意**

- 要从此模块生成优化代码，请启用 `TI
  C28x` 或 `TI C28x (ISO)` 代码替换库。

  此模块的实现在代码生成期间不会调用相应的 Texas Instruments 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks 代码会根据模块输入动态调整 Q 格式。有关更多信息，请参阅 Using the IQmath Library。

- C2000 PID Controller 模块
