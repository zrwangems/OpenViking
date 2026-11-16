---
type: simulink-block
title: 'Digital Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'digitalwrite'
documentation_source_path: 'nucleo/ref/digitalwrite.html'
language: zh-CN
chinese_source: official
---

# Digital Write

## 端口

### 输入

### **Port\_1** — 输入信号 标量

该模块将此值设置为您在**引脚**参数中指定的数字输出引脚。

## 参数

### **引脚** — 数字输出的引脚编号

指定数字引脚。

要打开引脚映射表，请点击**查看引脚映射**。

确保不要为模型中的多个模块指定相同的引脚名称。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018a 中推出**

## 描述

设置数字输出引脚的逻辑状态

Digital Write 模块设置板上指定数字引脚的逻辑状态。

在外部模式仿真期间，该模块将值设置为您在**引脚**参数中指定的引脚。

在其他所有模式的仿真期间，该模块不执行任何操作。
