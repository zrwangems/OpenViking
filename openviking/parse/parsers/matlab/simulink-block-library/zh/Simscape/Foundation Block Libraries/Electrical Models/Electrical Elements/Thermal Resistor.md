---
type: simulink-block
title: 'Thermal Resistor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'thermalresistor'
documentation_source_path: 'ref/thermalresistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermal Resistor

## 端口

### 守恒

### **H** — 热端口 thermal

提供电阻温度的热守恒端口。

### **+** — 正极端子 electrical

与电阻正极端子关联的电气守恒端口。

### **-** — 负极端子 electrical

与电阻负极端子关联的电气守恒端口。

## 参数

### **标称电阻** — 参考温度下的电阻 `1 Ohm` (默认) | 正标量

热敏电阻在参考温度下的标称电阻。许多数据手册给出 25°C（298.15 K）下的标称电阻，并将其列为 R25。

### **参考温度** — 与标称电阻对应的温度 `298.15 K` (默认) | 正标量

测量标称电阻时的温度。

### **温度系数** — 电阻温度依赖系数 `5e-05 1/K` (默认) | 正标量

描述电阻随温度变化的方程中的系数 *α*。

### **热时间常数** — 热方程的时间常数 `10 s` (默认) | 正标量

当环境温度发生阶跃变化时，电阻温度达到最终温度变化的 63% 所需的时间。

### **耗散系数** — 热方程的耗散系数 `0.001 W/K` (默认) | 正标量

使热电阻温度升高 1 K 所需的热功率。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

带热端口的电阻

Thermal Resistor 模块表示一个温度相关电阻。当热端口处的温度为 *T* 时，电阻为

R=R0(1+α(T−T0))

其中：

- *R*0 是参考温度 *T*0 下的标称电阻。
- *α* 是温度系数。

以下方程描述该模块的热行为：

Q=KdtcdTdt−i2R

其中：

- *Q* 是流入端口 **H** 的净热流。
- *K*d 是 **耗散系数** 参数值。
- *t*c 是 **热时间常数** 参数值。
- *dT/dt* 是温度变化率。
- *i* 是流过电阻的电流。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。

特别是，**Temperature** 变量允许你为仿真开始时热电阻的温度设置高优先级目标。默认值为 `300` K。
