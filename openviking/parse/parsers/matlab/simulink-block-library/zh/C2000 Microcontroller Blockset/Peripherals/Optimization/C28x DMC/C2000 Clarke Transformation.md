---
type: simulink-block
title: 'C2000 Clarke Transformation'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000clarketransformation'
documentation_source_path: 'ref/c2000clarketransformation.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Clarke Transformation

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

将平衡三相量转换为平衡两相正交量

# C2000 Clarke Transformation

将平衡三相量转换为平衡两相正交量

将现有 DMC 模块替换为 MCB 模块，以提高可用性和未来兼容性。建议使用 Control Algorithm Design (Motor Control Blockset) 中的模块。虽然这些模块并非一对一替代，但它们可帮助您实现相同的功能。

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

此模块将平衡三相量转换为平衡两相正交量。该变换实现以下方程

并在下图中说明。

此模块的输入是平衡三相量的 a 相 (`As`) 和 b 相 (`Bs`) 分量，输出是变换后信号的直轴 (`Alpha`) 分量和交轴 (`Beta`) 分量。

瞬时输出由以下方程定义，并在下图中显示：

上述方程和图中使用的变量与模块上的变量对应关系如下表所示：

|  | 方程变量 | 模块变量 |
| --- | --- | --- |
| 输入 | ia | As |
|  | ib | Bs |
| 输出 | id | Alpha |
|  | iq | Beta |

**注意**

- 要从此模块生成优化代码，请启用 `TI C28x` 或 `TI C28x (ISO)` CRL。
- 此模块的实现不会在代码生成期间调用对应的 Texas Instruments® 库函数。TI 函数使用全局 Q 设置，而此模块使用的 MathWorks® 代码会根据模块输入动态调整 Q 格式。有关更多信息，请参阅 Using the IQmath Library。

- C2000 Clarke Transformation 模块
