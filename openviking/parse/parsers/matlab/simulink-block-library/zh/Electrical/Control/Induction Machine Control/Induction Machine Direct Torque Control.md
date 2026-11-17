---
type: simulink-block
title: 'Induction Machine Direct Torque Control'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinedirecttorquecontrol'
documentation_source_path: 'ref/inductionmachinedirecttorquecontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Direct Torque Control

## 端口
```yaml
ports:
- name: FluxRef
  summary: 磁链标量
  direction: input
  data_types: single | double
- name: TqRef
  summary: 转矩标量
  direction: input
  data_types: single | double
- name: vabc
  summary: 电压矢量
  direction: input
  data_types: single | double
- name: iabc
  summary: 电流矢量
  direction: input
  data_types: single | double
- name: G
  summary: 门极脉冲矢量 | 0 或 1
  direction: output
  data_types: single | double
```

### 输入

### **FluxRef** — 磁链标量

参考定子磁链。

**数据类型：** `single` | `double`

### **TqRef** — 转矩标量

参考转矩。

**数据类型：** `single` | `double`

### **vabc** — 电压矢量

定子相电压。

**数据类型：** `single` | `double`

### **iabc** — 电流矢量

定子相电流。

**数据类型：** `single` | `double`
### 输出

### **G** — 门极脉冲矢量 | `0` 或 `1`

逆变器门极脉冲。该模块不考虑任何死区时间。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Stator resistance (Ohm)
  summary: 电阻 0.25（默认值）| 正标量
  group: ''
- name: Number of pole pairs
  summary: 极对数 1（默认值）| 正整数
  group: ''
- name: Flux hysteresis bandwidth (Wb)
  summary: 磁链 0.02（默认值）| 正标量
  group: ''
- name: Torque hysteresis bandwidth (N\*m)
  summary: 转矩 10（默认值）| 正标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认值）| 正标量
  group: ''
```

### **Stator resistance (Ohm)** — 电阻 `0.25`（默认值）| 正标量

电机定子电阻。

### **Number of pole pairs** — 极对数 `1`（默认值）| 正整数

电机极对数。

### **Flux hysteresis bandwidth (Wb)** — 磁链 `0.02`（默认值）| 正标量

围绕磁链设定点对称分布的总带宽。

### **Torque hysteresis bandwidth (N\*m)** — 转矩 `10`（默认值）| 正标量

围绕设定点对称分布的总带宽。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认值）| 正标量

连续模块执行之间的时间，以 s 为单位。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。
## 所属库

Simscape / Electrical / Control / Induction Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

感应电机 DTC

Induction Machine Direct Torque Control 模块实现感应电机直接转矩控制（DTC）结构。该图显示了该模块的等效电路。

### 方程

为了估计转矩和磁链，Induction Machine Direct Torque Control 模块使用后向欧拉法在静止 *ɑβ* 参考坐标系中离散化电机电压方程。*ɑβ* 坐标系中定子磁链的离散时间方程为：

ψα=(vα−iαRs)Tszz−1

以及

ψβ=(vβ−iβRs)Tszz−1

其中：

- *vɑ* 是 *ɑ* 轴电压。
- *iɑ* 是 *ɑ* 轴电流。
- *Rs* 是定子电阻。
- *Ψɑ* 是 *ɑ* 轴定子磁链。
- *vβ* 是 *β* 轴电压。
- *iβ* 是 *β* 轴电流。
- *Ψβ* 是 *β* 轴定子磁链。

该模块计算转矩和磁链如下：

T=3p2(ψαiβ−ψβiα)

以及

ψs=ψα2+ψβ2

其中：

- *p* 是极对数。
- *Ψs* 是定子磁链。

为了检测磁链和转矩估计误差，该模块使用滞环比较器。该图显示了滞环比较器及相关的开关扇区。

该表显示了逆变器高侧系统的最优开关。

| *cΨ*, *cT**S*(*θ*) | | *S0* | *S1* | *S2* | *S3* | *S4* | *S5* |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cΨ = 1 | *cT* = 1 | `1, 1, 0` | `0, 1, 0` | `0, 1, 1` | `0, 0, 1` | `1, 0, 1` | `1, 0, 0` |
| *cT* = 0 | `1, 1, 1` | `0, 0, 0` | `1, 1, 1` | `0, 0, 0` | `1, 1, 1` | `0, 0, 0` |
| *cT* = -1 | `1, 0, 1` | `1, 0, 0` | `1, 1, 0` | `0, 1, 0` | `0, 1, 1` | `0, 0, 1` |
| cΨ = 0 | *cT* = 1 | `0, 1, 0` | `0, 1, 1` | `0, 0, 1` | `1, 0, 1` | `1, 0, 0` | `1, 1, 0` |
| *cT* = 0 | `0, 0, 0` | `1, 1, 1` | `0, 0, 0` | `1, 1, 1` | `0, 0, 0` | `1, 1, 1` |
| *cT* = -1 | `0, 0, 1` | `1, 0, 1` | `1, 0, 0` | `1, 1, 0` | `0, 1, 0` | `0, 1, 1` |

### 假设和限制

- 不考虑功率逆变器死区时间。对于硬件实现，请在外部添加死区时间。
