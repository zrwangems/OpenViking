---
type: simulink-block
title: 'PMSM Rs Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Parameter Estimation / PMSM Parameter Estimation'
documentation_page: 'pmsmrsestimator'
documentation_source_path: 'ref/pmsmrsestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Rs Estimator

## 端口

### 输入

### **Iabc** — 三相电流响应矢量

由电流传感器测量的电机三相电流响应（单位为安培）。

**注意**

提供相 *c* 电流输入是可选的。如果不提供相 *c* 电流输入，模块功能不受影响。

**数据类型：** `single`

### **Vdc** — 直流母线电压标量

您提供给逆变器的直流母线电压（单位为伏特）。

**数据类型：** `single`

### **StartStop** — *Rs* 估计逻辑的控制信号

启动或停止 *Rs* 估计的信号：

- `1`（脉冲上升沿）— 此信号启动 *Rs* 估计过程。
- `0`（脉冲下降沿）— 此信号立即停止 *Rs* 估计过程。如果您在完成之前突然中断估计过程，模块不会计算或输出 *Rs* 值。

**数据类型：** `Boolean`

### **Config** — 总线信号输入总线

下表总结了总线信号输入中预期的配置元素。

| 类别 | 配置元素 | | | 单位 |
| --- | --- | --- | --- | --- |
| 电机和逆变器硬件元素 | 极对数 | | | - |
| 电机额定转速 | | | RPM |
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

### **Vabc** — *a*、*b* 和 *c* 轴定子参考电压分量矢量

沿 *abc* 参考坐标系的 *a*、*b* 和 *c* 轴的定子参考电压分量。每个电压分量的范围在 `-1` 和 `1` 之间。

**数据类型：** `single`

### **Rs** — 估计的定子电阻标量

PMSM 的估计定子电阻（单位为欧姆）。

**数据类型：** `single`

### **Log** — 调试信号总线

模块提供的用于检查的调试信号。该总线包含以下调试信号。

| 调试信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| *I1* | | | 第一次测量的相电流 | A |
| *V1* | | | 第一次注入的相电压 | V |
| *I2* | | | 第二次测量的相电流 | A |
| *V2* | | | 第二次注入的相电压 | V |
| *Rs1* | | | 估算的 *a* 轴电阻 | ohms |
| *Rs2* | | | 估算的 *b* 轴电阻 | ohms |
| *Rs3* | | | 估算的 *c* 轴电阻 | ohms |
| *status* | | `0` | *Rs* 估算尚未开始。 | - |
| `1` | *Rs* 估算正在进行中。 | - |
| `2` | *Rs* 估算成功完成。 | - |
| `8000` | *Rs* 估算失败，原因是来自电机的电流反馈未随注入电压的上升而成比例增加。观察日志输出中的所有三个相电阻，如果它们处于可接受范围内，则增大模块掩码中的阈值以容纳电阻不平衡。 | - |
| `8001` | *Rs1* 估算失败，原因是 *Ia* 相电流存在问题。检查电机是否正确连接，以及 ADC 是否正确测量 *Ia*。 | - |
| `8002` | *Rs2* 估算失败，原因是 *Ib* 相电流存在问题。检查电机是否正确连接，以及 ADC 是否正确测量 *Ib*。 | - |
| `8003` | *Rs3* 估算失败，原因是 *Ic* 相电流存在问题。检查电机是否正确连接，以及 ADC 是否正确测量 *Ic*。 | - |

**数据类型：** `single`

## 参数

### **Maximum current limit (A)** — 测试期间允许的最大电流 `15`（默认）| `scalar`

测试期间允许的最大电流（以安培为单位）。

### **Step size during injected voltage ramp up (per-unit)** — 注入电压斜坡上升期间的步长 `0.0001`（默认）| `scalar`

注入电压斜坡上升期间的步长（以标幺值为单位）。

### **Maximum voltage ramp up time limit (s)** — 最大电压斜坡上升持续时间 `0.25`（默认）| `scalar`

注入电压斜坡上升允许的最大持续时间（以秒为单位）。

### **Number of voltage and current samples per voltage injection instance** — 用于 Rs 估算的电压和电流采样数 `1000`（默认）| `scalar`

每次电压注入中用于 Rs 估算的电压和电流采样数。

### **Dwell time between voltage injections (s)** — 电压注入之间的等待持续时间 `0.25`（默认）| `scalar`

连续电压注入之间的等待持续时间（以秒为单位）。

### **Threshold to determine imbalance in phase resistances (0,1)** — 用于确定相电阻不平衡的阈值 `0.2`（默认）| `scalar`

用于确定相电阻之间不平衡的阈值（指定为 `0` 到 `1` 之间的值），超过该阈值即判定为不平衡。

## 所属库

Motor Control Blockset / Parameter Estimation / PMSM Parameter Estimation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a：新增模块参数

“模块参数”对话框现在包含用于配置参数估算过程的高级选项。

## 描述

估算永磁同步电机 (PMSM) 的定子电阻 ( R s )

PMSM Rs Estimator 模块使用相电流、电机两端的直流电压以及测试配置元素来计算 PMSM 的定子电阻。

该模块为每一相注入两个电压 *V1* 和 *V2*，并测量相应的电流响应 *I1* 和 *I2* 以估算各相电阻。然后，它通过对三个相电阻取平均值来估算电机电阻。
