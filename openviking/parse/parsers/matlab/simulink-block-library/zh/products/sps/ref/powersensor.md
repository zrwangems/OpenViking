---
type: simulink-block
title: 'Power Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Sensors'
documentation_page: 'powersensor'
documentation_source_path: 'ref/powersensor.html'
language: zh-CN
chinese_source: official
---

# Power Sensor

## 端口

### 输出

### **P** — 测得功率 物理信号

输出测得功率的物理信号端口
### 守恒

### **S** — 正电源轨 电气

连接到正电源轨的电气守恒端口

### **+** — 负载正端子 电气

连接到负载正端子的电气守恒端口

### **-** — 负载负端子 电气

连接到负载负端子的电气守恒端口

## 参数

### **测量类型** — 测量类型 **瞬时功率** (默认) | **瞬时功率**

选择是要测量**瞬时功率**还是**指定周期内的平均功率**。默认值为**瞬时功率**。

### **平均周期** — 平均周期 `1e-4` **秒** (默认)

测量平均功率的固定时间段。

#### 依赖关系

仅当为**测量类型**参数选择**指定周期内的平均功率**时，此参数才可见。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2012a 中推出**

## 描述

理想的瞬时或周期平均功率测量

Power Sensor 模块计算连接在 + 端子和 - 端子之间的负载所消耗的功率（假设只有负载连接到 + 端子）。请参阅模块图标了解内部电流和电压传感器的布置。

传感器可以返回瞬时功率，也可以返回固定时间段内的平均功率。对周期性电流和电压波形使用后一种选项，例如与 PWM 控制相关联的波形。

下图显示了如何连接模块来测量电阻中耗散的功率。

有关使用数据记录查看组件功率的替代工作流，请参阅降压转换器示例。
