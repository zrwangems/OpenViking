---
type: simulink-block
title: 'Field-Oriented Current Controller'
family: 'mcb'
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
```yaml
ports:
- name: IdqRef
  summary: 参考 *d* 轴和 *q* 轴电流向量
  direction: input
  data_types: single | double | fixed point
- name: IabMeas
  summary: 测量的 *a* 相和 *b* 相电流向量
  direction: input
  data_types: single | double | fixed point
- name: θe
  summary: 电机电角度位置标量
  direction: input
  data_types: single | double | fixed point
- name: VSatLim
  summary: '*d-q* 电压饱和限值标量'
  direction: input
  data_types: single | double | fixed point
- name: Kp,Ki\*Ts
  summary: '*d* 轴和 *q* 轴 PI 控制器增益向量'
  direction: input
  data_types: single | double | fixed point
- name: PIConfig
  summary: PI 控制器输出的初始值和限值向量
  direction: input
  data_types: single | double | fixed point
- name: Enable
  summary: 复位模块标量
  direction: input
  data_types: single | double | fixed point
- name: Vabc
  summary: 电机相电压向量
  direction: output
  data_types: single | double | fixed point
- name: Debug
  summary: 调试信号向量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **IdqRef** — 参考 *d* 轴和 *q* 轴电流向量

旋转 *d-q* 参考坐标系中沿 *d* 轴和 *q* 轴的参考电机电流。

`IdqRef = [IdRef,
IqRef]`

**数据类型：** `single` | `double` | `fixed point`

### **IabMeas** — 测量的 *a* 相和 *b* 相电流向量

电机的测量 *a* 相和 *b* 相电流。

`IabMeas = [IaMeas,
IbMeas]`

**数据类型：** `single` | `double` | `fixed point`

### **θe** — 电机电角度位置标量

电机的电角度位置。

**数据类型：** `single` | `double` | `fixed point`

### **VSatLim** — *d-q* 电压饱和限值标量

由内部 PI 控制器生成的 *d* 轴和 *q* 轴参考电压的饱和限值。该值取决于直流母线电压（*Vdc*）和所选的 PWM 方法。通常，该值等于 *Vdc/2*（对于 SPWM）和 *Vdc/sqrt(3)*（对于 SVM）。有关 PWM 技术的更多信息，请参阅 PWM Reference Generator。

**数据类型：** `single` | `double` | `fixed point`

### **Kp,Ki\*Ts** — *d* 轴和 *q* 轴 PI 控制器增益向量

*d* 轴和 *q* 轴 PI 控制器的增益（分别为 *Kp* 和 *Ki*），与模块采样时间（*Ts*）复用。

`Kp,Ki*Ts
= [Kp(d-axis),
Ki*Ts(d-axis),
Kp(d-axis),
Ki*Ts(d-axis)]`

**数据类型：** `single` | `double` | `fixed point`

### **PIConfig** — PI 控制器输出的初始值和限值向量

内部 PI 控制器积分器的初始值与其限值的复用。

PIConfig = [PI 控制器积分器饱和上限，PI 控制器积分器饱和下限，*d* 轴 PI 控制器积分器初始值，*q* 轴 PI 控制器积分器初始值]

**数据类型：** `single` | `double` | `fixed point`

### **Enable** — 复位模块标量

复位模块中使用的 PI 控制器的信号：

- `1` — 复位内部 PI 控制器。
- `0` — 不执行操作。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Vabc** — 电机相电压向量

驱动电机的定子 *a* 相、*b* 相和 *c* 相电压。

**数据类型：** `single` | `double` | `fixed point`

### **Debug** — 调试信号向量

模块为调试目的捕获的内部计算复用信号。该复用信号由以下元素组成：

- *Idq* — 根据电机相电流计算的实际 *d* 轴和 *q* 轴电机电流。
- *Vdq* — 由内部 *d* 轴和 *q* 轴电流 PI 控制器计算的 *d* 轴和 *q* 轴电机电压。
- *Vαβ* — 模块内部使用 *Vdq* 的逆 Park 变换计算的 *α* 轴和 *β* 轴电压。
- *Iαβ* — 模块内部使用 **IabMeas** 输入的 Clarke 变换计算的 *α* 轴和 *β* 轴电流。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Input electrical position unit
  summary: 电角度位置输入的单位 Radians（默认）| Degrees | Per-unit
  group: ''
- name: Number of data points for sine-cosine lookup table
  summary: 查找表数组的大小 1024（默认）| [125, 4095] 范围内的标量
  group: ''
- name: Alpha (phase-a) axis alignment
  summary: '*dq* 参考坐标系对齐 D-axis（默认）| Q-axis'
  group: ''
- name: Saturation method
  summary: 模块使用的饱和方法 D-Q equivalence（默认）| Prioritize D axis | Prioritize Q axis
  group: ''
- name: PWM 方法
  summary: '调制技术 SVM: space vector modulation（默认）| SPWM: sinusoidal PWM'
  group: ''
```

### **Input electrical position unit** — 电角度位置输入的单位 `Radians`（默认）| `Degrees` | `Per-unit`

电机电角度位置输入 **θe** 的单位。

### **Number of data points for sine-cosine lookup table** — 查找表数组的大小 `1024`（默认）| [125, 4095] 范围内的标量

内部正弦-余弦查找算法使用的查找表数组的大小，该算法计算电机电角度位置的正弦和余弦。此参数接受 [125, 4095] 范围内的值。

### **Alpha (phase-a) axis alignment** — *dq* 参考坐标系对齐 `D-axis`（默认）| `Q-axis`

将旋转参考坐标系的 *d* 轴或 *q* 轴与静止参考坐标系的 *α* 轴对齐。

### **Saturation method** — 模块使用的饱和方法 `D-Q equivalence`（默认）| `Prioritize D axis` | `Prioritize Q axis`

将饱和方法设置为以下之一：

- `D-Q equivalence`
- `Prioritize D axis`
- `Prioritize Q axis`

### **PWM 方法** — 调制技术 `SVM: space vector modulation`（默认）| `SPWM: sinusoidal PWM`

该模块输出的三相电压的脉宽调制技术，指定为以下之一：

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

Field-Oriented Current Controller 模块使用 FOC 算法实现三相永磁同步电机（PMSM）或交流感应电机（ACIM）的电流控制。您可以输入参考 *d* 轴和 *q* 轴电流、测量的定子 *a* 相和 *b* 相电流、电机电角度位置以及 PI 控制器参数，以计算驱动电机的三相电压。

该模块使用 Clarke 和 Park 变换，根据测量的相电流和电机电角度位置计算实际的 *d* 轴和 *q* 轴电流。它使用 PI Controller 模块实现 *d* 轴和 *q* 轴电流控制器。电流控制环路使用参考和实际的 *d* 轴和 *q* 轴电流生成驱动电机的参考电压。有关该模块实现的 FOC 算法的更多信息，请参阅 Field-Oriented Control (FOC)。

该模块支持 SI 和标幺值输入，但所有模块输入的单位应相同。
