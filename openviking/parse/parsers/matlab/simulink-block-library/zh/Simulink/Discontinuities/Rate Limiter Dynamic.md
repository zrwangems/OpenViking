---
type: simulink-block
title: 'Rate Limiter Dynamic'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'ratelimiterdynamic'
documentation_source_path: 'slref/ratelimiterdynamic.html'
language: zh-CN
chinese_source: worker-translation
---

# Rate Limiter Dynamic

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: lo
  summary: 输入递减时的导数限值 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: up
  summary: 输入递增时的导数限值 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Y
  summary: 输出信号 标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | enumerated
    | bus
```

### 输入

### **u** — 输入信号 标量

速率限幅算法的输入信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **lo** — 输入递减时的导数限值 标量

提供输入信号下降速率限值的动态值。使 `lo` 的信号数据类型与输入信号 `u` 的数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **up** — 输入递增时的导数限值 标量

提供输入信号上升速率限值的动态值。使 `up` 的信号数据类型与输入信号 `u` 的数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Y** — 输出信号 标量

速率限幅算法的输出信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

代码生成器不会在生成的代码中显式地将构成非原子掩码子系统模块的基元模块分组。这种灵活性允许更高效的代码生成。在某些情况下，您可以通过选择 **Treat as atomic unit** 选项将掩码子系统模块配置为作为原子单元执行来实现分组。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

限制信号的变化率

Rate Limiter Dynamic 模块限制信号的上升和下降速率。

- 外部信号 `up` 设置信号上升速率的上限。
- 外部信号 `lo` 设置信号下降速率的下限。

使用 Rate Limiter Dynamic 模块时，请遵循以下准则：

- 确保 `up` 和 `lo` 的数据类型与输入信号 `u` 的数据类型相同。

  当下限使用有符号类型而输入信号使用无符号类型时，无论输入和限值如何，输出信号都会持续增加。
- 使用固定步长求解器来仿真包含此模块的模型。

  因为 Rate Limiter Dynamic 模块仅支持离散采样时间。
