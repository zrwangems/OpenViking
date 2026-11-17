---
type: simulink-block
title: 'Lq Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / PMSM Parameter Estimation'
documentation_page: 'lqestimator'
documentation_source_path: 'ref/lqestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# Lq Estimator

## 端口
```yaml
ports:
- name: Iabc
  summary: 三相电流响应向量
  direction: input
  data_types: single
- name: Rs
  summary: 估算的定子电阻标量
  direction: input
  data_types: single
- name: StartStop
  summary: '*Lq* 估算的逻辑控制信号'
  direction: input
  data_types: Boolean
- name: Config
  summary: 总线信号输入总线
  direction: input
  data_types: single
- name: Vabc
  summary: '*a*、*b* 和 *c* 轴定子参考电压分量向量'
  direction: output
  data_types: single
- name: Lq
  summary: 估算的 *q* 轴定子电感标量
  direction: output
  data_types: single
- name: Log
  summary: 调试信号总线
  direction: output
  data_types: single
```

### 输入

### **Iabc** — 三相电流响应向量

由电流传感器测量的电机三相电流响应（单位为安培）。

**注意**

提供 phase-*c* 电流输入是可选的。如果不提供 phase-*c* 电流输入，模块功能不会受到影响。

**数据类型：** `single`

### **Rs** — 估算的定子电阻标量

PMSM 的估算定子电阻（单位为欧姆）。您可以将此输入端口连接到 PMSM Rs Estimator 模块的 `Rs` 输出，也可以使用 Constant 模块手动提供电阻值。

**数据类型：** `single`

### **StartStop** — *Lq* 估算的逻辑控制信号

启动或停止 *Lq* 估算的信号：

- `1`（脉冲上升沿）— 此信号启动 *Lq* 估算。
- `0`（脉冲下降沿）— 此信号立即停止 *Lq* 估算过程。如果您在完成之前突然中断估算过程，模块不会计算或输出 *Lq* 值。

**数据类型：** `Boolean`

### **Config** — 总线信号输入总线

此表总结了总线信号输入中预期的配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 电机和逆变器硬件元素 | 极对数 | | | - |
| 电机额定转速 | | | RPM |
| 电机额定电流 | | | A |
| 逆变器最大可测电流 | | | A |
| 板电阻 | | | ohms |
| 电流检测增益 | | | A/ADC Count |
| 电压检测增益 | | | V/ADC Count |
| 参数估算采样时间 | | | seconds |
| 用于估算电机电感（*Ld* 和 *Lq*）的元素 | 最大频率 | | | Hz |
| 最小频率 | | | Hz |
| 频率扫描步长 | | | Hz |
| 估算的频率步长 | | | Hz |
| 估算的频率数量 | | | - |
| 用于估算反电动势常数（*Ke*）、电机惯量（*J*）和摩擦常数（*B*）的元素 | 反电动势估算时间 | | | seconds |
| 反电动势估算最大速度限制 | | | RPM |
| 指定电流控制器增益（off/on） | | | - |
| 比例增益 | | | - |
| 积分增益 | | | - |
| *Iq* 参考电流与电机额定电流的比值 | | | PU current |
| 惯量估算的下限速度限制 | | | RPM |

您可以将此输入端口连接到 PMSM Parameter Estimation Configurator 模块的 `Config` 输出端口。

**数据类型：** `single`
### 输出

### **Vabc** — *a*、*b* 和 *c* 轴定子参考电压分量向量

沿 *abc* 参考坐标系的 *a*、*b* 和 *c* 轴的定子参考电压分量。每个电压分量的范围在 `-1` 到 `1` 之间。

**数据类型：** `single`

### **Lq** — 估算的 *q* 轴定子电感标量

估算的 *q* 轴定子电感（单位为亨利）。

**数据类型：** `single`

### **Log** — 调试信号总线

模块提供的用于检查的调试信号。该总线包含以下调试信号。

| 调试信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| *InjFreq* | | | 最近注入信号的频率 | Hz |
| *status* | | `0` | *Lq* 估计尚未开始。 | - |
| `1` | *Lq* 估计正在进行中。 | - |
| `2` | *Lq* 估计已成功完成。 | - |
| `8200` | *Lq* 估计失败，因为来自电机的电流反馈未随注入电压的上升而成比例增加。请检查电机连接，并确保 ADC 正确测量 *Ia* 和 *Ib*。 | - |
| `8201` | 估计的 *Lq* 为负值，因为相位差大于 `90°`。请检查日志输出中的相位差，并根据需要调整注入频率范围。确保在 PMSM Parameter Estimation Configurator 模块中准确配置了 **Current measurement delay** 参数，并尝试提高 PWM 频率。 | - |
| *Iq* | | | *Q* 轴电流 | A |
| *Vq* | | | *Q* 轴电压 | V |
| *PhaseDiff\_rad* | | | 注入电压与电流响应之间的相位差 | radians |

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Maximum current limit (A)
  summary: 测试期间允许的最大电流 15（默认值）| scalar
  group: ''
- name: Step size during injected voltage ramp up (per-unit)
  summary: 注入电压斜坡上升期间的步长 0.0001（默认值）| scalar
  group: ''
- name: Number of sinusoidal voltage injections per frequency sweep step
  summary: 频率扫描期间每个频率的正弦电压注入次数 5（默认值）| scalar
  group: ''
- name: Number of sinusoidal voltage injections per frequency during Lq estimation
  summary: Lq 估计期间每个频率的正弦电压注入次数 5（默认值）| scalar
  group: ''
```

### **Maximum current limit (A)** — 测试期间允许的最大电流 `15`（默认值）| `scalar`

测试期间允许的最大电流（以安培为单位）。

### **Step size during injected voltage ramp up (per-unit)** — 注入电压斜坡上升期间的步长 `0.0001`（默认值）| `scalar`

注入电压斜坡上升期间的步长（以标幺值表示）。

### **Number of sinusoidal voltage injections per frequency sweep step** — 频率扫描期间每个频率的正弦电压注入次数 `5`（默认值）| `scalar`

每个频率扫描步长中每个频率的正弦电压注入次数。

### **Number of sinusoidal voltage injections per frequency during Lq estimation** — Lq 估计期间每个频率的正弦电压注入次数 `5`（默认值）| `scalar`

每个 Lq 估计步长中每个频率的正弦电压注入次数。
## 所属库

Motor Control Blockset / Parameter Estimation / PMSM Parameter Estimation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a：新增模块参数

模块参数对话框现在包含用于配置参数估计过程的高级选项。

## 描述

估计永磁同步电机（PMSM）的定子电感（ L q ）

Lq Estimator 模块使用相电流、定子电阻和测试配置元素来计算 PMSM 的 *q* 轴定子电感。

首先，该模块通过注入恒定电压（*Vd*）将转子锁定在 *d* 轴方向。这确保在频率注入期间转子保持静止（与 *d* 轴对齐）。为了估计 *q* 轴定子电感，该模块沿 *q* 轴注入高频电压信号，然后通过使用 **Step for frequency sweep (Hz)** 参数定义的步长逐渐降低注入信号频率来执行频率扫描过程。在频率扫描期间，该模块监测电机相电流的幅值。当注入信号频率达到最小值（**Minimum frequency (Hz)** 参数）时，该模块通过注入频率上升的信号来启动估计过程，其步长为 **Frequency step size for estimation (Hz)**，步数由 **Number of frequencies for estimation** 参数定义。有关这些参数的详细信息，请参阅 PMSM Parameter Estimation Configurator。

此图显示了频率扫描和频率上升的增量步进。

*Lq* 估计过程使用测得的频率扫描持续时间以及变化频率的步长来估计 *q* 轴定子电感 *Lq*。
