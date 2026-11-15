---
type: simulink-block
title: 'Digital Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'digitalread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/digitalread.html'
language: zh-CN
chinese_source: official
---

# Digital Read

## 端口

### 输出

### **Port\_1** — 输出信号 标量

该端口输出您在**引脚**参数中指定的板上数字引脚的逻辑状态。

## 参数

### **引脚** — 数字输入的引脚编号

指定数字引脚。

要打开引脚映射表，请点击**查看引脚映射**。

确保为模型中的不同模块分配不同引脚名称。

### **采样时间** — 模块读取输入引脚值的频率 `-1` (默认)

以秒为单位指定此模块读取引脚值的频率。

当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

读取数字输入引脚的逻辑状态

Digital Read 模块输出板上指定的数字引脚的逻辑状态。

在外部模式仿真期间，模块输出从在目标硬件上运行的可执行文件返回的仿真结果。

在所有其他模式下的仿真期间，模块输出零。
