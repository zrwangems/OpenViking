---
type: simulink-block
title: 'Single Point Interpolation'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Software Component Modeling / Component Development / AUTOSAR Calibration and Measurement Data'
documentation_page: 'singlepointinterpolation'
documentation_source_path: 'ref/singlepointinterpolation.html'
language: zh-CN
chinese_source: worker-translation
---

# Single Point Interpolation

## 端口

### 输入

### **u1** — 第一个输入信号 标量 | 向量

输入信号，指定为标量或向量。

**数据类型：** `single`

### **u2** — 第二个输入信号 标量 | 向量

输入信号，指定为标量或向量。

**数据类型：** `single`

### **f** — Fraction 值 标量

`Ifl_Interpolate_f32` 例程的系数。

#### 依赖关系

要启用此端口，请将 Fraction 参数的 Source 字段设置为
Input port。

**数据类型：** `single`
### 输出

### **y** — 输出信号 标量 | 向量

输出信号，以标量或向量形式返回。

**数据类型：** `single`

## 参数

### **Fraction** — Fraction 来源和值 `0`（默认） | 标量

`Ifl_Interpolate_f32` 例程系数的来源和值。

将此参数的 **Source** 字段指定为以下值之一。

- `Dialog` — 使用此参数的
  **Value** 字段设置系数。
- `Input port` — 使用
  `f` 端口设置系数。模块使用此端口的值作为
  系数。

#### 编程使用

|  |
| --- |
| **模块参数：** `FractionValue` |
| **类型：** character vector |
| **值：** `'0' |` scalar |
| **默认值：** `'0'` |

## 所属库

AUTOSAR Blockset / Classic Platform / Library Routines / Interpolation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a: AUTOSAR 代码替换库支持 Release 4.0 之后的 Schema

从 25a 开始，AUTOSAR 代码替换库支持 AUTOSAR 4.0 之后的 AUTOSAR schema 版本。
要使用最新的 AUTOSAR 例程，请在模型 Configuration Parameters
对话框的 **Code Generation** > **Interface** 窗格中，将 **Code replacement libraries** 指定为
`AUTOSAR 4.x`。

## 描述

执行单点插值

Single Point Interpolation 模块使用
AUTOSAR `Ifl_Interpolate_f32` 例程执行线性插值。Single Point
Interpolation 模块根据以下方程，使用输入
*u*1 和
*u*2 以及分数来源参数
*f* 执行插值： y=u1+f(u2−u1)

您可以使用 Block Parameters 对话框或 Input
port 指定分数来源。Single Point Interpolation 模块支持 software-in-the-loop (SIL)
模式。

当您为 AUTOSAR 模型选择 AUTOSAR 4.x 代码替换库 (CRL) 时，
您的模型会将为此模块生成的代码替换为对
`Ifl_Interpolate_f32` AUTOSAR 库例程的调用。
