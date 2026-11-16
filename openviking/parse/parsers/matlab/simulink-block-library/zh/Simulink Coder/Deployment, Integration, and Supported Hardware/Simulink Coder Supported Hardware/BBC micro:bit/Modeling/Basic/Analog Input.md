---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Basic'
documentation_page: 'analoginput'
documentation_source_path: 'microbit/ref/analoginput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Input

## 端口

### 输出

### **Port\_1** — 模拟输入引脚的电压 scalar

如果测量的电压等于地电压，则模块输出
`0`。如果测量的电压等于模拟参考电压，则模块输出 `1`。

## 参数

### **Pin** — 模拟输入的引脚名称

指定数字引脚。

要打开引脚映射表，请点击 **查看引脚映射**。

确保为模型的不同模块分配不同的引脚名称。

除了引脚映射表中提到的引脚名称外，还有其他备用引脚名称 `(Px_y_ALTz)`，这些名称可用于访问连接到同一引脚的其他硬件外设。

备用引脚名称仅适用于 Simulink® Coder™ Support Package for STMicroelectronics® Nucleo Boards and Discovery boards。

### **Sample time** — 模块读取输入引脚值的频率 -1（默认）

指定此模块测量模拟输入引脚电压的频率，以 seconds 为单位。

当您将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

测量模拟输入引脚的电压

Analog Input 模块测量模拟引脚相对于硬件上模拟输入参考电压的电压。该模块将测量结果输出为 0–1 范围内的 float 值。

- 如果测量的电压等于地电压，则模块输出
  `0`。
- 如果测量的电压等于模拟参考电压，则模块输出
  `1`。

在外部模式仿真期间，该模块输出由目标硬件上运行的可执行文件返回的仿真结果。

在所有其他模式下的仿真期间，该模块输出零。
