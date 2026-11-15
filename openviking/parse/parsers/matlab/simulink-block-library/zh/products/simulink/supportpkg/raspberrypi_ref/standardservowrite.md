---
type: simulink-block
title: 'Standard Servo Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'standardservowrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/standardservowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Standard Servo Write

## 端口

### 输入

### **Data** — 输入值，用于确定标准旋转舵机的速度和方向，范围 [`0`, `255`] 中的正整数

在输入端口发送到模块的值确定与 Raspberry Pi 硬件板连接的标准旋转舵机的旋转速度和方向。例如：

- 输入值为 `0` 时，将轴定位在
  `0` 度。
- 输入值为 `180` 时，将轴定位在
  `180` 度。
- [`0`, `180`] 范围内的任何输入值，例如 `50`，将轴定位在
  `50` 度。
- [`0`, `180`] 范围之外的任何输入值，例如 `-2` 或 `188`，分别将轴定位在
  `0` 度和 `180` 度。

**数据类型：** `double`

## 参数

### **Board** — Raspberry Pi 硬件板 `Pi 4 Model B` (default) | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

选择您的 Raspberry Pi 硬件板。您可以在目标硬件、产品包装或产品文档上找到此信息。

### **Pin** — 标准舵机写入引脚编号 `18` (default) | `4` | `17` | `27` | `22` | `10` | `9` | `11` | `14` | `15` | `21` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

选择标准旋转舵机写入电机输入信号所连接的 Raspberry Pi 硬件板引脚编号。要打开 Raspberry Pi 板的引脚映射，请点击 **查看引脚映射**。

**注意**

不要将同一引脚编号分配给模型中的多个模块。

### **Minimum pulse duration** — 舵机信号的最小脉冲持续时间 `1000e-6` (default) | positive scalar

设置舵机信号的最小脉冲持续时间，单位为 seconds。

### **Maximum pulse duration** — 舵机信号的最大脉冲持续时间 `2000e-6` (default) | positive scalar

设置舵机信号的最大脉冲持续时间，单位为 seconds。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将标准舵机的轴位置设置为以度为单位指定的角度

使用 Standard Servo Write 模块控制连接到 Raspberry Pi® 硬件板上脉宽调制 (PWM) 输出引脚的舵机的轴角度。

在没有硬件的情况下进行仿真时，此模块不执行任何操作。请参阅“仿真中模块产生零或不执行任何操作”。
