---
type: simulink-block
title: 'Six Step Commutation'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'sixstepcommutation'
documentation_source_path: 'ref/sixstepcommutation.html'
language: zh-CN
chinese_source: worker-translation
---

# Six Step Commutation

## 端口

### 输入

### **Hall** — 霍尔传感器序列标量

霍尔传感器序列。如果霍尔传感器相隔 `120` 度放置，则序列号介于 `1` 到 `6` 之间。对于自定义霍尔传感器序列（当霍尔传感器相隔 `60` 度放置时），序列号介于 `0` 到 `7` 之间。

**注意**

如果向此端口提供无效的霍尔序列，模块会将输出端口 **Ctrl** 设置为零。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为 `Hall`。

**数据类型：** `single` | `double` | `fixed point`

### **Position** — 转子位置标量

由霍尔传感器或正交编码器传感器检测到的位置，单位为弧度（`0` 到 `2π`）、度（`0` 到 `360`）或标幺值（`0` 到 `1`）。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为 `Position`。

**数据类型：** `single` | `double` | `fixed point`

### **TorqueSign** — 旋转方向标量

转矩符号（`+1` 或 `-1`），指示 BLDC 电机的旋转方向。

当您将转矩符号从 `+1` 更改为 `-1` 时，模块使用的开关模式与 `+1` 转矩符号所使用的开关模式互补。类似地，当您将转矩符号从 `-1` 更改为 `+1` 时，模块使用的开关模式与 `-1` 转矩符号所使用的开关模式互补。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32`
### 输出

### **Ctrl** — 电机控制开关序列标量

用于在 BLDC 电机上实现六步换相（或梯形换相）的开关序列信号。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Input type** — 模块输入类型 `Hall`（默认）| `Position`

连接到模块输入的位置传感器反馈类型。

### **Position Unit** — 位置输入单位 `Per-unit`（默认）| `Degrees` | `Radians`

位置反馈输入的单位。

#### 依赖关系

要启用此参数，请将 **Input type** 设置为 `Position`。

### **Hall Sequence number** — 霍尔序列 `[5,4,6,2,3,1]`（默认）| 向量

自定义霍尔序列。

如果霍尔传感器相隔 120 度放置，则序列号介于 1 到 6 之间。如果霍尔传感器相隔 60 度放置，则序列号介于 0 到 7 之间。

#### 依赖关系

要启用此参数，请将 **Input type** 设置为 `Hall`。

### **Enable custom commutation** — 启用 **Commutation switching** 参数 `off`（默认）| `on`

选择此参数以使模块启用 **Commutation switching** 参数。

#### 依赖关系

要启用此参数，请将 **Input type** 设置为 `Hall`。

### **Commutation switching** — 换相开关序列 `[0 0 1 0 0 1;0 1 1 0 0 0;0 1 0 0 1 0;0 0 0 1 1 0;1 0 0 1 0 0;1 0 0 0 0 1]`（默认）| 向量

用于 BLDC 电机换相的自定义开关序列。

#### 依赖关系

要启用此参数，请将 **Input type** 设置为 `Hall` 并选择 **Enable custom commutation** 参数。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中引入**

## 描述

为无刷直流（BLDC）电机的六步换相生成开关序列

Six Step Commutation 模块使用 120 度导通模式生成开关序列，以在三相 BLDC 电机上实现六步换相（或梯形换相）。您可以使用这些开关信号来操作开关并控制定子电流，从而控制电机速度和旋转方向。

该模块接受霍尔序列号或转子位置（来自位置传感器，例如霍尔传感器或正交编码器传感器）以及转矩方向作为输入。它使用霍尔序列或位置输入来确定转子当前所在的扇区。该模块计算开关序列，使其激励相应的相以维持 90 度的转矩角（转子 d 轴与定子磁场之间的角度）（偏差为 30 度）。例如，如下图所示，对于霍尔状态 5，触发相 A 和相 C 以使电机旋转。

该图是一个示例，显示了定子磁场相量及其默认霍尔序列。建议您使用 Hall Sensor Sequence Calibration of BLDC Motor 来获取霍尔序列，并将此霍尔序列与该模块一起使用以实现六步换相。

该模块使用基于霍尔序列的换相逻辑来生成开关序列。

| Hall State (Hall a, Hall b, Hall c) | Switching Sequence (AA' BB' CC') | | |
| --- | --- | --- | --- |
| AA' | BB' | CC' |
| 4 (100) | 00 | 10 | 01 |
| 6 (110) | 01 | 10 | 00 |
| 2 (010) | 01 | 00 | 10 |
| 3 (011) | 00 | 01 | 10 |
| 1 (001) | 10 | 01 | 00 |
| 5 (101) | 10 | 00 | 01 |

该图显示了定子磁场相量以及可能的扇区（根据输入转子位置确定）。

该模块使用基于位置传感器信号的换相逻辑来生成开关序列。

| Position (θ) | Sector | Switching Sequence (AA' BB' CC') | | |
| --- | --- | --- | --- | --- |
| AA' | BB' | CC' |
| (-30°, 30°] | 1 | 00 | 10 | 01 |
| (30°, 90°] | 2 | 01 | 10 | 00 |
| (90°, 150°] | 3 | 01 | 00 | 10 |
| (150°, 210°] | 4 | 00 | 01 | 10 |
| (210°, 270°] | 5 | 10 | 01 | 00 |
| (270°, 330°] | 6 | 10 | 00 | 01 |
