---
type: simulink-block
title: 'Enable Profiler'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Profiling'
documentation_page: 'enableprofiler'
documentation_source_path: 'io_ref/enableprofiler.html'
language: zh-CN
chinese_source: official
---

# Enable Profiler

## 端口

### 输入

### **Start** — 启动探查器 `0` | `1`

当 `Start` 输入从 `0` 变为 `1` 时，该模块启动探查器。

在后台获取数据所需的资源就绪后，探查器开始收集数据。分析器准备工作可能跨越多个时间步长。

**数据类型:** `Boolean`

### **Stop** — 停止探查器 `0` | `1`

当 `Stop` 输入从 `0` 变为 `1` 时，该模块将停止探查器。

如果应用程序停止时探查器仍在运行，探查器将自动停止。您无需触发 `Stop` 输入。

收集的数据量限制为 `1`GB。当达到此限制时，探查器会自动停止。

**数据类型:** `Boolean`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink Real-Time / Profiling

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

在目标计算机上启动和停止执行探查器

Enable Profiler 模块检测到其 `Start` 输入端的上升沿时，将在 Speedgoat® 目标计算机上启动执行探查器。`Stop` 输入端的上升沿会停止执行探查器。两个端口上的上升沿均无影响。
