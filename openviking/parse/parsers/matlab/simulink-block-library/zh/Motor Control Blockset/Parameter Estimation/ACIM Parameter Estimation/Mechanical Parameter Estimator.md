---
type: simulink-block
title: 'ACIM Mechanical Parameter Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / ACIM Parameter Estimation'
documentation_page: 'acimmechanicalparameterestimator'
documentation_source_path: 'ref/acimmechanicalparameterestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# ACIM Mechanical Parameter Estimator

## 端口

### 输入

### **Iabc** — 三相电流响应标量

由电流传感器测量的电机三相电流响应。

**注意**

提供相位-*c* 电流输入是可选的。如果不提供相位-*c* 电流输入，模块功能不受影响。

**数据类型：** `single`

### **Vdc** — 直流母线电压标量

您提供给逆变器的直流母线电压。

**数据类型：** `single`

### **Speed** — 转子速度标量

当前电机速度。

**数据类型：** `single`

### **Id0** — 估计的励磁电流标量

感应电机的估计励磁电流。您可以将此输入端口连接到 Id0 Estimator 模块的 `Id0` 输出，或者使用 Constant 模块手动提供励磁电流值。

**数据类型：** `single`

### **Rtotal** — 定子和逆变器板电阻之和标量

估计的定子电阻 *Rs* 与逆变器板电阻之和。您可以通过利用 ACIM Rs Estimator 模块的 `Rs` 输出提供此输入，或者使用 Constant 模块手动提供此值。

**数据类型：** `single`

### **Rr** — 估计的转子电阻标量

感应电机的估计转子电阻。您可以将此输入端口连接到 RrL Estimator 模块的 `Rr` 输出，或者使用 Constant 模块手动提供转子电阻值。

**数据类型：** `single`

### **Lm** — 估计的励磁电感标量

感应电机的估计励磁电感。您可以将此输入端口连接到 RrL Estimator 模块的 `Lm` 输出，或者使用 Constant 模块手动提供励磁电感值。

**数据类型：** `single`

### **Lls** — 估计的定子漏电感标量

感应电机的估计定子漏电感。您可以将此输入端口连接到 RrL Estimator 模块的 `Lls` 输出，或者使用 Constant 模块手动提供定子漏电感值。

**数据类型：** `single`

### **StartStop** — 机械参数估计的控制信号 逻辑

启动或停止模块执行的信号：

- `1`（脉冲的上升沿）— 此信号启动模块执行。
- `0`（脉冲的下降沿）— 此信号立即停止模块执行以及模块正在运行的任何测试。如果您在完成之前突然中断估计过程，模块不会计算或输出机械参数值。

**数据类型：** `Boolean`

### **Config** — 总线信号输入总线

此表汇总了总线信号输入中预期的配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 电机和逆变器硬件元素 | 极对数 | | | - |
| 额定频率 | | | Hz |
| 标称电机电流 | | | A |
| 标称电压 | | | V |
| 最大可测量逆变器电流 | | | A |
| 板电阻 | | | ohm |
| 电流检测增益 | | | A/ADC Count |
| 电压检测增益 | | | V/ADC Count |
| 用于估计励磁电流 *Id0* 的元素 | 测量时间 | | | seconds |
| 开环斜坡时间 | | | seconds |
| 用于估计电机电阻 (*Rs*) 的元素 | 估计时间 | | | seconds |
| *Vd* 参考电压 1 | | | PU voltage |
| *Vd* 参考电压 2 | | | PU voltage |
| 用于估计转子电阻 (*Rr*)、励磁电感 (*Lm*)、定子漏电感 (*Lls*) 和转子漏电感 (*Llr*) 的元素 | 频率 1 与额定频率之比 | | | PU frequency |
| 频率 2 与额定频率之比 | | | PU frequency |
| 用于 *Lm* 的高频 | | | Hz |
| 电压扫描起始电压 | | | PU voltage |
| 电压扫描电压步长 | | | PU voltage |
| 高频注入电压 | | | PU voltage |
| 用于估计电机惯量 (*J*) 和摩擦常数 (*B*) 的元素 | 闭环速度持续时间 | | | seconds |
| 闭环速度 | | | RPM |
| 用于 FOC 的 *Iq* 参考电流 | | | PU current |
| 比例增益 | | | - |
| 积分增益 | | | - |
| 惯量估计的速度下限 | | | RPM |
| - | 参数估计采样时间 | | | seconds |

您可以将此输入端口连接到 ACIM Parameter Estimation Configurator 模块的 `Config` 输出端口。

**数据类型：** `single`
### 输出

### **Vabc** — *a*、*b* 和 *c* 轴定子参考电压分量标量

沿 *abc* 参考系的 *a*、*b* 和 *c* 轴的定子参考电压分量。

**数据类型：** `single`

### **J** — 估计的转子惯量标量

感应电机的估计惯量（单位：kg.m2）。

**数据类型：** `single`

### **B** — 估计的粘性阻尼标量

感应电机的估计粘性阻尼（单位：N.s/m）。

**数据类型：** `single`

### **InverterEn** — 逆变器控制信号逻辑

开启或关闭逆变器的信号：

- `1`（逻辑高电平）— 在此信号为高电平的持续时间内，逆变器的所有六个开关均开启。
- `0`（逻辑低电平）— 在此信号为低电平的持续时间内，逆变器的所有六个开关均关闭。

**数据类型：** `single`

### **Log** — 调试信号总线

模块提供的用于检查的调试信号。该总线包含以下调试信号。

| 调试信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| *status* | | `0` | 未完成机械参数估计 | - |
| `1` | 机械参数估计成功完成 | - |
| *CoastDownTime* | | | 测得的滑行持续时间 | seconds |
| *Vdq* | | | *d* 轴和 *q* 轴电压 | Volts |
| *Idq* | | | *d* 轴和 *q* 轴电流 | Amperes |
| *VIAlphaBeta* | | | *α* 轴和 *β* 轴电压和电流 | Volts, Amperes |
| *SlipPU* | | | 电机闭环运行期间的转差（以标幺值表示） | - |

**数据类型：** `single`

## 参数

R2025b 中未记录。

## 所属库

Motor Control Blockset / Parameter Estimation / ACIM Parameter Estimation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

估计交流感应电机（ACIM）的转子惯量和粘性阻尼

ACIM 机械参数估计器模块使用相电流和电压、电机两端的直流电压、电机转速、励磁电流、转子和完整电机电阻、励磁电感和定子漏电感，以及其他测试配置元素来计算感应电机的以下机械参数：

- 转子惯量（*J*）
- 粘性阻尼（*B*）

该模块使用有限转速下的闭环磁场定向控制（FOC）运行电机。在运行电机的同时，该模块还运行测试以估计粘性阻尼（*B*）。在预配置的持续时间之后，该模块结束这些测试以计算 *B*，然后通过关闭所有六个逆变器开关触发惯性滑行。惯性滑行导致电机转速逐渐下降，最终达到零。该模块测量电机达到零转速所需的时间，并使用它来计算转子惯量（*J*）。
