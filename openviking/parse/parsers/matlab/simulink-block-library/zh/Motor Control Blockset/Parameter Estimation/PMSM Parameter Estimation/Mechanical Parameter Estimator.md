---
type: simulink-block
title: 'PMSM Mechanical Parameter Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / PMSM Parameter Estimation'
documentation_page: 'pmsmmechanicalparameterestimator'
documentation_source_path: 'ref/pmsmmechanicalparameterestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Mechanical Parameter Estimator

## 端口
```yaml
ports:
- name: Iabc
  summary: 三相电流响应向量
  direction: input
  data_types: single
- name: Vdc
  summary: 直流母线电压标量
  direction: input
  data_types: single
- name: Theta
  summary: 转子位置标量
  direction: input
  data_types: single
- name: Speed
  summary: 转子速度标量
  direction: input
  data_types: single
- name: Rs
  summary: 估计的定子电阻标量
  direction: input
  data_types: single
- name: Ld
  summary: 估计的 *d* 轴定子电感标量
  direction: input
  data_types: single
- name: StartFOC
  summary: 启动闭环 FOC 逻辑
  direction: input
  data_types: single
- name: StartStop
  summary: 机械参数估计的控制信号逻辑
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
- name: Ke
  summary: 估计的反电动势常数标量
  direction: output
  data_types: single
- name: J
  summary: 估计的转子惯量标量
  direction: output
  data_types: single
- name: B
  summary: 估计的粘性阻尼标量
  direction: output
  data_types: single
- name: InverterEn
  summary: 逆变器控制信号 逻辑
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

提供相位-*c* 电流输入是可选的。如果您不提供相位-*c* 电流输入，模块功能不会受到影响。

**数据类型：** `single`

### **Vdc** — 直流母线电压标量

您提供给逆变器的直流母线电压（单位为伏特）。

**数据类型：** `single`

### **Theta** — 转子位置标量

转子的当前位置（单位为标幺值）。有关标幺值系统的更多详细信息，请参阅标幺值系统。

**数据类型：** `single`

### **Speed** — 转子速度标量

当前电机速度（单位为 RPM）。

**数据类型：** `single`

### **Rs** — 估计的定子电阻标量

PMSM 的估计定子电阻（单位为欧姆）。您可以将此输入端口连接到 PMSM Rs Estimator 模块的 `Rs` 输出，或者使用 Constant 模块手动提供电阻值。

**数据类型：** `single`

### **Ld** — 估计的 *d* 轴定子电感标量

PMSM 的估计 *d* 轴定子电感（单位为亨利）。您可以将此输入端口连接到 Ld Estimator 模块的 `Ld` 输出，或者使用 Constant 模块手动提供 *d* 轴电感值。

**数据类型：** `single`

### **StartFOC** — 启动闭环 FOC 逻辑

启动电机以闭环 FOC 模式运行的信号：

- `1`（脉冲上升沿）— 此信号通过使用 FOC 以闭环方式运行电机来启动机械参数估计。
- `0`（脉冲下降沿）— 此信号开始使用开环控制运行电机。

**数据类型：** `single`

### **StartStop** — 机械参数估计的控制信号逻辑

启动或停止模块执行的信号：

- `1`（脉冲上升沿）— 此信号启动模块执行。
- `0`（脉冲下降沿）— 此信号立即停止模块执行以及模块正在运行的任何测试。如果您在完成之前突然中断估计过程，模块不会计算或输出机械参数值。

**数据类型：** `Boolean`

### **Config** — 总线信号输入总线

此表总结了总线信号输入中预期的配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 电机和逆变器硬件元素 | 极对数 | | | - |
| 电机额定速度 | | | RPM |
| 电机额定电流 | | | A |
| 最大可测量逆变器电流 | | | A |
| 板电阻 | | | ohms |
| 电流检测增益 | | | A/ADC Count |
| 电压检测增益 | | | V/ADC Count |
| 参数估计采样时间 | | | seconds |
| 用于估计电机电感（*Ld* 和 *Lq*）的元素 | 最大频率 | | | Hz |
| 最小频率 | | | Hz |
| 频率扫描步长 | | | Hz |
| 估计的频率步长 | | | Hz |
| 估计的频率数量 | | | - |
| 用于估计反电动势常数（*Ke*）、电机惯量（*J*）和摩擦常数（*B*）的元素 | 反电动势估计时间 | | | seconds |
| 反电动势估计最大速度限制 | | | RPM |
| 指定电流控制器增益（off/on） | | | - |
| 比例增益 | | | - |
| 积分增益 | | | - |
| *Iq* 参考电流与电机额定电流的比值 | | | PU current |
| 惯量估计的下限速度限制 | | | RPM |

您可以将此输入端口连接到 PMSM Parameter Estimation Configurator 模块的 `Config` 输出端口。

**数据类型：** `single`
### 输出

### **Vabc** — *a*、*b* 和 *c* 轴定子参考电压分量向量

定子参考电压分量沿 *abc* 参考系的 *a*、*b* 和 *c* 轴。每个电压分量的范围在 `-1` 和 `1` 之间。

**数据类型：** `single`

### **Ke** — 估计的反电动势常数标量

PMSM 的估计反电动势常数（单位：V/m/s）。

**数据类型：** `single`

### **J** — 估计的转子惯量标量

PMSM 的估计惯量（单位：kg.m2）。

**数据类型：** `single`

### **B** — 估计的粘性阻尼标量

PMSM 的估计粘性阻尼（单位：N.s/m）。

**数据类型：** `single`

### **InverterEn** — 逆变器控制信号 逻辑

用于开启或关闭逆变器的信号：

- `1`（逻辑高电平）— 在该信号为高电平期间，逆变器的所有六个开关均导通。
- `0`（逻辑低电平）— 在该信号为低电平期间，逆变器的所有六个开关均关断。

**数据类型：** `single`

### **Log** — 调试信号总线

模块提供的用于检查的调试信号。该总线包含以下调试信号。

| 调试信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| *status* | | `0` | 机械参数估计尚未开始。 | - |
| `1` | 机械参数估计正在进行中。 | - |
| `2` | 机械参数估计已成功完成。 | - |
| `8300` | 反电动势估计失败，因为电机未能在 **Back EMF estimation time (s)**+10 秒的时间内达到 **Back EMF estimation maximum speed limit (RPM)** 的 90%。有关 **Back EMF estimation maximum speed limit (RPM)** 和 **Back EMF estimation time (s)** 参数的更多详细信息，请参阅 PMSM Parameter Estimation Configurator。 | - |
| *CoastDownTime* | | | 测得的惯性滑行持续时间 | 秒 |
| *Vdq* | | | *d* 轴和 *q* 轴电压 | 伏特 |
| *Idq* | | | *d* 轴和 *q* 轴电流 | 安培 |
| *VIAlphaBeta* | | | *α* 轴和 *β* 轴电压和电流 | 伏特，安培 |

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Slowdown factor for current PI controller gains [1,20]
  summary: 估计反电动势时电流 PI 控制器的减速因子 5（默认）| scalar
  group: ''
```

### **Slowdown factor for current PI controller gains [1,20]** — 估计反电动势时电流 PI 控制器的减速因子 `5`（默认）| `scalar`

反电动势估计期间电流 PI 控制器的减速因子（指定为 `1` 到 `20` 之间的整数）。较小的值会导致控制器更激进。
## 所属库

Motor Control Blockset / Parameter Estimation / PMSM Parameter Estimation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a：新增模块参数

“模块参数”对话框现在包含用于配置参数估计过程的高级选项。

## 描述

估计永磁同步电机（PMSM）的反电动势常数、转子惯量和粘性阻尼

PMSM Mechanical Parameter Estimator 模块使用相电流和电压、电机两端的直流电压、电机位置和速度、定子电阻、*d* 轴电感以及其他测试配置元素来计算 PMSM 的以下机械参数：

- 反电动势常数（*Ke*）
- 转子惯量（*J*）
- 粘性阻尼（*B*）

该模块以有限速度运行电机的闭环磁场定向控制（FOC），在此期间运行测试以估计反电动势常数（*Ke*）和粘性阻尼（*B*）。在预配置的持续时间之后，模块结束这些测试以计算 *Ke* 和 *B*，然后通过关断所有六个逆变器开关触发惯性滑行。惯性滑行导致电机速度逐渐下降，最终达到零。模块测量并利用达到零速度的时间来计算转子惯量（*J*）。
