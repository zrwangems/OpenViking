---
type: simulink-block
title: 'Vapor Quality Sensor (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sensors'
documentation_page: 'vaporqualitysensor2p'
documentation_source_path: 'ref/vaporqualitysensor2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Vapor Quality Sensor (2P)

## 端口

### 输出

### **X** — 蒸汽干度，无量纲物理信号

用于测量两相流体中蒸汽分数的物理信号输出端口。使用 **Vapor fraction specification** 参数选择测量类型。
### 守恒

### **A** — 传感器入口两相流体

两相流体守恒端口。将此端口连接到两相流体网络中您想要测量蒸汽干度的节点。

## 参数

### **Vapor fraction specification** — 以质量基准还是体积基准表示蒸汽分数 `Vapor quality`（默认）| `Vapor void fraction`

在端口 **X** 处报告的测量类型。选择 `Vapor quality` 表示两相流体中蒸汽的质量分数。选择 `Vapor void fraction` 表示体积分数。两种情况下测量范围均为 `0` 到 `1`。对于临界和超临界流体，输出为 `-1`。

## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

测量两相流体中的蒸汽分数

Vapor Quality Sensor (2P) 模块测量两相流体中蒸汽的分数。该分数可以以质量基准（流体的蒸汽干度）或体积基准（蒸汽空隙率）表示。使用 **Vapor fraction specification** 模块参数指定基准。

该模块测量端口 **A** 处的蒸汽干度，并将其作为物理信号在端口 **X** 处报告。物理信号值范围从纯液体中的 `0` 到纯蒸汽中的 `1`。中间值对应于两相混合物。该传感器是理想的，即不发生质量或能量交换。

如果压力升至流体的临界点以上，蒸汽和液体不再存在，测量变得不确定。此时模块输出 `-1`，该值用于指示临界或超临界状态。
