---
type: simulink-block
title: 'Thyristor 12-Pulse Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'thyristor12pulsegenerator'
documentation_source_path: 'ref/thyristor12pulsegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Thyristor 12-Pulse Generator

## 端口
```yaml
ports:
- name: theta
  summary: 同步角度，rad 标量
  direction: input
  data_types: single | double
- name: alpha
  summary: 触发角，rad 标量
  direction: input
  data_types: single | double
- name: Pdelta
  summary: Delta 脉冲向量 向量
  direction: output
  data_types: single | double
- name: Pwye
  summary: Wye 脉冲向量 向量
  direction: output
  data_types: single | double
```

### 输入

### **theta** — 同步角度，rad 标量

同步角度，范围为 `[0, 2*pi]`，单位为 rad。

**数据类型：** `single` | `double`

### **alpha** — 触发角，rad 标量

晶闸管触发角，单位为 rad。

**数据类型：** `single` | `double`
### 输出

### **Pdelta** — Delta 脉冲向量 向量

用于 delta 连接的晶闸管脉冲向量。

**数据类型：** `single` | `double`

### **Pwye** — Wye 脉冲向量 向量

用于 wye 连接的晶闸管脉冲向量。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Pulse ordering
  summary: 脉冲排序策略 Sequential device order（默认）| Natural order of commutation
  group: ''
- name: Delta connection
  summary: Delta 正弦相位偏差模型 Leading (Delta11)（默认）| Lagging (Delta1)
  group: ''
- name: Pulse width (rad)
  summary: 脉冲宽度 5*pi/6 rad（默认）| 范围为 [0, pi] 的正标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 1e-5（默认）| 正标量
  group: ''
```

### **Pulse ordering** — 脉冲排序策略 `Sequential device order`（默认）| `Natural order of commutation`

根据所控制的晶闸管网络配置指定脉冲排序规则。使用 `Sequential
device order` 策略为 Converter (Three-Phase)
模块生成脉冲。

### **Delta connection** — Delta 正弦相位偏差模型 `Leading (Delta11)`（默认）| `Lagging (Delta1)`

用于 delta 连接的正弦相位偏差模型。

### **Pulse width (rad)** — 脉冲宽度 `5*pi/6 rad`（默认）| 范围为 [0, pi] 的正标量

指定每个脉冲的宽度，范围为 `[0,
pi]`。

### **Sample time (-1 for inherited)** — 模块采样时间 `1e-5`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。
## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

以单脉冲模式生成晶闸管 12 脉冲波形

Thyristor 12-Pulse Generator 模块以单脉冲模式实现晶闸管 12 脉冲波形发生器。

您可以使用此模块通过以下方式执行相控 AC 到 DC 转换：

- 使用锁相环测量 AC 信号的同步角度
- 使用此模块生成的脉冲控制晶闸管换流器网络

### 模型

Thyristor 12-Pulse Generator 为 delta 门极驱动器输出六个脉冲，为 wye 门极驱动器输出六个脉冲。delta 连接可以超前（Delta11）或滞后（Delta1）。有关控制模型的信息，请参阅 Thyristor 6-Pulse
Generator 模块。
