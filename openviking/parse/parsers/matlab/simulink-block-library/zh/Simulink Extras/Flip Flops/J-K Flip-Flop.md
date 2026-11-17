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
chinese_source: worker-translation
---

# J-K Flip-Flop

## 端口

### 输入

### **J** — 输入信号 J 标量

输入信号 **J**，指定为标量、向量或矩阵。

#### 依赖关系

J-K Flip-Flop 模块接受的数据类型取决于 **Implement logic signals as boolean data
(vs. double)** 配置参数的设置：

- `On` — J-K Flip-Flop 模块
  仅接受类型为 `boolean` 的实标量信号。
- `Off` — J-K Flip-Flop
  模块接受类型为 `boolean` 或 `double`
  的实标量信号（两个输入必须具有相同类型）。

**数据类型：** `double` | `Boolean`

### **CLK** — 时钟信号 标量

时钟信号，指定为标量、向量或矩阵。

#### 依赖关系

J-K Flip-Flop 模块接受的数据类型取决于 **Implement logic signals as boolean data
(vs. double)** 配置参数的设置：

- `On` — J-K Flip-Flop 模块
  仅接受类型为 `boolean` 的实标量信号
- `Off` — J-K Flip-Flop
  模块接受类型为 `boolean` 或 `double`
  的实标量信号（两个输入必须具有相同类型）。

**数据类型：** `double` | `Boolean`

### **K** — 输入信号 K 标量

输入信号 **K**，指定为标量、向量或矩阵。

#### 依赖关系

J-K Flip-Flop 模块接受的数据类型取决于 **Implement logic signals as boolean data
(vs. double)** 配置参数的设置：

- `On` — J-K Flip-Flop 模块
  仅接受类型为 `boolean` 的实标量信号
- `Off` — J-K Flip-Flop
  模块接受类型为 `boolean` 或 `double`
  的实标量信号（两个输入必须具有相同类型）。

**数据类型：** `double` | `Boolean`
### 输出

### **Q** — 输出信号 Q 标量

输出信号 **!Q**，具有与输入相同的维度和
数据类型。

**数据类型：** `double` | `Boolean`

### **!Q** — 输出信号 !Q 标量

输出信号 **!Q**，具有与输入相同的维度和
数据类型。

**数据类型：** `double` | `Boolean`

## 参数

### **Initial condition (state of Q)** — 输出 Q 的初始值 `0`（默认）| 标量

指定输出 **Q** 的初始值。非零
值被视为真（`1`）。

#### 程序化使用

|  |
| --- |
| **模块参数：** `initial_condition` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'0'` |

## 所属库

Simulink Extras / Flip Flops

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2008b 中引入**

## 描述

对负边沿触发的 J-K 触发器进行建模

J-K Flip-Flop 模块对负边沿触发的 J-K 触发器进行建模。J-K
触发器模块具有三个输入：**J**、
**K** 和 **CLK**。在时钟信号（**CLK**）的负（下降）沿，
J-K Flip-Flop 模块根据以下真值表输出 **Q** 及其补码 **!Q**。
在此真值表中，**Q**n-1 是上一时间
步的输出。

**注意**

J-K Flip-Flop 模块将非零输入视为真
（`1`）。

| J | K | Q n | !Q n |
| --- | --- | --- | --- |
| 0 | 0 | Q n-1 | !Q n-1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | !Q n-1 | Q n-1 |

当 **J** 为 1 且 **K** 为 0 时，触发器进入
置位状态（**Q**n 为 1）。当
**J** 为 0 且 **K** 为 1 时，触发器进入
复位状态（**Q**n 为 0）。当 **J**
和 **K** 均为 0 时，触发器保持
先前状态（**Q**n 为
**Q**n-1）。当 **J**
和 **K** 均为 1 时，触发器翻转
（**Q**n 为
**Q**n-1 的补码）。

### 逻辑信号作为布尔或双精度数据类型

**Implement logic signals as boolean data (vs. double)** 配置
参数设置会影响 J-K Flip-Flop 模块的输入和输出数据类型，因为该模块是一个使用
Combinatorial Logic 模块的掩码子系统。有关此配置参数的更多
信息，请参阅 Implement logic signals as Boolean data (vs. double)。
