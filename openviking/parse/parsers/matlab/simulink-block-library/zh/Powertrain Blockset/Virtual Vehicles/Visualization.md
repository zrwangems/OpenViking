---
type: simulink-block
title: 'Visualization'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'visualization'
documentation_source_path: 'ref/visualization.html'
language: zh-CN
chinese_source: worker-translation
---

# Visualization

## 端口

### 输入

### **Vis** — Visualization reference signals `Bus`

Bus containing the visualization reference signals, including longitudinal and
lateral displacement, and steering.

### **VehRef** — Vehicle reference signals `Bus`

Bus containing the vehicle reference signals, including longitudinal and lateral
displacement, and steering.

### **Fdbk** — Vehicle location feedback signals `Bus`

Bus containing vehicle displacement feedback signals.

### 输出

### **ExtVehFdbk** — Command signals `Bus`

Bus containing the commands, including steering, acceleration, braking, and gear
commands.

#### 依赖项

To create this port, select **Vehicle feedback**.

## 参数

### **Vehicle feedback** — Enable vehicle feedback outport `off` (default) | `on`

Specify to create a top-level model non-virtual bus port feedback outport,
`ExtVehFdbk`, with vehicle system signals. Consider selecting to make
signals available when the model is simulated with other systems.

## 所属库

Not documented in R2025b.

## 模块特性

Not documented in R2025b.

## 扩展功能

Not documented in R2025b.

## 版本历史

**Introduced in R2024b**

## 描述

Configure visualization

The Visualization subsystem contains
signal logging, scopes, and other visualization features. Selecting **Vehicle
feedback** creates a top-level model non-virtual bus port, making commonly used
vehicle system signals available when the model is simulated with other systems.
