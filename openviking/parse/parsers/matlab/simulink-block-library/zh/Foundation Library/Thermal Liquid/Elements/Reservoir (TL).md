---
type: simulink-block
title: 'Reservoir (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'reservoirtl'
documentation_source_path: 'ref/reservoirtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Reservoir (TL)

## 端口

### 守恒

### **A** — 储液器入口处的热液体

与储液器入口相关联的热液体守恒端口。

## 参数

### **储液器压力指定方式** — 储液器压力的指定方法 `Atmospheric pressure` (默认) | `Specified pressure`

储液器压力的指定方法：

- `Atmospheric pressure` — 使用连接到该回路的 Thermal Liquid Settings (TL)
  或 Thermal Liquid Properties (TL) 模块所指定的大气压力。
- `Specified pressure` — 使用 **储液器压力** 参数指定值。

### **储液器压力** — 储液器中的压力 `0.101325 MPa` (默认)

储液器中的期望压力。该压力在仿真过程中保持恒定。

#### 依赖关系

当 **储液器压力指定方式** 参数设置为 `Specified pressure` 时启用。

### **储液器温度** — 储液器中的温度 `293.15 K` (默认)

储液器中的期望温度。该温度在仿真过程中保持恒定。

### **端口 A 处的横截面积** — 储液器入口处垂直于流动路径的面积 `0.01 m^2` (默认)

储液器入口管道的横截面积。该模块使用此面积来确定管道在热传导方向上的特征长度。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

恒温恒压的热液体储液罐

Reservoir (TL) 模块表示一个压力和温度固定的无限储液罐。储液罐及其入口可以处于大气压力下，也可以处于指定压力下。端口 **A** 是一个热液体守恒端口，表示储液罐的入口。

入口温度取决于液体的流动方向。如果液体流入储液罐，则入口温度等于上游液体的温度，储液罐充当热沉。如果液体流出储液罐，则入口温度等于储液罐的温度，储液罐充当热源。

为确保液体流动换向期间储液罐入口处的温度平滑变化，该模块包含了沿一段长度的热传导，该长度等于入口管道的有效直径。该直径是指定的入口管道横截面积的函数。

### 假设和限制

- 储液罐的压力和温度恒定。
