---
type: simulink-block
title: 'Prod. Sigmoidal MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'prod.sigmoidalmf'
documentation_source_path: 'prod.sigmoidalmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Prod. Sigmoidal MF

## 端口

### 输入

### **x** — 输入值 scalar | vector

为其计算隶属度值的输入值，指定为 scalar 或 vector。
### 输出

### **MF** — 隶属度值 scalar | vector

隶属度值，以 scalar 或 vector 形式返回。**MF** 的维度与 **x** 的维度匹配。**MF** 的每个元素是为 **x** 的对应元素计算得到的隶属度值。

## 参数

### **左曲线 a1** — 左曲线的过渡区域形状参数 `2`（默认）| scalar

参数 *a*1 控制左曲线的过渡区域形状。*a*1 的大小控制过渡区域的宽度。

当 *a*1 的符号为正时，曲线从左到右递增。相反，当 *a*1 的符号为负时，曲线从左到右递减。

#### 编程使用

|  |
| --- |
| **模块参数：** `a1` |
| **类型：** string, character vector |
| **默认值：** `"2"` |

### **左曲线 c1** — 左曲线的过渡区域中心 `-5`（默认）| scalar

左曲线的过渡区域中心 *c*1。

#### 编程使用

|  |
| --- |
| **模块参数：** `c1` |
| **类型：** string, character vector |
| **默认值：** `"-5"` |

### **右曲线 a2** — 右曲线的过渡区域形状参数 `-5`（默认）| scalar

参数 *a*2 控制右曲线的过渡区域形状。*a*2 的大小控制过渡区域的宽度。

当 *a*2 的符号为正时，曲线从左到右递增。相反，当 *a*2 的符号为负时，曲线从左到右递减。

#### 编程使用

|  |
| --- |
| **模块参数：** `a2` |
| **类型：** string, character vector |
| **默认值：** `"-5"` |

### **右曲线 c2** — 右曲线的过渡区域中心 `5`（默认）| scalar

右曲线的过渡区域中心 *c*2。

#### 编程使用

|  |
| --- |
| **模块参数：** `c2` |
| **类型：** string, character vector |
| **默认值：** `"5"` |

## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**R2006a 之前引入**

## 描述

两个 S 型隶属度函数的乘积

Prod. Sigmoidal MF 模块基于两个 S 型曲线的乘积实现一个隶属度函数。S 型曲线由以下方程定义。

f(x;ak,ck)=11+e−ak(x−ck)

其中 *k* = 1,2。参数 *a*1 和 *a*2 控制左曲线和右曲线的斜率。参数 *c*1 和 *c*2 控制左曲线和右曲线的拐点。

要定义最大值为 `1` 的单峰隶属度函数，请为 *a*1 和 *a*2 指定相反的符号，并选择彼此相距足够远的 *c* 值，以使两个过渡区域都能达到 `1`。

此模块与 Diff. Sigmoidal MF 和 Sigmoidal MF 模块相关。
