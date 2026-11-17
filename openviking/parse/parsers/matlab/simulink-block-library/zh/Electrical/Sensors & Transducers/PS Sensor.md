---
type: simulink-block
title: 'PS Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'pssensor'
documentation_source_path: 'ref/pssensor.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Sensor

## 端口

### 输入

### **U** — 物理输入信号 physical signal

物理输入信号。
### 守恒

### **+** — 正电压 electrical

与 PS sensor 正电压相关联的电气守恒端口。

### **-** — 负电压 electrical

与 PS sensor 负电压相关联的电气守恒端口。

## 参数

### **Output type** — 传感器输出类型 `Variable voltage`（默认）| `Variable current` | `Variable resistor`

指示传感器输出是 *Y* V 的 `Variable voltage`、*Y* A 的 `Variable current`，还是值为 *Y* Ω 的 `Variable resistor`。

### **Sensor gain, A** — 输出灵敏度 `1`（默认）

输出 *Y* 相对于输入 *U* 的灵敏度，*dY/dU*。

### **Sensor offset, B** — 传感器偏移 `0`（默认）

输入 *U* 为零时的输出。输出不超过限值 *Y*max 和 *Y*min。

### **Maximum output, Ymax** — 最大输出 `5`（默认）

传感器输出的上限。下表显示了此参数的单位，这些单位取决于 **Output type** 参数的所选值。

| **Output type** | 单位 |
| --- | --- |
| `Variable voltage` | V |
| `Variable current` | A |
| `Variable resistor` | Ω |

### **Minimum output, Ymin** — 最小输出 `0.01`（默认）

传感器输出的下限。下表显示了此参数的单位，这些单位取决于 **Output type** 参数的所选值。

| **Output type** | 单位 |
| --- | --- |
| `Variable voltage` | V |
| `Variable current` | A |
| `Variable resistor` | Ω |

如果为 **Output type** 参数选择 `Variable resistance`，则最小电阻 *Y*min 必须大于零。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

具有电气输出的通用线性传感器

PS Sensor 模块表示一个通用线性传感器。该模块将物理信号输入 *U* 转换为 + 和 - 端口上的电气输出 *Y*。**Output type** 参数值决定该模块产生以下哪种电气输出：

- 输出电压
- 输出电流
- 输出电阻

*Y* 与 *U* 的关系为 *Y* = max(min(*A* ·
*U* +
*B*,*Y*max),*Y*min)，其中 *Y*min 和 *Y*max 分别是输出的最小限值和最大限值。
