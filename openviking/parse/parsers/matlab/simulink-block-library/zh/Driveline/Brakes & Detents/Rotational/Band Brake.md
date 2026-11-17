---
type: simulink-block
title: 'Band Brake'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Rotational'
documentation_page: 'bandbrake'
documentation_source_path: 'ref/bandbrake.html'
language: zh-CN
chinese_source: worker-translation
---

# Band Brake

## 端口

### 输入

### **F** — 皮带张紧力物理信号

与施加到皮带上的外部张紧力相关联的物理信号输入端口。
### 守恒

### **S** — 鼓轴旋转旋转机械

与旋转鼓轴相关联的旋转守恒端口。

### **H** — 热流，单位为 W 热

与热流相关联的热守恒端口。

#### 依赖关系

仅当在**摩擦**设置中将**热端口**参数设置为
`Model` 时，此端口才可见。

暴露此端口会使相关设置可见。

## 参数

### 几何

### **Drum radius** — 接触表面半径 `150` `mm`（默认）| 正标量

鼓接触表面的半径。该参数必须大于零。

### **Wrap angle** — 接触角 `270` `deg`（默认）| 正标量

柔性皮带与旋转鼓之间的接触角。该参数必须大于零。

### 摩擦

### **Viscous friction coefficient** — 粘性摩擦 `.01` `n*m/(rad/s)`（默认）| 非负标量

皮带-鼓接触表面处的粘性摩擦系数。该参数必须大于或等于零。

### **Thermal port** — 热模型 `Omit`（默认）| `Model`

热流和温度变化的模型：

- `Omit` — 忽略热动态。
- `Model` — 包含热动态。

#### 依赖关系

当此参数设置为 `Model` 时，热端口及相关参数和变量可见。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

用于构造一维温度-效率查找表的温度数组。数组值必须从左到右递增。

#### 依赖关系

仅当**热端口**参数设置为 `Model` 时，此参数才可见。

### **Contact friction coefficient** — 库仑摩擦 `0.3`（默认）| 正标量

皮带-鼓接触表面处的库仑摩擦系数。该值必须大于零。

#### 依赖关系

仅当**热端口**参数设置为 `Omit` 时，此参数才可见。

### **Contact friction coefficient vector** — 库仑摩擦 `[.1, .05, .03]`（默认）| 正值的递增向量

皮带-鼓接触表面处的库仑摩擦系数，满足：

- 向量中的元素数量必须与**温度**参数指定向量中的元素数量相同
- 值从左到右递增。
- 每个值必须大于零。

#### 依赖关系

仅当**热端口**参数设置为 `Model` 时，此参数才可见。

### **Angular velocity threshold** — 接近稳态接触摩擦所需的旋转速度 `0.01` `rad/s`（默认）| 正标量

接触摩擦系数实际达到其稳态值时的角速度。该值必须大于零。

### 故障

要修改故障，请创建一个故障，然后在模块对话框中点击
**Open fault properties**。在 Property Inspector 中，点击
**Fault behavior** 链接以打开故障。

### **Belt tension fault** — 对皮带张力故障建模的选项 `Add fault`

是否在模块中对皮带张力故障建模。该故障将端口 **F** 处的值替换为
**Belt tension when faulted** 参数的值。要添加故障，请点击
**Add fault** 超链接。

### **Belt tension when faulted** — 故障时的皮带张力 `0` `N`（默认）| 正标量

触发故障时的皮带张力。当您触发故障时，模块在仿真的剩余时间内应用
**Belt tension when faulted** 参数的值，而不是端口
**F** 处的值。当该值为 `0` 时，不发生制动。当该值相对较大时，制动器卡住。

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。

### 热端口

### **Thermal mass** — 对温度变化的阻力 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的阻力越大。

#### 依赖关系

要启用此参数，请将 **Thermal Port** 设置为
`Model`。

## 所属库

Simscape / Driveline / Brakes & Detents / Rotational

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

Band Brake 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

带有缠绕在旋转鼓上的柔性带的摩擦制动器

Band Brake 模块表示一种摩擦制动器，其柔性带缠绕在旋转鼓的外围以产生制动作用。正的致动力使带在旋转鼓周围收紧，并使摩擦表面接触。鼓表面与柔性带之间的粘性和接触摩擦使旋转鼓减速。

您可以通过使用端口 **H**（可选的热守恒端口）来对模块的热流和温度变化效应进行建模。

带式制动器在绞车鼓、链锯、卡丁车和迷你摩托车等应用中提供高制动扭矩，但代价是制动精度降低。

### 方程

该模块使用简单制动器几何形状和摩擦参数的简单参数化。

作为使皮带收紧的外部制动致动力的函数的制动扭矩为

T=(FTB−FA)⋅rD+μvisc⋅ω

其中：

- *T* 是制动扭矩。
- *FTB* 是作用在带张紧分支上的张力。
- *FA* 是外部制动致动力。
- *rD* 是鼓半径。
- *μvisc* 是粘性摩擦系数。
- *μ* 是接触摩擦系数。
- *ϕ* 是包角。

力 *FTB* 和 *FA* 满足关系

FTBFA=eμϕ

将关系代入制动扭矩公式可消去力 *FTB*，使得

T=FA(eμϕ−1)⋅rD+μvisc⋅ω

为避免零相对速度处的不连续性，模型将致动力 *FS* 定义为双曲函数

FA=Fin⋅tanh(4ωωthreshold)

其中：

- *Fin* 是力输入信号。
- *ωthreshold* 是角速度阈值。

### 故障

要对 Band Brake 模块中的故障建模，请在
**Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的更多信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，模块在仿真的剩余时间内应用 **Belt force when faulted** 参数的值，而不是端口 **F** 处的值。当该值为 `0` 时，不发生制动。当该值相对较大时，制动器卡住。

### 热模型

您可以通过暴露可选的热端口来对热流和温度变化效应进行建模。要暴露该端口，请在**摩擦**设置中将 **Thermal Port** 参数设置为 `Model`。

### 限制和假设

该模型不考虑致动器流量消耗。
