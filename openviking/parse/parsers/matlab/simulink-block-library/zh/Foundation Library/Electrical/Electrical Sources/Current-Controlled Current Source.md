---
type: simulink-block
title: 'Current-Controlled Current Source'
family: 'electrical'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'currentcontrolledcurrentsource'
documentation_source_path: 'ref/currentcontrolledcurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Current-Controlled Current Source

## 端口

该模块有四个电气守恒端口。模块左侧的 + 和 – 连接端为控制端口。另外两个端口是提供输出电流的电气端子。每对端口之间的箭头表示电流流动的正方向。

## 参数

**电流增益 K**
:   两个输出端子之间的电流与两个控制端子之间流过的电流之比。默认值为
    `1`。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**于 R2007a 中引入**

## 描述

线性电流控制电流源

Current-Controlled Current Source 模块对线性电流控制电流源进行建模，其方程如下：

I2=K·I1

其中

|  |  |
| --- | --- |
| *`I2`* | 输出电流 |
| *`K`* | 电流增益 |
| *`I1`* | 从 + 控制端口流向 – 控制端口的电流 |

要使用该模块，请将模块左侧的 + 和 – 端口（控制端口）连接到控制电流源。这些端口之间的箭头表示控制电流流动的正方向。模块右侧的两个端口（输出端口）生成输出电流，其间的箭头表示输出电流流动的正方向。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅“修改模块变量的标称值”。
