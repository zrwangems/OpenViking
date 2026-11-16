---
type: simulink-block
title: 'Voltage-Controlled Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'voltagecontrolledvoltagesource'
documentation_source_path: 'ref/voltagecontrolledvoltagesource.html'
language: zh-CN
chinese_source: official
---

# Voltage-Controlled Voltage Source

## 端口

该模块有四个电气守恒端口。模块左侧的连接端 + 和 - 是控制端口。另外两个端口是提供输出电压的电气端子。极性由 + 和 - 符号表示。

## 参数

**电压增益 K**
:   输出电压的变化除以引起该变化的控制电压的变化。默认值为 `1`。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

线性压控电压源

Voltage-Controlled Voltage Source 模块对一个线性压控电压源进行建模，用以下方程描述：

V=K·(V(+)−V(−))

其中

|  |  |
| --- | --- |
| *`V`* | 输出电压 |
| *`K`* | 电压增益 |
| *`V(+)`*,*`V(-)`* | 在 + 和 - 控制端口处呈现的电压 |

要使用该模块，请将模块左侧的 + 和 - 端口（控制端口）连接到控制电压源。该模块右侧的两个端口（输出端口）产生输出电压。极性由 + 和 - 符号表示。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
