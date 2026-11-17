---
type: simulink-block
title: 'Air Muscle Actuator (G)'
family: 'gas'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Actuators'
documentation_page: 'airmuscleactuatorg'
documentation_source_path: 'ref/airmuscleactuatorg.html'
language: zh-CN
chinese_source: worker-translation
---

# Air Muscle Actuator (G)

## 端口

### 守恒

### **A** — 执行器入口气体

用于给执行器加压的气体开口。将此端口连接到执行器的压力源。该端口处的压力控制执行器产生的力。

### **R** — 执行器端盖机械平移

两个端盖之一，执行器力施加于该端盖。将此端口连接到要安装执行器的固定装置，或连接到执行器要移动的负载。

### **C** — 执行器端盖机械平移

两个端盖之一，执行器力施加于该端盖。将此端口连接到要安装执行器的固定装置，或连接到执行器要移动的负载。

### **H** — 执行器壁热

执行器气体体积与其周围环境之间的热边界条件。将此端口连接到 Thermal 域中的模块，以例如捕捉传导、对流或辐射传热，或将执行器与环境隔热。

## 参数

### **Initial actuator length** — 空载且未加压时端盖之间的距离 `0.575 m`（默认）| 以长度单位表示的正标量

执行器处于松弛状态（即既空载又未加压）时其端盖之间的距离。在仿真期间给执行器充气会使其变宽并同时缩短。执行器比其编织层短，也就是说，其初始长度应小于 **Unstretched braid length** 参数。

### **Unstretched braid length** — 空载时拉直编织层的长度 `0.65 m`（默认）| 以长度单位表示的正标量

编织层在将其圈数拉直并移除任何载荷后测得的长度。如果编织层是弹性的，其（共同）长度将在仿真期间随压力和负载变化。由于编织层围绕执行器的纵轴缠绕，其长度始终大于 **Initial actuator length** 参数。

### **Number of turns per braid** — 编织层围绕执行器长度轴所做的圈数 `4.7`（默认）| 正的无量纲标量

一条编织层从一个端盖到另一个端盖围绕执行器纵轴所做的圈数。

### **Braid stretching** — 选择是否为编织层的拉伸建模 `Inelastic braids`（默认）| `Elastic braids`

选择是否对编织层的拉伸建模。默认选项 `Inelastic braids` 将编织层视为柔性的但不可伸展。这是原始 Chou-Hannaford 方程中隐含的假设。此时编织层的长度在仿真期间保持恒定。

替代选项 `Elastic braids` 允许编织层随执行器负载和压力而伸展。此时编织层的长度在仿真期间被视为可变的。此更改会为力的 Chou-Hannaford 方程添加一个修正项。

### **Thickness of braided shell and bladder** — 外壳和气囊的组合厚度 `0.075 m`（默认）| 以长度单位表示的正标量

编织外壳及其内部气囊的厚度之和。有限厚度会为力的 Chou-Hannaford 方程添加一个修正项。（在原始 Chou-Hannaford 方程中，假设外壳和气囊为无限薄。）

### **Cross-sectional area at port A** — 气体端口处垂直于流动的面积 `0.01 m`（默认）| 以长度单位表示的正标量

执行器气体端口处垂直于流动的面积。

### **Total number of braids** — 编织外壳中的编织层数量 `80`（默认）| 正的无量纲标量

围绕气囊的外壳中编织层的数量。由于每条编织层都是一束相互缠绕的股线，编织层数量通常不与股线数量相同。

#### 依赖关系

当 **Braid stretching** 选项设置为 `Elastic Braids` 时，此参数生效。

### **Number of strands per braid** — 一条编织层中单根股线的数量 `3`（默认）| 正的无量纲标量

一条编织层中单根股线的数量。此数量与 **Total number of braids** 参数的乘积给出外壳中的股线总数。

#### 依赖关系

当 **Braid stretching** 选项设置为 `Elastic Braids` 时，此参数生效。

### **Strand diameter** — 股线的直径 `0.25 m`（默认）| 以长度单位表示的正标量

一根股线沿其长度的平均直径。

#### 依赖关系

当 **Braid stretching** 选项设置为 `Elastic Braids` 时，此参数生效。

### **Young's modulus of strands** — 股线在压力下伸展的程度 `3e9 GPA`（默认）

股线材料的杨氏弹性模量。此参数确定股线在压力下伸展的程度。

#### 依赖关系

当 **Braid stretching** 选项设置为 `Elastic Braids` 时，此参数生效。

### **Environment pressure specification** — 执行器外部的压力条件 `Atmospheric pressure`（默认）| `Specified pressure`

执行器紧邻周围的压力条件。执行器中的表压相对于此压力获得。选择 `Atmospheric pressure` 以使用 Two-Phase Fluid Properties (2P) 模块中指定的大气压值，或选择 `Specified pressure` 以使用不同的压力。

### **Environment pressure** — 执行器外部的绝对压力 `0.101325`（默认）| 以压力单位表示的标量

执行器紧邻周围的绝对压力。当端口 **A** 处的表压（相对于此值测量）大于零时，执行器收缩。

#### 依赖关系

当 **Environment pressure specification** 选项设置为 `Specified pressure` 时，此参数生效。

### **Contact stiffness of braids at full muscle contraction or extension** — 执行器运动限值处接触力的刚度系数 `1e6 N/m`（默认）

执行器运动范围限值处接触力的刚度系数。接触力防止执行器伸展或收缩超过其物理限值。接触力使用弹簧-阻尼系统建模。弹簧元件添加一个恢复力，一旦端盖达到任一运动限值，该力会将端盖拉回。

有关力模型的详细信息，请参阅 Translational Hard Stop 模块。

### **Contact damping of braids at full muscle contraction or extension** — 执行器运动限值处接触力的阻尼系数 `1e4 N/(m/s)`（默认）

执行器运动范围限值处接触力的阻尼系数。接触力防止执行器伸展或收缩超过其物理限值。此力使用弹簧-阻尼系统建模。一旦端盖达到运动限值，阻尼器会向端盖添加粘性力，使其减速至停止。

有关力模型的详细信息，请参阅 Translational Hard Stop。

## 所属库

Simscape / Fluids / Gas / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

具有生物肌肉力特性的线性执行器

Air Muscle Actuator (G) 模块对一种在机器人技术中流行的线性执行器建模，其特性让人联想到生物肌肉。该执行器由编织外壳内的可膨胀气囊组成。当气囊加压时，二者变宽并同时缩短，在端盖处产生收缩力。气囊在气体端口 **A** 处加压；力施加在机械平移端口 **R** 和 **C** 处。

**松弛状态下的气动肌肉**

气动肌肉通常成对安装——一块肌肉作为主动肌，另一块作为拮抗肌。这种成对结构在人体中很常见，其中（手臂中的）肱二头肌与肱三头肌相伴，而（腿部的）股四头肌与腘绳肌相伴。肌肉一端附着在关节上，但带有偏移以产生扭矩。当净扭矩不为零时，如果负载条件允许，关节会旋转。

### 执行器力

执行器的质量和能量平衡如 Translational Mechanical Converter (G) 模块所述。然而，执行器力基于标准 Chou-Hannaford 方程（针对原始模型的简化假设进行了两项修正）。在其原始形式中，Chou-Hannaford 方程给出：

FC-H=πDM2P4[3(Ll)2−1],

其中：

- *F* 是执行器施加在其端部的收缩力。下标 `C-H` 表示原始 Chou-Hannaford 模型的理论值。
- *D* 是气囊和外壳组件的直径。下标 `M` 表示其最大理论值——即外壳的编织层与其纵轴成直角时的值。
- *P* 是气囊中的表压（相对于执行器外部环境测量）。
- *L* 是执行器的长度（机械端口 **R** 和 **C** 之间的距离。
- *l* 是一条编织层的自然长度（在加压气囊中拉伸之前）。由于编织层围绕执行器的纵轴缠绕，它们总是比执行器本身长）。

执行器的最大理论直径定义为：

DM=lnπ,

其中 *n* 是一条编织层围绕执行器纵轴所做的圈数。

Chou-Hannaford 方程中隐含的假设是气囊和外壳无限薄，以及编织层为不可拉伸的非弹性编织层。两项假设都可能降低模型精度，并在此模块中进行了修正。对编织层拉伸的修正将常数长度 *l* 替换为可变长度 *l*\*：

l\*=Cl+(Cl)2+12L2(C+1)2(C+1)+2nPD2Ed,

其中 *l* 是原始 Chou-Hannaford 方程中使用的编织层自然长度，并且：

- *C* 是编织层拉伸的修正项。
- *E* 是编织层材料的杨氏弹性模量。
- *d* 是一条编织层中股线的直径（每条编织层都是一束紧密缠绕的股线）。

编织层拉伸的修正项定义为：

C=n2π2Ed2NPlL,

其中 *N* 是编织外壳中的股线总数。对气囊和外壳厚度的修正会向总执行器力添加因子：

FT=πP[t(2D−DM2D)−t2]

其中 *t* 是气囊和外壳的总厚度，下标 `T` 表示厚度修正。总执行器力为：

F=FH-F+FT,

其中用于计算 Chou-Hannaford 项的股线长度是变量 *l*\*。在伸展和收缩极限处，此力由平移硬限位抵消。这些按 Translational Hard Stop 模块所述建模。

### 建模假设

- 气体入口（端口 **A**）与执行器内部之间没有流动阻力。
- 执行器壁（端口 **H**）与其封闭的气体之间没有热阻。
- 执行器是密封的，不会泄漏。
- 忽略摩擦和惯性的影响。
- 无论充气程度如何，气囊和外壳均为完美圆柱形。
- 忽略气囊的纵向弹性。
