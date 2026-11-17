---
type: simulink-block
title: 'Controlled Reservoir (TL)'
family: 'thermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'controlledreservoirtl'
documentation_source_path: 'ref/controlledreservoirtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled Reservoir (TL)

## 端口

### 输入

### **T** — Temperature control signal, K physical signal

提供储液器温度控制信号的物理信号端口。

### 守恒

### **A** — Reservoir inlet thermal liquid

与储液器入口关联的热液体守恒端口。

## 参数

### **Reservoir pressure specification** — 储液器压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure`

储液器压力的指定方法：

- `Atmospheric pressure` — 使用由连接到回路的 Thermal Liquid Settings (TL) 或 Thermal Liquid Properties (TL) 模块指定的大气压力。
- `Specified pressure` — 使用 **Reservoir pressure** 参数指定一个值。

### **Reservoir pressure** — 储液器中的压力 `0.101325 MPa`（默认）

储液器中的所需压力。该压力在仿真期间保持恒定。

#### 依赖关系

当 **Reservoir pressure specification** 参数设置为 `Specified pressure` 时启用。

### **Cross-sectional area at port A** — 储液器入口处垂直于流动路径的面积 `0.01 m^2`（默认）

储液器入口管道的横截面积。该模块使用此面积确定进行热传导的管道特征长度。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

时变温度下的热液体储液器

Controlled Reservoir (TL) 模块表示处于固定压力和可变温度下的无限储液器。储液器及其入口可以处于大气压力或指定压力。端口 **A** 是热液体守恒端口，表示储液器入口。端口 **T** 是物理信号端口，提供储液器温度控制信号。

入口温度取决于液体流动方向。如果液体流入储液器，则入口温度等于上游液体的温度，储液器充当热沉。如果液体流出储液器，则入口温度等于储液器的温度，储液器充当热源。

为确保液体流动反向期间储液器入口处的温度平滑变化，该模块包含沿长度等于入口管道有效直径的热传导。该直径是入口管道指定横截面积的函数。
