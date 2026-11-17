---
type: simulink-block
title: 'UAV Scenario Get Transform'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Scenario and Sensor Modeling'
documentation_page: 'uavscenariogettransform'
documentation_source_path: 'ref/uavscenariogettransform.html'
language: zh-CN
chinese_source: worker-translation
---

# UAV Scenario Get Transform

## 端口
```yaml
ports:
- name: transform
  summary: 变换矩阵 4×4 矩阵
  direction: output
```

### 输出

### **transform** — 变换矩阵 4×4 矩阵

输出变换，指定为 4×4 变换矩阵。
## 参数
```yaml
parameters:
- name: Source Frame
  summary: 源坐标系 'ENU'（默认）| 'NED' | 来自 UAV Scenario 的字符串
  group: ''
- name: Target Frame
  summary: 目标坐标系 'NED'（默认）| 'ENU' | 来自 UAV Scenario 的字符串
  group: ''
```

### **Source Frame** — 源坐标系 `'ENU'`（默认）| `'NED'` | 来自 UAV Scenario 的字符串

使用 **Select** 从模型中加载的 UAV Scenario 中选择全局坐标源坐标系。选择 North-East-Down（`'NED'`）或 East-North-Up（`'ENU'`）。

### **Target Frame** — 目标坐标系 `'NED'`（默认）| `'ENU'` | 来自 UAV Scenario 的字符串

使用 **Select** 从模型中加载的 UAV Scenario 中选择全局坐标源坐标系。选择 North-East-Down（`'NED'`）或 East-North-Up（`'ENU'`）。
## 所属库

UAV Toolbox / UAV Scenario and Sensor Modeling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

从 UAV 场景平台获取变换

此模块输出一个 4×4 变换矩阵，该矩阵将 UAV Scenario 中源坐标系中的点映射到目标坐标系。

要使用此模块，请确保模型中包含 UAV Scenario Configuration 模块。

此模块使用 UAV Scenario Configuration 模块中指定的采样时间。
