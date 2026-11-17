---
type: simulink-block
title: 'Busbar (DC)'
family: 'connectors-references'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'busbardc'
documentation_source_path: 'ref/busbardc.html'
language: zh-CN
chinese_source: worker-translation
---

# Busbar (DC)

## 端口

### 输出

### **Vt** — 电压，V 物理信号

与标幺电压测量相关联的物理信号端口，单位为 Volts。

#### 依赖项

要启用此端口，请在 **Parameters** 设置中将 **Measurements ports** 参数设置为 `Yes`。

### **P** — 功率，W 物理信号

与功率测量相关联的物理信号端口，单位为 watts。

#### 依赖项

要启用此端口，请在 **Parameters** 设置中将 **Measurements ports** 参数设置为 `Yes`，并将 **Number of connections** 参数设置为 `2`、`3` 或 `4`。

### 守恒

### **1+** — 正极连接 1 electrical

与第一个正极连接相关联的 electrical 守恒端口。

### **2+** — 正极连接 2 electrical

与第二个正极连接相关联的 electrical 守恒端口。

#### 依赖项

要启用此端口，请在 **Parameters** 设置中将 **Number of connections** 参数设置为 `2`、`3` 或 `4`。

### **3+** — 正极连接 3 electrical

与第三个正极连接相关联的 electrical 守恒端口。

#### 依赖项

要启用此端口，请在 **Parameters** 设置中将 **Number of connections** 参数设置为 `3` 或 `4`。

### **4+** — 正极连接 4 electrical

与第四个正极连接相关联的 electrical 守恒端口。

#### 依赖项

要启用此端口，请在 **Parameters** 设置中将 **Number of connections** 参数设置为 `4`。

### **1-** — 负极连接 1 electrical

与第一个负极连接相关联的 electrical 守恒端口。

### **2-** — 负极连接 2 electrical

与第二个负极连接相关联的 electrical 守恒端口。

#### 依赖项

要启用此端口，请在 **Parameters** 设置中将 **Number of connections** 参数设置为 `2`、`3` 或 `4`。

### **3-** — 负极连接 3 electrical

与第三个负极连接相关联的 electrical 守恒端口。

#### 依赖项

要启用此端口，请在 **Parameters** 设置中将 **Number of connections** 参数设置为 `3` 或 `4`。

### **4-** — 负极连接 4 electrical

与第四个负极连接相关联的 electrical 守恒端口。

#### 依赖项

要启用此端口，请在 **Parameters** 设置中将 **Number of connections** 参数设置为 `4`。

## 参数

### **Number of connections** — 端口连接数 `2` (default) | `1` | `3` | `4`

要在模块上暴露的端口连接数。

### **Rated DC voltage** — 母线额定直流电压 `1e3` `V` (default) | 正标量

母线的额定直流电压。此模块使用该值对标幺电压值进行缩放。

### **Measurement type** — 测量类型 `Instantaneous` (default) | `Average over a specified period`

测量类型。在时间仿真模式下，您可以将此参数设置为 `Instantaneous` 或 `Average over a specified period`。在频率-时间仿真模式下，必须将此参数设置为 `Instantaneous`。

### **Averaging period** — 测量的平均周期 `1e-2` `s` (default) | 正标量

对电压和功率值求平均的周期。

#### 依赖项

要启用此参数，请将 **Measurement type** 设置为 `Average over a specified period`。

### **Measurement ports** — 测量端口暴露 `No` (default) | `Yes`

是否暴露 **Vt** 和 **P** 物理信号输出测量端口。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

潮流分析直流母线连接器

Busbar (DC) 模块是用于潮流分析的直流连接器。您可以将此模块与配置为在时间或频率-时间仿真模式下运行的 Simscape™ Electrical™ DC 网络一起使用。您可以通过启用仿真数据记录，或通过暴露模块上的可选测量端口来查看电压和功率值。有关数据记录的详细信息，请参阅 About Simscape Data Logging。
