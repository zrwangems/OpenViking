---
type: simulink-block
title: 'Timestamp'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Simulation / Target Profiling'
documentation_page: 'timestamp'
documentation_source_path: 'ref/timestamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Timestamp

## 端口

### 输入

### **Signals** — 用于捕获时间戳的信号 vector

实际数据值会被忽略。

### 输出

### **Timestamps** — 信号的时间戳 vector of double

对于连接到 `Signals` 的每个信号，该模块返回从模型执行开始起测量的信号时间戳。

## 参数

R2025b 中未记录。

## 所属库

Simulink Desktop Real-Time / Target Profiling

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

### R2024b：对具有端口名称的模块的更新

在 R2024b 中，当您启用可选端口（例如 **Show "Missed Ticks" port**）时，这些 Simulink® Desktop Real-Time™ 模块端口会带有标签显示。

## 描述

在 Run in Kernel 模式下输出信号时间戳

Timestamp 模块输出其输入信号的时间戳。该时间戳相对于 **Run in Kernel** 模式下的模型启动时间。输入信号可以是任意数据类型的任意信号。

在 **Connected IO** 模式下，此模块不执行任何操作。它输出零。
