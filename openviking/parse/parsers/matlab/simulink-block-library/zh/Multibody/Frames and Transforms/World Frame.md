---
type: simulink-block
title: 'World Frame'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Frames and Transforms'
documentation_page: 'worldframe'
documentation_source_path: 'ref/worldframe.html'
language: zh-CN
chinese_source: worker-translation
---

# World Frame

## 端口

### Frame

### **W** — 世界坐标系坐标系

由该模块表示的世界坐标系。连接到另一个坐标系以将该坐标系的位置和方向固定到世界坐标系。

## 参数

在 R2025b 中未记录。

## 所属库

Simscape / Multibody / Frames and Transforms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

惯性参考坐标系

该模块表示模型中的全局参考坐标系。该坐标系是惯性的，处于绝对静止状态。将坐标系刚性连接到世界坐标系可使该坐标系成为惯性坐标系。坐标系轴是正交的，并按照右手定则排列。

在坐标系网络中，世界坐标系是最终参考坐标系。直接或间接地，所有其他坐标系都相对于世界坐标系定义。如果多个 World Frame 模块连接到同一个坐标系网络，则这些模块标识的是同一个坐标系。如果没有 World Frame 模块连接到坐标系网络，则现有坐标系的副本（冻结在其初始位置和方向）将作为世界坐标系。
