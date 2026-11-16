---
type: simulink-block
title: 'Velocity Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control\u200b'
documentation_page: 'velocitycontroller'
documentation_source_path: 'ref/velocitycontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Velocity Controller

## 端口

### 输入

### **wRef** — 期望速度标量

期望或参考速度，单位为 rad/s。

**数据类型：** `single` | `double`

### **wMechanical** — 实际速度标量

测量的机械速度，单位为 rad/s。

**数据类型：** `single` | `double`

### **TqRefSat** — 饱和参考转矩标量

用于积分抗饱和增益的饱和转矩参考，单位为
N\*m。

**数据类型：** `single` | `double`

### **Reset** — 积分复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`
### 输出

### **TqRefUnsat** — 未饱和期望转矩标量

未饱和参考转矩，单位为 N\*m。

**数据类型：** `single` | `double`

## 参数

### **Control type** — 控制模型 `PI control`（默认）| `P control` | `P-PI control`

控制器类型：

- `PI control` — 比例-积分控制
  使用单反馈环路
- `P control` — 比例-积分控制
  使用单反馈环路
- `P-PI control` — 比例控制和
  比例-积分控制，使用双反馈环路

#### 依赖关系

**Control type** 选项会影响这些参数的可见性或可配置性：

- **Controller integral gain**
- **P controller proportional gain**
- **Anti-windup gain**
- **Integral anti-windup gain**
- **Sample time (-1 for inherited)**
- **Enable zero cancellation**

### **Controller proportional gain** — 比例增益 `1`（默认）| 正标量

比例增益，用于：

- PI 控制器
- 单环路控制模型中的 P 控制器
- P-PI 控制器中的 PI 控制器

### **Controller integral gain** — 积分增益 `1`（默认）| 正标量

PI 或 P-PI 控制器的积分增益。

#### 依赖关系

仅当 **Control type** 设置为 `PI control` 或 `P-PI control` 时，此参数才可见。

### **P controller proportional gain** — P 比例增益 `1`（默认）| 正标量

P-PI 控制器中 P 控制器的比例增益。

#### 依赖关系

仅当 **Control type** 设置为 `P-PI control` 时，此参数才可见。

### **Integral anti-windup gain** — PI 抗饱和增益 `1`（默认）| 正标量

PI 控制器的抗饱和增益。

#### 依赖关系

仅当 **Control type** 设置为 `PI control` 或 `P-PI control` 时，此参数才可见。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，则通过将此参数设置为 `-1` 来继承采样时间。如果此模块位于连续可变步长模型中，则使用正标量显式指定采样时间。

#### 依赖关系

仅当 **Control type** 设置为 `PI control` 或 `P-PI control` 时，此参数才可见。

### **Discretization sample time** — 用于离散化的采样时间 `0.001`（默认）| 正标量

连续离散化之间的时间，单位为 s。零点抵消需要离散化。

#### 依赖关系

仅当满足以下所有条件时，此参数才可见：

- **Control type** 设置为 `PI control` 或 `P-PI control`。
- **Sample time** 设置为 `-1`。
- 选中 **Enable zero cancellation**。

### **Enable zero cancellation** — 前馈零点抵消 `off`（默认）| `on`

在前馈路径上使用零点抵消的选项。

#### 依赖关系

仅当 **Control type** 设置为 `PI control` 或 `P-PI control` 时，**Enable zero cancellation** 参数才可见。

仅当选中 **Enable zero cancellation** 时，**Discretization sample time** 参数才可见。

## 所属库

Simscape / Electrical / Control / General Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

离散时间速度控制器

Velocity Controller 模块以离散时间实现速度控制器。

您将测量和参考转子速度（*w* 和 *wref*）作为输入提供给该模块。然后，该模块为电气驱动器输出参考转矩 *Tref*。

为防止积分器中的积分饱和，将来自电气驱动器的饱和参考转矩 *Tref\_sat* 反馈回速度控制器。

### 方程

您可以使用以下三种常见方法之一，以离散采样时间 *Ts* 控制转子角速度：

- 比例-积分（PI）控制，具有比例增益和积分增益 *Kp\_w* 和 *Ki\_w*：

  Tref=(Kp\_w+Ki\_wTszz−1)(wref−w)
- 比例（P）控制，具有比例增益 *Kp\_w*：

  Tref=Kp\_w(wref−w)
- P-PI 控制，其特征在于双重速度反馈环路，如下图所示：

  此处，PI Controller 模块的结构与 PI 控制策略中的结构相同，*Kv* 是 P 控制器的比例增益。

**零点抵消**

使用 PI 控制会在闭环传递函数中产生一个零点，这可能导致闭环响应中出现不期望的超调。可以通过在前馈路径中引入零点抵消模块来抵消该零点。离散时间中的零点抵消传递函数为

GZC\_w(z)=TsKi\_wKp\_wz+(Ts−Kp\_wKi\_wKp\_wKi\_w)
