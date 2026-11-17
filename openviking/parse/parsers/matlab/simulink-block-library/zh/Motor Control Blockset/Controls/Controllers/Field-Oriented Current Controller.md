---
type: simulink-block
title: 'Field-Oriented Current Controller'
family: 'controls'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'fieldorientedcurrentcontroller'
documentation_source_path: 'ref/fieldorientedcurrentcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Field-Oriented Current Controller

## 端口

### 输入

### **IdqRef** — 参考 *d* 轴和 *q* 轴电流向量

旋转 *d-q* 参考坐标系的参考电机 *d* 轴和 *q* 轴电流。

`IdqRef = [IdRef,
IqRef]`

**数据类型：** `single` | `double` | `fixed point`

### **IabMeas** — 测量的 *a* 相和 *b* 相电流向量

电机的测量 *a* 相和 *b* 相电流。

`IabMeas = [IaMeas,
IbMeas]`

**数据类型：** `single` | `double` | `fixed point`

### **θe** — 电机电气位置标量

电机的电气位置。

**数据类型：** `single` | `double` | `fixed point`

### **VSatLim** — *d-q* 电压饱和限值标量

内部 PI 控制器生成的 *d* 轴和 *q* 轴参考电压的饱和限值。此值取决于直流母线电压（*Vdc*）和所选的 PWM 方法。通常，对于 SPWM，此值等于 *Vdc/2*；对于 SVM，此值等于 *Vdc/sqrt(3)*。有关 PWM 技术的更多信息，请参阅 PWM Reference Generator。

**数据类型：** `single` | `double` | `fixed point`

### **Kp,Ki\*Ts** — *d* 轴和 *q* 轴 PI 控制器增益向量

*d* 轴和 *q* 轴 PI 控制器的增益（分别为 *Kp* 和 *Ki*），与模块采样时间（*Ts*）多路复用。

`Kp,Ki*Ts
= [Kp(d-axis),
Ki*Ts(d-axis),
Kp(d-axis),
Ki*Ts(d-axis)]`

**数据类型：** `single` | `double` | `fixed point`

### **PIConfig** — PI 控制器输出的初始值和限值向量

内部 PI 控制器积分器的初始值与其限值多路复用。

PIConfig = [PI 控制器积分器的饱和上限，PI 控制器积分器的饱和下限，*d* 轴 PI 控制器积分器的初始值，*q* 轴 PI 控制器积分器的初始值]

**数据类型：** `single` | `double` | `fixed point`

### **Enable** — 复位模块标量

用于复位模块中 PI 控制器的信号：

- `1` — 复位内部 PI 控制器。
- `0` — 无操作。

**数据类型：** `single` | `double` | `fixed point`

### 输出

### **Vabc** — 电机相电压向量

驱动电机的定子 *a*、*b* 和 *c* 相电压。

**数据类型：** `single` | `double` | `fixed point`

### **Debug** — 用于调试的信号向量

模块为调试目的捕获的内部计算多路复用信号。该多路复用信号由以下元素组成：

- *Idq* — 根据电机相电流计算得到的实际 *d* 轴和 *q* 轴电机电流。
- *Vdq* — 由内部 *d* 轴和 *q* 轴电流 PI 控制器计算得到的 *d* 轴和 *q* 轴电机电压。
- *Vαβ* — 模块使用 *Vdq* 的 Park 逆变换在内部计算的 *α* 轴和 *β* 轴电压。
- *Iαβ* — 模块使用 **IabMeas** 输入的 Clarke 变换在内部计算的 *α* 轴和 *β* 轴电流。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **输入电气位置单位** — 电气位置输入的单位 `Radians`（默认） | `Degrees` | `Per-unit`

电机电气位置输入 **θe** 的单位。

### **正弦-余弦查找表的数据点数量** — 查找表数组大小 `1024`（默认） | [125, 4095] 范围内的标量

内部正弦-余弦查找算法使用的查找表数组的大小，该算法计算电机电气位置的正弦和余弦。此参数接受 [125, 4095] 范围内的值。

### **Alpha（phase-a）轴对齐** — *dq* 参考坐标系对齐 `D-axis`（默认） | `Q-axis`

将旋转参考坐标系的 *d* 轴或 *q* 轴对齐到静止参考坐标系的 *α* 轴。

### **饱和方法** — 模块使用的饱和方法 `D-Q equivalence`（默认） | `Prioritize D axis` | `Prioritize Q axis`

将饱和方法设置为以下之一：

- `D-Q equivalence`
- `Prioritize D axis`
- `Prioritize Q axis`

### **PWM 方法** — 调制技术 `SVM: space vector modulation`（默认） | `SPWM: sinusoidal PWM`

模块输出的三相电压的脉宽调制技术，指定为以下之一：

- `SVM: space vector modulation`
- `SPWM: sinusoidal PWM`

## 所属库

Motor Control Blockset / Controls / Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2023b 中引入**

## 描述

使用磁场定向控制（FOC）技术实现三相电机的电流控制

Field-Oriented Current Controller 模块使用 FOC 算法实现三相永磁同步电机（PMSM）或交流感应电机（ACIM）的电流控制。您可以输入参考 *d* 轴和 *q* 轴电流、测量的定子 *a* 相和 *b* 相电流、电机电气位置以及 PI 控制器参数，以计算驱动电机的三相电压。

该模块使用 Clarke 和 Park 变换，根据测量的相电流和电机电气位置计算实际 *d* 轴和 *q* 轴电流。它使用 PI Controller 模块实现 *d* 轴和 *q* 轴电流控制器。电流控制器环路使用参考和实际 *d* 轴和 *q* 轴电流生成驱动电机的参考电压。有关该模块实现的 FOC 算法的更多信息，请参阅 Field-Oriented Control (FOC)。

该模块支持 SI 和 per-unit 输入，但所有模块输入的单位应相同。
