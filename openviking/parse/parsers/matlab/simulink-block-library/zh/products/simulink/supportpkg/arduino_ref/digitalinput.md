---
type: simulink-block
title: 'Digital Input'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'digitalinput'
documentation_source_path: 'supportpkg/arduino_ref/digitalinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Input

## 端口

### 输出

### **Port\_1** — Arduino 数字输入引脚上的输出信号电压 scalar

该模块输出你在 **Pin number** 参数中指定的 Arduino 板上数字引脚逻辑状态。

- 如果数字引脚的逻辑值为 LOW（0 `V`），则该
  模块输出发出 `0`。
- 如果数字引脚的逻辑值为 HIGH（5 `V` 或
  3.3 `V`，具体取决于板电压），则该模块输出
  发出 `1`。

**数据类型：** `Boolean`

## 参数

### **Pin number** — Arduino 引脚编号 `8` (default) | Arduino 板引脚编号

输入 Arduino 板数字输入引脚编号。要打开 Arduino 引脚映射
表，请点击 **View pin map**。有关如何为 Digital Input 模块分配
引脚的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

### **Pin mode** — Arduino 板数字引脚的模式 `Default` (default) | `Input Pullup`

设置 Arduino 板数字引脚的模式。

- `Default` — 选择此模式将 Arduino 板数字引脚设置为默认模式。此模式将引脚设为
  高阻抗状态。在此模式下，引脚可以检测施加到它的电压，
  为 HIGH 或 LOW。
- `Input Pullup` — 选择此模式将
  Arduino 板数字引脚设置为输入上拉模式，并激活内部
  上拉电阻。当未施加外部信号时，上拉电阻确保引脚默认读取为 HIGH 状态。

### **Sample time** — 模块读取输入引脚值的时间间隔 `0.1` (default) | scalar

指定此模块读取引脚值的频率，以秒为单位。输入一个大于零的值。

较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。当您将此参数指定为
`–1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

获取 Arduino 上数字输入引脚逻辑状态

使用 Digital Input 模块读取并输出 Arduino® 板上数字引脚的逻辑状态。

在外部模式仿真期间，该模块输出从目标硬件上运行的可执行文件返回的仿真结果。在所有其他模式的仿真期间，该模块输出零值。
