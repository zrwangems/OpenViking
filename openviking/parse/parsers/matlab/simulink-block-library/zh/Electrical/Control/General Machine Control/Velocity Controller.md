---
type: simulink-block
title: 'Velocity Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Machine Control'
documentation_page: 'velocitycontroller'
documentation_source_path: 'ref/velocitycontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Velocity Controller

## 端口
```yaml
ports:
- name: wRef
  summary: 期望速度标量
  direction: input
  data_types: single | double
- name: wMechanical
  summary: 实际速度标量
  direction: input
  data_types: single | double
- name: TqRefSat
  summary: 饱和参考转矩标量
  direction: input
  data_types: single | double
- name: Reset
  summary: 积分复位标量
  direction: input
  data_types: single | double
- name: TqRefUnsat
  summary: 未饱和期望转矩标量
  direction: output
  data_types: single | double
```

### 输入

### **wRef** — 期望速度标量

期望或参考速度，单位为 rad/s。

**数据类型：** `single` | `double`

### **wMechanical** — 实际速度标量

测量的机械速度，单位为 rad/s。

**数据类型：** `single` | `double`

### **TqRefSat** — 饱和参考转矩标量

用于积分抗饱和增益的饱和转矩参考值，单位为 N\*m。

**数据类型：** `single` | `double`

### **Reset** — 积分复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`
### 输出

### **TqRefUnsat** — 未饱和期望转矩标量

未饱和参考转矩，单位为 N\*m。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Control type
  summary: 控制模型 PI control（默认）| P control | P-PI control
  group: ''
- name: Controller proportional gain
  summary: 比例增益 1（默认）| 正标量
  group: ''
- name: Controller integral gain
  summary: 积分增益 1（默认）| 正标量
  group: ''
- name: P controller proportional gain
  summary: P 比例增益 1（默认）| 正标量
  group: ''
- name: Integral anti-windup gain
  summary: PI 抗饱和增益 1（默认）| 正标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 正标量
  group: ''
- name: Discretization sample time
  summary: 离散化采样时间 0.001（默认）| 正标量
  group: ''
- name: Enable zero cancellation
  summary: 前馈零点对消 off（默认）| on
  group: ''
```

### **Control type** — 控制模型 `PI control`（默认）| `P control` | `P-PI control`

控制器类型：

- `PI control` — 使用单反馈环路的比例积分控制
- `P control` — 使用单反馈环路的比例积分控制
- `P-PI control` — 使用双反馈环路的比例控制和比例积分控制

#### 依赖关系

**Control type** 选项会影响以下参数的可见性或可配置性：

- **Controller integral gain**
- **P controller proportional gain**
- **Anti-windup gain**
- **Integral anti-windup gain**
- **Sample time (-1 for inherited)**
- **Enable zero cancellation**

### **Controller proportional gain** — 比例增益 `1`（默认）| 正标量

以下控制器的比例增益：

- PI 控制器
- 单环路控制模型中的 P 控制器
- P-PI 控制器中的 PI 控制器

### **Controller integral gain** — 积分增益 `1`（默认）| 正标量

PI 或 P-PI 控制器的积分增益。

#### 依赖关系

此参数仅在 **Control type** 设置为 `PI control` 或 `P-PI
control` 时可见。

### **P controller proportional gain** — P 比例增益 `1`（默认）| 正标量

P-PI 控制器中 P 控制器的比例增益。

#### 依赖关系

此参数仅在 **Control type** 设置为 `P-PI control` 时可见。

### **Integral anti-windup gain** — PI 抗饱和增益 `1`（默认）| 正标量

PI 控制器的抗饱和增益。

#### 依赖关系

此参数仅在 **Control type** 设置为 `PI control` 或 `P-PI
control` 时可见。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

#### 依赖关系

此参数仅在 **Control type** 设置为 `PI control` 或 `P-PI
control` 时可见。

### **Discretization sample time** — 离散化采样时间 `0.001`（默认）| 正标量

连续离散化之间的时间，单位为 s。零点对消需要离散化。

#### 依赖关系

此参数仅在满足以下所有条件时可见：

- **Control type** 设置为 `PI
  control` 或 `P-PI
  control`。
- **Sample time** 设置为
  `-1`。
- **Enable zero cancellation** 已选中。

### **Enable zero cancellation** — 前馈零点对消 `off`（默认）| `on`

在前馈路径上使用零点对消的选项。

#### 依赖关系

**Enable zero cancellation** 参数仅在 **Control type** 设置为 `PI
control` 或 `P-PI control` 时可见。

**Discretization sample time** 参数仅在 **Enable zero cancellation** 已选中时可见。
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

Velocity Controller 模块在离散时间中实现速度控制器。

您将测量的和参考的转子速度（*w* 和
*wref*）作为输入提供给该模块。然后，该模块为
电力驱动输出参考转矩 *Tref*。

为防止积分器中的饱和，将来自电力驱动的饱和参考
转矩 *Tref\_sat* 反馈
到速度控制器。

### 方程

您可以使用以下三种常见方法之一，通过离散采样时间
*Ts* 控制转子角速度：

- 比例积分（PI）控制，具有比例和积分
  增益 *Kp\_w* 和
  *Ki\_w*：

  Tref=(Kp\_w+Ki\_wTszz−1)(wref−w)
- 比例（P）控制，具有比例增益
  *Kp\_w*：

  Tref=Kp\_w(wref−w)
- P-PI 控制，其特征在于双速度反馈环路，如下图所示：

  此处，PI Controller 模块的结构与
  PI 控制策略中相同，*Kv* 是
  P 控制器的比例增益。

**零点对消**

使用 PI 控制会在闭环传递函数中产生一个零点，这
可能导致闭环响应中出现不期望的超调。该零点可以通过在前馈路径中引入零点对消模块来
对消。离散时间中的
零点对消传递函数为

GZC\_w(z)=TsKi\_wKp\_wz+(Ts−Kp\_wKi\_wKp\_wKi\_w)
