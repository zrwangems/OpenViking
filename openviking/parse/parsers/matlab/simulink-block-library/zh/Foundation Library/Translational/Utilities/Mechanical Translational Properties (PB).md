---
type: simulink-block
title: 'Mechanical Translational Properties (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Utilities'
documentation_page: 'mechanicaltranslationalpropertiespb'
documentation_source_path: 'ref/mechanicaltranslationalpropertiespb.html'
language: zh-CN
chinese_source: worker-translation
---

# Mechanical Translational Properties (PB)

## 端口

### 守恒

### **R** — 将模块连接到电路的基于位置的机械平移的端口

基于位置的机械平移守恒端口，将模块连接到物理网络。

## 参数

### **向下重力加速度，g** — 作用于网络的重力加速度 `9.81 m/s^2`（默认）| 非负标量

作用于连接电路中所有模块的重力加速度。

### **正方向倾斜角，θ** — 导轨的倾斜角 `0 deg`（默认）| 标量

导轨正方向与正水平方向之间的夹角。

## 所属库

Simscape / Foundation Library / Translational / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

为电路指定重力加速度和导轨倾斜角

Mechanical Translational Properties (PB) 模块为所连接电路中的所有模块指定全局参数，例如重力加速度和倾斜角。在基于位置的平移网络中，模块具有与全局正方向对齐的固定方向。想象所有部件都组装在一根导轨上。

重力与倾斜角示意图

倾斜角 *θ* 是导轨正方向与水平方向之间的夹角。该角度从正水平方向逆时针测量。对于 0 到 180 度之间的角度，导轨正方向具有向上坡度；对于 0 到 -180 度之间的角度，具有向下坡度。

重力 *g* 向下作用。根据倾斜角，重力可以有两个分量：

- 平行分量，沿导轨作用，*g*·sin(*θ*)。这是引起运动的分量。正的 *g*·sin(*θ*) 对应于正的倾斜角，其引起沿导轨负方向的运动。
- 垂直分量，垂直于导轨作用，*g*·|cos(*θ*)|。这是引起质量块与导轨之间法向力并影响摩擦力的分量。

以下是一些导轨方向示例。

|  |  |  |
| --- | --- | --- |
| 竖直导轨 | *g* = 9.81 m/s^2  *θ* = 90 deg | 重力使质量块沿负方向加速  竖直导轨示意图 |
| 水平导轨 | *g* = 9.81 m/s^2  *θ* = 0 deg | 重量增加法向力  水平导轨示意图 |
