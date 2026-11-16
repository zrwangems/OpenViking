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
chinese_source: official
---

# BLDC Average-Value Inverter

## 端口

### 输入

### **Dsw** — 与六个逆变器开关对应的占空比 `1`×`6` 数组

范围 [0, 1] 内的六个占空比，用于生成运行电机的三相电压。

**数据类型:** `single` | `double` | `fixed point`

### **Vdc** — 逆变器 DC 电压 标量

逆变器的 DC 总线电压输入。

**数据类型:** `single` | `double` | `fixed point` | `uint8` | `uint16` | `uint32`
### 输出

### **Vabc** — 三相电压输出 `1`×`3` 数组

对应于运行电机的输入占空比的三相梯形电压（伏特）。

**数据类型:** `single` | `double` | `fixed point`

## 参数

R2025b 官方文档未提供。

## 所属库

Motor Control Blockset / Electrical Systems / Inverters

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2023a 中推出**

## 描述

根据逆变器 DC 电压计算三相梯形 AC 电压

BLDC Average-Value Inverter 模块对平均值和全波逆变器进行建模。它通过使用与六个逆变器开关相对应的六个占空比，根据逆变器 DC 电压计算三相梯形电压输出。

### 方程

下列方程描述该模块如何计算三相 AC 电压。

Va=Vdc×(Da−Da')

Vb=Vdc×(Db−Db')

Vc=Vdc×(Dc−Dc')

其中：

- *Da*、*Db*、*Dc*、*Da'*、*Db'* 和 *Dc'* 是与逆变器的六个开关对应的占空比（范围在 0 和 1 之间）（如上图所示）。
- Va、Vb 和 Vc 是输出三相梯形电压（伏特）。
- *Vdc* 是逆变器的 DC 总线电压（伏特）。
