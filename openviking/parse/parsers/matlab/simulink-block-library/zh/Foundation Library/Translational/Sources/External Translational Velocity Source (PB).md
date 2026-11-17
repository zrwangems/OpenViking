---
type: simulink-block
title: 'External Translational Velocity Source (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sources'
documentation_page: 'externaltranslationalvelocitysourcepb'
documentation_source_path: 'ref/externaltranslationalvelocitysourcepb.html'
language: zh-CN
chinese_source: worker-translation
---

# External Translational Velocity Source (PB)

## 端口
```yaml
ports:
- name: S
  summary: 控制信号，m/s 物理信号
  direction: input
- name: R
  summary: 向基于位置的机械平移网络施加外部速度的端口
  direction: input
```

### 输入

### **S** — 控制信号，m/s 物理信号

用于驱动源的控制信号的物理信号输入端口。此端口上的正信号在端口 **R** 处向网络施加正速度。
### 守恒

### **R** — 向基于位置的机械平移网络施加外部速度的端口

基于位置的机械平移守恒端口，将模块连接到电路并向物理网络施加外部速度。
## 参数
```yaml
parameters: []
```

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

理想机械能源，生成与输入信号成比例的速度

External Translational Velocity Source (PB) 模块表示一个理想的外部速度源，无论连接端口处的负载如何，它都会生成指定的速度。

端口 **R** 是一个基于位置的机械平移守恒端口。在物理信号端口 **S** 处指定速度。端口 **S** 处的正信号在端口 **R** 处向网络施加正速度。

该模块记录变量 `f`，它表示在端口 **R** 处为生成指定速度而施加的力。正力对应于正方向上的加速度。有关详细信息，请参阅数据记录。
