---
type: simulink-block
title: 'Clock'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Flip Flops'
documentation_page: 'clock'
documentation_source_path: 'slref/clock.html'
language: zh-CN
chinese_source: worker-translation
---

# Clock

## 端口

### 输出

### **Port\_1** — 采样时间标量

采样时间，指定为每个仿真时间步的当前仿真时间。

**数据类型：** `double`

## 参数

### **Display time** — 在模块图标上显示仿真时间 `off`（默认）| `on`

选中此复选框可在 Clock 模块图标上显示仿真时间。清除此复选框时，仿真时间不会显示在模块图标上。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DisplayTime` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **Decimation** — 更新模块图标的间隔 `10`（默认）| 正整数

将 Simulink® 更新 Clock 图标的间隔指定为正整数。

假设抽取为 1000。对于 1 毫秒的固定积分步长，Clock 图标在 1 秒、2 秒等时刻更新。

#### 依赖关系

要在模块图标上显示仿真时间，必须选中 **Display time** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Decimation` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'10'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。涉及嵌入式系统中常见的资源限制以及速度和内存限制。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化较大的执行时间。虽然该代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。通常，模块会逐步演变为适合生产代码。因此，适合生产代码的模块仍然适合。

## 版本历史

**在 R2006a 之前引入**

## 描述

显示并提供仿真时间

Clock 模块在每个仿真步输出当前仿真时间。此模块对于需要仿真时间的其他模块很有用。

当您需要在离散系统内获取当前时间时，请使用 Digital Clock 模块。
