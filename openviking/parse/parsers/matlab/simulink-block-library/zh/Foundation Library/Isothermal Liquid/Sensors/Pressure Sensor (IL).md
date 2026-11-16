---
type: simulink-block
title: 'Pressure Sensor (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Sensors'
documentation_page: 'pressuresensoril'
documentation_source_path: 'ref/pressuresensoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Sensor (IL)

## 端口

### 输出

### **P** — 压力差测量，Pa 物理信号

压力差测量的物理信号输出端口。

#### 依赖关系

如果将 **Pressure Measurements** 参数设置为 `Pressure difference`，则此端口可见。

### **Pa** — 绝对压力测量，单位为 Pascal (Pa) 的物理信号

绝对压力测量的物理信号输出端口。

#### 依赖关系

如果将 **Pressure Measurements** 参数设置为 `Absolute pressure`，则此端口可见。

### **Pg** — 表压测量，Pa 物理信号

表压测量的物理信号输出端口。

#### 依赖关系

如果将 **Pressure Measurements** 参数设置为 `Gauge pressure`，则此端口可见。
### 守恒

### **A** — 传感器入口等温液体

等温液体守恒端口。

### **B** — 传感器出口等温液体

等温液体守恒端口。

#### 依赖关系

如果将 **Pressure Measurements** 参数设置为 `Pressure difference`，则此端口可见。

## 参数

### **Pressure Measurements** — 选择传感器测量压力差、绝对压力还是表压 `Pressure difference` (默认) | `Absolute pressure` | `Gauge pressure`

选择测量类型：

- `Pressure difference` — 传感器测量传感器两端的压力差。选择此选项会显示物理信号输出端口 **P** 和第二个等温液体端口 **B**。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。
- `Absolute pressure` — 传感器测量端口 **A** 处的绝对压力。选择此选项会显示物理信号输出端口 **Pa**。
- `Gauge pressure` — 传感器测量端口 **A** 处的表压。选择此选项会显示物理信号输出端口 **Pg**。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

测量压力差、绝对压力或表压

Pressure Sensor (IL) 模块表示一个理想传感器，用于测量等温液体网络中的压力。通过传感器的质量流量为零。

**Pressure Measurements** 参数控制测量类型和传感器配置：

- `Pressure difference` — 物理信号端口 **P** 报告传感器两端的压力差：

  P=pA−pB,

  其中 *p*A 和 *p*B 是传感器端口处的压力。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。
- `Absolute pressure` — 物理信号端口 **Pa** 报告端口 **A** 处的绝对压力：

  Pa=pA,

  其中 *p*A 是端口 **A** 处的压力，相对于绝对零压测量。在此配置中，传感器只有一个等温液体端口。
- `Gauge pressure` — 物理信号端口 **Pg** 报告端口 **A** 处的表压：

  Pg=pA−patm,

  其中 *p*A 是端口 **A** 处的压力，相对于绝对零压测量，*p*atm 是连接到电路的 Isothermal Liquid Properties (IL) 模块所指定的大气压。在此配置中，传感器只有一个等温液体端口。

模块图标会根据 **Pressure Measurements** 参数的值而变化。

| Pressure Measurements | 模块图标 |
| --- | --- |
| `Pressure difference` |  |
| `Absolute pressure` |  |
| `Gauge pressure` |  |
