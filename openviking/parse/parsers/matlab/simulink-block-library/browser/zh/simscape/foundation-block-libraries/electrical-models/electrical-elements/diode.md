---
type: simulink-block
title: 'Diode'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'diode'
documentation_source_path: 'ref/diode.html'
language: zh-CN
chinese_source: official
---

# Diode

## 端口

### 守恒

### **+** — 正极端子 电气

与二极管正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

与二极管负极端子关联的电气守恒端口。

## 参数

### **正向电压** — 正向偏置二极管的最小电压 `0.6 V` (默认) | 正标量

使二极管正向偏置所需施加的最小电压。

### **导通电阻** — 正向偏置二极管的电阻 `0.3 Ohm` (默认) | 正标量

正向偏置二极管的电阻。

### **关断电导** — 反向偏置二极管的电导 `1e-8 1/Ohm` (默认) | 正标量

反向偏置二极管的电导。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

### R2023b: 减少正向电压附近的震颤

模块方程已经过增强，以减少二极管在正向电压附近工作时的过零点数。

在先前版本中，二极管使用

```
if v > Vf
```

作为开启和关闭状态之间的切换条件。从 R2023b 开始，切换条件修改为包括一个用于过零检测的电阻 *Rzc*：

```
if v + i*Rzc < Vf + Vf*Goff*Rzc
    % Off
      i == v*Goff;
    else
    % On
       v == i*Ron + Vf*(1-Ron*Goff);
```

当二极管在正向电压附近工作时，新的切换条件可提供改进的“开启到关闭”和“关闭到开启”特性。

## 描述

电气系统中的分段线性二极管

Diode 模块对分段线性二极管进行建模。如果二极管两端的电压大于**正向电压**参数值，则二极管的行为类似于具有低电阻（由**导通电阻**参数值给出）加上恒定串联电压源的线性电阻器。如果二极管两端的电压小于正向电压，则二极管的行为类似于具有低电导（由**关断电导**参数值给出）的线性电阻器。

Diode current plot

正向偏置时，二极管行为用以下方程描述：

v=i⋅Ron+Vsource,Vsource=Vf(1−RonGoff),

其中：

- *v* 是电压。
- *i* 是电流。
- *V*source 是串联电压源的电压。
- *V*f 是正向电压。
- *R*on 是正向偏置二极管的电阻。
- *G*off 是反向偏置二极管的电导。

反向行为根据 *v = i/Goff* 得出。

*Ron.Goff* 项确保二极管在开启和关闭状态之间切换时，二极管电流不会存在不连续性。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
