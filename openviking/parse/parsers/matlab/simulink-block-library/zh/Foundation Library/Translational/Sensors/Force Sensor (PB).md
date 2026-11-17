---
type: simulink-block
title: 'Force Sensor (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sensors'
documentation_page: 'forcesensorpb'
documentation_source_path: 'ref/forcesensorpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Force Sensor (PB)

## 端口
```yaml
ports:
- name: f
  summary: 力，N 物理信号
  direction: output
- name: B
  summary: 基座端口 基于位置的机械平移
  direction: output
- name: F
  summary: 从动端口 基于位置的机械平移
  direction: output
```

### 输出

### **f** — 力，N 物理信号

力的物理信号输出端口。
### 守恒

### **B** — 基座端口 基于位置的机械平移

基于位置的机械平移守恒端口，表示基座连接。

### **F** — 从动端口 基于位置的机械平移

基于位置的机械平移守恒端口，表示从动连接。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Translational / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于位置的机械平移系统中的力传感器

Force Sensor (PB) 模块测量基于位置的平移网络中的力。该传感器表示一个刚性测力传感器。传感器两端没有位置或速度变化。传感器的长度为 0 m。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。物理信号端口 **f** 输出沿从端口 **B** 到端口 **F** 方向施加的力。

将此传感器与被测力的模块串联连接，因为力是通变量（Through variable）。有关详细信息，请参阅通变量和跨变量。

Force Sensor (PB) 模块的正方向为从端口 **B** 到端口 **F**。当传感器正方向与网络正方向一致时：

- 正输出信号表示网络中测量点处于压缩状态。
- 负输出信号表示网络中测量点处于拉伸状态。

反之，如果传感器正方向与网络正方向相反，则正输出信号表示网络处于拉伸状态，负输出信号表示网络处于压缩状态。
