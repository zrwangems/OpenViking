---
type: simulink-block
title: 'Mach Number Sensor (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Sensors'
documentation_page: 'machnumbersensorg'
documentation_source_path: 'ref/machnumbersensorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Mach Number Sensor (G)

## 端口

### 输出

### **Mach** — 马赫数测量值，无量纲物理信号

用于马赫数测量的物理信号输出端口，无量纲。

### 守恒

### **A** — 传感器入口气体

与传感器入口关联的气体守恒端口。正流向为从端口 **A** 到端口 **B**。

### **B** — 传感器出口气体

与传感器出口关联的气体守恒端口。正流向为从端口 **A** 到端口 **B**。

## 参数

### **流路面积** — 流路面积 `0.01 m^2`（默认）| 正标量

流路的横截面积。

## 所属库

Simscape / Foundation Library / Gas / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

测量内部气体流动的马赫数

Mach Number Sensor (G) 模块表示一个理想传感器，用于测量气体流动的马赫数。马赫数表示流速与当地声速之比，并量化管路中气体的可压缩性效应。该模块按如下方式计算马赫数

M=m˙ρ⋅a⋅A,

其中：

- *ṁ* 是质量流量。
- *ρ* 是密度。
- *a* 是当地声速。
- *A* 是流路的横截面积，由 **流路面积** 参数指定。

这些值取决于 Gas Properties (G) 模块的设置。当流动方向从端口 **A** 到 **B** 时，该模块在端口 **Mach** 输出流动的马赫数。该模块将马赫数饱和在 1。使用该模块不会影响流动。
