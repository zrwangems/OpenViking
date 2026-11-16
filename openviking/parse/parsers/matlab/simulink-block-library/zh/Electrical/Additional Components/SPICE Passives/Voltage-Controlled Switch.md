---
type: simulink-block
title: 'Voltage-Controlled Switch'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Passives'
documentation_page: 'voltagecontrolledswitch'
documentation_source_path: 'ref/voltagecontrolledswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Voltage-Controlled Switch

## 端口

### 守恒

### **1+** — 正输入端口（电气）

与 Voltage-Controlled Switch 正输入关联的电气守恒端口。

### **1-** — 负输入端口（电气）

与 Voltage-Controlled Switch 负输入关联的电气守恒端口。

### **2+** — 正输出端口（电气）

与 Voltage-Controlled Switch 正输出关联的电气守恒端口。

### **2-** — 负输出端口（电气）

与 Voltage-Controlled Switch 负输出关联的电气守恒端口。

## 参数

### **开关模型** — 开关模型 `Abrupt transition after delay`（默认） | `Smooth transition between Ion and Ioff`

on 状态和 off 状态电流之间的过渡是否为瞬时。要将此模块建模为可变电阻开关，请选择 `Smooth transition between Ion and Ioff`。要将此模块建模为短过渡开关，请选择 `Abrupt transition after delay`。

### **阈值电压，VT** — 阈值电压 `0` `V`（默认）

高于此电压时，模块将控制电压解释为 HIGH。

**注意**

控制电压与阈值电压之差必须至少为 **迟滞电压，VH** 参数值，才能改变开关状态。

#### 依赖关系

要启用此参数，请将 **开关模型** 设置为 `Abrupt transition after delay`。

### **迟滞电压，VH** — 迟滞电压 `0` `V`（默认）

控制电压必须超过或低于 **阈值电压，VT** 参数值的量，以改变开关状态。

#### 依赖关系

要启用此参数，请将 **开关模型** 设置为 `Abrupt transition after delay`。

### **导通状态控制电压，VON** — 导通状态控制电压 `1e-3` `V`（默认）

导通状态下的开关控制电压。

#### 依赖关系

要启用此参数，请将 **开关模型** 设置为 `Smooth transition between Von and Voff`。

### **关断状态控制电压，IOFF** — 关断状态控制电压 `0` `V`（默认）

关断状态下的开关控制电压。

#### 依赖关系

要启用此参数，请将 **开关模型** 设置为 `Smooth transition between Von and Voff`。

### **导通电阻，RON** — 闭合开关电阻 `1` `Ohm`（默认）

开关闭合时的电阻。

### **使用 1/GMIN 作为关断电阻** — 是否使用 1/GMIN 作为关断电阻 `No`（默认） | `Yes`

是否自动将此开关的关断电阻计算为 `1/GMIN`。

**注意**

并联电导 *GMIN* 的值取决于您的模型是否包含 Environment Parameters 模块。

默认情况下，*GMIN* 与 Environment Parameters 模块的 **GMIN** 参数匹配，其默认值为 1e–12。要更改 *GMIN*，请将 Environment Parameters 模块添加到您的模型，并将 **GMIN** 参数设置为所需值。

#### 依赖关系

要启用此参数，请将 **开关模型** 设置为 `Abrupt transition after delay`。

### **关断电阻，ROFF** — 断开开关电阻 `1e12` `Ohm`（默认） | `1e6`

开关断开时的电阻。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **开关模型** 设置为 `Abrupt transition after delay`，并将 **使用 1/GMIN 作为关断电阻** 设置为 `No`。默认值为 `1e12`。
- 将 **开关模型** 设置为 `Smooth transition between Von and Voff`。默认值为 `1e6`。

### **时间延迟，TD** — 时间延迟 `0` `s`（默认）

开关转换发生的时间延迟。

#### 依赖关系

要启用此参数，请将 **开关模型** 设置为 `Abrupt transition after delay`。

## 所属库

Simscape / Electrical / Additional Components / SPICE Passives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

带迟滞的电压控制开关

Voltage-Controlled Switch 模块表示状态由输入端口两端电压（即 *控制电压*）控制的开关的电气特性。

此模块可建模可变电阻开关或短过渡开关。对于可变电阻开关，将 **开关模型** 参数设置为 `Smooth transition between Von and Voff`。对于短过渡开关，将 **开关模型** 设置为 `Abrupt transition after delay`。

### 短过渡开关

在短过渡开关中，off 状态和 on 状态之间的过渡是瞬时的：

- 当控制电压大于或等于 **阈值电压，VT** 和 **迟滞电压，VH** 参数值之和时，开关闭合，其电阻等于 **导通电阻，RON** 参数值。
- 当控制电压小于 **阈值电压，VT** 参数值减去 **迟滞电压，VH** 参数值的差时，开关断开，其电阻等于 **关断电阻，ROFF** 参数值。
- 当控制电压高于或低于 **阈值电压，VT** 参数值的量小于或等于 **迟滞电压，VH** 参数值时，电压处于 *交叉区域* 中，开关状态保持不变。

**注意**

如果 **迟滞电压，VH** 参数值小于 `0`，则无论 **开关模型** 参数设置为何值，该模块都会建模为可变电阻开关。

### 可变电阻开关

在可变电阻开关中，off 状态和 on 状态之间的过渡是指数式的：

- 当 **导通状态控制电压，VON** 大于 **关断状态控制电压，VOFF** 时：

  - 如果控制电压大于 **导通状态控制电压，VON** 参数值，则开关闭合，其电阻等于 **导通电阻，RON** 参数值。
  - 如果控制电压小于 **关断状态控制电压，VOFF** 参数值，则开关断开，其电阻等于 **关断电阻，ROFF** 参数值。
  - 如果控制电压大于 **关断状态控制电压，VOFF** 参数值或小于 **导通状态控制电压，VON** 参数值，则电阻由下式定义：

    Rs=exp[Lm+3Lr(Vc−Vm2Vd)−2Lr((Vc−Vm)3Vd3)]

    其中：

    - *Rs* 是开关电阻。
    - Lm=ln[(RON\*ROFF)12] 是电阻值的对数均值。
    - Lr=ln(RONROFF) 是电阻值的对数比。
    - *Vc* 是控制电压。
    - Vm=VON+VOFF2 是控制电压的均值。
    - Vd=VON−VOFF 是控制电压之差。
- 当 **导通状态控制电压，VON** 小于 **关断状态控制电压，VOFF** 时：

  - 如果控制电压小于 **导通状态控制电压，VON** 参数值，则开关闭合，其电阻等于 **导通电阻，RON** 参数值。
  - 如果控制电压大于 **关断状态控制电压，VOFF** 参数值，则开关断开，其电阻等于 **关断电阻，ROFF** 参数值。
  - 如果控制电压小于 **关断状态控制电压，VOFF** 参数值或大于 **导通状态控制电压，VON** 参数值，则电阻由下式定义：

    Rs=exp[Lm+3Lr(Ic−Im2Id)−2Lr((Ic−Im)3Id3)]
