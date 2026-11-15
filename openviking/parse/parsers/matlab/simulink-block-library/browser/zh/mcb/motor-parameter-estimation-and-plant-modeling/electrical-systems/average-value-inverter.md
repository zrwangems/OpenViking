---
type: simulink-block
title: 'Average Value Inverter'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'averagevalueinverter'
documentation_source_path: 'ref/averagevalueinverter.html'
language: zh-CN
chinese_source: official
---

# Average Value Inverter

## 端口

### 输入

### **Dabc** — 三相电压的占空比 `1`×`3` 数组

范围 [0,1] 内的三相调制索引，用于生成运行电机的电压。

**数据类型:** `single` | `double` | `fixed point`

### **Vdc** — 逆变器 DC 电压 标量

逆变器的 DC 总线电压输入。

**数据类型:** `single` | `double` | `fixed point` | `uint8` | `uint16` | `uint32`
### 输出

### **Vabc** — 三相电压输出 `1`×`3` 数组

对应于运行电机的输入占空比的三相电压（伏特）。

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

**在 R2020a 中推出**

## 描述

根据逆变器 DC 电压计算三相 AC 电压

Average-Value Inverter 模块对平均值和全波逆变器进行建模。它通过使用占空比信息根据逆变器 DC 电压计算三相 AC 电压输出。

### 方程

下列方程描述该模块如何计算三相 AC 电压。

D0=(Da+Db+Dc)3

Va=Vdc×(Da−D0)

Vb=Vdc×(Db−D0)

Vc=Vdc×(Dc−D0)

其中：

- Da、Db 和 Dc 是范围在 0 到 1 之间的调制索引。
- Vdc 是逆变器的 DC 总线电压（伏特）。
- Va、Vb 和 Vc 是输出三相电压（伏特）。
