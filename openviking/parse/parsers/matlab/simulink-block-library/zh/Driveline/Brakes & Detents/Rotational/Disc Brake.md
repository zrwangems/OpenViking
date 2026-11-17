---
type: simulink-block
title: 'Disc Brake'
family: 'vdynblks'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes'
documentation_page: 'discbrake'
documentation_source_path: 'ref/discbrake.html'
language: zh-CN
chinese_source: worker-translation
---

# Disc Brake

## 端口
```yaml
ports:
- name: P
  summary: 缸压物理信号
  direction: input
- name: S
  summary: 轴旋转机械
  direction: input
- name: H
  summary: 热
  direction: input
```

### 输入

### **P** — 缸压物理信号

与缸压相关联的物理信号端口，单位为
bar。
### 守恒

### **S** — 轴旋转机械

与轴相关联的旋转机械守恒端口。

### **H** — 热

与热流相关联的热守恒端口。

#### 依赖关系

此端口仅在
**Friction** 设置中，**Thermal
Port** 参数设置为
`Model` 时可见。

暴露此端口会使相关参数和变量
可见。
## 参数
```yaml
parameters:
- name: Mean pad radius
  summary: 摩擦片半径 150 mm（默认）| 正标量
  group: 几何
- name: Cylinder bore
  summary: 缸径 10 mm（默认）| 正标量
  group: 几何
- name: Number of brake pads
  summary: 摩擦片数量 2（默认）| 正整数标量
  group: 几何
- name: Thermal port
  summary: 热模型 Omit（默认）| Model
  group: 摩擦
- name: Temperature
  summary: 温度 [280, 300, 320] K（默认）| 递增向量
  group: 摩擦
- name: Static friction coefficient
  summary: 静摩擦 0.9（默认）| 标量
  group: 摩擦
- name: Static friction coefficient vector
  summary: 静摩擦 [.9, .8, .7] | 向量
  group: 摩擦
- name: Coulomb friction coefficient
  summary: 接触摩擦 0.7（默认）| 正标量
  group: 摩擦
- name: Coulomb friction coefficient vector
  summary: 接触摩擦 [.8, .7, .6]（默认）| 正值的递增向量
  group: 摩擦
- name: Breakaway friction velocity
  summary: 摩擦阈值 0.1 rad/s（默认）| 标量
  group: 摩擦
- name: Viscous friction coefficient
  summary: 粘性摩擦 0 N*m/(rad/s)（默认）| 非负标量
  group: 摩擦
- name: Brake pressure fault
  summary: 对制动压力故障建模的选项 Add fault
  group: 故障
- name: Brake pressure when faulted
  summary: 设置故障时的制动压力 0 bar（默认）| 正标量
  group: 故障
- name: Thermal mass
  summary: 对温度变化的阻力 50 kJ/K（默认）| 标量
  group: 热端口
```

### 几何

### **Mean pad radius** — 摩擦片半径 `150` `mm`（默认）| 正标量

摩擦片的平均半径。

### **Cylinder bore** — 缸径 `10` `mm`（默认）| 正标量

活塞的直径。

### **Number of brake pads** — 摩擦片数量 `2`（默认）| 正整数标量

摩擦片的数量。

### 摩擦

### **Thermal port** — 热模型 `Omit`（默认）| `Model`

热流和温度变化的模型：

- `Omit` — 忽略热
  动力学。
- `Model` — 包含热
  动力学。

#### 依赖关系

当此参数设置为 `Model` 时，
热端口及相关参数和变量
可见。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

用于构建一维温度-效率查找表的温度数组。数组值必须从左到右递增。

#### 依赖关系

此参数仅在 **Thermal
Port** 参数设置为
`Model` 时可见。

### **Static friction coefficient** — 静摩擦 `0.9`（默认）| 标量

静摩擦系数。为此参数指定的值必须大于为
**Coulomb friction coefficient** 参数指定的值。

#### 依赖关系

此参数仅在 **Thermal
Port** 参数设置为
`Omit` 时可见。

### **Static friction coefficient vector** — 静摩擦 `[.9, .8, .7]` | 向量

静摩擦系数，满足：

- 向量中的元素数量必须与
  **Temperature** 参数指定向量中的元素数量相同
- 这些值必须大于为 **Coulomb friction
  coefficient vector** 参数指定的对应值。

#### 依赖关系

此参数仅在 **Thermal
Port** 参数设置为
`Model` 时可见。

### **Coulomb friction coefficient** — 接触摩擦 `0.7`（默认）| 正标量

制动带-制动鼓接触面的库仑摩擦系数。该值必须大于零。

#### 依赖关系

此参数仅在 **Thermal
Port** 参数设置为
`Omit` 时可见。

### **Coulomb friction coefficient vector** — 接触摩擦 `[.8, .7, .6]`（默认）| 正值的递增向量

制动带-制动鼓接触面的库仑摩擦系数，满足：

- 向量中的元素数量必须与
  **Temperature** 参数指定向量中的元素数量相同
- 这些值从左到右递增。
- 每个值必须大于零。

#### 依赖关系

此参数仅在 **Thermal
Port** 参数设置为
`Model` 时可见。

### **Breakaway friction velocity** — 摩擦阈值 `0.1` `rad/s`（默认）| 标量

摩擦从静摩擦切换为动摩擦时的角速度。

### **Viscous friction coefficient** — 粘性摩擦 `0` `N*m/(rad/s)`（默认）| 非负标量

对于湿式制动器，粘性摩擦表示离合器片之间冷却/润滑流体的能量损失。要对湿式制动器建模，请为粘性摩擦系数指定非零值。默认值表示干式制动器。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击
**Open fault properties**。在 Property Inspector 中，点击
**Fault behavior** 链接以打开故障。

### **Brake pressure fault** — 对制动压力故障建模的选项 `Add fault`

是否在模块中对故障建模。要添加故障，请点击
**Add fault** 超链接。

### **Brake pressure when faulted** — 设置故障时的制动压力 `0` `bar`（默认）| 正标量

触发故障时的制动带力。当您触发故障时，模块在仿真剩余时间内应用
**Brake pressure when
faulted** 参数的值，而不是端口
**P** 处的值。当该值为 `0` 时，不发生制动。当该值相对较大时，制动器卡死。

#### 依赖关系

要启用此参数，请点击
**Add fault** 超链接为模块启用故障。

### 热端口

### **Thermal mass** — 对温度变化的阻力 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的阻力越大。

#### 依赖关系

此参数仅在
**Friction** 设置中，**Thermal
Port** 参数设置为
`Model` 时可见。
## 所属库

Simscape / Driveline / Brakes & Detents / Rotational

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

Disc Brake 模块现在支持 Simscape 故障接口。要了解更多信息，
请参阅 Introduction to Simscape Faults。

## 描述

带施加压力缸和摩擦片的摩擦制动器

Disc Brake 模块表示一种制动器，其布置为气缸对一个或多个可与轴转子接触的摩擦片施加压力。来自气缸的压力使摩擦片对轴施加摩擦力矩。摩擦力矩阻碍轴旋转。

### Disc Brake 模型

下图显示了盘式制动器的侧视图和前视图。

盘式制动器将来自制动气缸的制动缸压力转换为力。盘式制动器在制动片平均半径处施加该力。

模块用于计算制动扭矩的方程取决于车轮速度 *Ω*，因此当 Ω≠0 时，

T=μkPπDb2RmN4。

然而当 Ω=0 时，制动器施加的扭矩等于外部施加的用于车轮旋转的扭矩。当 Ω=0 时，制动器可施加的扭矩最大值为

T=μsPπDb2RmN4。

在两种情况下，Rm=Ro+Ri2。

其中：

- *T* 是制动扭矩。
- *P* 是施加的制动压力。
- *Ω* 是车轮速度。
- *N* 是盘式制动器总成中制动片的数量。
- *μs* 是制动片-转子的静摩擦系数。
- *μk* 是制动片-转子的动摩擦系数。
- *Db* 是制动执行器缸径。
- *Rm* 是制动片在制动转子上施加力的平均半径。
- *Ro* 是制动片的外半径。
- *Ri* 是制动片的内半径。

模块默认对干式制动器建模。您可以通过将 **Viscous friction coefficient**、*k*v 设置为非零值来对湿式制动器中的流体摩擦建模。湿式制动系统中车轮上的扭矩为：

Twet=T+kvΩ。

### 故障

要对 Disc Brake 模块中的故障建模，请在
**Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的更多信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，模块在仿真剩余时间内应用 **Brake
pressure when faulted** 参数的值，而不是端口
**P** 处的值。当该值为 `0` 时，不发生制动。当该值相对较大时，制动器卡死。

### 热模型

您可以通过暴露可选热端口来对热流和温度变化的影响建模。要暴露该端口，请在 **Friction** 设置中，将 **Thermal Port** 参数设置为 `Model`。暴露该端口还会暴露或更改以下相关设置、参数和变量的默认值：

- **Friction** > **Temperature**
- **Friction** > **Static friction coefficient vector**
- **Friction** > **Coulomb friction coefficient vector**
- **Thermal Port** > **Thermal mass**
- **Variables** > **Temperature**
