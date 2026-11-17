---
type: simulink-block
title: 'Reservoir (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'reservoirg'
documentation_source_path: 'ref/reservoirg.html'
language: zh-CN
chinese_source: worker-translation
---

# Reservoir (G)

## 端口

### 守恒端口

### **A** — 储气库入口气体

与储气库入口关联的气体守恒端口。

## 参数

### **Reservoir pressure specification** — 选择储气库压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure`

选择储气库压力的指定方法：

- `Atmospheric pressure` — 使用与回路连接的气体属性（G）模块所指定的大气压。
- `Specified pressure` — 使用 **Reservoir pressure** 参数指定一个值。

### **Reservoir pressure** — 储气库中的压力 `0.101325 MPa`（默认）

输入储气库中的所需压力。该压力在仿真期间保持恒定。

#### 依赖关系

当 **Reservoir pressure specification** 参数设置为 `Specified pressure` 时启用。

### **Reservoir temperature** — 储气库中的温度 `293.15 K`（默认）

输入储气库中的所需温度。该温度在仿真期间保持恒定。

### **Cross-sectional area at port A** — 储气库入口处垂直于流动路径的面积 `0.01 m^2`（默认）

储气库入口处沿垂直于气体流动路径方向的横截面积。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体网络在恒定压力和温度下的边界条件

Reservoir (G) 模块表示一个处于固定压力和温度下的无限储气库。储气库及其入口可以处于大气压或指定压力下。端口 **A** 为气体守恒端口，表示储气库入口。

储气库内部的气体体积假定为无限大。因此，流动假定为准稳态。

气体以储气库压力进入和离开储气库，但其温度由气体流动方向决定。如果气体流入储气库，其温度由上游气体网络决定。储气库充当散热器。如果气体流出储气库，其温度等于储气库温度。储气库充当热源。

该模块还用作气体网络中压力和温度测量的参考点。这些测量值分别相对于储气库压力和温度。将储气库连接到 Pressure and Temperature Sensor (G) 模块的端口 **B**，以测量连接到传感器 **A** 端口的节点的相对压力和温度。

### 假设和限制

- 储气库压力和温度恒定。
- 储气库中的气体为准稳态。
