---
type: simulink-block
title: 'Cartridge Valve Actuator (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces'
documentation_page: 'cartridgevalveactuatoril'
documentation_source_path: 'ref/cartridgevalveactuatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Cartridge Valve Actuator (IL)

## 端口

### 守恒

### **A** — 等温液体压力端口

与阀入口关联的压力端口。

### **B** — 等温液体压力端口

与阀出口关联的压力端口。

### **X** — 等温液体压力端口

阀芯端部的压力端口。

### **Y** — 等温液体压力端口

先导压力端口。要启用此端口，请将 **Number of pressure ports** 设置为 `4`。
### 输出

### **S** — 阀芯位置，m 物理信号

以 m 为单位的阀芯位置，指定为物理信号。

## 参数

### **Number of pressure ports** — 先导压力端口数量 `3`（默认）| `4`

先导压力端口的数量。端口 **X** 测量阀芯端部的压力。将此参数设置为 `4` 会启用额外的先导侧端口 **Y**。

### **Port A poppet area** — 端口 A 的横截面积 `1e-4 m^2`（默认）| 正标量

端口 **A** 的横截面积。

### **Port A poppet to port X pilot area ratio** — 入口与先导端口面积之比 `0.5`（默认）| 正标量

入口端口 **A** 与先导压力端口 **X** 的面积之比。此值用于计算端口 **X** 处的力。

### **Port Y pilot area** — 端口 Y 的横截面积 `1.5e-4 m^2`（默认）| 正标量

端口 **Y** 的横截面积。

#### 依赖关系

要启用此参数，请将 **Number of pressure ports** 设置为 `4`。

### **Spring preload force** — 初始弹簧力 `25 N`（默认）| 正标量

由于弹簧预紧而在阀中产生的弹簧力。此参数是一个阈值，当将其加到端口 **X** 和 **Y** 处的先导压力上时，可抵消由端口 **A** 和 **B** 处压力引起的阀开启。

### **Spring stiffness** — 刚度常数 `15e3 N/m`（默认）| 正标量

弹簧刚度常数。

### **Poppet stroke** — 最大阀芯伸出量 `5e-3 m`（默认）| 正标量

最大阀芯伸出量。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当活塞位置接近完全伸出或完全缩回时，会向活塞位置引入一层逐渐变化。将此值设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

### **Connected valve opening orientation** — 阀芯位移方向 `Positive displacement opens valve`（默认）| `Negative displacement opens valve`

打开连接阀的阀芯位移方向。将此参数设置为 `Positive displacement opens valve` 表示阀芯伸出。将参数设置为 `Negative displacement opens valve` 表示阀芯缩回。

### **Actuator dynamics** — 是否考虑致动过程中的瞬态 `Off`（默认）| `On`

是否考虑致动导致的滑阀位置瞬态效应。将 **Actuator dynamics** 设置为 `On` 会通过在滑阀位置中引入一阶滞后来近似执行器运动。**Actuator time constant** 也会影响建模的动力学。

### **Actuator time constant** — 活塞位移时间常数 `0.1 s`（默认）| 正标量

该常数表示活塞从一个位置移动到另一个位置时达到稳态所需的时间。此参数会影响建模的执行器动力学。

#### 依赖关系

要启用此参数，请将 **Actuator dynamics** 设置为 `On`。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2020a 中引入**

## 描述

在等温液体系统中维持阀压力与先导压力之间平衡的执行器

Cartridge Valve Actuator (IL) 模块对一种执行器进行建模，该执行器维持阀压力与先导管路压力之间的平衡。端口 **A** 和 **B** 之间的阀保持关闭，直到超过先导弹簧 **Spring preload force**，此时活塞开始移动。活塞位置作为物理信号在端口 **S** 输出。4 端口插装阀执行器的示意图如下所示。

### 执行器力平衡

执行器活塞移动以调节执行器腔室中的压力，从而维持执行器端口压力与先导管路压力之间的平衡：

pAAA+pBAB=Fpreload+Fpilot,

其中：

- *p*A 和
  *p*B 是端口 **A** 和 **B** 处的压力。
- *A*X 根据 **Port A to port X area ratio** 计算。
- 当 **Number of pressure ports** 设置为 `3` 时，*A*B 是端口 **B** 面积，AX−AA。当 **Number of pressure ports** 设置为 `4` 时，*A*B 是 AX−AA+AY。
- *F*preload 是系统中的初始弹簧力。
- 如果 **Number of pressure ports** 设置为 `3`，*F*pilot 是 pXAX；如果 **Number of pressure ports** 设置为 `4`，*F*pilot 是 pXAX+pYAY。

### 活塞位置

稳态活塞位移计算如下：

xsteady=Fεk=FA+FB−Fpilot−Fpreloadkε,

其中 *ε* 是 **Opening orientation**，它将运动分配为正方向（伸出）或负方向（缩回）。活塞位移的动态变化为：

x˙dyn=xsteady−xdynτ,

其中 *τ* 是 **Actuator time constant**。当 x˙dyn=xdynτ. 小于 **Spring preload force** 时，*x*steady = 0。

如果 x˙dyn=xdynτ. 大于预紧力与 *kx*stroke 之和，则 *x*steady = *x*stroke。

### 开启动力学

如果对开启动力学进行建模，则会向流量对建模控制压力的响应引入一个滞后。*p*control 变为动态控制压力 *p*dyn；否则，*p*control 是稳态压力。动态控制压力的瞬时变化根据 **Opening time constant** *τ* 计算：

p˙dyn=pcontrol−pdynτ.

默认情况下，**Opening dynamics** 设置为 `Off`。

### 数值平滑后的力

当执行器接近完全伸出或完全缩回时，您可以通过调整模块的 **Smoothing factor** 来保持仿真的数值稳健性。平滑函数会应用于所有计算得出的力，但主要影响活塞运动极端位置处的仿真。

归一化力为

F^=FA+FB−FPreload−FPilotkxstroke.

其中：

- *FA* 是端口 **A** 处的力。
- *FB* 是端口 **B** 处的力。
- *FPreload* 是 **Spring preload force**。
- *FPilot* 是端口 **X** 处的力。

如果 **Smoothing factor** 参数非零，则模块会将归一化力平滑地饱和在 `0` 和 `1` 之间。

有关详细信息，请参阅数值平滑。

### 假设和限制

此模块不建模内部流体体积。端口 **A**、**B**、**X** 和 **Y** 中没有质量流量。
