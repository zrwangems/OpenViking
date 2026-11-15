---
type: simulink-block
title: 'C2000 Ramp Control'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Optimization / C28x DMC'
documentation_page: 'c2000rampcontrol'
documentation_source_path: 'ref/c2000rampcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# C2000 Ramp Control

## 端口

R2025b 中未记录。

## 参数

**Maximum delay rate**
:   乘以采样循环时间周期以确定每个斜坡步的时间延迟的值。有效值为大于 0 的整数。

**Minimum limit**
:   最小允许斜坡值。如果输入低于此值，它将被饱和到此最小值。您可输入的最小值是由模型中与此 Ramp Control 模块连接的输入和输出模块的定点数据格式可表示的最小值。如果输入低于此最小值，则在代码生成或仿真开始时会出错。例如，如果输入为 Q29 格式，其最小值为 -4。

**Maximum limit**
:   最大允许斜坡值。如果输入超过此值，它将被减小到此最大值。您可输入的最大值是由模型中与此 Ramp Control 模块连接的输入和输出模块的定点数据格式可表示的最大值。如果输入高于此最大值，则在代码生成或仿真开始时会出错。例如，如果输入为 Q29 格式，其最大值为 3.9999....。

**Maximum delay rate**
:   乘以采样循环时间周期以确定每个斜坡步的时间延迟的值。有效值为大于 0 的整数。

**Minimum limit**
:   最小允许斜坡值。如果输入低于此值，它将被饱和到此最小值。您可输入的最小值是由模型中与此 Ramp Control 模块连接的输入和输出模块的定点数据格式可表示的最小值。如果输入低于此最小值，则在代码生成或仿真开始时会出错。例如，如果输入为 Q29 格式，其最小值为 -4。

**Maximum limit**
:   最大允许斜坡值。如果输入超过此值，它将被减小到此最大值。您可输入的最大值是由模型中与此 Ramp Control 模块连接的输入和输出模块的定点数据格式可表示的最大值。如果输入高于此最大值，则在代码生成或仿真开始时会出错。例如，如果输入为 Q29 格式，其最大值为 3.9999....。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

创建斜坡上升和斜坡下降功能

# C2000 Ramp Control

创建斜坡上升和斜坡下降功能

将现有 DMC 模块替换为 MCB 模块，以提高可用性和未来兼容性。建议使用 Control Algorithm Design (Motor Control Blockset) 中的模块。虽然这些模块不是一一对应的替换，但它们使您能够实现相同的功能。

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

此模块实现斜坡上升和斜坡下降功能。输入是 `target` 值，输出是设定点值（`setpt`）和一个 `flag`。当输出 `setpt` 值达到输入 `target` 值时，`flag` 输出设置为 `7FFFFFFFh`。`target` 和 `setpt` 值是有符号 32 位定点数，Q 值在 16 和 29 之间。`flag` 是一个 long 型数字。

将 `target` 值与 `setpt` 值进行比较。如果它们不相等，则输出 `setpt` 会按固定步长（0.0000305）向上或向下调整。

如果固定步长相对于 `target` 值较大，则输出可能会围绕 `target` 值振荡。

- C2000 Ramp Control 模块
