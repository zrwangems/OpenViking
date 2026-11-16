---
type: simulink-block
title: 'Counter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'counter'
documentation_source_path: 'ref/counter.html'
language: zh-CN
chinese_source: official
---

# Counter

## 端口

### 输出

### **T** — 计数器值 标量

计数器值。

**数据类型:** `single` | `double`

## 参数

### **计数器类型** — 计数器策略 **递增** (默认) | **递减** | **增减**

计数器类型。

### **输出范围** — 范围 **[0 1]** (默认) | **[-1 1]**

输出的范围。

### **计时器周期(秒)** — 周期 `0.001` (默认) | 正标量

计时器周期，以秒为单位。

### **相位延迟(秒)** — 延迟 `0` (默认) | `0` 或正标量

相位延迟，以秒为单位。添加相位延迟以更改计数器的初始状态。

### **采样时间** — 模块采样时间 `0.0001` (默认) | `0` 或正标量

连续两次模块执行之间的时间。在执行期间，模块产生输出，并在需要时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于离散时间仿真，请将采样时间设置为正标量。对于连续时间仿真，请将采样时间设置为 `0`。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2018b 中推出**

## 描述

离散时间或连续时间计数器

Counter 模块实现离散时间或连续时间的增量计数器。该计数器根据下列条件之一递增：

- 上升 - 输入上升时。
- 下降 - 输入下降时。
- 上升-下降 - 输入上升或下降时。
