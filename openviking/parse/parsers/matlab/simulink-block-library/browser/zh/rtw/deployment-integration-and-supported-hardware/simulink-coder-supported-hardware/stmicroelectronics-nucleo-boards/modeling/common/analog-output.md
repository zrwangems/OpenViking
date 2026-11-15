---
type: simulink-block
title: 'Analog Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'analogoutput'
documentation_source_path: 'nucleo/ref/analogoutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Output

## 端口

### 输入

### **Port\_1** — 模拟输出引脚的电压，标量

如果生成的电压等于接地电压，则该模块输出 `0`。如果生成的电压等于模拟参考电压，则该模块输出 `1`。

## 参数

### **Pin** — 模拟输出的引脚名称

指定数字引脚。

要打开引脚映射表，请点击 **View pin map**。

确保为模型的不同模块分配不同的引脚名称。

除了引脚映射表中提到的引脚名称之外，还有其他备用引脚名称 `(Px_y_ALTz)`，可用于访问连接到同一引脚的其他硬件外设。要了解更多信息，请参阅。

备用引脚名称仅适用于 Simulink® Coder™ Support Package for STMicroelectronics® Nucleo Boards 和 Discovery boards。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

在指定的模拟输出引脚上生成以伏特 (V) 为单位的电压

Analog Output 模块在硬件上的指定模拟输出引脚上生成以伏特 (V) 为单位的电压。该模块接受范围为 `0` – `1` 的归一化十进制值。
