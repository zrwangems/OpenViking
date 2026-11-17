---
type: simulink-block
title: 'Sun-Planet Bevel'
family: 'gears'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Subcomponents'
documentation_page: 'sunplanetbevel'
documentation_source_path: 'ref/sunplanetbevel.html'
language: zh-CN
chinese_source: worker-translation
---

# Sun-Planet Bevel

## 端口

### 守恒

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **P** — 行星齿轮旋转机械

与行星齿轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 参数

### 主要

### **行星轮 (P) 与太阳轮 (S) 齿数比 (NP/NS)** — 行星轮与太阳轮旋转比 `2`（默认）| 标量

行星齿轮与太阳轮旋转的比值 *gPS*，定义为行星齿轮齿数除以太阳轮齿数。该齿轮比必须严格大于 1。

### **装配方向** — 齿轮相对旋转方向 `Left - Sun and planet gears rotate in same direction`（默认）| `Right - Sun and planet gears rotate in opposite directions`

太阳轮和行星齿轮的相对方向及其同向旋转方向。左或右方向分别表示齿轮以相同或相反方向共同旋转。

### 啮合损耗

### **摩擦模型** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation` — 齿轮啮合是理想的。
- `Constant efficiency` — 齿轮副之间的扭矩传递按恒定效率 *η* 降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮副之间的扭矩传递由基于温度的查表定义。

### **普通效率** — 扭矩传递效率 `0.9`（默认）| 标量

行星齿轮到太阳轮齿轮副啮合的扭矩传递效率 *ηPS*。此值必须大于 `0` 且小于或等于 `1`。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`。

### **温度** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构造一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **效率** — 齿轮效率 `[.95, .9, .85]`（默认）| 向量

描述从外行星齿轮到内行星齿轮的功率流的输出-输入功率比向量，*ηPS*。该模块使用这些值构造一维温度-效率查找表。

每个元素是与 **温度** 向量中某个温度对应的效率。向量的长度必须等于 **温度** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **太阳轮-行星架功率阈值** — 太阳轮-行星架齿轮耦合的最小效率功率阈值 `0.001` `W`（默认）| 标量

功率阈值 *pth*，高于该值时全效率生效。低于此值时，双曲正切函数会平滑效率因子。

当将 **摩擦模型** 设置为 `Constant efficiency` 时，模块在没有功率传输时将效率损耗降为零。当将 **摩擦模型** 设置为 `Temperature-dependent efficiency` 时，模块会在静止时的零值与功率阈值处温度-效率查找表提供的值之间平滑效率因子。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 黏性损耗

### **太阳轮-行星架黏性摩擦系数** — 齿轮黏性摩擦 `0` `N*m/(rad/s)`（默认）| 标量

太阳轮-行星架齿轮运动的黏性摩擦系数 *μS*。

### 热端口

要启用这些设置，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **热质量** — 热质量 `50` `J/K`（默认）| 标量

使组件温度改变一个温度单位所需的热能。热质量越大，组件抵抗温度变化的能力越强。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 所属库

Simscape / Driveline / Gears / Planetary Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

由行星架以及锥形行星轮和太阳轮组成的行星齿轮组，具有可调节的齿轮比、装配方向和摩擦损耗

Sun-Planet Bevel 齿轮模块表示行星架以及锥形行星轮和太阳轮。行星轮连接到行星架并相对于行星架旋转。行星轮和太阳轮以固定齿轮比共同旋转。通过将装配方向设置为左或右来控制旋转方向。有关模型详细信息，请参阅方程。

### 热模型

通过启用可选热端口，可以对热流和温度变化的影响进行建模。要启用该端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Sun-Planet Bevel 模块对三个连接的轴施加一个运动学约束和一个几何约束：

rCωC=rSωS±rPωP

rC=rS±rP

其中：

- *rC* 是行星架齿轮的半径。
- *ωC* 是行星架齿轮的角速度。
- *rS* 是太阳轮的半径。
- *ωS* 是太阳轮的角速度。
- *rP* 是行星齿轮的半径。
- *ωP* 是行星齿轮的角速度。

行星轮-太阳轮齿轮比定义为

gPS=rPrS=NPNS,

其中：

- *gPS* 是行星轮-太阳轮齿轮比。由于 rP>rS，gPS>1。
- *NP* 是行星齿轮的齿数。
- *NS* 是太阳轮的齿数。

根据该比值，关键运动学约束为：

- ωS=gPSωP+ωC，对于左向锥齿轮组件
- ωS=−gPSωP+ωC，对于右向锥齿轮组件

三个自由度减少为两个独立自由度。齿轮对为 (1,2) = (*S*,*P*)。

**警告**

行星轮-太阳轮齿轮比 *gPS* 必须严格大于一。

扭矩传递定义为

τP=τloss−gPSτS,

其中：

- *τloss* 是扭矩损耗。
- *τs* 是太阳轮的扭矩。
- *τp* 是行星齿轮的扭矩。

在没有扭矩损耗的理想情况下，*τloss* = 0。得到的扭矩传递方程为 τP=gPSτS。

**非理想齿轮约束和损耗**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅对具有损耗的齿轮建模。

### 变量

使用 **变量** 设置可在仿真前为模块变量设置优先级和初始目标值。有关详细信息，请参阅设置模块变量的优先级和初始目标。

### 假设和限制

- 齿轮惯量假定可忽略。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅调整模型保真度。
