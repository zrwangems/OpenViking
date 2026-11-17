---
type: simulink-block
title: 'Current-Controlled Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'currentcontrolledvoltagesource'
documentation_source_path: 'ref/currentcontrolledvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Current-Controlled Voltage Source

## 端口

该模块有四个电气守恒端口。模块左侧的连接 + 和 – 是控制端口。箭头指示电流流动的正方向。另外两个端口是提供输出电压的电气端子。极性由 + 和 – 符号指示。

## 参数

**Transresistance K**
:   两个输出端子之间的电压与流过两个控制端子之间的电流之比。默认值为 `1` Ω。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

线性电流控制电压源

Current-Controlled Voltage Source 模块对线性电流控制电压源进行建模，用以下方程描述：

V=K·I1

其中

|  |  |
| --- | --- |
| *`V`* | 电压 |
| *`K`* | 互阻 |
| *`I1`* | 从 + 流向 – 控制端口的电流 |

要使用该模块，请将模块左侧的 + 和 – 端口（控制端口）连接到控制电流源。箭头指示电流流动的正方向。模块右侧的两个端口（输出端口）生成输出电压。极性由 + 和 – 符号指示。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
