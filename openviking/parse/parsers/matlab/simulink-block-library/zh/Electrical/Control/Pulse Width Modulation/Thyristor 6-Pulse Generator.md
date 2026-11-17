---
type: simulink-block
title: 'Thyristor 6-Pulse Generator'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'thyristor6pulsegenerator'
documentation_source_path: 'ref/thyristor6pulsegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Thyristor 6-Pulse Generator

## 端口

### 输入

### **theta** — 同步角，radians 标量

同步角，范围为 `[0, 2*pi]`，以 radians 为单位。

**数据类型：** `single` | `double`

### **alpha** — 触发角，radians 标量

晶闸管触发角，以 radians 为单位。

**数据类型：** `single` | `double`
### 输出

### **P** — 脉冲向量 vector

晶闸管脉冲向量。

**数据类型：** `single` | `double`

## 参数

### **Pulse ordering** — 脉冲排序策略 `Sequential device order`（默认） | `Natural order of commutation`

根据您所控制的晶闸管网络的配置，指定脉冲排序规则。使用 `Sequential device order` 策略为 Converter 模块生成脉冲。

### **Pulse width (rad)** — 脉冲宽度 `5*pi/6 rad`（默认） | [0, pi] 范围内的正标量

指定每个脉冲的宽度，范围为 `[0, pi]`。

### **Sample time (-1 for inherited)** — 模块采样时间 `1e-5`（默认） | 正标量

连续模块执行之间的时间，以 s 为单位。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，则通过将此参数设置为 `-1` 来继承采样时间。如果此模块位于连续可变步长模型中，则使用正标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

以单脉冲模式生成晶闸管 6 脉冲波形

Thyristor 6-Pulse Generator 模块实现单脉冲模式下的晶闸管 6 脉冲波形生成器。

您可以使用此模块通过以下方式执行相控 AC-to-DC 转换：

- 使用锁相环测量 AC 信号的同步角
- 使用此模块生成的脉冲控制晶闸管换流器网络

### 模型

该图显示了 Thyristor 6-Pulse Generator 的等效电路。

基于同步角 *theta* 和触发角 *alpha*，模块内部生成六个斜坡，输出向量中的每个脉冲元素对应一个斜坡。

当相关斜坡沿上升方向达到或越过指定的触发角时，模块在某一输出处生成脉冲。该图显示了其中一个输出的这种脉冲生成机制。

设置脉冲排序策略以修改每个斜坡的不同相移，从而修改生成脉冲的顺序：

- 将 `Pulse ordering` 属性设置为 `Sequential device order`，以按顺序生成脉冲。使用此策略为 Converter (Three-Phase) 模块或其他使用顺序排序的晶闸管网络生成脉冲。
- 将 `Pulse ordering` 属性设置为 `Natural order of commutation`，以按自然顺序生成脉冲。使用此策略为使用自然排序的晶闸管网络生成脉冲。
