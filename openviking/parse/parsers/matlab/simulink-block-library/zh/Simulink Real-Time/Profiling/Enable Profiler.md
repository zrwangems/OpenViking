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
chinese_source: worker-translation
---

# Enable Profiler

## 端口
```yaml
ports:
- name: Start
  summary: 启动性能分析器 0 | 1
  direction: input
  data_types: Boolean
- name: Stop
  summary: 停止性能分析器 0 | 1
  direction: input
  data_types: Boolean
```

### 输入

### **Start** — 启动性能分析器 `0` | `1`

当 `Start` 输入从 `0` 变为 `1` 时，该模块启动性能分析器。

在后台收集数据所需的资源可用后，性能分析器开始收集数据。性能分析器的准备工作可能跨越多个时间步。

**数据类型：** `Boolean`

### **Stop** — 停止性能分析器 `0` | `1`

当 `Stop` 输入从 `0` 变为 `1` 时，该模块停止性能分析器。

如果应用程序停止时性能分析器仍在运行，性能分析器会自行停止。您不必触发 `Stop` 输入。

收集的数据量限制为 `1`GB。当达到此限制时，性能分析器会自行停止。

**数据类型：** `Boolean`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink Real-Time / Profiling

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

在目标计算机上启动和停止执行性能分析器

Enable Profiler 模块检测其 `Start` 输入上的上升沿，并在 Speedgoat® 目标计算机上启动执行性能分析器。`Stop` 输入上的上升沿会停止执行性能分析器。两个端口同时出现上升沿时没有任何效果。
