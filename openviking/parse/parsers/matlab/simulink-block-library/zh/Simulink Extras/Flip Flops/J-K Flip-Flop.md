---
type: simulink-block
title: 'J-K Flip-Flop'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Flip Flops'
documentation_page: 'jkflipflop'
documentation_source_path: '../simulink/ref_extras/jkflipflop.html'
language: zh-CN
chinese_source: official
---

# J-K Flip-Flop

## 端口

### 输入

### **J** — 输入信号 J 标量

输入信号 **J**，指定为标量、向量或矩阵。

#### 依赖关系

J-K Flip-Flop 模块接受的数据类型取决于**将逻辑信号实现为布尔数据(而不是双精度数据)** 配置参数的设置：

- `On` - J-K Flip-Flop 模块只接受 `boolean` 类型的实数标量信号。
- `Off` - J-K Flip-Flop 模块接受 `boolean` 或 `double` 类型的实数标量信号（两个输入必须具有相同的类型）。

**数据类型:** `double` | `Boolean`

### **CLK** — 时钟信号 标量

时钟信号，指定为标量、向量或矩阵。

#### 依赖关系

J-K Flip-Flop 模块接受的数据类型取决于**将逻辑信号实现为布尔数据(而不是双精度数据)** 配置参数的设置：

- `On` - J-K Flip-Flop 模块只接受 `boolean` 类型的实数标量信号
- `Off` - J-K Flip-Flop 模块接受 `boolean` 或 `double` 类型的实数标量信号（两个输入必须具有相同的类型）。

**数据类型:** `double` | `Boolean`

### **K** — 输入信号 K 标量

输入信号 **K**，指定为标量、向量或矩阵。

#### 依赖关系

J-K Flip-Flop 模块接受的数据类型取决于**将逻辑信号实现为布尔数据(而不是双精度数据)** 配置参数的设置：

- `On` - J-K Flip-Flop 模块只接受 `boolean` 类型的实数标量信号
- `Off` - J-K Flip-Flop 模块接受 `boolean` 或 `double` 类型的实数标量信号（两个输入必须具有相同的类型）。

**数据类型:** `double` | `Boolean`
### 输出

### **Q** — 输出信号 Q 标量

输出信号 **!Q**，具有与输入相同的维度和数据类型。

**数据类型:** `double` | `Boolean`

### **!Q** — 输出信号 !Q 标量

输出信号 **!Q**，具有与输入相同的维度和数据类型。

**数据类型:** `double` | `Boolean`

## 参数

### **初始条件(Q 的状态)** — 输出 Q 的初始值 `0` (默认) | 标量

指定输出 **Q** 的初始值。非零值被视为 true (`1`)。

#### 编程用法

|  |
| --- |
| **模块参数**：`initial_condition` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'0'` |

## 所属库

Simulink Extras / Flip Flops

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2008b 中推出**

## 描述

负边沿触发的 J-K 触发器建模

J-K Flip-Flop 模块对负边沿触发的 J-K 触发器进行建模。J-K flip-flop 模块有三个输入，即 **J**，**K** 和 **CLK**。在时钟信号 (**CLK**) 的负（下降）沿，J-K Flip-Flop 模块根据以下真值表输出 **Q** 及其反值 **!Q**。在此真值表中，**Q**n-1 是前一时间步的输出。

**注意**

J-K Flip-Flop 模块将非零输入视为 true (`1`)。

| J | K | Qn | !Qn |
| --- | --- | --- | --- |
| 0 | 0 | Qn-1 | !Qn-1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | !Qn-1 | Qn-1 |

当 **J** 为 1 且 **K** 为 0 时，触发器进入设置状态（**Q**n 为 1）。当 **J** 为 0 且 **K** 为 1 时，触发器进入重置状态（**Q**n 为 0）。当 **J** 和 **K** 都为 0 时，触发器停留在先前的状态（**Q**n 为 **Q**n-1）。当 **J** 和 **K** 都为 1 时，触发器会发生切换（**Q**n 是 **Q**n-1 的反值）。

### 布尔或双精度数据类型的逻辑信号

**将逻辑信号实现为布尔数据(而不是双精度数据)** 配置参数设置会影响 J-K Flip-Flop 模块的输入和输出数据类型，因为该模块是使用 Combinatorial Logic 模块的封装子系统。有关此配置参数的详细信息，请参阅将逻辑信号实现为布尔数据(而不是双精度数据)。
