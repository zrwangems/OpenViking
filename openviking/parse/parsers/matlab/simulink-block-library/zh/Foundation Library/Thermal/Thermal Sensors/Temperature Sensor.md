---
type: simulink-block
title: 'Temperature Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sensors'
documentation_page: 'temperaturesensor'
documentation_source_path: 'ref/temperaturesensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Temperature Sensor

## 端口

### 输出

### **T** — 温度测量值，K 物理信号

用于温度测量的物理信号输出端口。
### 守恒

### **A** — 传感器入口热

热守恒端口。

### **B** — 传感器出口热

热守恒端口。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

#### 依赖关系

要启用此端口，请将 **Measurement reference** 参数设置为 `Difference`。

## 参数

### **Measurement reference** — 在绝对测量和相对测量之间选择 `Difference`（默认）| `Absolute`

在绝对测量和相对测量之间选择：

- `Difference` — 传感器测量模型中两个节点之间的温差。选择此选项会在模块图标上显示端口 **B**。
- `Absolute` — 传感器测量端口 **A** 处的绝对温度。传感器包含一个隐式参考节点，这意味着只需一个端口即可进行绝对测量。选择此选项会隐藏模块图标上的端口 **B**。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

### R2023a：传感器可用性增强

Temperature Sensor 模块现在包含一个隐式参考节点，这意味着只需一个端口即可进行温度的绝对测量。

此更改没有兼容性影响。

## 描述

理想温度传感器

Temperature Sensor 模块表示一个理想温度传感器，即一种测量节点处绝对温度或两个节点之间温差而不吸收任何热量的设备。

连接 **A** 和 **B** 是热守恒端口，连接到正在监测温度的两个点。端口 **T** 是输出温差值的物理信号端口。

模块正方向为从端口 **A** 到端口 **B**。测得的温度确定为 *T = TA – TB*。

要测量节点处的绝对温度，请将 **Measurement reference** 参数设置为 `Absolute`，并将端口 **A** 连接到正在测量的节点。
