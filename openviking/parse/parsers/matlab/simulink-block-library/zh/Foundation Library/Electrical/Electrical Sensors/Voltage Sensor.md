---
type: simulink-block
title: 'Voltage Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sensors'
documentation_page: 'voltagesensor'
documentation_source_path: 'ref/voltagesensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Voltage Sensor

## 端口
```yaml
ports:
- name: V
  summary: 电压，V 物理信号
  direction: output
- name: +
  summary: 正极端子 电气
  direction: output
- name: '-'
  summary: 负极端子 电气
  direction: output
```

### 输出

### **V** — 电压，V 物理信号

用于电压测量的物理信号输出端口。
### 守恒

### **+** — 正极端子 电气

与传感器正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

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

电气系统中的电压传感器

Voltage Sensor 模块表示理想电压传感器，即一种将电气电路两点之间测得的电压转换为与该电压成比例的物理信号的设备。

使用 **+** 和 **-** 端口将传感器与要测量电压的模块（或若干模块）并联连接。端口 **V** 将测量结果作为物理信号输出。使用 PS-Simulink Converter 模块将此端口连接到 Simulink® 模块，例如 Scope 或 Display。
