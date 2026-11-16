---
type: simulink-block
title: 'ACIM Rs Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / ACIM Parameter Estimation'
documentation_page: 'acimrsestimator'
documentation_source_path: 'ref/acimrsestimator.html'
language: zh-CN
chinese_source: official
---

# ACIM Rs Estimator

## 端口

### 输入

### **Iabc** — 三相电流响应 标量

电流传感器测量的电机三相电流响应。

**注意**

提供 *c* 相电流输入是可选的。如果不提供 *c* 相电流输入，模块功能不会受到影响。

**数据类型:** `single`

### **Vdc** — DC 母线电压 标量

您提供给逆变器的 DC 总线电压。

**数据类型:** `single`

### **StartStop** — 用于 *Rs* 估计的控制信号 逻辑值

用于启动或停止 Rs 估计的信号：

- `1`（脉冲的上升沿）- 此信号会启动 *Rs* 估计过程。
- `0`（脉冲的下降沿）- 此信号会立即停止 *Rs* 估计过程。如果在估计过程完成前突然中断，该模块不会计算或输出 *Rs* 值。

**数据类型:** `Boolean`

### **Config** — 总线信号输入 总线

下表总结了总线信号输入中与我们预期相符的配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 电机和逆变器硬件元素 | 极对数 | | | - |
| 额定频率 | | | Hz |
| 标称电机电流 | | | A |
| 标称电压 | | | V |
| 最大可测量逆变器电流 | | | A |
| 板电阻 | | | 欧姆 |
| 电流感测增益 | | | A/ADC 计数 |
| 电压感测增益 | | | V/ADC 计数 |
| 用于估计磁化电流 *Id0* 的元素 | 测量时间 | | | 秒 |
| 开环斜坡时间 | | | 秒 |
| 用于估计电机电阻 (*Rs*) 的元素 | 估计时间 | | | 秒 |
| *Vd* 参考电压 1 | | | PU 电压 |
| *Vd* 参考电压 2 | | | PU 电压 |
| 用于估计转子电阻 (*Rr*)、磁化电感 (*Lm*)、定子泄漏电感 (*Lls*) 和转子泄漏电感 (*Llr*) 的元素 | 频率 1 (相对于额定频率的比率) | | | PU 频率 |
| 频率 2 (相对于额定频率的比率) | | | PU 频率 |
| *Lm* 的高频 | | | Hz |
| 电压扫描的起始电压 | | | PU 电压 |
| 电压扫描的电压阶跃 | | | PU 电压 |
| 高频注入电压 | | | PU 电压 |
| 用于估计电机惯量 (*J*) 和摩擦常量 (*B*) 的元素 | 闭环转速持续时间 | | | 秒 |
| 闭环转速 | | | RPM |
| FOC 的 *Iq* 参考电流 | | | PU 电流 |
| 比例增益 | | | - |
| 积分增益 | | | - |
| 惯量估计的转速下限 | | | RPM |
| - | 参数估计采样时间 | | | 秒 |

您可以将此输入端口连接到 ACIM Parameter Estimation Configurator 模块的 `Config` 输出端口。

**数据类型:** `single`
### 输出

### **Vabc** — *a*、*b* 和 *c* 轴定子参考电压分量 标量

沿 *abc* 参考系的 *a*、*b* 和 *c* 轴的定子参考电压分量。

**数据类型:** `single`

### **Rs** — 估计定子电阻 标量

估计的感应电机的定子电阻（以 ohm 为单位）。

**数据类型:** `single`

### **Log** — 调试信号 总线

模块提供的用于检查的调试信号。总线包括以下调试信号。

| 调试信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| *Id* | | | *D* 轴电流 | 安培 |
| *Vd* | | | *D* 轴电压 | 伏特 |
| *status* | | `0` | 未完成 *Rs* 估计 | - |
| `1` | *Rs* 估计已成功完成 | - |

**数据类型:** `single`

## 参数

R2025b 官方文档未提供。

## 所属库

Motor Control Blockset / Parameter Estimation / ACIM Parameter Estimation

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2023a 中推出**

## 描述

估计 AC 感应电机 (ACIM) 的定子电阻 ( R s )

ACIM Rs Estimator 模块使用相电流、穿过电机的 DC 电压和测试配置元素来估计感应电机的定子电阻。

该模块在电机各个相位之间注入电压，并测量电流响应以估计电机电阻。
