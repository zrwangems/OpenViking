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
chinese_source: official
---

# IEEE 1588 Read Parameter

## 端口

### 输出

### **Output** — 通过参数选择输出以读取参数 `double` | `[uint32]`

当前要读取的参数。

## 参数

### **Parameter to read** — 输出时显示的参数 **System time (nanosecond)** (默认) | **Calendar time (time\_t)** | **Offset from Client** | **Client to Server Delay** | **One Way Delay**

指定要读取的参数。请选择以下选项之一：

| 参数 | 数据类型 | 描述 |
| --- | --- | --- |
| **System time (nanosecond)** | `uint64` | 当前 SLRT 系统时间的纳秒数，从当前纪元开始计数。 |
| **Calendar time (time\_t)** | `int32` 向量 | 当前 SLRT 日历时间为 `time_t`。 |
| **Offset from Client** | `double` | 时间偏移量（单位：秒）。 |
| **Client to Server Delay** | `double` | 时间延迟（单位：秒）。 |
| **One Way Delay** | `double` | 时间延迟（单位：秒）。 |

**注意**

这些参数选项将在未来版本中移除，并在模型构建期间生成警告消息：**Offset from Client**、**Client to Server Delay** 和 **One Way Delay**。

**Calendar time (time\_t)** 向量包含以下组件：

- 分钟后的秒数 - 0 到 61（C99 标准前）和 0 到 60（C99 标准后）
- 整点后的几分钟 - 0 到 59
- 午夜后的小时数 - 0 至 23
- 本月日期 - 1 至 31
- 自一月起算的月份 - 0 至 11
- 自 1900 年以来的年份
- 自上周日以来的天数 - 0 至 6
- 自 1 月 1 日起的天数 - 0 至 365
- 夏令时标记。该值为正表示夏令时生效，为零表示未生效，为负表示无可用信息。

#### 编程用法

|  |
| --- |
| **模块参数：**`param` |

### **Sample time (-1 for inherited)** — 模块采样时间 `-1` (默认) | 数值

输入基本采样时间或基本采样时间的倍数。

#### 编程用法

|  |
| --- |
| **模块参数：**`sample_time` |

## 所属库

Simulink Real-Time / PTP

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

输出精确时间协议状态参数值，例如目标计算机系统时间、日历时间和延迟。

IEEE 1588 Read Parameter 模块读取您选择的参数，并将该参数的值发送至模块输出端口。模块标签会根据您选择的参数进行变化。即使没有运行 PTP 进程，您也可以使用 IEEE 1588 Read Parameter 模块读取目标计算机系统的 Speedgoat® 时间。

**注意**

IEEE 1588 Read Parameter 模块输出系统时间，该时间每 1 毫秒更新一次。该输出与模块的采样时间以及模块输出的纳秒级精度无关。有关更多信息，请参阅 QNX® Neutrino® 文档中的  `clock_gettime()`。
