---
type: simulink-block
title: 'SM Current Reference Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smcurrentreferencegenerator'
documentation_source_path: 'ref/smcurrentreferencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# SM Current Reference Generator

## 端口

### 输入

### **TqRef** — 参考转矩，N\*m 标量

由同步电机产生的期望机械转矩。

**数据类型：** `single` | `double`

### **wMechanical** — 转子机械转速，rad/s 标量

同步电机转子的机械角速度，通过同步电机直接测量获得。

**数据类型：** `single` | `double`

### **Vdc** — 直流母线电压，V 标量

变换器的直流母线电压。对于 ZDAC 方法，该值用于限制输出参考转矩和转矩限值。对于查找表方法，该值用作查找表的输入。

**数据类型：** `single` | `double`
### 输出

### **idqfRef** — 参考电流，A 向量

要作为电流控制器输入的参考 d-q 电流和励磁电流。

**数据类型：** `single` | `double`

### **TqRefSat** — 参考转矩，N\*m 标量

由计算得出的转矩限值 **TqLim** 饱和后的参考转矩。

**数据类型：** `single` | `double`

### **TqLim** — 转矩限值，N\*m 标量

由系统的电气和机械约束共同施加的转矩限值。

**数据类型：** `single` | `double`

## 参数

#### 通用参数

### **标称直流母线电压 (V)** — 额定直流电压 `300``V`（默认） | 正数

电源的标称直流母线电压。

### **最大功率 (W)** — 最大功率 `30000``W`（默认） | 正数

同步电机的最大功率。

### **最大转矩 (N\*m)** — 最大转矩 `250``N*m`（默认） | 正数

同步电机的最大转矩。

### **最大励磁电流 (A)** — 最大励磁电流 `25``A`（默认） | 正数

同步电机的最大励磁电流。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认） | -1 或正数

模块的采样时间（-1 表示继承）。如果该模块在触发子系统内使用，采样时间应为 -1。如果该模块在连续可变步长模型中使用，则可以显式指定采样时间。

#### 参考生成策略

### **电流参考** — 电流参考策略 `Zero d-axis control`（默认） | `Lookup-table based`

选择用于确定电流参考的策略。

### **转矩常数 (N\*m/A)** — 转矩常数 `0.0375`（默认） | 正数

同步电机的转矩常数。

### **机械转速向量, wMechanical (rpm)** — 转子转速查找向量 `[0, 3000]`（默认） | 正单调递增向量

用于确定电流参考的查找表中的转速向量。

### **转矩参考向量, TqRef (N\*m)** — 转矩参考查找向量 `[-100, 0, 100]`（默认） | 正单调递增向量

用于确定电流参考的查找表中的转矩向量。

### **直流母线电压向量, Vdc (V)** — 直流母线电压查找向量 `[300, 350]`（默认） | 正单调递增向量

用于确定电流参考的查找表中的直流母线电压向量。

### **d 轴电流参考矩阵, id(wMechanical,TqRef,Vdc), (A)** — 参考 d 轴电流值 `zeros(2,3,2)`（默认） | 实矩阵

直轴电流参考查找数据。

### **q 轴电流参考矩阵, iq(wMechanical,TqRef,Vdc), (A)** — 参考 q 轴电流值 `zeros(2,3,2)`（默认） | 实矩阵

交轴电流参考查找数据。

### **励磁电流参考矩阵, iq(wMechanical,TqRef,Vdc), (A)** — 参考励磁电流值 `zeros(2,3,2)`（默认） | 实矩阵

励磁电流参考查找数据。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

同步电机电流参考生成器

SM Current Reference Generator 模块实现了一个电流参考生成器，用于在转子 *d*-*q* 参考坐标系中进行同步电机 (SM) 电流控制。

### 定义方程

SM Current Reference Generator 模块可以使用以下方法之一获得电流参考：

- Zero *d*-axis control (ZDAC)。
- 查找表。

对于 ZDAC 方法，该模块设置：

- 将 *d* 轴电流参考 idref 设置为零：

  idref=0,
- 使用转矩参考设置励磁电流参考 ifref：

  ifref=|Trefif,max|Tmax,

  其中 *if,max* 是最大励磁电流，*Tmax* 是最大转矩。
- 使用转矩方程设置 *q* 轴电流参考 iqref：

  iqref= TrefKtifref,

  其中 *Tref* 是参考转矩输入，*Kt* 是同步电机的转矩常数，由简化转矩方程 T=Ktifiq 表示。

对于低于同步电机基速的运行，ZDAC 是一种合适的方法。高于基速时，需要弱磁控制器来调整 *d* 轴参考。

为了针对多个工作点预生成电流参考，请使用查找表方法定义三个查找表：

idref=f(nm,Tref,vdc),

iqref= g(nm,Tref,vdc),

以及

ifref= h(nm,Tref,vdc).
