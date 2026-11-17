---
type: simulink-block
title: 'External Force Source (PB)'
family: 'translational'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sources'
documentation_page: 'externalforcesourcepb'
documentation_source_path: 'ref/externalforcesourcepb.html'
language: zh-CN
chinese_source: worker-translation
---

# External Force Source (PB)

## 端口

### 输入

### **S** — 控制信号，N physical signal

用于驱动该源的控制信号的物理信号输入端口。此端口上的正信号会在端口 **R** 处向网络施加正力。
### 守恒

### **R** — 将外部力施加到网络的基于位置的机械平移端口

基于位置的机械平移守恒端口，用于将模块连接到回路，并将外部力施加到物理网络。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Translational / Sources

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

产生与输入信号成比例的力的理想机械能源

External Force Source (PB) 模块表示一个理想外部力源，该源无论连接端口处的负载或速度如何，都生成指定的力。

端口 **R** 是一个基于位置的机械平移守恒端口。在物理信号端口 **S** 处指定力。端口 **S** 处的正信号会在端口 **R** 处向网络施加正力。

例如，在此模型中，External Force Source (PB) 模块在两个弹簧之间施加 1 N 的正力。导轨的正方向为水平方向，从左到右。

已施加力的模型图

力从 External Force Source (PB) 模块向外流动。因此，负力流过左侧弹簧，正力流过右侧弹簧。左侧弹簧处于拉伸状态，右侧弹簧处于压缩状态。

该模块记录变量 `f`，其表示在端口 **R** 处施加到网络的力。有关详细信息，请参阅数据记录。
