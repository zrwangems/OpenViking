---
type: simulink-block
title: 'Bearing'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'bearing'
documentation_source_path: 'ref/bearing.html'
language: zh-CN
chinese_source: worker-translation
---

# Bearing

## 端口

### 输入

### **Load** — 可变载荷输入，N 物理信号

与轴承上的载荷相关联的物理信号输入端口，单位为 N。

#### 依赖

要启用此端口，请将 **Radial load specification** 设置为 `Variable`。
### 守恒

### **B** — 基座机械旋转

与轴基座端相关联的机械旋转守恒端口。

### **F** — 从动机械旋转

与轴从动端相关联的机械旋转守恒端口。此端口保持与端口 **B** 相同的角速度。

#### 依赖

要启用此端口，请选中 **Enable follower port**。

### **C** — 壳体机械旋转

与轴承壳体相关联的机械旋转守恒端口。启用此端口后，模块假定壳体参考为静止。

#### 依赖

要启用此端口，请选中 **Enable case port**。

## 参数

### 机械特性

### **Bearing type** — 轴承选项 `Ball or Roller`（默认）| `Journal`

模块在仿真期间所表现的轴承类型。

### **Enable follower port** — 从动端口选项 `off`（默认）| `on`

是否启用从动端口。

### **Enable case port** — 壳体端口选项 `off`（默认）| `on`

是否启用壳体端口。

### **Radius** — 轴承界面半径 `30` `mm`（默认）| 正标量

轴承与轴之间界面的半径。

### **Length** — 轴承界面长度 `100` `mm`（默认）| 正标量

轴承与轴之间界面的长度。

### **Radial load specification** — 控制径向载荷的选项 `Constant`（默认）| `Variable`

模块使用恒定载荷还是通过 **Load** 端口指定可变载荷。

### **Load on bearing** — 恒定轴承载荷 `10` `N`（默认）| 正标量

轴施加在轴承上的恒定载荷。

#### 依赖

要启用此参数，请将 **Radial load specification** 设置为 `Constant`。

### **Force threshold** — 载荷阈值 `0.001` `N`（默认）

模块向轴承施加载荷时所超过的载荷阈值。

#### 依赖

要启用此参数，请将 **Radial load specification** 设置为 `Variable`。

### **Angular velocity threshold** — 角速度阈值 `0.001` `rev/s`（默认）

模块施加轴承摩擦力时所超过的角速度阈值。

#### 依赖

要启用此参数，请将 **Bearing type** 设置为 `Ball or Roller`。

### **Coefficient of friction specification** — 指定摩擦系数的选项 `Constant`（默认）| `Variable`

模块摩擦系数是恒定的还是随轴承速度变化。

#### 依赖

要启用此参数，请将 **Bearing type** 设置为 `Ball or Roller`，并将 **Coefficient of friction specification** 设置为 `Constant`。

### **Coefficient of friction** — 摩擦系数 `0.002`（默认）| 正标量

恒定摩擦系数。

#### 依赖

要启用此参数，请将 **Coefficient of friction specification** 设置为 `Constant`。

### **Interpolation method** — 断点值之间的插值方法 `Linear`（默认）| `Smooth`

用于查找表断点插值的方法。模块使用 `tablelookup` 函数，通过数组数据将输入值映射到输出值来建模非线性：

- `Linear` — 选择此选项以获得最低的计算成本。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

### **Extrapolation method** — 处理超出断点数据集范围的输入值的方法 `Linear`（默认）| `Nearest` | `Error`

用于查找表断点外推的方法。当输入值超出参数列表指定的范围时，此方法确定输出值。该模块使用 `tablelookup` 函数，通过数组数据将输入值映射到输出值来建模非线性：

- `Linear` — 选择此选项可生成在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不高于数据中最高点或不低于数据中最低点的外推。
- `Error` — 当希望数据位于表范围内时，选择此选项可避免外推。如果输入信号超出表范围，仿真将停止并生成错误。

### **Bearing angular speed vector, ω** — 轴承角速度 `[10, 2500, 5000, 10000, 25000]` `rpm`（默认）| 长度为 *N* 的向量

轴承角速度。

### **Coefficient of friction, f(ω)** — 摩擦系数 `[.004, .001, .0005, .00025, .000125]`（默认）| 长度为 *N* 的向量

给定轴承角速度下的摩擦系数。此向量中的元素必须与 **Bearing angular speed vector, ω** 参数一一对应。

### Fluid Properties

要启用这些参数，请将 **Bearing type** 设置为 `Journal`。

### **Customize friction curve** — 用于自定义轴承摩擦曲线的选项 `off`（默认）| `on`

是否自定义轴承摩擦曲线。

#### 依赖关系

要启用此参数，请将 **Bearing type** 设置为 `Journal`。

### **Dynamic viscosity** — 润滑剂动力粘度 `0.29` `Pa*s`（默认）| 正标量

轴承润滑剂的动力粘度。

#### 依赖关系

要启用此参数，请将 **Bearing type** 设置为 `Journal`。

### **Minimum coefficient of friction** — 最小摩擦系数 `0.002`（默认）| 正标量

该模块对任何角速度使用的最低摩擦系数。

#### 依赖关系

要启用此参数，请将 **Bearing type** 设置为 `Journal`。

### **Bearing Modulus** — 滑动轴承模数 `7.2519e-08` `rev`（默认）| 正标量

滑动轴承模数。

#### 依赖关系

要启用此参数，请将 **Bearing type** 设置为 `Journal` 并选择 **Customize friction curve**。

### **Normalized Hersey number vector** — 归一化 Hersey 数 `[.4306, .6124, .6651, .7512, .866, 1, 1.1962, 1.4354, 3.8517]`（默认）| 长度为 *M* 的向量

归一化 Hersey 数。

#### 依赖关系

要启用此参数，请将 **Bearing type** 设置为 `Journal` 并选择 **Customize friction curve**。

### **Normalized viscous coefficient vector** — 归一化粘性摩擦系数 `[3.6621, 1.672, 1.3397, 1.1811, 1.0743, 1, 1.0358, 1.1173, 2.2792]`（默认）| 长度为 *M* 的向量

归一化粘性摩擦系数。此向量中的元素与 **Normalized Hersey number vector** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Bearing type** 设置为 `Journal` 并选择 **Customize friction curve**。

### **Interpolation method** — 断点值之间的插值方法 `Linear`（默认）| `Smooth`

用于查找表断点插值的方法。该模块使用 `tablelookup` 函数，通过数组数据将输入值映射到输出值来建模非线性：

- `Linear` — 选择此选项可实现最低的计算成本。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

#### 依赖关系

要启用此参数，请将 **Bearing type** 设置为 `Journal` 并选择 **Customize friction curve**。

### **Extrapolation method** — 处理超出断点数据集范围的输入值的方法 `Linear`（默认）| `Nearest` | `Error`

用于查找表断点外推的方法。此方法确定当输入值超出参数列表中指定的范围时的输出值。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可生成一条在插值区域中外推区域及边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不高于数据中最高点或不低于数据中最低点的外推。
- `Error` — 当您希望数据位于表范围内时，选择此选项可避免外推。如果输入信号超出表的范围，仿真将停止并生成错误。

#### 依赖关系

要启用此参数，请将 **Bearing type** 设置为 `Journal`，并选择 **Customize friction curve**。

### 故障

要修改故障，请创建一个故障，然后在模块对话框中点击 **Open fault properties**。在 Property Inspector 中，点击 **Fault behavior** 链接以打开故障。

### **Damping fault** — 用于对轴承故障建模的选项 `Add fault`

是否对轴承中的故障进行建模。要添加故障，请点击 **Add fault** 超链接。

### **Faulted damping coefficient multiplier** — 阻尼乘数 `5`（默认）| 正标量

触发故障时的阻尼系数。

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为该模块启用故障。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL Code Generation 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

## 版本历史

**在 R2023a 中引入**

### R2024a：使用 Simscape faults 接口对故障建模

Bearing 模块现在支持 Simscape faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

为自由旋转轴提供跨轴支撑的轴承

Bearing 模块表示球轴承或滚子轴承，或滑动轴承。这些轴承在横向平面内约束轴，因此轴只能在轴承中轴向旋转。由于摩擦，轴承还会向系统贡献扭矩。您可以通过仅将网络连接到端口 **B**，或通过使用端口 **B** 和 **F** 将轴承与其他组件串联，将轴承摩擦添加到机械旋转网络中。

您可以对轴承施加恒定载荷或可变载荷 *F*。当您将 **Radial load specification** 设置为 `Constant` 时，模块使用 **Load on bearing** 参数的值。当您将 **Radial load specification** 设置为 `Variable` 时，模块从端口 **Load** 接收物理信号输入，并对该信号进行平滑处理，使得

F=(Finput2+FThr2)1/2,

其中：

- *Finput* 是 **Load** 端口处的物理信号输入。
- *FThr* 是 **Force threshold** 参数。

模块计算摩擦产生的扭矩，使得

Tf=μ⋅F⋅r,

其中：

- *μ* 是摩擦系数。
- *Ff* 是作用在轴承上的摩擦力。
- *r* 是 **Bearing radius** 参数。

模块如何计算 *μ* 取决于您所仿真的轴承类型。

### 球轴承或滚子轴承

当您将 **Bearing type** 设置为 `Ball or
Roller` 时，该模块根据 **Coefficient of friction specification**
参数计算总摩擦系数。当您将此参数设置为 `Constant` 时，该模块在整个仿真过程中计算恒定的摩擦系数。该模块使用双曲正切函数来平滑过零过渡。
当您将 **Coefficient of friction specification** 设置为
`Variable` 时，该模块使用一维查找表，其中
*μ* 随角速度 *ɷ* 变化，使得

μ=tablelookup(ω⇀,μ⇀,ω,interpolation=interp\_method\_1,extrapolation=extrap\_method\_1),

其中：

- ω⇀ 是 **Bearing angular speed vector,
  N** 参数。
- μ⇀ 是 **Coefficient of friction,
  f(N)** 参数。

该模块默认使用线性插值和外推。您可以使用 **Interpolation method** 和 **Extrapolation
method** 参数分别更改插值和外推。

### 滑动轴承

当您将 **Bearing type** 设置为 `Journal` 时，该模块使用 Hersey 数查找表来定义摩擦系数，使得

μ=tablelookup(H⇀⋅K,μ⇀⋅μmin,H,interpolation=interp\_method\_2,extrapolation=extrap\_method\_2),

其中：

- H⇀ 是可选 **Normalized Hersey number
  vector** 参数。
- μ⇀ 是可选 **Normalized viscous
  coefficient vector** 参数。
- *K* 是轴承模数，即 *H* 在
  *μmin* 出现处的值。
- *μmin* 是
  **Minimum coefficient of friction**
  参数。

该模块将轴承特性数（即 Hersey 数）定义为

H=μωP,

其中 *P* 是轴承润滑剂压力，使得

P=F2rl,

其中 *r* 是 **Radius**
参数，*l* 是 **Length**
参数。

### 故障

要在 Bearing 模块中对故障建模，请在
**Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当该模块发生故障时，它会使用
**Faulted damping coefficient multiplier** 参数的值来增加轴承摩擦。当
您触发故障时，该模块计算摩擦系数，使得

μfault=μ⋅fault factor,

其中 *fault factor* 是 **Faulted
damping coefficient multiplier** 参数。

### 假设和限制

该模块假设轴承润滑剂是具有零滑移边界条件的牛顿流体。
