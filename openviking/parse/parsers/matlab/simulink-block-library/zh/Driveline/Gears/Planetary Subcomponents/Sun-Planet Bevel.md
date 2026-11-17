---
type: simulink-block
title: 'Sun-Planet Bevel'
family: 'sdl'
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

### 守恒端口

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **P** — 行星齿轮旋转机械

与行星齿轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

## 参数

### 主要

### **Planet (P) to sun (S) teeth ratio (NP/NS)** — 行星齿轮与太阳齿轮的旋转比 `2`（默认）| 标量

行星齿轮与太阳齿轮旋转的比值 *gPS*，定义为行星齿轮齿数除以太阳齿轮齿数。该齿轮比必须严格大于 1。

### **Assembly orientation** — 齿轮相对旋转方向 `Left - Sun and planet gears rotate in same direction`（默认）| `Right - Sun and planet gears rotate in opposite directions`

太阳齿轮和行星齿轮的相对方向及其同向旋转方向。左或右方向分别意味着齿轮以相同或相反方向同向旋转。

### 啮合损耗

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合为理想状态。
- `Constant efficiency` — 齿轮副之间的扭矩传递
  通过恒定效率 *η* 降低，使得 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮副之间的
  扭矩传递由基于温度的查表定义。

### **Ordinary efficiency** — 扭矩传递效率 `0.9`（默认）| 标量

行星齿轮与太阳齿轮副啮合的扭矩传递效率 *ηPS*。该值必须大于
`0` 且小于或等于
`1`。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。
向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Efficiency** — 齿轮效率 `[.95, .9, .85]`（默认）| 向量

描述从外行星齿轮到内行星齿轮的功率流的输出-输入功率比向量
*ηPS*。模块使用
这些值构建一维温度-效率查找
表。

每个元素是与 **Temperature** 向量中某个温度
对应的效率。
向量的长度必须等于
**Temperature** 向量的长度。向量中的每个元素
必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Sun-carrier power threshold** — 太阳齿轮-行星架齿轮耦合的最小效率功率阈值 `0.001` `W`（默认）| 标量

功率阈值 *pth*，高于
此值时全效率生效。低于此值时，双曲
正切函数对效率因子进行平滑处理。

当您将 **Friction model** 设置为
`Constant efficiency` 时，模块在无功率传输时将
效率损耗降至零。当您将
**Friction model** 设置为
`Temperature-dependent efficiency` 时，模块
在静止时的零值与功率阈值处温度-效率查找表提供的值之间
对效率因子进行平滑处理。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency` 或
`Temperature-dependent
efficiency`。

### 粘性损耗

### **Sun-carrier viscous friction coefficient** — 齿轮粘性摩擦 `0` `N*m/(rad/s)`（默认）| 标量

太阳齿轮-行星架齿轮运动的粘性摩擦系数
*μS*。

### 热端口

要启用这些设置，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

将组件温度改变一个温度单位所需的热能。热质量越大，组件对温度
变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent
efficiency`。

## 所属库

Simscape / Driveline / Gears / Planetary Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

具有可调齿轮比、装配方向和摩擦损耗的行星架及锥形行星齿轮和太阳齿轮的行星齿轮组

Sun-Planet Bevel 齿轮模块表示一个行星架
以及锥形行星齿轮和太阳齿轮。行星齿轮连接到行星架并相对于行星架旋转。行星齿轮和太阳齿轮以固定齿轮比同向旋转。您通过将装配方向设置为左或右来控制旋转方向。有关模型
详细信息，请参见方程。

### 热模型

您可以通过启用可选热端口来建模
热流和温度变化的影响。要启用
该端口，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Sun-Planet Bevel 模块对三个连接轴施加一个
运动学约束和一个几何约束：

rCωC=rSωS±rPωP

rC=rS±rP

其中：

- *rC* 是行星架齿轮的
  半径。
- *ωC* 是行星架齿轮的
  角速度。
- *rS* 是太阳齿轮的
  半径。
- *ωS* 是太阳齿轮的
  角速度。
- *rP* 是行星齿轮的
  半径。
- *ωP* 是行星齿轮的
  角速度。

行星齿轮-太阳齿轮比定义为

gPS=rPrS=NPNS，

其中：

- *gPS* 是行星齿轮-太阳齿轮
  齿轮比。由于 rP>rS，gPS>1。

- *NP* 是行星齿轮的
  齿数。
- *NS* 是太阳齿轮的
  齿数。

根据该比值，关键运动学约束为：

- ωS=gPSωP+ωC 对于左向锥形装配
- ωS=−gPSωP+ωC 对于右向锥形装配

三个自由度简化为两个独立自由度。齿轮副为 (1,2) = (*S*,*P*)。

**警告**

行星齿轮-太阳齿轮比 *gPS*
必须严格大于 1。

扭矩传递定义为

τP=τloss−gPSτS，

其中：

- *τloss* 是扭矩
  损耗。
- *τs* 是太阳齿轮的
  扭矩。
- *τp* 是行星齿轮的
  扭矩。

在无扭矩损耗的理想情况下，*τloss* = 0。由此得到的扭矩传递方程为 τP=gPSτS。

**非理想齿轮约束和损耗**

在非理想情况下，*τloss* ≠ 0。有关更多信息，请参见 Model Gears with Losses。

### 变量

使用 **Variables** 设置可在仿真前设置模块变量的优先级和初始目标
值。有关更多信息，请参见 Set Priority and Initial Target for Block Variables。

### 假设和限制

- 假设齿轮惯量可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关更多信息，请参见 Adjust Model Fidelity。
