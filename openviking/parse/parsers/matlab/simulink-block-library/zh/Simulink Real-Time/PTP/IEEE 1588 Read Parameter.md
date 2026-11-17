---
type: simulink-block
title: 'IEEE 1588 Read Parameter'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'PTP'
documentation_page: 'ieee1588readparameter'
documentation_source_path: 'io_ref/ieee1588readparameter.html'
language: zh-CN
chinese_source: worker-translation
---

# IEEE 1588 Read Parameter

## 端口

### 输出

### **Output** — 由 Parameter to read 参数选择输出的参数 `double` | `[uint32]`

要读取的当前参数。

## 参数

### **Parameter to read** — 在输出端显示的参数 `System time (nanosecond)`（默认）| `Calendar time (time_t)` | `Offset from Client` | `Client to Server Delay` | `One Way Delay`

指定要读取的参数。选择以下之一：

| 参数 | 数据类型 | 描述 |
| --- | --- | --- |
| `System time (nanosecond)` | `uint64` | 当前 SLRT 系统时间的纳秒数，从当前纪元开始计数。 |
| `Calendar time (time_t)` | `int32` 向量 | 当前 SLRT 日历时间，以 `time_t` 表示。 |
| `Offset from Client` | `double` | 时间偏移量，以秒为单位。 |
| `Client to Server Delay` | `double` | 时间延迟，以秒为单位。 |
| `One Way Delay` | `double` | 时间延迟，以秒为单位。 |

**注意**

这些参数选项将在未来版本中移除，并在模型构建期间生成警告消息：`Offset from Client`、`Client to Server Delay` 和 `One Way Delay`。

`Calendar time (time_t)` 向量包含以下分量：

- 分钟后的秒数 — 0 到 61（C99 之前）和 0 到 60（C99 起）
- 小时后的分钟数 — 0 到 59
- 午夜后的小时数 — 0 到 23
- 月中的日期 — 1 到 31
- 自一月以来的月份 — 0 到 11
- 自 1900 年以来的年份
- 自星期日以来的天数 — 0 到 6
- 自 1 月 1 日以来的天数 — 0 到 365
- 夏令时标志。如果夏令时生效，该值为正；如果未生效，该值为零；如果无可用信息，该值为负

#### 编程使用

|  |
| --- |
| **模块参数**：`param` |

### **Sample time (-1 for inherited)** — 模块的采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。

#### 编程使用

|  |
| --- |
| **模块参数**：`sample_time` |

## 所属库

Simulink Real-Time / PTP

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

输出精确时间协议状态参数值，例如目标计算机系统时间、日历时间和延迟

IEEE 1588 Read Parameter 模块读取您选择的参数，并将其值发送到模块输出。模块标签会根据您选择的参数而变化。您可以使用 IEEE 1588 Read Parameter 模块读取 Speedgoat® 目标计算机系统时间，即使没有运行 PTP 进程。

**注意**

IEEE 1588 Read Parameter 模块输出系统时间，该时间每 1 ms 更新一次。此输出与模块的采样时间以及模块输出的纳秒精度无关。有关详细信息，请参阅 QNX® Neutrino® 文档中的 `clock_gettime()`。
