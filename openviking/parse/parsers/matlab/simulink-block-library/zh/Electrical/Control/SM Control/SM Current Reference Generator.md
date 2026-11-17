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

同步电机产生的期望机械转矩。

**数据类型：** `single` | `double`

### **wMechanical** — 转子机械转速，rad/s 标量

同步电机转子的机械角速度，通过同步电机直接测量获得。

**数据类型：** `single` | `double`

### **Vdc** — 直流母线电压，V 标量

变换器的直流母线电压。对于 ZDAC 方法，该值用于限制输出参考转矩和转矩限值。对于查表方法，该值用作查找表的输入。

**数据类型：** `single` | `double`
### 输出

### **idqfRef** — 参考电流，A 向量

参考 d-q 轴电流和励磁电流，作为电流控制器的输入。

**数据类型：** `single` | `double`

### **TqRefSat** — 参考转矩，N\*m 标量

经计算的转矩限值 **TqLim** 饱和后的参考转矩。

**数据类型：** `single` | `double`

### **TqLim** — 转矩限值，N\*m 标量

由系统电气和机械约束共同施加的转矩限值。

**数据类型：** `single` | `double`

## 参数

#### 通用参数

### **Nominal dc-link voltage (V)** — 额定直流电压 `300``V`（默认）| 正数

电源的额定直流母线电压。

### **Maximum power (W)** — 最大功率 `30000``W`（默认）| 正数

同步电机的最大功率。

### **Maximum torque (N\*m)** — 最大转矩 `250``N*m`（默认）| 正数

同步电机的最大转矩。

### **Maximum field current (A)** — 最大励磁电流 `25``A`（默认）| 正数

同步电机的最大励磁电流。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| -1 或正数

模块的采样时间（-1 表示继承）。如果该模块在触发子系统中使用，采样时间应设为 -1。如果该模块在连续变步长模型中使用，则可以显式指定采样时间。

#### 参考生成策略

### **Current references** — 电流参考策略 `Zero d-axis control`（默认）| `Lookup-table based`

选择确定电流参考的策略。

### **Torque constant (N\*m/A)** — 转矩常数 `0.0375`（默认）| 正数

同步电机的转矩常数。

### **Mechanical speed vector, wMechanical (rpm)** — 转子转速查找向量 `[0, 3000]`（默认）| 正单调递增向量

用于确定电流参考的查找表中的转速向量。

### **Torque reference vector, TqRef (N\*m)** — 转矩参考查找向量 `[-100, 0, 100]`（默认）| 正单调递增向量

用于确定电流参考的查找表中的转矩向量。

### **DC-link voltage vector, Vdc (V)** — 直流母线电压查找向量 `[300, 350]`（默认）| 正单调递增向量

用于确定电流参考的查找表中的直流母线电压向量。

### **D-axis current reference matrix, id(wMechanical,TqRef,Vdc), (A)** — 参考 d 轴电流值 `zeros(2,3,2)`（默认）| 实数矩阵

直轴电流参考查找数据。

### **Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc), (A)** — 参考 q 轴电流值 `zeros(2,3,2)`（默认）| 实数矩阵

交轴电流参考查找数据。

### **Field current reference matrix, iq(wMechanical,TqRef,Vdc), (A)** — 参考励磁电流值 `zeros(2,3,2)`（默认）| 实数矩阵

励磁电流参考查找数据。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

同步电机电流参考生成器

SM Current Reference Generator 模块实现了在转子 *d*-*q* 参考坐标系下用于同步电机（SM）电流控制的电流参考生成器。

### 定义方程

SM Current Reference Generator 模块可以使用以下方法之一获取电流参考：

- 零 *d* 轴控制（ZDAC）。
- 查找表。

对于 ZDAC 方法，该模块设置：

- *d* 轴电流参考 idref 为零：

  idref=0，
- 励磁电流参考 ifref 使用转矩参考：

  ifref=|Trefif,max|Tmax，

  其中
  *if,max* 是最大
  励磁电流，*Tmax* 是
  最大转矩。
- *q* 轴电流参考 iqref 使用转矩方程：

  iqref= TrefKtifref，

  其中 *Tref*
  是参考转矩输入，
  *Kt* 是同步电机的转矩常数，由简化转矩方程 T=Ktifiq 表示。

对于在同步电机基速以下运行的情况，ZDAC 是一种合适的方法。在基速以上，需要弱磁控制器来调整 *d* 轴参考。

要为多个工作点预生成电流参考，使用查找表方法定义三个查找表：

idref=f(nm,Tref,vdc)，

iqref= g(nm,Tref,vdc)，

以及

ifref= h(nm,Tref,vdc)。
