---
type: simulink-block
title: 'Current Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sensors'
documentation_page: 'currentsensor'
documentation_source_path: 'ref/currentsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Sensor

## 端口
```yaml
ports:
- name: I
  summary: 电流，物理信号
  direction: output
- name: +
  summary: 正极端子电气
  direction: output
- name: '-'
  summary: 负极端子电气
  direction: output
```

### 输出

### **I** — 电流，物理信号

用于电流测量的物理信号输出端口。
### 守恒

### **+** — 正极端子电气

与传感器正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与传感器负极端子关联的电气守恒端口。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Sensors Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

电气系统中的电流传感器

Current Sensor 模块表示理想电流传感器，即将任何电气支路中测得的电流转换为与电流成比例的物理信号的设备。

使用 **+** 和 **-** 端口将传感器与要测量电流的支路中的其他模块串联连接。端口 **I** 将测量结果作为物理信号输出。使用 PS-Simulink Converter 模块将此端口连接到 Simulink® 模块，例如 Scope 或 Display。
