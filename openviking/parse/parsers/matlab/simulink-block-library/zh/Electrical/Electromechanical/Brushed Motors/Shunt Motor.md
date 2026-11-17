---
type: simulink-block
title: 'Shunt Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Brushed Motors'
documentation_page: 'shuntmotor'
documentation_source_path: 'ref/shuntmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Shunt Motor

## 端口

### 守恒端口

### **+** — 正极端子电气

与并励电机正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与并励电机负极端子关联的电气守恒端口。

### **C** — 电机外壳机械

与并励电机外壳关联的机械旋转守恒端口。

### **R** — 电机转子机械

与并励电机转子关联的机械旋转守恒端口。

### **Hf** — 励磁绕组热端口热

励磁绕组热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **Ha** — 电枢绕组热端口热

电枢绕组热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 电气转矩

### **Model parameterization** — 模块参数化 `By equivalent circuit parameters`（默认）| `By rated power, rated speed & no-load speed`

选择以下方法之一进行模块参数化：

- `By equivalent circuit
  parameters` — 为电机的等效电路模型提供电气参数。
- `By rated power, rated speed & no-load
  speed` — 提供功率和速度参数，模块将其转换为电机的等效电路模型。

### **Armature resistance** — 电枢电阻 `110` `Ohm`（默认）

电枢的电阻。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Field winding resistance** — 励磁绕组电阻 `2500` `Ohm`（默认）

励磁绕组的电阻。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By
equivalent circuit parameters` 时，此参数才可见。

### **Back-emf constant** — 反电动势常数 `5.11` `s*V/rad/A`（默认）

电机产生的电压与电机转速之比。

### **Armature inductance** — 电枢电感 `0.1` `H`（默认）

电枢的电感。如果没有关于此电感的信息，请将此参数的值设置为一个较小的非零数。该值可以为零。

### **Field winding inductance** — 励磁绕组电感 `0.1` `H`（默认）

励磁绕组的电感。如果没有关于此电感的信息，请将此参数的值设置为一个较小的非零数。该值可以为零。

### **No-load speed** — 空载转速 `4600` `rpm`（默认）

未施加负载时电机的转速。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By rated
power, rated speed & no-load speed` 时，此参数才可见。

### **Rated speed (at rated load)** — 额定转速 `4000` `rpm`（默认）

额定负载下的电机转速。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By rated
power, rated speed & no-load speed` 时，此参数才可见。

### **Rated load (mechanical power)** — 额定负载 `50` `W`（默认）

电机额定运行所对应的机械负载。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By rated
power, rated speed & no-load speed` 时，此参数才可见。

### **Rated DC supply voltage** — 额定直流电源电压 `220` `V`（默认）

电机额定运行所对应的电压。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By rated
power, rated speed & no-load speed` 时，此参数才可见。

### **Starting current at rated DC supply voltage** — 额定直流电源电压下的启动电流 `2.09` `A`（默认）

在额定直流电源电压下启动电机时的初始电流。

#### 依赖关系

仅当将 **Model
parameterization** 参数设置为 `By rated
power, rated speed & no-load speed` 时，此参数才可见。

### 机械

### **Rotor inertia** — 转子惯量 `2e-4` `kg*m^2`（默认）

转子对电机运动变化的阻力。该值可以为零。

### **Rotor damping** — 转子耗散能量 `1e-6` `N*m/(rad/s)`（默认）

转子耗散的能量。该值可以为零。

### **Initial rotor speed** — 初始转子转速 `0` `rpm`（默认）

仿真开始时转子的转速。

### 温度依赖性

此选项卡仅对具有暴露热端口的模块显示。

### **Resistance temperature coefficients, [alpha\_f alpha\_a]** — 定子和转子电阻温度系数 `[.00393, .00393]` `1/K`（默认）

一个 1×2 行向量，定义电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。第一个元素对应励磁绕组，第二个元素对应电枢。默认值为铜的值。

### **Measurement temperature** — 测量温度 `25` `C`（默认）

定义电机参数所对应的温度。

### 热端口

此选项卡仅对具有暴露热端口的模块显示。

### **Thermal masses, [Mf Ma]** — 热质量 `[100, 100]` `J/K`（默认）

一个 1×2 行向量，定义励磁绕组和电枢绕组的热质量。热质量是使温度升高一度所需的能量。

### **Initial temperatures** — 初始温度 `[25, 25]` `C`（默认）

一个 1×2 行向量，定义仿真开始时励磁绕组和电枢热端口的温度。

## 所属库

Simscape / Electrical / Electromechanical / Brushed Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

具有电气和转矩特性的并励电机

Shunt Motor 模块使用以下等效电路模型表示并励电机的电气和转矩特性。

当将 **Model parameterization** 参数设置为 `By equivalent circuit parameters` 时，需要为此模型指定等效电路参数：

- *Ra* — **Armature
  resistance**
- *La* — **Armature
  inductance**
- *Rf* — **Field
  winding resistance**
- *Lf* — **Field
  winding inductance**

Shunt Motor 模块按如下方式计算电机转矩：

1. 电机中的磁场在电枢中感应出以下反电动势
   *vb*：

   vb=Lafifω

   其中 *Laf* 是比例常数，*ω* 是角速度。
2. 机械功率等于反电动势所反应的功率：

   P=vbia=Lafifiaω
3. 电机转矩为：

   T=P/ω=Lafifia

Shunt Motor 模块模型的转矩-转速特性与上图所示参数相关。当将 **Model parameterization** 参数设置为 `By rated power, rated speed & no-load speed` 时，模块按如下方式求解等效电路参数：

1. 对于稳态转矩-转速关系，*L* 没有影响。
2. 对回路中的电压求和：

   V=iaRa+LafifωV=ifRf
3. 求解上述方程得到
   *ia* 和
   *if*：

   if=VRfia=VRa(1−LafwRf)
4. 将这些 *ia*
   和 *if* 的值代入转矩方程：

   T=LafRaRf(1−LafωRf)V2

   模块使用额定转速和功率计算额定转矩。模块使用额定转矩和空载转速值得到一个关联 *Ra* 和
   *Laf/Rf* 的方程。它使用零转矩时的空载转速得到关联这两个量的第二个方程。然后，求解
   *Ra* 和 *Laf/Rf*。

对于 **Model parameterization** 参数的所有取值，模块都对电机惯量 *J* 和阻尼
*B* 进行建模。输出转矩为：

Tload=LafRaRf(1−LafωRf)V2−Jω˙−Bω

模块产生从机械 C 端口到 R 端口的正向转矩。

### 热效应建模

可以暴露热端口来对将功率转换为热量的损耗效应进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含多个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
