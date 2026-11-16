---
type: simulink-block
title: 'Pi-shaped MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'pishapedmf'
documentation_source_path: 'pishapedmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Pi-shaped MF

## 端口

### 输入

### **x** — 输入值 scalar | vector

要计算隶属度值的输入值，指定为 scalar 或 vector。
### 输出

### **Pi MF** — 隶属度值 scalar | vector

隶属度值，以 scalar 或 vector 形式返回。**Pi MF** 的维度与 **x** 的维度匹配。**Pi MF** 的每个元素是为 **x** 的对应元素计算得到的隶属度值。

## 参数

### **左基点 a** — 左过渡区的底点 `-9`（默认）| scalar

左侧过渡区的底点 *a*。

#### 编程用法

|  |
| --- |
| **模块参数：** `a` |
| **类型：** string, character vector |
| **默认值：** `"-9"` |

### **左顶点 b** — 左过渡区的肩部 `-7`（默认）| scalar

左侧过渡区的肩部 *b*。

#### 编程用法

|  |
| --- |
| **模块参数：** `b` |
| **类型：** string, character vector |
| **默认值：** `"-7"` |

### **右顶点 c** — 右过渡区的肩部 `-9`（默认）| scalar

右侧过渡区的肩部 *c*。

#### 编程用法

|  |
| --- |
| **模块参数：** `c` |
| **类型：** string, character vector |
| **默认值：** `"2"` |

### **右基点 d** — 右过渡区的底点 `-7`（默认）| scalar

右侧过渡区的底点 *d*。

#### 编程用法

|  |
| --- |
| **模块参数：** `d` |
| **类型：** string, character vector |
| **默认值：** `"8"` |

## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成
使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

Pi 形隶属函数

Pi-shaped MF 模块实现 Pi 形隶属函数。

f(x;a,b,c,d)={0,x≤a2(x−ab−a)2,a≤x≤a+b21−2(x−bb-a)2,a+b2≤x≤b1,b≤x≤c1−2(x−cd−c)2,c≤x≤c+d22(x−dd-c)2,c+d2≤x≤d0,x≥d}

参数 *a* 和 *d* 控制曲线的左基点和右基点或*底点*。参数 *b* 和 *c* 控制曲线的左顶点和右顶点或*肩部*。

此模块与 Z-shaped MF 和 S-shaped MF 模块相关。
