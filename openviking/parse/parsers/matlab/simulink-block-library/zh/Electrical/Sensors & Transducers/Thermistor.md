---
type: simulink-block
title: 'Thermistor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'thermistor'
documentation_source_path: 'ref/thermistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermistor

## 端口
```yaml
ports:
- name: A
  summary: 热端口 thermal
  direction: conserving
- name: +
  summary: 正端口 electrical
  direction: conserving
- name: '-'
  summary: 负端口 electrical
  direction: conserving
```

### 守恒端口

### **A** — 热端口 thermal

热端口。

### **+** — 正端口 electrical

与热敏电阻正端口关联的电学守恒端口。

### **-** — 负端口 electrical

与热敏电阻负端口关联的电学守恒端口。
## 参数
```yaml
parameters:
- name: Nominal resistance R0 at reference temperature T0
  summary: 参考温度下的标称电阻 1000 Ohm（默认值）
  group: 电气
- name: Characteristic temperature constant B
  summary: 特征温度常数 3500 K（默认值）
  group: 电气
- name: Reference temperature T0
  summary: 参考温度 298.15 K（默认值）
  group: 电气
- name: Thermal time constant
  summary: 热时间常数 5.0 s（默认值）
  group: 热
- name: Dissipation factor
  summary: 耗散系数 0.75e-3 W/K（默认值）
  group: 热
```

### 电气

### **Nominal resistance R0 at reference temperature T0** — 参考温度下的标称电阻 `1000` `Ohm`（默认值）

热敏电阻在参考温度下的标称电阻。许多数据手册给出 25°C 时的标称电阻，并将其列为 R25。

### **Characteristic temperature constant B** — 特征温度常数 `3500` `K`（默认值）

描述电阻随温度变化的方程中的系数 *B*。

### **Reference temperature T0** — 参考温度 `298.15` `K`（默认值）

测量标称电阻时的温度。

### 热

### **Thermal time constant** — 热时间常数 `5.0` `s`（默认值）

当环境温度发生阶跃变化时，传感器温度达到最终温度变化量的 63% 所需的时间。

### **Dissipation factor** — 耗散系数 `0.75e-3` `W/K`（默认值）

使热敏电阻温度升高一 K 所需的热功率。
## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

使用 B 参数方程的负温度系数热敏电阻

Thermistor 模块使用 B 参数方程表示一个 NTC 热敏电阻。温度为 *T* 时的电阻为

R=R0eB(1/T−1/T0)

其中：

- *R0* 是参考温度 *T0* 下的标称电阻。
- *B* 是特征温度常数。

以下方程描述了模块的热行为：

Q=KdtcdTdt

其中：

- *Q* 是流入端口 A 的净热流。
- *K*d 是 **Dissipation factor** 参数值。
- *t*c 是 **Thermal time constant** 参数值。
- *dT/dt* 是温度变化率。

要在自由空间中建模热敏电阻：

1. 将热敏电阻连接到 Simscape™ Convective Heat Transfer 模块的 B 端口。
2. 将 Convective Heat Transfer 模块的 A 端口连接到 Simscape Ideal Temperature Source 模块，其温度设置为环境温度。
3. 将 Convective Heat Transfer 模块的 **Area** 参数设置为近似面积 *A*nom。
4. 将 Convective Heat Transfer 模块的 **Heat transfer coefficient** 参数设置为 *K*d/*A*nom。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
