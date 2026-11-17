---
type: simulink-block
title: 'World Frame'
family: 'frames-and-transforms'
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

### **W** — World frame frame

由该模块表示的 World frame。连接到另一个坐标系，以将该坐标系的位置和方向固定到 World frame。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Multibody / Frames and Transforms

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2012a 中引入**

## 描述

惯性参考坐标系

该模块表示模型中的全局参考坐标系。该坐标系为惯性系，并处于绝对静止状态。将坐标系刚性连接到 World frame 会使该坐标系成为惯性系。坐标系的轴相互正交，并按照右手定则排列。

在坐标系网络中，World frame 是最终参考坐标系。所有其他坐标系都直接或间接地相对于 World frame 定义。如果多个 World Frame 模块连接到同一坐标系网络，则这些模块标识同一个坐标系。如果没有任何 World Frame 模块连接到某个坐标系网络，则现有坐标系的副本（冻结在其初始位置和方向）将充当 World frame。
