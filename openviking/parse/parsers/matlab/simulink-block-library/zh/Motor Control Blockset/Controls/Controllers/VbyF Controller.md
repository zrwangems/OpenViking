---
type: simulink-block
title: 'VbyF Controller'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'vbyfcontroller'
documentation_source_path: 'ref/vbyfcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# VbyF Controller

## 端口

### 输入

### **ωmref** — 参考速度标量

V/F 控制的参考机械速度。

**数据类型：** `single` | `double` | `fixed point`

### **ωmrated** — 电机额定速度标量

电机的额定机械速度。

**数据类型：** `single` | `double` | `fixed point`

### **Npp** — 电机极对数标量

三相电机中可用的极对数。

**数据类型：** `single` | `double` | `fixed point` | `uint` | `int`

### **Vrated** — 电机额定相电压幅值标量

对应于电机额定速度的电机额定相电压的幅值（峰值）。

**数据类型：** `single` | `double` | `fixed point`

### **Vmin** — 最小输出电压标量

应施加到电机的模块输出电压的最小幅值（峰值）。

**数据类型：** `single` | `double` | `fixed point`

### **NRamp** — 初始斜坡上升步数标量

用于电机速度初始斜坡上升的离散时间步数。

**数据类型：** `single` | `double` | `fixed point` | `uint` | `int`

### **Enable** — 使能模块输出标量

使能模块输出的信号：

- `1` — 使能模块输出。
- `0` — 复位内部积分器。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Vabc** — 电机相电压向量

驱动电机的定子相 *a*、*b* 和 *c* 电压。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Input speed unit** — 速度输入的单位 `Radians/Sec`（默认）| `RPM` | `Degrees/Sec` | `Per unit based on dialog`

**ωmref**
和 **ωmrated**
输入的单位。

选择 `Per unit based on dialog` 以对两个速度输入使用标幺制系统。有关标幺制系统的更多信息，请参阅 Per-Unit System。

### **Per unit speed (RPM)** — 电机的基准速度（RPM） `1200`（默认）| 标量

模块在标幺制计算中使用的电机额定速度（以 rpm 为单位）。有关标幺制系统的更多信息，请参阅 Per-Unit System。

#### 依赖关系

要启用此参数，请将 **Input speed unit** 设置为
`Per unit based on dialog`。

### **Discrete step size (s) (-1 for inherit)** — 模块再次执行前的采样时间 `50e-6`（默认）| 标量

模块两次连续执行实例之间的固定时间间隔（以秒为单位）。

## 所属库

Motor Control Blockset / Controls / Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

**限制**

如果指定 16 位定点输入，由于分辨率不足，模块可能无法产生准确的输出。

## 版本历史

**在 R2023b 中引入**

## 描述

实现三相电机的 V/F（开环或标量）控制

VbyF Controller 模块为三相永磁同步电机（PMSM）或交流感应电机（ACIM）实现 V/F（开环或标量）控制。

您可以指定参考转速、电机额定转速、电机极对数、电机额定电压、模块最小输出电压，以及初始斜坡上升的离散时间步数作为输入，以计算驱动电机的三相电压。

当您启动电机时，该模块使用 **NRamp** 输入来确定将电机转速逐渐斜坡上升至参考转速所需的模块采样数。

NRamp=TrampDiscrete step size (s)

模块的输出电压幅值根据参考电机转速（*ωref*）变化，同时保持额定电压与额定频率之比恒定。

Vabc\_amplitude=  (Vratedfrated)fref=(Vratedωrated)ωref

其中：

- *Vabc\_amplitude* 是输出电压 **Vabc** 的幅值。
- *Vrated* 是电机额定相电压的幅值。
- *frated* 是电机的额定频率。
- *fref* 是电机的参考频率。
- *ωrated* 是电机的额定转速。
- *ωref* 是电机的参考转速。

V/F 控制技术不需要来自电机的任何反馈。该控制技术通过保持电机相电压与其频率成正比来确保恒定的定子磁通。有关此技术的更多信息，请参阅 Open-Loop Motor Control。

**注意**

- 建议您使用此模块启动电机并在较低转速下运行，然后切换到其他控制方法（如磁场定向控制（FOC））以在较高转速下运行电机。
- 如果您指定 16 位定点输入，由于分辨率不足，模块可能无法产生准确的输出。
