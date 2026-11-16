---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'analoginput'
documentation_source_path: 'nucleo/ref/analoginput.html'
language: zh-CN
chinese_source: official
---

# Analog Input

## 端口

### 输出

### **Port\_1** — 模拟输入引脚的电压 标量

如果测量的电压等于地电压，则模块发出 `0`。如果测量的电压等于模拟参考电压，则模块发出 `1`。

## 参数

### **引脚** — 模拟输入的引脚名称

指定数字引脚。

要打开引脚映射表，请点击**查看引脚映射**。

确保为模型中的不同模块分配不同引脚名称。

除了引脚映射表中提到的引脚名称外，还有其他备用引脚名称 `(Px_y_ALTz)` 可用于访问连接到同一引脚的其他硬件外设。

备用引脚名称仅适用于 Simulink® Coder™ Support Package for STMicroelectronics® Nucleo Boards and Discovery boards。

### **采样时间** — 模块读取输入引脚值的频率 -1 (默认)

指定此模块测量模拟输入引脚电压的频率，以秒为单位。

当您将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

测量模拟输入引脚的电压

Analog Input 模块测量模拟引脚的电压，该电压是相对于硬件上的模拟输入参考电压而言的。该模块将测量输出为范围 0-1 内的浮点值。

- 如果测量的电压等于地电压，则模块发出 `0`。
- 如果测量的电压等于模拟参考电压，则模块发出 `1`。

在外部模式仿真期间，模块输出从在目标硬件上运行的可执行文件返回的仿真结果。

在所有其他模式下的仿真期间，模块输出零。
