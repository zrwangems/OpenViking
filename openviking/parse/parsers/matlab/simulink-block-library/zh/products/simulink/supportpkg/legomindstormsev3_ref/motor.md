---
type: simulink-block
title: 'Motor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'motor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/motor.html'
language: zh-CN
chinese_source: worker-translation
---

# Motor

## 端口

### 输入

### **Port\_1** — 到 EV3 电机的方向和功率整数 [`-100`, `100`]

此模块将这些值作为输入，这些值决定 EV3 电机的方向和功率。

- `1` 到 `100` — 在该范围内将值输入到模块，以使电机沿正向移动。
  `1` 表示最小功率，`100` 表示正向的最大功率。
- `-1` 到 `-100` — 在该范围内将值输入到模块，以使电机沿反向移动。
  `-1` 表示最小功率，`-100` 表示反向的最大功率。
- `0` — 无功率

**数据类型：** `int8`

## 参数

### **EV3 brick output port** — EV3 主机的输出端口号 `A`（默认） | `B` | `C` | `D`

选择电机所连接的 EV3 主机输出端口。如果您的 Simulink® 模型同时包含 Motor 和 Encoder 模块，请将两个模块中的 **EV3 brick output port** 参数设置为同一端口。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

控制 EV3 电机的功率和方向

使用 Motor 模块控制 EV3 电机的功率和方向。您可以将此模块与 Encoder 模块一起使用，以测量连接到 EV3 主机的电机的旋转。

此模块会转换其接收值的数据类型。您不需要转换输入信号的数据类型。

在没有硬件的仿真期间，此模块输出零。请参阅“模块在仿真中产生零或不执行任何操作”。
