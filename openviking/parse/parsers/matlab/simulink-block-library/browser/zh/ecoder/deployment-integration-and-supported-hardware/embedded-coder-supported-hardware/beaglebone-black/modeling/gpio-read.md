---
type: simulink-block
title: 'GPIO Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'gpioread'
documentation_source_path: 'beaglebone/ref/gpioread.html'
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

### **GPIO 编号** — BeagleBone® 硬件板的 GPIO 引脚 `P9_11`（默认） | `P8_10` | `P8_11` | `P8_12` | `P8_13` | `P8_14` | `P8_15` | `P8_16` | `P8_17` | `P8_18` | `P8_19` | `P8_20` | `P8_21` | `P8_22` | `P8_23` | `P8_24` | `P8_25` | `P8_26` | `P8_27` | `P8_28` | `P8_29` | `P8_3` | `P8_30` | `P8_31` | `P8_32` | `P8_33` | `P8_34` | `P8_35` | `P8_36` | `P8_37` | `P8_38` | `P8_39` | `P8_4` | `P8_40` | `P8_41` | `P8_42` | `P8_43` | `P8_44` | `P8_45` | `P8_46` | `P8_5` | `P8_6` | `P8_7` | `P8_8` | `P8_9` | `P9_11` | `P9_12` | `P9_13` | `P9_14` | `P9_15` | `P9_16` | `P9_17` | `P9_18` | `P9_19` | `P9_20` | `P9_21` | `P9_22` | `P9_23` | `P9_24` | `P9_25` | `P9_26` | `P9_27` | `P9_28` | `P9_29` | `P9_30` | `P9_31` | `P9_41` | `P9_42`

选择 BeagleBone 硬件板的 GPIO 引脚以读取其逻辑状态。不要在 Simulink® 模型内的多个模块中使用同一个 GPIO 引脚。有关 BeagleBone GPIO 引脚的详细信息，请点击 **查看引脚映射**。

### **采样时间** — 读取 GPIO 引脚上逻辑状态的时间间隔 `0.1`（默认） | 标量

输入用于读取 GPIO 引脚逻辑值的采样时间。较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。输入大于零的值。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

读取配置为输入的 GPIO 引脚的逻辑值

使用此模块可以：

- 从 GPIO 引脚创建物理输入。
- 按由 **采样时间** 确定的时间间隔读取 GPIO 引脚的逻辑值。
- 将逻辑值作为 Boolean 值流发送到模型中的其他模块。
- GPIO 引脚的最大输入电压为 1.8 V。

**注意**

以下操作可能会损坏目标硬件：

- 将 GPIO 引脚短接到地。
- 将高电压的 GPIO 引脚与低电压的另一个 GPIO 引脚短接。
- 将 GPIO 引脚连接到高于最大电压的电压源。
- 同时将多个 GPIO 引脚驱动为高电平，从而超过最大电流。
