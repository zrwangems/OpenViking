---
type: simulink-block
title: 'Id0 Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / ACIM Parameter Estimation'
documentation_page: 'id0estimator'
documentation_source_path: 'ref/id0estimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Id0 Estimator

## 端口

### 输入

### **Iabc** — 三相电流响应 标量

由电流传感器测量的电机三相电流响应。

**注意**

提供相位-*c* 电流输入是可选的。如果不提供相位-*c* 电流输入，模块功能不受影响。

**数据类型：** `single`

### **StartStop** — *Id0* 估计的控制信号 逻辑

启动或停止 Id0 估计的信号：

- `1`（脉冲上升沿）— 此信号启动 *Id0* 估计。
- `0`（脉冲下降沿）— 此信号立即停止 *Id0* 估计过程。如果在完成之前突然中断估计过程，模块不会计算或输出 *Id0* 值。

**数据类型：** `Boolean`

### **Config** — 总线信号输入 总线

此表总结了总线信号输入中预期的配置元素。

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
| 用于估计电机电阻（*Rs*）的元素 | 估计时间 | | | seconds |
| *Vd* 参考电压 1 | | | PU voltage |
| *Vd* 参考电压 2 | | | PU voltage |
| 用于估计转子电阻（*Rr*）、励磁电感（*Lm*）、定子漏电感（*Lls*）和转子漏电感（*Llr*）的元素 | 频率 1 与额定频率之比 | | | PU frequency |
| 频率 2 与额定频率之比 | | | PU frequency |
| 用于 *Lm* 的高频 | | | Hz |
| 电压扫描的起始电压 | | | PU voltage |
| 电压扫描的电压步长 | | | PU voltage |
| 高频注入电压 | | | PU voltage |
| 用于估计电机惯量（*J*）和摩擦常数（*B*）的元素 | 闭环速度持续时间 | | | seconds |
| 闭环速度 | | | RPM |
| 用于 FOC 的 *Iq* 参考电流 | | | PU current |
| 比例增益 | | | - |
| 积分增益 | | | - |
| 惯量估计的速度下限 | | | RPM |
| - | 参数估计采样时间 | | | seconds |

您可以将此输入端口连接到 ACIM Parameter Estimation Configurator 模块的 `Config` 输出端口。

**数据类型：** `single`
### 输出

### **Vabc** — *a*、*b* 和 *c* 轴定子参考电压分量 标量

沿 *abc* 参考坐标系的 *a*、*b* 和 *c* 轴的定子参考电压分量。

**数据类型：** `single`

### **Id0** — 估计的励磁电流 标量

估计的励磁电流（以安培为单位）。

**数据类型：** `single`

### **Log** — 调试信号 总线

模块提供的用于检查的调试信号。总线包含这些调试信号。

| 调试信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| *Id* | | | *D* 轴电流 | Amperes |
| *status* | | `0` | 未完成 *Id0* | - |
| `1` | *Id0* 估计成功完成 | - |

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

估算交流感应电机（ACIM）的励磁电流（I d0）

Id0 Estimator 模块使用相电流和测试配置元素来计算感应电机的励磁电流。

该模块在开环控制下运行感应电机，在此期间，它测量峰值电流响应值并在给定时段内对其求平均。此外，该模块测量电机从零达到额定频率 90% 所需的时间。它使用该持续时间以及计算出的平均电流来估算感应电机的励磁电流。
