---
type: simulink-block
title: 'C2000 Inverse Park Transformation'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000inverseparktransformation'
documentation_source_path: 'ref/c2000inverseparktransformation.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Inverse Park Transformation

## 端口

R2025b 中未记录。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

将旋转参考坐标系向量转换为两相静止参考坐标系

# C2000 Inverse Park Transformation

将旋转参考坐标系向量转换为两相静止参考坐标系

将现有 DMC 模块替换为 MCB 模块，以提高可用性并确保未来兼容性。建议使用 Control Algorithm Design (Motor Control Blockset) 中的模块。尽管这些模块并非一对一替代，但它们可实现相同的功能。

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

此模块将正交旋转参考坐标系中的向量转换为两相正交静止参考坐标系。该变换实现以下方程：

并如下图所示。

此模块的输入是旋转坐标系中变换后信号的直轴 (`Ds`) 和交轴 (`Qs`) 分量，以及静止坐标系与旋转坐标系之间的相位角 (`Angle`)。

输出是变换后信号的直轴 (`Alpha`) 和交轴 (`Beta`) 分量。

上述图和方程中使用的变量对应下表中所示的模块变量：

|  | 方程变量 | 模块变量 |
| --- | --- | --- |
| 输入 | ID | Ds |
|  | IQ | Qs |
|  | θ | Angle |
| 输出 | id | Alpha |
|  | iq | Beta |

**注意**

- 要通过此模块生成优化代码，请启用 `TI C28x` 或 `TI C28x (ISO)` 代码替换库。
- 此模块的实现不会在代码生成期间调用相应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关详细信息，请参阅 Using the IQmath Library。

- C2000 Inverse Park Transformation 模块
