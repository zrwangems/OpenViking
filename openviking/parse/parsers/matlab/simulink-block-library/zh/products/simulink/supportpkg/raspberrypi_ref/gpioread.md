---
type: simulink-block
title: 'GPIO Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Basic'
documentation_page: 'gpioread'
documentation_source_path: 'supportpkg/raspberrypi_ref/gpioread.html'
language: zh-CN
chinese_source: worker-translation
---

# GPIO Read

## 端口

### 输出

### **Port\_1** — 包含逻辑值标量的输出端口

该模块输出数字引脚的逻辑值。

**数据类型：** `Boolean`

## 参数

### **Board** — Raspberry Pi 硬件板 `Pi 4 Model B`（默认）| `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 2 Model B` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Compute Module 4` | `Pi Zero 2 W` | `Pi 5 Model`

选择您的 Raspberry Pi 硬件板。您可以在目标硬件、产品包装或产品文档中找到此信息。

### **GPIO number** — Raspberry Pi 硬件板的 GPIO 引脚 `17`（默认）| `4` | `27` | `22` | `10` | `9` | `11` | `14` | `15` | `18` | `23` | `24` | `25` | `8` | `7` | `5` | `6` | `12` | `13` | `19` | `16` | `26` | `20` | `21`

选择 Raspberry Pi 硬件板的 GPIO 引脚以读取其逻辑状态。不要在 Simulink® 模型中的多个模块中使用同一个 GPIO 引脚。有关 Raspberry Pi GPIO 引脚的详细信息，请点击 **查看引脚映射**。

### **Sample time** — 读取 GPIO 引脚上逻辑状态的时间间隔 `0.1`（默认）| 标量

输入采样时间以读取 GPIO 引脚的逻辑值。较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。请输入大于零的值。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

读取 GPIO 引脚状态

使用 GPIO Read 模块读取 Raspberry Pi® 板的数字引脚的逻辑值。

**警告**

您可能通过以下方式损坏目标硬件：

- 超过可施加到 GPIO 引脚的最大电压。
- 将 GPIO 引脚短路到地。
- 将高电压的 GPIO 引脚与低电压的另一 GPIO 引脚短接。
- 将 GPIO 引脚连接到高于最大电压的电压源。
- 通过同时将多个 GPIO 引脚驱动为高电平来超过最大电流。
