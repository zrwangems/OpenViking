---
type: simulink-block
title: '4-Speed Ravigneaux'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Transmissions with Gear Ratios and Clutch Schedules'
documentation_page: '4speedravigneaux'
documentation_source_path: 'ref/4speedravigneaux.html'
language: zh-CN
chinese_source: worker-translation
---

# 4-Speed Ravigneaux

## 端口

### 输入

### **Gear** — 挡位标量的数值输入

为倒挡指定 -1，为空挡指定 0，为前进挡指定 1–4。

**数据类型：** `single` | `double`
### 守恒

### **B** — 基座接口机械旋转

与基座轴关联的守恒端口。

### **F** — 从动接口机械旋转

与从动轴关联的守恒端口。

## 参数

### **Initial gear** — 仿真开始时的挡位状态 `Neutral`（默认） | `4` | `3` | `2` | `1` | `Reverse`

使用离合器切换表设置离合器的初始接合或分离。当变速器处于空挡时，从基座轴到从动轴没有动力流。

## 所属库

Simscape / Driveline / Transmissions

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

四速 Ravigneaux 变速器的离合器切换表

4-Speed Ravigneaux 模块由一个 Ravigneaux 齿轮组和五个离合器组成。从动轴连接到 Ravigneaux 组的齿圈。其中三个离合器确定基座轴为传递动力所连接的齿轮。另外两个离合器用作制动器，将 Ravigneaux 组的各个齿轮接地到变速器壳体。

此图显示了一个四速 Ravigneaux 齿轮变速器。齿轮部件的标签叠加在输入和输出齿轮上。下表列出了图中标注的齿轮和离合器部件。

| 标签 | 部件 |
| --- | --- |
| R.G. | Ravigneaux 齿轮 |
| R | 齿圈 |
| C | 行星齿轮架 |
| SL | 大太阳轮 |
| SS | 小太阳轮 |
| A–C | 控制动力流路径的前进离合器 |
| D–E | 前进、制动离合器 |

### 传动比、离合器切换表和动力流

变速器输入轴和输出轴之间的传动比由为齿轮模块指定的基本齿轮比得出。基本齿轮比为

g1=NRNSL，

以及

g2=NRNSS，

其中：

- *N*R 是 Ravigneaux 齿圈的齿数。
- *N*SL 是 Ravigneaux 大太阳轮的齿数。
- *N*SS 是 Ravigneaux 小太阳轮的齿数。

下表显示了 4-Speed Ravigneaux 模块各个挡位的离合器切换表、传动比表达式、传动比默认值和动力流图。

离合器切换表各列中的字母表示制动器和离合器。值 `1` 表示锁定状态，值 `0` 表示解锁状态。离合器切换表基于 Gear 端口输入信号生成这些信号。这些信号通过 Gain 模块进行缩放，并用作离合器模块中的致动输入。

动力流图显示每个挡位设置下输入轴和输出轴之间的动力流路径。动力流以橙色显示。与变速器壳体（机械接地）的连接以黑色显示。

| 挡位 | 离合器切换表 | | | | | 传动比方程 | 默认传动比 | 动力流 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **A** | **B** | **C** | **D** | **E** |  |  |  |
| 4 | **1** | 0 | 0 | 0 | **1** | g11+g1 | 0.67 |  |
| 3 | **1** | **1** | 0 | 0 | 0 | 1 | 1 |  |
| 2 | 0 | **1** | 0 | 0 | **1** | g1+g21+g1 | 1.67 |  |
| 1 | 0 | **1** | 0 | **1** | 0 | g2 | 3 |  |
| E | 0 | 0 | **1** | **1** | 0 | −g1 | -2 |  |
