---
type: simulink-block
title: 'PWM'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'pwm'
documentation_source_path: 'supportpkg/raspberrypi_ref/pwm.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM

## 端口

### 输入

### **In** — 确定方波脉冲宽度的输入值，是范围 [`0`, `1`] 内的正标量

模块输入继承上游模块的数据类型，并在内部将其转换为 double。发送到模块输入的值确定 Raspberry Pi® 硬件在指定 PWM 引脚上输出的方波宽度，称为*占空比*。模块输入接受从 `0` 到 `1` 的值范围（占空比的 0% 到 100%）。

例如：

- 最大输入值 `1` 将占空比设置为 100%，即全功率。
- 最小输入值 `0` 将占空比设置为 0%，即无功率。
- 中间输入值（例如 `0.333`）将占空比设置为 33.3%，即 1/3 功率。
- 超出范围的输入值（例如 `-0.2` 或 `1.2`）会输出最小或最大功率。

**数据类型：** `double`

## 参数

### **Board** — Raspberry Pi 硬件板 `Pi 4 Model B`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

选择您的 Raspberry Pi 硬件板。您可以在目标硬件、产品包装或产品文档上找到此信息。

### **Pin** — PWM 引脚编号 `21`（默认） | `4` | `17` | `27` | `22` | `10` | `9` | `11` | `14` | `15` | `18` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

选择 PWM 输入信号连接到的 Raspberry Pi 硬件板引脚编号。要打开 Raspberry Pi 板的引脚图，请点击 **查看引脚图**。

**注意**

不要将同一引脚编号分配给模型中的多个模块。

### **Frequency** — PWM 输出频率 `500`（默认） | `8000` | `4000` | `2000` | `1600` | `1000` | `800` | `400` | `320` | `250` | `200` | `160` | `100` | `80` | `50` | `40` | `20` | `10`

选择 PWM 信号的输出频率。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

生成数字输出引脚的脉宽调制信号

使用 PWM 模块改变数字输出引脚的功率输出。此模块使数字输出能够提供一系列不同的功率级别，类似于模拟输出。

在没有硬件的仿真期间，此模块不执行任何操作。请参阅“模块在仿真中产生零值或不执行任何操作”。
