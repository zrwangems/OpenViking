---
type: simulink-block
title: 'Diff. Sigmoidal MF'
family: 'fuzzy'
product_id: 'fuzzy'
product_name: 'Fuzzy Logic Toolbox'
documentation_release: R2025b
official_category: 'Membership Functions'
documentation_page: 'diff.sigmoidalmf'
documentation_source_path: 'diff.sigmoidalmf.html'
language: zh-CN
chinese_source: worker-translation
---

# Diff. Sigmoidal MF

## 端口
```yaml
ports:
- name: x
  summary: 输入值 标量 | 向量
  direction: input
- name: MF
  summary: 隶属度值 标量 | 向量
  direction: output
```

### 输入

### **x** — 输入值 标量 | 向量

用于计算隶属度值的输入值，指定为标量或向量。

### 输出

### **MF** — 隶属度值 标量 | 向量

隶属度值，以标量或向量形式返回。**MF** 的维度与 **x** 的维度一致。**MF** 的每个元素是对 **x** 中对应元素计算得到的隶属度值。
## 参数
```yaml
parameters:
- name: Left curve a1
  summary: 左曲线的过渡区域形状参数 3（默认）| 标量
  group: ''
  block_parameter: a1
  type: string, character vector
  default: '"3"'
- name: Left curve c1
  summary: 左曲线的过渡区域中心 -5（默认）| 标量
  group: ''
  block_parameter: c1
  type: string, character vector
  default: '"-5"'
- name: Right curve a2
  summary: 右曲线的过渡区域形状参数 1（默认）| 标量
  group: ''
  block_parameter: a2
  type: string, character vector
  default: '"1"'
- name: Right curve c2
  summary: 右曲线的过渡区域中心 5（默认）| 标量
  group: ''
  block_parameter: c2
  type: string, character vector
  default: '"5"'
```

### **Left curve a1** — 左曲线的过渡区域形状参数 `3`（默认）| 标量

控制左曲线过渡区域形状的参数 *a*1。*a*1 的大小控制过渡区域的宽度。

当 *a*1 的符号为正时，曲线从左到右递增。反之，当 *a*1 的符号为负时，曲线从左到右递减。

#### 编程使用

|  |
| --- |
| **模块参数**：`a1` |
| **类型**：string, character vector |
| **默认值**：`"3"` |

### **Left curve c1** — 左曲线的过渡区域中心 `-5`（默认）| 标量

左曲线的过渡区域中心 *c*1。

#### 编程使用

|  |
| --- |
| **模块参数**：`c1` |
| **类型**：string, character vector |
| **默认值**：`"-5"` |

### **Right curve a2** — 右曲线的过渡区域形状参数 `1`（默认）| 标量

控制右曲线过渡区域形状的参数 *a*2。*a*2 的大小控制过渡区域的宽度。

当 *a*2 的符号为正时，曲线从左到右递增。反之，当 *a*2 的符号为负时，曲线从左到右递减。

#### 编程使用

|  |
| --- |
| **模块参数**：`a2` |
| **类型**：string, character vector |
| **默认值**：`"1"` |

### **Right curve c2** — 右曲线的过渡区域中心 `5`（默认）| 标量

右曲线的过渡区域中心 *c*2。

#### 编程使用

|  |
| --- |
| **模块参数**：`c2` |
| **类型**：string, character vector |
| **默认值**：`"5"` |
## 所属库

Fuzzy Logic Toolbox / Membership Functions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

两个 sigmoid 函数之差的隶属函数

Diff. Sigmoidal MF 模块在 Simulink® 中基于两个 sigmoid 函数之差实现隶属函数。sigmoid 曲线由以下方程定义。

f(x;ak,ck)=11+e−ak(x−ck)

其中 *k* = 1,2。参数 *a*1 和 *a*2 控制左曲线和右曲线的斜率。参数 *c*1 和 *c*2 控制左曲线和右曲线的拐点。

要定义最大值为 `1` 的单峰隶属函数，请为 *a*1 和 *a*2 指定相同的符号，并选择相距足够远的 *c* 值，以使两个过渡区域都能达到 `1`。

此模块与 Sigmoidal MF 和 Prod. Sigmoidal MF 隶属函数模块相关。
