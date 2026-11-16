---
type: simulink-block
title: '7-Speed Lepelletier'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Transmissions with Gear Ratios and Clutch Schedules'
documentation_page: '7speedlepelletier'
documentation_source_path: 'ref/7speedlepelletier.html'
language: zh-CN
chinese_source: worker-translation
---

# 7-Speed Lepelletier

## 端口

### 输入

### **Gear** — 挡位标量的数值输入

将 -1 指定为倒挡，0 指定为空挡，1–7 指定为前进挡。

**数据类型：** `single` | `double`
### 守恒

### **B** — 基座接口机械旋转

与基座轴关联的守恒端口。

### **F** — 从动接口机械旋转

与从动轴关联的守恒端口。

## 参数

### **Initial gear** — 仿真开始时的挡位状态 `Neutral` (默认) | `7` | `6` | `5` | `4` | `3` | `2` | `1` | `Reverse`

使用离合器调度表设置离合器的初始接合或分离。当变速器处于空挡时，从基座轴到从动轴没有功率流。

## 所属库

Simscape / Driveline / Transmissions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

七速 Lepelletier 变速器的离合器调度表

7–Speed Lepelletier 模块由一个行星齿轮组、一个 Ravigneaux 齿轮组和六个盘式摩擦离合器组成。变速器基座轴连接到行星齿轮组的齿圈。从动轴连接到 Ravigneaux 齿轮组的齿圈。其中三个离合器控制行星齿轮组与 Ravigneaux 齿轮组之间的功率流路径。另外三个离合器用作制动器，将 Ravigneaux 齿轮组的各个齿轮接地到变速器壳体。

此图显示了一个七速 Lepelletier 变速器。齿轮组件的标签叠加在输入和输出齿轮上。下表列出了图中标注的齿轮和离合器组件。

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
| D–F | 前进、制动离合器 |

### 传动比、离合器调度表和功率流

变速器输入轴与输出轴之间的传动比由为齿轮模块指定的基本齿轮比得出。基本齿轮比为

g1=NPRNPS，

g2=NRRNRSL，

以及

g3=NRRNRSS，

其中：

- *N*PR 是行星齿圈的齿数。
- *N*PS 是行星太阳轮的齿数。
- *N*RR 是 Ravigneaux 齿圈的齿数。
- *N*RSL 是 Ravigneaux 大太阳轮的齿数。
- *N*RSS 是 Ravigneaux 小太阳轮的齿数。

下表显示了 7-Speed Lepelletier 模块每个挡位的离合器调度表、传动比表达式、传动比默认值和功率流图。

离合器调度表列中的字母表示制动器和离合器。值 `1` 表示锁止状态，值 `0` 表示未锁止状态。离合器调度表基于 Gear 端口输入信号生成这些信号。这些信号通过 Gain 模块缩放，并在离合器模块中用作致动输入。

功率流图显示了每个挡位设置下输入轴与输出轴之间的功率流路径。功率流以橙色显示。与变速器壳体（机械接地）的连接以黑色显示。

| 挡位 | 离合器调度表 | | | | | | 传动比方程 | 默认传动比 | 功率流 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **A** | **B** | **C** | **D** | **E** | **F** |  |  |  |
| 7 | 0 | **1** | 0 | 0 | **1** | **1** | g21+g2 | 0.70 |  |
| 6 | **1** | **1** | 0 | 0 | 0 | **1** | g2(1+g1)g2(1+g1)+1 | 0.86 |  |
| 5 | **1** | **1** | **1** | 0 | 0 | 0 | 1 | 1 |  |
| 4 | 0 | **1** | **1** | 0 | 0 | **1** | g3(1+g1)g3(1+g1)−1 | 1.17 |  |
| 3 | **1** | 0 | **1** | 0 | 0 | **1** | 1+g1g1 | 1.63 |  |
| 2 | 0 | 0 | **1** | 0 | **1** | **1** | (1+g1)(g3+g2)g1(1+g2) | 2.43 |  |
| 1 | 0 | 0 | **1** | **1** | 0 | **1** | g3(1+g1)g1 | 4.31 |  |
| R | **1** | 0 | 0 | **1** | 0 | **1** | −g2(1+g1)g1 | -3.82 |  |
