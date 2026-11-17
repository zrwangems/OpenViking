---
type: simulink-block
title: '6-Speed Lepelletier'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Transmissions'
documentation_page: '6speedlepelletier'
documentation_source_path: 'ref/6speedlepelletier.html'
language: zh-CN
chinese_source: worker-translation
---

# 6-Speed Lepelletier

## 端口
```yaml
ports:
- name: Gear
  summary: 挡位标量的数值输入
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

### **Gear** — 挡位标量的数值输入

指定 -1 表示倒挡，0 表示空挡，1–6 表示前进挡。

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
  summary: 仿真开始时的挡位状态 Neutral（默认）| 6 | 5 | 4 | 3 | 2 | 1 | Reverse
  group: ''
```

### **Initial gear** — 仿真开始时的挡位状态 `Neutral`（默认）| `6` | `5` | `4` | `3` | `2` | `1` | `Reverse`

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

六速 Lepelletier 变速器的离合器调度表

6-Speed Lepelletier 由一个行星齿轮组、一个 Ravigneaux 齿轮组和五个盘式摩擦离合器组成。变速器基座轴连接到行星齿轮组的齿圈。从动轴连接到 Ravigneaux 齿轮组的齿圈。其中三个离合器控制行星齿轮组和 Ravigneaux 齿轮组之间的功率流路径。另外两个离合器用作制动器，将 Ravigneaux 齿轮组的各个齿轮接地到变速器壳体。

此图展示了一个六速 Lepelletier 变速器。齿轮组件的标签叠加在输入和输出齿轮上。下表列出了图中标注的齿轮和离合器组件。

| 标签 | 组件 |
| --- | --- |
| P.G. | 行星齿轮 |
| R.G. | Ravigneaux 齿轮 |
| R | 齿圈 |
| C | 行星齿轮架 |
| S | 太阳轮 |
| SL | 大太阳轮 |
| SS | 小太阳轮 |
| A–C | 控制功率流路径的前进离合器 |
| D–E | 前进制动离合器 |

### 传动比、离合器调度表和功率流

变速器输入轴和输出轴之间的传动比由齿轮模块指定的基本齿轮比决定。基本齿轮比为

g1=NPRNPS，

g2=NRRNRSL，

以及

g3=NRRNRSS，

其中：

- *N*PR 是行星齿轮组齿圈的齿数。
- *N*PS 是行星齿轮组太阳轮的齿数。
- *N*RR 是 Ravigneaux 齿轮组齿圈的齿数。
- *N*RSL 是 Ravigneaux 齿轮组大太阳轮的齿数。
- *N*RRS 是 Ravigneaux 齿轮组小太阳轮的齿数。

下表展示了 6-Speed Lepelletier 模块每个挡位的离合器调度表、传动比表达式、传动比默认值和功率流图。

离合器调度表列中的字母表示制动器和离合器。值为 `1` 表示锁定状态，值为 `0` 表示解锁状态。离合器调度表根据 Gear 端口输入信号生成这些信号。这些信号通过 Gain 模块进行缩放，并用作离合器模块中的致动输入。

功率流图展示了每个挡位设置下输入轴和输出轴之间的功率流路径。功率流以橙色显示。与变速器壳体（机械接地）的连接以黑色显示。

| 挡位 | 离合器调度表 | | | | | 传动比方程 | 默认传动比 | 功率流 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **A** | **B** | **C** | **D** | **E** |  |  |  |
| 6 | 0 | **1** | 0 | 0 | **1** | g21+g2 | 0.69 |  |
| 5 | **1** | **1** | 0 | 0 | 0 | g2g2+1/(1+g1) | 0.87 |  |
| 4 | 0 | **1** | **1** | 0 | 0 | g3(1+g1)g3(1+g1)−1 | 1.14 |  |
| 3 | **1** | 0 | **1** | 0 | 0 | 1+g1g1 | 1.50 |  |
| 2 | 0 | 0 | **1** | 0 | **1** | (1+g1)(g3+g2)g1(1+g2) | 2.31 |  |
| 1 | 0 | 0 | **1** | **1** | 0 | g3(1+g1)g1 | 4.12 |  |
| R | **1** | 0 | 0 | **1** | 0 | −g2(1+g1)g1 | -3.36 |  |
