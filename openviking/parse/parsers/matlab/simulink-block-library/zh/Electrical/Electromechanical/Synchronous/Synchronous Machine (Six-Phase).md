---
type: simulink-block
title: 'Synchronous Machine (Six-Phase)'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Synchronous'
documentation_page: 'synchronousmachinesixphase'
documentation_source_path: 'ref/synchronousmachinesixphase.html'
language: zh-CN
chinese_source: worker-translation
---

# Synchronous Machine (Six-Phase)

## 端口

### 守恒

### **fd+** — 励磁绕组正极端子电气

与励磁绕组正极端子关联的电气守恒端口。

### **fd-** — 励磁绕组负极端子电气

与励磁绕组负极端子关联的电气守恒端口。

### **R** — 电机转子机械

与电机转子关联的机械旋转守恒端口。

### **C** — 电机机壳机械

与电机机壳关联的机械旋转守恒端口。

### **~ABC** — 定子 ABC 绕组电气

与定子 ABC 绕组关联的三相电气端口。

### **~XYZ** — 定子 XYZ 绕组电气

与定子 XYZ 绕组关联的三相电气端口。

### **n1** — ABC 绕组中性点电气

与 ABC 绕组配置的中性点关联的电气守恒端口。

#### 依赖关系

要启用此端口，将 **Zero sequence** 设为 `Include`。

### **n2** — XYZ 绕组中性点电气

与 XYZ 绕组配置的中性点关联的电气守恒端口。

#### 依赖关系

要启用此端口，将 **Zero sequence** 设为 `Include`。

### **HA** — *a* 相端子热端口 热

与定子绕组 *a* 关联的热守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设为 `Show thermal port`。

### **HB** — *b* 相端子热端口 热

与定子绕组 *b* 关联的热守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设为 `Show thermal port`。

### **HC** — *c* 相端子热端口 热

与定子绕组 *c* 关联的热守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设为 `Show thermal port`。

### **HX** — *x* 相端子热端口 热

与定子绕组 *x* 关联的热守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设为 `Show thermal port`。

### **HY** — *y* 相端子热端口 热

与定子绕组 *y* 关联的热守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设为 `Show thermal port`。

### **HZ** — *z* 相端子热端口 热

与定子绕组 *z* 关联的热守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设为 `Show thermal port`。

### **HR** — 转子热端口 热

与转子关联的热守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 主要

### **Nominal power** — 额定功率 `100e3` `V*A`（默认） | scalar

额定功率。

### **Nominal voltage (line-to-line,rms)** — 额定均方根电压 `240` `V`（默认） | scalar

额定均方根 (RMS) 线电压。

### **Nominal electrical frequency** — 额定电频率 `60` `Hz`（默认） | scalar

给出额定功率时的额定电频率。

### **Number of pole pairs** — 转子极对数 `2`（默认） | positive scalar

电机极对数。

### **Zero sequence** — 零序模型 `Include`（默认） | `Exclude`

零序模型，包含两个选项：

- `Include` — 优先考虑模型保真度。如果对使用 Partitioning 求解器的仿真 Include 零序项，则发生错误。有关详细信息，请参阅 Increase Simulation Speed Using the Partitioning Solver。
- `Exclude` — 优先考虑桌面仿真或实时部署的仿真速度。

### **Rotor angle definition** — 转子角度参考点 `Angle between the a-phase magnetic axis and the d-axis`（默认） | `Angle between the a-phase magnetic axis and the q-axis`

转子角度测量的参考点。如果选择默认值，则对于零转子角度，转子和 *a* 相磁通对齐。否则，对于零转子角度，*a* 相电流生成最大转矩值。

### 阻抗

### **Stator resistance, Rs** — 定子电阻 `0.0288`（默认） | positive scalar

定子电阻。此参数必须大于 `0`。

### **Stator leakage inductance, Ll** — 定子漏电感 `0.0969`（默认） | positive scalar

定子漏电感。此参数必须大于 `0`。

### **Stator d-axis mutual inductance, Lmd** — 定子 *d* 轴互感 `1.9583`（默认） | positive scalar

定子 *d* 轴互感。此参数必须大于 0。

### **Stator q-axis mutual inductance, Lmq** — 定子 *q* 轴互感 `0.9045`（默认） | positive scalar

定子 *q* 轴互感。此参数必须大于 0。

### **Rotor field winding resistance, Rfd'** — 转子励磁绕组电阻 `0.0028`（默认） | positive scalar

转子励磁绕组电阻。此参数必须大于 0。

### **Rotor field winding inductance, Llfd'** — 转子励磁绕组电感 `0.0813`（默认） | positive scalar

转子励磁绕组电感。此参数必须大于 0。

### **Rotor d-axis damper winding resistance, Rkd'** — 转子 *d* 轴阻尼绕组电阻 `0.0041`（默认） | positive scalar

转子 *d* 轴阻尼绕组电阻。此参数必须大于 0。

### **Rotor d-axis damper winding inductance, Llkd'** — 转子 *d* 轴阻尼绕组电感 `0.0918`（默认） | positive scalar

转子 *d* 轴阻尼绕组电感。此参数必须大于 0。

### **Rotor q-axis damper winding resistance, Rkq'** — 转子 *q* 轴阻尼绕组电阻 `0.0043`（默认） | positive scalar

转子 *q* 轴阻尼绕组电阻。此参数必须大于 0。

### **Rotor q-axis damper winding inductance, Llkq'** — 转子 *q* 轴阻尼绕组电感 `0.1174`（默认） | positive scalar

转子 *q* 轴阻尼绕组电感。此参数必须大于 0。

### 初始条件

### **Initialization option** — 初始化选项 `Set real power, reactive power, terminal voltage, and terminal phase`（默认） | `Set targets for rotor angle and Park's transform variables`

用于在仿真开始时为某些参数和变量指定值的模型：

- 要设置独立于所连接网络的工作点，请选择 `Set real power, reactive power, terminal voltage and terminal phase`。
- 要使用 **Variables** 设置在仿真前指定模块变量的优先级和初始目标值，请选择 `Set targets for rotor angle and Park's transform variables`。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

### **Terminal voltage magnitude** — 端子电压幅值 `240` `V`（默认） | scalar

端子电压幅值。

#### 依赖关系

要启用此参数，将 **Initialization option** 设为 `Set real power, reactive power, terminal voltage, and terminal phase`。

### **Terminal voltage angle corresponding to ABC group** — 对应 ABC 组的端子电压角度 `0` `deg`（默认） | scalar

对应 ABC 定子的端子电压角度。

#### 依赖关系

要启用此参数，将 **Initialization option** 设为 `Set real power, reactive power, terminal voltage, and terminal phase`。

### **Terminal active power (ABC group)** — ABC 端子有功功率 `50e3` `V*A`（默认） | scalar

由定子 ABC 绕组产生的端子有功功率。

#### 依赖关系

要启用此参数，将 **Initialization option** 设为 `Set real power, reactive power, terminal voltage, and terminal phase`。

### **Terminal reactive power (ABC group)** — ABC 端子无功功率 `0` `V*A`（默认） | scalar

由定子 ABC 绕组产生的端子无功功率。

#### 依赖关系

要启用此参数，将 **Initialization option** 设为 `Set real power, reactive power, terminal voltage, and terminal phase`。

### **Terminal active power (XYZ group)** — XYZ 端子有功功率 `20e3` `V*A`（默认） | scalar

由定子 XYZ 绕组产生的端子有功功率。

#### 依赖关系

要启用此参数，将 **Initialization option** 设为 `Set real power, reactive power, terminal voltage, and terminal phase`。

### **Terminal reactive power (XYZ group)** — XYZ 端子无功功率 `0` `V*A`（默认） | scalar

由定子 XYZ 绕组产生的端子无功功率。

#### 依赖关系

要启用此参数，将 **Initialization option** 设为 `Set real power, reactive power, terminal voltage, and terminal phase`。

### 热

要启用这些参数，将 **Modeling option** 设为 `Show thermal port`。

### **Measurement temperature** — 额定温度 `298.15` `k`（默认） | real scalar

电机参数对应的温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认） | positive scalar

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值 `3.93e-3` 1/K 适用于铜。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认） | positive scalar

每个定子绕组的热质量值。热质量是使温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认） | positive scalar

转子的热质量。热质量是使转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Synchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

六相同步电机

Synchronous Machine (Six-Phase) 模块对六相同步电机（也称为双星型电机）进行建模。

六相同步电机有两组定子绕组：ABC 组和 XYZ 组。这两组之间有 30 度的相移。

六相同步电机在直轴、交轴和两个零序下的等效电路为：

### 方程

同步电机方程相对于同步旋转参考坐标系表示，该坐标系由下式定义：

θe(t)=Nθr(t)+x\_rotor\_offset,

其中：

- *θe* 是转子电角度。
- *N* 是极对数。
- *θr* 是转子机械角度。
- *x\_rotor\_offset* 为 `0`（如果相对于 *d* 轴定义转子电角度），或者为 `-pi/2`（如果相对于 *q* 轴定义转子电角度）。

两个 Park 变换将同步电机方程映射到相对于电角度的旋转参考坐标系。第一组定子绕组（ABC 组）的 Park 变换定义为：

Ps1=23[cosθecos(θe−2π3)cos(θe+2π3)−sinθe−sin(θe−2π3)−sin(θe+2π3)121212].

第二组定子绕组（XYZ 组）的 Park 变换定义为：

Ps2=23[cos(θe−π6)cos(θe−5π6)cos(θe+π2)−sin(θe−π6)−sin(θe−5π6)sin(θe+π2)121212].

Park 变换用于定义标幺值同步电机方程。

ABC 组的定子电压方程定义为：

vd1=Rsid1−ψq1ωr+1ωbasedψd1dt

vq1=Rsiq1+ψd1ωr+1ωbasedψq1dt

v01=Rsi01+1ωbasedψ01dt

其中：

- *vd1*、*vq1* 和 *v01* 是由下式定义的 *d* 轴、*q* 轴和零序 ABC 定子电压：

  [vd1vq1v01]=Ps1[vavbvc].

  *va*、*vb* 和 *vc* 是从端口 **~ABC** 到中性点端口 **n1** 测得的 ABC 定子电压。
- *ωbase* 是标幺值基准电速度。
- *ψd1*、*ψq1* 和 *ψ01* 是 ABC 组的 *d* 轴、*q* 轴和零序定子磁链。
- *ωr* 是标幺值转子转速。
- *Rs* 是定子电阻。
- *id1*、*iq1* 和 *i01* 是由下式定义的 *d* 轴、*q* 轴和零序 ABC 定子电流：

  [id1iq1i01]=Ps1[iAiBiC].

  *ia*、*ib* 和 *ic* 是从端口 **~ABC** 流向端口 **n1** 的 ABC 定子电流。

XYZ 组的定子电压方程定义为：

vd2=Rsid2−ψq2ωr+1ωbasedψd2dt

vq2=Rsiq2+ψd2ωr+1ωbasedψq2dt

v02=Rsi02+1ωbasedψ02dt

其中：

- *vd2*、*vq2* 和 *v02* 是由下式定义的 *d* 轴、*q* 轴和零序 XYZ 定子电压：

  [vd2vq2v02]=Ps2[vxvyvz].

  *vx*、*vy* 和 *vz* 是从端口 **~XYZ** 到中性点端口 **n2** 测得的 XYZ 定子电压。
- *ψd2*、*ψq2* 和 *ψ02* 是 XYZ 组的 *d* 轴、*q* 轴和零序定子磁链。
- *id2*、*iq2* 和 *i02* 是由下式定义的 *d* 轴、*q* 轴和零序 XYZ 定子电流：

  [id2iq2i02]=Ps2[iXiYiZ].

  *ix*、*iy* 和 *iz* 是从端口 **~XYZ** 流向端口 **n2** 的 XYZ 定子电流。

转子电压方程定义为：

v'fd=R'fdi'fd+1ωbasedψ'fddt

v'kd=R'kdi'kd+1ωbasedψ'kddt=0

v'kq=R'kqi'kq+1ωbasedψ'kqdt=0

其中：

- *v'fd* 是折算到定子侧的励磁绕组电压。
- *v'kd* 和 *v'kq* 是折算到定子侧的 *dq* 轴阻尼绕组电压。它们都等于 0。
- *ψ'fd*、*ψ'kd* 和 *ψ'kq* 是链接励磁电路、*d* 轴阻尼绕组和 *q* 轴阻尼绕组的磁通。
- *R'fd*、*R'kd* 和 *R'kq* 是转子励磁电路、*d* 轴阻尼绕组和 *q* 轴阻尼绕组的电阻。
- *i'fd*、*i'kd* 和 *i'kq* 是折算到定子侧的励磁和 *dq* 轴阻尼绕组电流。

定子磁链方程定义为：

ψd1=Llid1+Lmd(id1+id2+i′fd+i′kd)

ψq1=Lliq1+Lmq(iq1+iq2+i′kq)

ψ01=Lli01

ψd2=Llid2+Lmd(id1+id2+i′fd+i′kd)

ψq2=Lliq2+Lmq(iq1+iq2+i′kq)

ψ02=Lli02

其中：

- *Ll* 是定子漏电感。
- *Lmd* 和 *Lmq* 是定子 *d* 轴和 *q* 轴的互感。

转子磁链方程定义为：

ψ'fd=L'lfdi'fd+Lmd(id1+id2+i′fd+i′kd)

ψ'kd=L'lkdi'kd+Lmd(id1+id2+i′fd+i′kd)

ψ'kq=L'lkqi'kq+Lmq(iq1+iq2+i′kq)

其中：

- *L'lfd* 是转子励磁绕组电感。
- *L'lkd* 是转子 *d* 轴阻尼绕组电感。
- *L'lkg* 是转子 *q* 轴阻尼绕组电感。

转子转矩定义为：

Te=ψd1iq1−ψq1id1+ψd2iq2−ψq2id2.

### 对热效应建模

您可以公开热端口，以对将功率转换为热量的损耗效应进行建模。要公开热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 该模块包含与定子绕组关联的扩展电气守恒端口，但不包含热端口。
- `Show thermal port` — 该模块包含与定子绕组关联的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

对于此模块，只有在 **初始条件** 部分将 **初始化选项** 参数设置为 `Set targets for rotor angle and Park's transform variables` 时，**初始目标** 设置才可见。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅基于标称值的系统缩放。
