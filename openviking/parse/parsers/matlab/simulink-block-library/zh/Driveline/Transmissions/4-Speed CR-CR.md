---
type: simulink-block
title: '4-Speed CR-CR'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Transmissions'
documentation_page: '4speedcrcr'
documentation_source_path: 'ref/4speedcrcr.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Speed CR-CR

## 端口
```yaml
ports:
- name: Gear
  summary: 挡位的数值输入标量
  direction: input
  data_types: single | double
- name: B
  summary: 基座接口机械旋转
  direction: input
- name: F
  summary: 从动接口机械旋转
  direction: input
```

### 输入

### **Gear** — 挡位的数值输入标量

指定 -1 表示倒挡，0 表示空挡，1–4 表示前进挡。

**数据类型：** `single` | `double`
### 守恒

### **B** — 基座接口机械旋转

与基座轴关联的守恒端口。

### **F** — 从动接口机械旋转

与从动轴关联的守恒端口。
## 参数
```yaml
parameters:
- name: Initial gear
  summary: 仿真开始时的挡位状态 Neutral（默认）| 4 | 3 | 2 | 1 | Reverse
  group: ''
```

### **Initial gear** — 仿真开始时的挡位状态 `Neutral`（默认）| `4` | `3` | `2` | `1` | `Reverse`

使用离合器调度表设置离合器的初始接合或分离状态。当变速器处于空挡时，从基座轴到从动轴没有功率流。
## 所属库

Simscape / Driveline / Transmissions

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

四速行星架环-行星架环变速器的离合器调度表

4-Speed CR-CR 模块由两个行星齿轮组和五个盘式摩擦离合器组成。从动轴连接到输出行星齿轮的行星齿轮架和输入行星齿轮的齿圈。离合器配置为实现四个传动比、一个倒挡传动比和空挡。倒挡离合器和其中两个离合器决定基座轴连接到哪些齿轮。另外两个离合器用作制动器，将行星齿轮组的各个齿轮接地到变速器壳体。

此图显示了一个四速行星架环-行星架环变速器。齿轮组件的标签叠加在输入和输出齿轮上。下表列出了图中标注的齿轮和离合器组件。

| 标签 | 组件 |
| --- | --- |
| I.P.G. | 输入行星齿轮 |
| O.P.G. | 输出行星齿轮 |
| R | 齿圈 |
| C | 行星齿轮架 |
| S | 太阳轮 |
| R | 倒挡离合器 |
| A–B | 控制功率流路径的前进挡离合器 |
| C–D | 前进挡、制动离合器 |

### 传动比、离合器调度表和功率流

变速器输入轴和输出轴之间的传动比由齿轮模块指定的基本齿轮比决定。基本齿轮比为

g1=NRINSI，

以及

g2=NRONSO，

其中：

- *N*RI 是输入轴侧行星齿圈的齿数。
- *N*SI 是输入轴侧行星太阳轮的齿数。
- *N*RO 是输出轴侧行星齿圈的齿数。
- *N*SO 是输出轴侧行星太阳轮的齿数。

下表显示了 4-Speed CR-CR 模块每个挡位的离合器调度表、传动比表达式、传动比默认值和功率流图。

离合器调度表列中的字母表示制动器和离合器。值为 `1` 表示锁定状态，值为 `0` 表示解锁状态。离合器调度表根据 Gear 端口输入信号生成这些信号。这些信号通过 Gain 模块缩放，并用作离合器模块中的致动输入。

功率流图显示了每个挡位设置下输入轴和输出轴之间的功率流路径。功率流以橙色显示。与变速器壳体（机械接地）的连接以黑色显示。

| 挡位 | 离合器调度表 | | | | | 传动比方程 | 默认传动比 | 功率流 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **A** | **B** | **C** | **D** | **R** |  |  |  |
| 4 | 0 | **1** | **1** | 0 | 0 | g11+g1 | 0.67 |  |
| 3 | **1** | **1** | 0 | 0 | 0 | 1 | 1 |  |
| 2 | **1** | 0 | **1** | 0 | 0 | g1+g2+11+g1 | 1.67 |  |
| 1 | **1** | 0 | 0 | **1** | 0 | g2+1 | 3 |  |
| R | 0 | 0 | 0 | **1** | **1** | −g1 | -2 |  |
