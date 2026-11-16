---
type: simulink-block
title: 'SPICE Resistor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Passives'
documentation_page: 'spiceresistor'
documentation_source_path: 'ref/spiceresistor.html'
language: zh-CN
chinese_source: worker-translation
---

# SPICE Resistor

## 端口

### 守恒

### **+** — 正端子电气

与 SPICE 电阻器正电压端子关联的电气守恒端口。

### **-** — 负端子电气

与 SPICE 电阻器负电压端子关联的电气守恒端口。

## 参数

### 电阻

### **设备比例因子, SCALE** — 设备比例因子 `1.0`（默认）

模块表示的并联电阻数量。此值乘以输出电流。

### **电阻参数化** — 参数化选项 `Use specified resistance`（默认） | `Calculate from process information`

选择以下选项之一来指定电阻值：

- `Use specified resistance` — 直接提供电阻值。
- `Calculate from process information` — 提供模块用于计算电阻值的工艺参数。

  选择此选项时，模块使用以下方程计算电阻：

  R=RSH\*(LENGTH−NARROW)/(WIDTH−NARROW)

  其中：

  - *RSH* 是 **薄层电阻, RSH** 参数值。
  - *LENGTH* 是 **电阻长度, LENGTH** 参数值。
  - *WIDTH* 是 **电阻宽度, WIDTH** 参数值。
  - *NARROW* 是 **蚀刻收窄, NARROW** 参数值。

### **电阻, R** — 电阻 `0` `Ohm`（默认）

电阻值。

#### 依赖关系

仅当为 **电阻参数化** 参数选择 `Use specified resistance` 时，此参数才可见。

### **薄层电阻, RSH** — 每方块电阻 `0` `Ohm`（默认）

电阻器的每方块电阻。

#### 依赖关系

仅当为 **电阻参数化** 参数选择 `Calculate from process information` 时，此参数才可见。

### **电阻长度, LENGTH** — 电阻长度 `1e-6` `m`（默认）

电阻的长度尺寸。

#### 依赖关系

仅当为 **电阻参数化** 参数选择 `Calculate from process information` 时，此参数才可见。

### **电阻宽度, WIDTH** — 电阻宽度 `1e-6` `m`（默认）

电阻的宽度尺寸。

#### 依赖关系

仅当为 **电阻参数化** 参数选择 `Calculate from process information` 时，此参数才可见。

### **蚀刻收窄, NARROW** — 蚀刻收窄 `0` `m`（默认）

由于侧蚀，电阻长度和宽度减少的量。

#### 依赖关系

仅当为 **电阻参数化** 参数选择 `Calculate from process information` 时，此参数才可见。

### 温度

### **温度依赖性建模方式** — 温度依赖性参数化 `Device temperature`（默认） | `Fixed temperature`

选择以下选项之一来对电阻温度依赖性建模：

- `Device temperature` — 使用设备温度，即 **温度** 参数值（如果电路中存在 Environment Parameters 模块，则取该模块的值；否则取此模块的默认值）加上 **本地电路温度偏移, TOFFSET** 参数值。
- `Fixed temperature` — 使用独立于电路温度的温度来对温度依赖性建模。

### **一阶温度系数, TC1** — 一阶温度系数 `0` `1/K`（默认）

模块用于根据温度调整指定或计算出的电阻值的方程中线性项的系数。

### **二阶温度系数, TC2** — 二阶温度系数 `0` `1/K^2`（默认）

模块用于根据温度调整指定或计算出的电阻值的方程中二次项的系数。

### **本地电路温度偏移, TOFFSET** — 本地电路温度偏移 `0` `K`（默认）

电阻温度与电路温度相差的量。

#### 依赖关系

仅当为 **温度依赖性建模方式** 参数选择 `Device temperature` 时，此参数才可见。

### **固定电路温度, TFIXED** — 固定电路温度 `300.15` `K`（默认）

用于仿真电阻的温度。

#### 依赖关系

仅当为 **温度依赖性建模方式** 参数选择 `Fixed temperature` 时，此参数才可见。

### **参数提取温度, TMEAS** — 参数提取温度 `300.15` `K`（默认）

测量电阻参数时的温度。

## 所属库

Simscape / Electrical / Additional Components / SPICE Passives

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

对 SPICE 兼容电阻建模

SPICE Resistor 模块表示 SPICE 兼容电阻。可以通过以下方式之一指定电阻：

- 作为电阻值
- 作为模块用于计算电阻值的工艺信息

模块对温度依赖性建模。可通过两种方式指定电阻温度：

- 当为 **温度依赖性建模方式** 参数选择 `Device temperature` 时，电阻温度为

  T=TC+TO

  其中：

  - *TC* 是来自 Environment Parameters 模块的 **温度** 参数值。如果电路中不存在此模块，则 *TC* 为此参数的默认值。
  - *TO* 是 **本地电路温度偏移, TOFFSET** 参数值。
- 当为 **温度依赖性建模方式** 参数选择 `Fixed temperature` 时，电阻温度为 **固定电路温度, TFIXED** 参数值。

模块使用以下方程根据温度调整指定或计算出的电阻值：

*R* =
*R0*(1+*TC1*(*T*–*Tnom*)+*TC2*(*T*–*Tnom*)^2)

其中

- *R0* 是指定或计算出的电阻值。
- *TC1* 是 **一阶温度系数, TC1** 参数值。
- *TC2* 是 **二阶温度系数, TC2** 参数值。
- *Tnom* 是 **参数提取温度, TMEAS** 参数值。
