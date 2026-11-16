---
type: simulink-block
title: 'UAV Scenario Get Transform'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'Scenario Simulation / UAV Cuboid Scenario Simulation'
documentation_page: 'uavscenariogettransform'
documentation_source_path: 'ref/uavscenariogettransform.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Scenario Get Transform

## 端口

### 输出

### **transform** — 变换矩阵 4×4 矩阵

输出变换，指定为 4×4 变换矩阵。

## 参数

### **Source Frame** — 源坐标系 `'ENU'`（默认）| `'NED'` | 来自 UAV Scenario 的 string

使用 **Select** 从模型中加载的 UAV Scenario 中选择全局坐标源坐标系。选择北-东-下（`'NED'`）或东-北-上（`'ENU'`）。

### **Target Frame** — 目标坐标系 `'NED'`（默认）| `'ENU'` | 来自 UAV Scenario 的 string

使用 **Select** 从模型中加载的 UAV Scenario 中选择全局坐标目标坐标系。选择北-东-下（`'NED'`）或东-北-上（`'ENU'`）。

## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

## 描述

从 UAV Scenario 平台获取变换

此模块输出一个 4×4 变换矩阵，该矩阵将源坐标系中的点映射到 UAV Scenario 中的目标坐标系。

要使用此模块，请确保您的模型中有 UAV Scenario Configuration 模块。

此模块使用 UAV Scenario Configuration 模块中指定的采样时间。
