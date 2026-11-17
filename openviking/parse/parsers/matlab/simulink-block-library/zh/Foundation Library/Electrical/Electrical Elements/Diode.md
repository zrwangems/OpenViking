---
type: simulink-block
title: 'Diode'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'diode'
documentation_source_path: 'ref/diode.html'
language: zh-CN
chinese_source: worker-translation
---

# Diode

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与二极管正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与二极管负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Forward voltage
  summary: 正向偏置二极管的最小电压 0.6 V（默认）| 正标量
  group: ''
- name: On resistance
  summary: 正向偏置二极管的电阻 0.3 Ohm（默认）| 正标量
  group: ''
- name: Off conductance
  summary: 反向偏置二极管的电导 1e-8 1/Ohm（默认）| 正标量
  group: ''
```

### **Forward voltage** — 正向偏置二极管的最小电压 `0.6 V`（默认）| 正标量

使二极管变为正向偏置所需施加的最小电压。

### **On resistance** — 正向偏置二极管的电阻 `0.3 Ohm`（默认）| 正标量

正向偏置二极管的电阻。

### **Off conductance** — 反向偏置二极管的电导 `1e-8 1/Ohm`（默认）| 正标量

反向偏置二极管的电导。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2023b：减少正向电压附近的抖动

模块方程已得到增强，以减少二极管在正向电压附近工作时的零交叉。

在之前的版本中，二极管使用

```
if v > Vf
```

作为导通和关断状态之间的切换条件。从 R2023b 开始，切换条件已被修改为包含用于零交叉检测的电阻 *Rzc*：

```
if v + i*Rzc < Vf + Vf*Goff*Rzc
    % Off
      i == v*Goff;
    else
    % On
       v == i*Ron + Vf*(1-Ron*Goff);
```

新的切换条件在二极管工作于正向电压附近时提供了改进的导通到关断和关断到导通特性。

## 描述

电气系统中的分段线性二极管

Diode 模块对分段线性二极管进行建模。如果二极管两端的电压大于 **Forward voltage** 参数值，则二极管表现为具有低电阻的线性电阻，该电阻由 **On resistance** 参数值给出，外加一个恒定串联电压源。如果二极管两端的电压小于正向电压，则二极管表现为具有低电导的线性电阻，该电导由 **Off conductance** 参数值给出。

二极管电流图

当正向偏置时，二极管行为由以下方程描述：

v=i⋅Ron+Vsource,Vsource=Vf(1−RonGoff),

其中：

- *v* 是电压。
- *i* 是电流。
- *V*source 是串联电压源的电压。
- *V*f 是正向电压。
- *R*on 是正向偏置二极管的电阻。
- *G*off 是反向偏置二极管的电导。

反向行为由 *v = i/Goff* 给出。

*Ron.Goff* 项确保二极管在导通和关断状态之间切换时二极管电流没有不连续性。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
