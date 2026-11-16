---
type: simulink-block
title: 'Voltage-Controlled Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'voltagecontrolledcurrentsource'
documentation_source_path: 'ref/voltagecontrolledcurrentsource.html'
language: zh-CN
chinese_source: official
---

# Voltage-Controlled Current Source

## 端口

该模块有四个电气守恒端口。模块左侧的连接端 + 和 - 是控制端口。另外两个端口是提供输出电流的电气端子。箭头指示电流的正方向。

## 参数

**跨导 K**
:   跨导，即输出电流的变化除以引起该变化的输入电压的变化。默认值为 `1` 1/Ω。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

线性压控电流源

Voltage-Controlled Current Source 模块对一个线性压控电流源进行建模，用以下方程描述：

I=K·(V(+)−V(−))

其中

|  |  |
| --- | --- |
| *`I`* | 电流 |
| *`K`* | 跨导 |
| *`V(+)`*,*`V(-)`* | 在 + 和 - 控制端口处呈现的电压 |

要使用该模块，请将模块左侧的 + 和 - 端口（控制端口）连接到控制电压源。该模块右侧的两个端口（输出端口）产生输出电流。箭头指示电流的正方向。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
