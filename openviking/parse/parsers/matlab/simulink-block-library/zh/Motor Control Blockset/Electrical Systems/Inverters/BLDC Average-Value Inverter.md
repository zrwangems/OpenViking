---
type: simulink-block
title: 'BLDC Average-Value Inverter'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Electrical Systems / Inverters'
documentation_page: 'bldcaveragevalueinverter'
documentation_source_path: 'ref/bldcaveragevalueinverter.html'
language: zh-CN
chinese_source: worker-translation
---

# BLDC Average-Value Inverter

## 端口

### 输入

### **Dsw** — 对应六个逆变器开关的占空比 `1`-by-`6` 数组

用于生成驱动电机的三相电压的六个占空比，范围为 [0, 1]。

**数据类型：** `single` | `double` | `fixed point`

### **Vdc** — 逆变器直流电压 标量

输入到逆变器的直流母线电压。

**数据类型：** `single` | `double` | `fixed point` | `uint8` | `uint16` | `uint32`
### 输出

### **Vabc** — 三相电压输出 `1`-by-`3` 数组

与输入占空比相对应的三相梯形电压（伏特），用于驱动电机。

**数据类型：** `single` | `double` | `fixed point`

## 参数

R2025b 中未记录。

## 所属库

Motor Control Blockset / Electrical Systems / Inverters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2023a 中引入**

## 描述

根据逆变器直流电压计算三相梯形交流电压

BLDC Average-Value Inverter 模块对平均值和全波逆变器进行建模。它通过使用对应于六个逆变器开关的六个占空比，根据逆变器直流电压计算三相梯形电压输出。

### 方程

这些方程描述了该模块如何计算三相交流电压。

Va=Vdc×(Da−Da')

Vb=Vdc×(Db−Db')

Vc=Vdc×(Dc−Dc')

其中：

- *Da*、
  *Db*、
  *Dc*、
  *Da'*、
  *Db'* 和
  *Dc'* 是对应于逆变器六个开关（如图所示）的占空比（范围在 0
  到 1 之间）。
- Va、Vb 和 Vc 是输出的三相梯形电压（伏特）。
- *Vdc* 是逆变器的直流母线电压
  （伏特）。
