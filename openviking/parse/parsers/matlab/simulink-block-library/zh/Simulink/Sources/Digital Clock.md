---
type: simulink-block
title: 'Digital Clock'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'digitalclock'
documentation_source_path: 'slref/digitalclock.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Clock

## 端口
```yaml
ports:
- name: Port_1
  summary: 采样时间标量
  direction: output
  data_types: double
```

### 输出

### **Port\_1** — 采样时间标量

采样时间，以秒为单位，位于指定的采样间隔。在其他时间，该模块将输出保持在前一个值。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Sample time
  summary: 采样间隔 1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar | vector
  default: '''1'''
```

### **Sample time** — 采样间隔 `1`（默认）| 标量 | 向量

以秒为单位指定采样间隔。您可以通过以下两种方式之一指定采样间隔：

- 作为周期，指定为数据类型为 double 的实值标量。
- 作为周期和偏移量，指定为数据类型为 double 的长度为 2 的实值向量。周期和偏移量必须为有限且非负，并且偏移量的值必须小于周期。

有关详细信息，请参阅 Specifying Sample Time。

**提示**

不要指定连续采样时间，即 `0` 或 `[0,0]`。此外，避免指定 `-1`（继承采样时间），因为该模块是源模块。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'1'` |
## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。涉及嵌入式系统中常见的资源限制以及速度和内存方面的限制。生成的代码可能包含动态内存分配和释放、递归、额外的内存开销以及变化很大的执行时间。虽然该代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。通常，模块会逐渐演变为适合生产代码。因此，适合生产代码的模块仍然适合。

## 版本历史

**在 R2006a 之前推出**

## 描述

在指定的采样间隔输出仿真时间

Digital Clock 模块仅在指定的采样间隔输出仿真时间。在其他时间，该模块将输出保持在前一个值。要控制此模块的精度，请使用模块对话框中的 **Sample time** 参数。

当您需要在离散系统内获取当前仿真时间时，请使用此模块而不是 Clock 模块，后者输出连续时间。
