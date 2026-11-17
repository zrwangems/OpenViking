---
type: simulink-block
title: 'Thermal Resistor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'thermalresistor'
documentation_source_path: 'ref/thermalresistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermal Resistor

## 端口

### 守恒端口

### **H** — 热端口 thermal

提供电阻温度的热守恒端口。

### **+** — 正极端子 electrical

与电阻正极端子关联的电守恒端口。

### **-** — 负极端子 electrical

与电阻负极端子关联的电守恒端口。

## 参数

### **Nominal resistance** — 参考温度下的电阻 `1 Ohm`（默认）| 正标量

热敏电阻在参考温度下的标称电阻。许多数据手册给出 25°C（298.15 K）时的标称电阻，并将其列为 R25。

### **Reference temperature** — 对应于标称电阻的温度 `298.15 K`（默认）| 正标量

测量标称电阻时的温度。

### **Temperature coefficient** — 电阻温度依赖系数 `5e-05 1/K`（默认）| 正标量

描述电阻随温度变化的方程中的系数 *α*。

### **Thermal time constant** — 热方程的时间常数 `10 s`（默认）| 正标量

当环境温度发生阶跃变化时，电阻温度达到最终温度变化量的 63% 所需的时间。

### **Dissipation factor** — 热方程的耗散系数 `0.001 W/K`（默认）| 正标量

使热敏电阻温度升高一 K 所需的热功率。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

带热端口的电阻

Thermal Resistor 模块表示一个温度相关电阻。当热端口处的温度为 *T* 时，电阻为

R=R0(1+α(T−T0))

其中：

- *R*0 是参考温度 *T*0 下的标称电阻。
- *α* 是温度系数。

以下方程描述了模块的热行为：

Q=KdtcdTdt−i2R

其中：

- *Q* 是流入端口 **H** 的净热流。
- *K*d 是 **Dissipation factor** 参数值。
- *t*c 是 **Thermal time constant** 参数值。
- *dT/dt* 是温度变化率。
- *i* 是通过电阻的电流。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

特别是，**Temperature** 变量允许您为仿真开始时热敏电阻的温度设置高优先级目标。默认值为 `300` K。
