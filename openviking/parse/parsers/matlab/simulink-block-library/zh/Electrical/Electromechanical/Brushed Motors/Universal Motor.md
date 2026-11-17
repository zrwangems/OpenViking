---
type: simulink-block
title: 'Universal Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Brushed Motors'
documentation_page: 'universalmotor'
documentation_source_path: 'ref/universalmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Universal Motor

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: C
  summary: 电机外壳机械
  direction: conserving
- name: R
  summary: 电机转子机械
  direction: conserving
- name: Hf
  summary: 励磁绕组热端口热
  direction: conserving
- name: Ha
  summary: 电枢绕组热端口热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与通用电机正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与通用电机负极端子关联的电气守恒端口。

### **C** — 电机外壳机械

与通用电机外壳关联的机械旋转守恒端口。

### **R** — 电机转子机械

与通用电机转子关联的机械旋转守恒端口。

### **Hf** — 励磁绕组热端口热

励磁绕组热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show
thermal port`。

### **Ha** — 电枢绕组热端口热

电枢绕组热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show
thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Model parameterization
  summary: 模块参数化 By DC rated power, rated speed & maximum torque（默认）| By equivalent circuit parameters | By DC rated power,
    rated speed & electrical power | By AC rated power, rated speed, current & electrical power
  group: 电气转矩
- name: Total armature and field winding resistance
  summary: 电枢和励磁绕组的总电阻 132.8 Ohm（默认）
  group: 电气转矩
- name: Back-emf constant
  summary: 反电动势常数 0.1722 s*V/rad/A（默认）
  group: 电气转矩
- name: Total armature and field winding inductance
  summary: 电枢和励磁绕组的总电感 0.525 H（默认）
  group: 电气转矩
- name: Rated speed (at rated load)
  summary: 额定转速 6500 rpm（默认）
  group: 电气转矩
- name: Rated load (mechanical power)
  summary: 额定负载 75 W（默认）
  group: 电气转矩
- name: Rated DC supply voltage
  summary: 额定直流电源电压 200 V（默认）
  group: 电气转矩
- name: Maximum (starting) torque
  summary: 最大转矩 0.39 N*m（默认）
  group: 电气转矩
- name: Electrical power in at rated load
  summary: 额定机械功率下的电功率 160 W（默认）
  group: 电气转矩
- name: RMS rated voltage
  summary: RMS 额定电压 240 V（默认）
  group: 电气转矩
- name: RMS current at rated load
  summary: 额定负载下的 RMS 电流 0.8 A（默认）
  group: 电气转矩
- name: AC frequency
  summary: 交流频率 50 Hz（默认）
  group: 电气转矩
- name: Rotor inertia
  summary: 转子惯量 2e-4 kg*m^2（默认）
  group: 机械
- name: Rotor damping
  summary: 转子耗散能量 1e-6 N*m/(rad/s)（默认）
  group: 机械
- name: Initial rotor speed
  summary: 初始转子转速 0 rpm（默认）
  group: 机械
- name: Field to armature resistance ratio, Rf/Ra
  summary: 定子和转子电阻温度系数 1（默认）
  group: 温度依赖性
- name: Resistance temperature coefficients, [alpha_f alpha_a]
  summary: 定子和转子电阻温度系数 [.00393, .00393] 1/K（默认）
  group: 温度依赖性
- name: Measurement temperature
  summary: 测量温度 25 C（默认）
  group: 温度依赖性
- name: Thermal masses, [Mf Ma]
  summary: 热质量 [100, 100] J/K（默认）
  group: 热端口
- name: Initial temperatures
  summary: 初始温度 [25, 25] C（默认）
  group: 热端口
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 电气转矩

### **Model parameterization** — 模块参数化 `By DC rated power, rated speed & maximum torque`（默认）| `By equivalent circuit parameters` | `By DC rated power, rated speed & electrical power` | `By AC rated power, rated speed, current & electrical power`

选择以下方法之一进行模块参数化：

- `By equivalent circuit parameters` — 提供电机等效电路模型的电气参数。
- `By DC rated power, rated speed & maximum torque`
  — 提供直流功率和转速参数，模块将其转换为电机的等效电路模型。
- `By DC rated power, rated speed & electrical power`
  — 提供交流功率和转速参数，模块将其转换为电机的等效电路模型。
- `By AC rated power, rated speed, current & electrical
  power` — 提供交流功率和转速参数，模块将其转换为电机的等效电路模型。

### **Total armature and field winding resistance** — 电枢和励磁绕组的总电阻 `132.8` `Ohm`（默认）

电枢和励磁绕组的总电阻。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By equivalent circuit
parameters` 时，此参数才可见。

### **Back-emf constant** — 反电动势常数 `0.1722` `s*V/rad/A`（默认）

电机产生的电压与电机转速之比。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By equivalent circuit
parameters` 时，此参数才可见。

### **Total armature and field winding inductance** — 电枢和励磁绕组的总电感 `0.525` `H`（默认）

电枢和励磁绕组的总电感。如果没有关于此电感的信息，请将此参数的值设置为一个较小的非零数。

**注意**

可以将 **Total armature and field winding inductance** 值设置为零，但仅在用直流电源驱动电机时才有意义。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By equivalent circuit
parameters`、`By DC rated power, rated speed & maximum
torque` 或 `By DC rated power, rated speed & electrical
power` 时，此参数才可见。

### **Rated speed (at rated load)** — 额定转速 `6500` `rpm`（默认）

额定机械负载下的电机转速。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By DC rated power, rated speed &
maximum torque`、`By DC rated power, rated speed & electrical
power` 或 `By AC rated power, rated speed, current &
electrical power` 时，此参数才可见。

### **Rated load (mechanical power)** — 额定负载 `75` `W`（默认）

电机额定运行所对应的机械负载。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By DC rated power, rated speed &
maximum torque`、`By DC rated power, rated speed & electrical
power` 或 `By AC rated power, rated speed, current &
electrical power` 时，此参数才可见。

### **Rated DC supply voltage** — 额定直流电源电压 `200` `V`（默认）

电机额定运行所对应的直流电压。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By DC rated power, rated speed &
maximum torque` 或 `By DC rated power, rated speed &
electrical power` 时，此参数才可见。

### **Maximum (starting) torque** — 最大转矩 `0.39` `N*m`（默认）

电机产生的最大转矩。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By DC rated power, rated speed &
maximum torque` 时，此参数才可见。

### **Electrical power in at rated load** — 额定机械功率下的电功率 `160` `W`（默认）

电机在额定机械功率下使用的电功率量。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By DC rated power, rated speed &
electrical power` 或 `By AC rated power, rated speed, current
& electrical power` 时，此参数才可见。

### **RMS rated voltage** — RMS 额定电压 `240` `V`（默认）

电机在交流电源下运行时的 RMS 电源电压。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By AC rated power, rated speed,
current & electrical power` 时，此参数才可见。

### **RMS current at rated load** — 额定负载下的 RMS 电流 `0.8` `A`（默认）

电机在额定负载下以交流电源运行时的 RMS 电流。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By AC rated power, rated speed,
current & electrical power` 时，此参数才可见。

### **AC frequency** — 交流频率 `50` `Hz`（默认）

交流电源电压的频率。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By AC rated power, rated speed,
current & electrical power` 时，此参数才可见。

### 机械

### **Rotor inertia** — 转子惯量 `2e-4` `kg*m^2`（默认）

转子对电机运动变化的阻力。该值可以为零。

### **Rotor damping** — 转子耗散能量 `1e-6` `N*m/(rad/s)`（默认）

转子耗散的能量。该值可以为零。

### **Initial rotor speed** — 初始转子转速 `0` `rpm`（默认）

仿真开始时转子的转速。

### 温度依赖性

此选项卡仅对具有暴露热端口的模块显示。

### **Field to armature resistance ratio, Rf/Ra** — 定子和转子电阻温度系数 `1`（默认）

励磁电阻与电枢电阻之比。仅当显示励磁和电枢热端口时才需要此参数。它用于确定励磁绕组和电枢绕组的各自电阻值，以便正确分配两个电阻产生的热量。

### **Resistance temperature coefficients, [alpha\_f alpha\_a]** — 定子和转子电阻温度系数 `[.00393, .00393]` `1/K`（默认）

一个 1×2 行向量，定义电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。第一个元素对应励磁绕组，第二个对应电枢。默认值为铜的值。

### **Measurement temperature** — 测量温度 `25` `C`（默认）

定义电机参数所对应的温度。

### 热端口

此选项卡仅对具有暴露热端口的模块显示。

### **Thermal masses, [Mf Ma]** — 热质量 `[100, 100]` `J/K`（默认）

一个 1×2 行向量，定义励磁绕组和电枢绕组的热质量。热质量是使温度升高一度所需的能量。

### **Initial temperatures** — 初始温度 `[25, 25]` `C`（默认）

一个 1×2 行向量，定义仿真开始时励磁和电枢热端口的温度。
## 所属库

Simscape / Electrical / Electromechanical / Brushed Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

具有电气和转矩特性的通用（或串励）电机

Universal Motor 模块使用以下等效电路模型表示通用（或串励）电机的电气和转矩特性。

其中：

- *Ra* 是电枢电阻。
- *La* 是电枢电感。
- *Rf* 是励磁绕组电阻。
- *Lf* 是励磁绕组电感。

当将 **Model parameterization** 参数设置为 `By
equivalent circuit parameters` 时，需要为此模型指定等效电路参数。Universal Motor 模块按如下方式计算电机转矩：

1. 电机中的磁场在电枢中感应出以下反电动势
   *vb*：

   vb=Lafifω

   其中 *Laf* 是比例常数，*ω* 是角速度。
2. 机械功率等于反电动势所反应的功率：

   P=vbif=Lafif2ω
3. 电机转矩为：

   T=P/ω=Lafif2

Universal Motor 模块模型的转矩-转速特性与上图中的参数相关。当将 **Model
parameterization** 参数设置为 `By DC rated power, rated speed &
maximum torque` 或 `By DC rated power, rated speed & electrical
power` 时，模块按如下方式求解等效电路参数：

1. 对于使用直流电源时的稳态转矩-转速关系，*L* 没有影响。
2. 对回路中的电压求和：

   V=(Rf+Ra)if+vb=(Rf+Ra+Lafω)if
3. 求解上述方程得到 *if*，并将该值代入转矩方程：

   T=Laf(VRf+Ra+Lafω)2

   模块使用额定转速和功率计算额定转矩。模块使用上述方程中的额定转矩和额定转速值以及相应的电功率来确定
   *Rf+Ra* 和
   *Laf* 的值。

当将 **Model parameterization** 参数设置为 `By AC
rated power, rated speed, current & electrical power` 时，模块必须在模型中包含感性项 *La* 和
*Lf*。这需要关于 RMS 额定电流和电压的信息以计算总电感。

对于所有 **Model parameterization** 参数值，模块都对电机惯量 *J* 和阻尼 *B* 进行建模。输出转矩为：

Tload=Laf(VRf+Ra+Lafω)2−Jω˙−Bω

模块产生从机械 C 端口到 R 端口的正向转矩。

### 热效应建模

可以暴露热端口来对将功率转换为热量的损耗效应进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
