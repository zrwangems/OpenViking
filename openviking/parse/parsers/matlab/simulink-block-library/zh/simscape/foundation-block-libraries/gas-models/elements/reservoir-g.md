---
type: simulink-block
title: 'Reservoir (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Gas Models / Elements'
documentation_page: 'reservoirg'
documentation_source_path: 'ref/reservoirg.html'
language: zh-CN
chinese_source: worker-translation
---

# Reservoir (G)

## 端口

### 守恒

### **A** — 储气库入口气体

与储气库入口关联的气体守恒端口。

## 参数

### **储气库压力指定** — 选择储气库压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure`

选择储气库压力的指定方法：

- `Atmospheric pressure` — 使用由连接到回路的 Gas Properties (G) 模块指定的
  大气压力。
- `Specified pressure` —
  使用 **储气库压力** 参数指定一个值。

### **储气库压力** — 储气库中的压力 `0.101325 MPa`（默认）

输入储气库中的所需压力。该压力在仿真期间保持恒定。

#### 依赖关系

当 **储气库压力指定** 参数设置为 `Specified pressure` 时启用。

### **储气库温度** — 储气库中的温度 `293.15 K`（默认）

输入储气库中的所需温度。该温度在仿真期间保持恒定。

### **端口 A 处的横截面积** — 储气库入口处垂直于流路的面积 `0.01 m^2`（默认）

储气库入口的横截面积，方向垂直于气体流路。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2016b 中引入**

## 描述

恒定压力和温度下气体网络的边界条件

Reservoir (G) 模块表示处于固定压力和温度下的无限储气库。储气库及其入口可处于大气压力或指定压力下。端口 **A** 是气体守恒端口，表示储气库入口。

假设储气库内部的气体体积为无限大。因此，流动假定为准稳态。

气体在储气库压力下进入和离开储气库，但其温度由气体流动方向决定。如果气体流入储气库，其温度由上游气体网络决定。储气库充当热沉。如果气体流出储气库，其温度等于储气库温度。储气库充当热源。

该模块还充当气体网络中压力和温度测量值的参考点。这些测量值分别相对于储气库压力和储气库温度。将储气库连接到 Pressure and Temperature Sensor (G) 模块的端口 **B**，以测量连接到该传感器 **A** 端口的节点的相对压力和温度。

### 假设和限制

- 储气库压力和温度恒定。
- 储气库中的气体为准稳态。
