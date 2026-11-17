---
type: simulink-block
title: 'Heat Flow Rate Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sensors'
documentation_page: 'heatflowratesensor'
documentation_source_path: 'ref/heatflowratesensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Flow Rate Sensor

## 端口
```yaml
ports:
- name: H
  summary: 热流率测量，W 物理信号
  direction: output
- name: A
  summary: 传感器入口热端口
  direction: output
- name: B
  summary: 传感器出口热端口
  direction: output
```

### 输出

### **H** — 热流率测量，W 物理信号

用于热流测量的物理信号输出端口。
### 守恒

### **A** — 传感器入口热端口

热守恒端口。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

### **B** — 传感器出口热端口

热守恒端口。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。
## 参数
```yaml
parameters: []
```

在 R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Thermal / Thermal Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

## 描述

理想热流计

Heat Flow Rate Sensor 模块表示理想热流计，即将通过该仪表的热流转换为与该热流成比例的控制信号的设备。

将此传感器与被测热流的模块串联连接，因为热流是（热域中的）通变量。并联连接传感器可能会影响仿真结果，因为它类似于在连接点之间添加旁路连接线。在现有线路中串联连接不会影响仿真结果，并能提供准确的测量。

连接 **A** 和 **B** 是热守恒端口。端口 **H** 是输出热流值的物理信号端口。

模块正方向为从端口 **A** 到端口 **B**。
