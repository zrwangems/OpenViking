---
type: simulink-block
title: 'PFC Rectifier Controller (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Converter Control'
documentation_page: 'pfcrectifiercontrollerthreephase'
documentation_source_path: 'ref/pfcrectifiercontrollerthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# PFC Rectifier Controller (Three-Phase)

## 端口
```yaml
ports:
- name: VdcRef (V)
  summary: 输出直流母线电压参考值，V 标量
  direction: input
  data_types: single | double
- name: QRef (pu)
  summary: 无功功率参考值，pu 标量
  direction: input
  data_types: single | double
- name: VdcSens (V)
  summary: 直流母线电压，V 标量
  direction: input
  data_types: single | double
- name: VabcSens (pu)
  summary: 测量的交流相电压，pu 向量
  direction: input
  data_types: single | double
- name: IabcSens (pu)
  summary: 测量的交流相电流，pu 向量
  direction: input
  data_types: single | double
- name: VabcRef (pu)
  summary: 参考电压，pu 向量
  direction: output
  data_types: single | double
- name: Visualization
  summary: 可视化总线 总线
  direction: output
  data_types: single | double
```

### 输入

### **VdcRef (V)** — 输出直流母线电压参考值，V 标量

输出直流母线电压参考值，单位为伏特。

**数据类型：** `single` | `double`

### **QRef (pu)** — 无功功率参考值，pu 标量

标幺值无功功率参考值。

**数据类型：** `single` | `double`

### **VdcSens (V)** — 直流母线电压，V 标量

测量的直流母线电压，单位为伏特。

**数据类型：** `single` | `double`

### **VabcSens (pu)** — 测量的交流相电压，pu 向量

标幺值测量的交流相电压。

**数据类型：** `single` | `double`

### **IabcSens (pu)** — 测量的交流相电流，pu 向量

标幺值测量的交流相电流。

**数据类型：** `single` | `double`
### 输出

### **VabcRef (pu)** — 参考电压，pu 向量

标幺值参考电压。

**数据类型：** `single` | `double`

### **Visualization** — 可视化总线 总线

包含用于可视化的内部信号的总线。有关信号列表，请参阅可视化。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: System frequency (Hz)
  summary: 系统频率 60（默认）| 正标量
  group: 常规
- name: AC filter inductance (H)
  summary: 交流滤波电感 1e-4（默认）| 正标量
  group: 常规
- name: AC side base impedance (Ohm)
  summary: 交流侧基准阻抗 1.722（默认）| 正标量
  group: 常规
- name: PLL proportional gain
  summary: 比例增益 0.05（默认）| 正标量
  group: 常规
- name: PLL integral gain
  summary: 积分增益 1（默认）| 正标量
  group: 常规
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 非负标量或 -1
  group: 常规
- name: Proportional gain
  summary: 比例增益 0.4（默认）| 正标量
  group: 电压控制器
- name: Integral gain
  summary: 积分增益 3（默认）| 正标量
  group: 电压控制器
- name: Derivative gain
  summary: 微分增益 0（默认）| 非负标量
  group: 电压控制器
- name: Derivative controller filter coefficient (N)
  summary: 微分控制器滤波系数 3（默认）| 非负标量
  group: 电压控制器
- name: DC bus base voltage (V)
  summary: 直流母线基准电压 700（默认）| 正标量
  group: 电压控制器
- name: Controller output upper limit (pu)
  summary: 控制器输出上限 1.5（默认）| 非负标量
  group: 电压控制器
- name: Controller output lower limit (pu)
  summary: 控制器输出下限 -1.5（默认）| 非正标量
  group: 电压控制器
- name: Id proportional gain
  summary: Id 比例增益 10（默认）| 正标量
  group: 电流控制器
- name: Id integral gain
  summary: Id 积分增益 350（默认）| 正标量
  group: 电流控制器
- name: Id derivative gain
  summary: Id 微分增益 0（默认）| 非负标量
  group: 电流控制器
- name: Id controller output upper limit (pu)
  summary: Id 控制器输出上限 1.2（默认）| 非负标量
  group: 电流控制器
- name: Id controller output lower limit (pu)
  summary: Id 控制器输出下限 -1.2（默认）| 非正标量
  group: 电流控制器
- name: Iq proportional gain
  summary: Iq 比例增益 10（默认）| 正标量
  group: 电流控制器
- name: Iq integral gain
  summary: Iq 积分增益 350（默认）| 正标量
  group: 电流控制器
- name: Iq derivative gain
  summary: Iq 微分增益 0（默认）| 非负标量
  group: 电流控制器
- name: Derivative current controller filter coefficient (N)
  summary: 微分电流控制器滤波系数 100（默认）| 非负标量
  group: 电流控制器
- name: Iq controller output upper limit (pu)
  summary: Iq 控制器输出上限 1.2（默认）| 非负标量
  group: 电流控制器
- name: Iq controller output lower limit (pu)
  summary: Iq 控制器输出下限 -1.2（默认）| 非正标量
  group: 电流控制器
```

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中，选择**属性检查器**。

### 常规

### **System frequency (Hz)** — 系统频率 `60`（默认）| 正标量

系统频率，单位为赫兹。

### **AC filter inductance (H)** — 交流滤波电感 `1e-4`（默认）| 正标量

交流滤波电感，单位为亨利。

### **AC side base impedance (Ohm)** — 交流侧基准阻抗 `1.722`（默认）| 正标量

交流侧基准阻抗，单位为欧姆。

### **PLL proportional gain** — 比例增益 `0.05`（默认）| 正标量

锁相环的比例增益。

### **PLL integral gain** — 积分增益 `1`（默认）| 正标量

锁相环的积分增益。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 非负标量或 `-1`

连续模块执行之间的时间，单位为秒。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关更多信息，请参阅什么是采样时间？和指定采样时间。

对于离散时间仿真：

- 要显式指定采样时间，请将此参数设置为正值。此值定义采样时间，单位为秒。
- 要继承采样时间，请将此参数设置为 `-1`。

对于连续时间仿真，请将此参数设置为 `0`。

有关连续和离散采样时间的更多信息，请参阅采样时间类型。

### 电压控制器

### **Proportional gain** — 比例增益 `0.4`（默认）| 正标量

电压控制器的比例增益。

### **Integral gain** — 积分增益 `3`（默认）| 正标量

电压控制器的积分增益。

### **Derivative gain** — 微分增益 `0`（默认）| 非负标量

电压控制器的微分增益。

### **Derivative controller filter coefficient (N)** — 微分控制器滤波系数 `3`（默认）| 非负标量

微分电压控制器滤波系数。

### **DC bus base voltage (V)** — 直流母线基准电压 `700`（默认）| 正标量

直流母线基准电压，单位为伏特。

### **Controller output upper limit (pu)** — 控制器输出上限 `1.5`（默认）| 非负标量

电压控制器标幺值输出的上限。

### **Controller output lower limit (pu)** — 控制器输出下限 `-1.5`（默认）| 非正标量

电压控制器标幺值输出的下限。

### 电流控制器

### **Id proportional gain** — Id 比例增益 `10`（默认）| 正标量

*d* 轴电流控制器的比例增益。

### **Id integral gain** — Id 积分增益 `350`（默认）| 正标量

*d* 轴电流控制器的积分增益。

### **Id derivative gain** — Id 微分增益 `0`（默认）| 非负标量

*d* 轴电流控制器的微分增益。

### **Id controller output upper limit (pu)** — Id 控制器输出上限 `1.2`（默认）| 非负标量

*d* 轴电流控制器标幺值输出的上限。

### **Id controller output lower limit (pu)** — Id 控制器输出下限 `-1.2`（默认）| 非正标量

*d* 轴电流控制器标幺值输出的下限。

### **Iq proportional gain** — Iq 比例增益 `10`（默认）| 正标量

*q* 轴电流控制器的比例增益。

### **Iq integral gain** — Iq 积分增益 `350`（默认）| 正标量

*q* 轴电流控制器的积分增益。

### **Iq derivative gain** — Iq 微分增益 `0`（默认）| 非负标量

*q* 轴电流控制器的微分增益。

### **Derivative current controller filter coefficient (N)** — 微分电流控制器滤波系数 `100`（默认）| 非负标量

微分电流控制器滤波系数。

### **Iq controller output upper limit (pu)** — Iq 控制器输出上限 `1.2`（默认）| 非负标量

*q* 轴电流控制器标幺值输出的上限。

### **Iq controller output lower limit (pu)** — Iq 控制器输出下限 `-1.2`（默认）| 非正标量

*q* 轴电流控制器标幺值输出的下限。
## 所属库

Simscape / Electrical / Control / Converter Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

基于 PID 的功率因数校正（PFC）整流器控制器

PFC Rectifier Controller (Three-Phase) 模块实现基于比例-积分-微分（PID）的功率因数校正（PFC）整流器控制器。此模块将三相交流电源转换为所需的稳定直流母线电压，并控制从电源汲取的无功功率。为减少谐波，模块汲取正弦电流。模块具有内置锁相环（PLL），可跟踪电源电压的角度和幅值。

对于离散时间仿真，请将 **Sample time (-1 for inherited)** 设置为正值或设置为 `-1` 以继承采样时间。对于连续时间仿真，请将 **Sample time (-1 for inherited)** 设置为 `0`。

此图显示了 PFC 整流器的电路配置。

- *V*S 是电源电压。
- *I*S 是电源侧电流。
- *X*L 是感抗。
- *V*i 是逆变器侧交流相电压。
- *V*dc 是直流母线电压。

此方程定义了电源电压 *V*S，

VS(t)=ISRL+LdiS(t)dt+Vi(t),

其中：

- *R*L 是滤波电感的电阻。
- *L* 是滤波电感。
- *i*s 是逆变器侧交流相电流。

### 控制器结构

此图显示了控制器的结构。

模块的输入为：

- 输出直流母线电压参考值 *VdcRef*，单位为伏特。
- 标幺值无功功率参考值 *QRef*。
- 测量的直流母线电压 *VdcSens*，单位为伏特。
- 标幺值测量的交流相电压 *VabcSens*。
- 标幺值测量的交流相电流 *IabcSens*。

输出为标幺值参考电压 *VabcRef* 和包含用于可视化的信号的总线。

直流电压控制器计算：

- 标幺值 *d* 轴参考电流 *IdRef*。
- 直流电压控制器的标幺值误差 *VdcCntrlError*。

PLL 计算：

- 测量的交流相电压的相位角 *pllAngle*，单位为弧度。
- 测量的交流相电压的标幺值幅值 *pllVmag*。
- 测量的交流相电压的标幺值 *d* 轴分量 *Vd*。
- 测量的交流相电压的标幺值 *q* 轴分量 *Vq*。

无功功率参考值计算标幺值 *q* 轴参考电流 *IqRef*。

电流控制器计算：

- 标幺值参考电压 *VabcRef*。
- *d* 轴电流控制器的标幺值误差 *IdCntrlError*。
- *q* 轴电流控制器的标幺值误差 *IqCntrlError*。

### 可视化

模块输出包含以下七个用于可视化的信号的总线：

- 测量的交流相电压的相位角 *pllAngle*，单位为弧度。
- 测量的交流相电压的标幺值电压幅值 *pllVmag*。
- 标幺值 *d* 轴参考电流 *IdRef*。
- 标幺值 *q* 轴参考电流 *IqRef*。
- 直流电压控制器的标幺值误差 *VdcCntrlError*。
- *d* 轴电流控制器的标幺值误差 *IdCntrlError*。
- *q* 轴电流控制器的标幺值误差 *IqCntrlError*。
