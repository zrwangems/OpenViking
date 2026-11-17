---
type: simulink-block
title: 'Pressure Transducer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'pressuretransducer'
documentation_source_path: 'ref/pressuretransducer.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Transducer

## 端口

### 守恒

### **A** — 压力测量 气体 | 液压 | 热液体 | 湿空气 | 两相流体 | 等温液体

与压力测量相关联的守恒流体端口。使用 **Fluid port type** 参数定义端口类型。

### **+** — 正极端子 电气

与正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与负极端子相关联的电气守恒端口。

## 参数

### **Fluid port type** — 流体端口类型 `Gas`（默认）| `Hydraulic` | `Thermal Liquid` | `Moist Air` | `Two-Phase Fluid` | `Isothermal Liquid`

流体端口类型。该值定义 **A** 守恒端口的域。

**注意**

Hydraulics 库将在未来版本中移除。请改用 Isothermal Liquid 库，将此参数设置为 `Isothermal Liquid`。

### **Pressure range** — 最大压力 `1e6` `Pa`（默认）| 正标量

传感器可测量的最大压力，单位为 Pa。

### **Operation mode** — 压力测量的参考点 `Absolute`（默认）| `Gauge` | `Sealed-Gauge`

操作模式。选择以下选项之一来定义压力测量的参考点：

- `Absolute` — 模块测量相对于零绝对压力（理想真空中的压力）的压力。
- `Gauge` — 模块测量相对于大气压力的压力。如果将 **Fluid port type** 参数设置为 `Hydraulic`，模块假定大气压力为 1 bar。在液压网络中无法更改大气压力，因为在液压域中，压力跨变量为表压。当节点值为 0 bar 时，节点处于大气压力，因此无法在网络中设置大气压力。如果要更改压力测量的参考压力，请将 **Operation mode** 参数设置为 `Sealed-Gauge`。

  对于其他流体域，可以在流体网络中设置大气压力，因为压力跨变量为绝对压力。大气压力的默认值为 0.101325 MPa。使用 Simscape™ Foundation 库中与 **Fluid port type** 参数所指定选项对应的模块来设置大气压力：

  - 对于 `Gas`，使用 Gas Properties (G) 模块。
  - 对于 `Thermal Liquid`，使用 Thermal Liquid Settings (TL) 模块。
  - 对于 `Moist Air`，使用 Moist Air Properties (MA) 模块。
  - 对于 `Two-Phase Fluid`，使用 Two-Phase Fluid Properties (2P) 模块。
  - 对于 `Isothermal Liquid`，使用 Isothermal Liquid Properties (IL) 模块。
- `Sealed-Gauge` — 模块测量相对于内部密封腔的压力。如果选择此选项，请通过设置 **Reference pressure** 参数来指定压力测量的参考点。

### **Reference pressure** — 参考压力 `101325` `Pa`（默认）| 正标量

内部密封腔中的参考压力。

#### 依赖关系

要启用此参数，请将 **Operation mode** 设置为 `Sealed-Gauge`。

### **Full-scale deflection** — 满量程偏转时的输出电压 `5` `V`（默认）| 正标量

当测量压力等于或大于 **Pressure range** 参数值时的输出电压。

### **Output resistance** — 传感器输出电阻 `200` `Ohm`（默认）| 非负标量

传感器的输出电阻。

### **Dynamics** — 传感器动态特性选项 `No dynamics — Suitable for HIL`（默认）| `Model transducer bandwidth`

用于对传感器动态特性建模的选项：

- `No dynamics — Suitable for HIL` — 不对传感器动态特性建模。如果传感器带宽较高，除非将传感器建模为无动态特性，否则需要较小的仿真时间步长。使用此选项可使用定步长求解器或为硬件在环测试生成代码。
- `Model transducer bandwidth` — 基于 **Bandwidth** 参数值，使用一阶滞后近似对传感器动态特性建模。指定 **Measured pressure** 初始目标以控制滞后的初始条件。

### **Bandwidth** — 带宽 `5` `kHz`（默认）| 正标量

带宽。此参数确定传感器滞后值。

#### 依赖关系

要启用此参数，请将 **Dynamics** 设置为 `Model transducer bandwidth`。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2023b：测量等温液体的压力

现在可以使用 Pressure Transducer 模块测量等温液体网络中的压力。要测量节点处的压力，请将 **Fluid port type** 参数设置为 `Isothermal Liquid`，并将 **A** 端口与该节点处的网络并联连接。

### R2019a：选择压力测量的域类型

在 R2019a 之前，Pressure Transducer 模块具有气动测量端口。气动模块不再是 Foundation 库的一部分，但它们作为示例自定义库包含在 Simscape 产品安装中。带有气动端口的旧版 Pressure Transducer 模块现在属于此自定义库。

现在可以使用 Gas 库对气动系统建模。使用带有气体端口的最新版 Pressure Transducer 模块。

## 描述

将压力测量转换为电压的压力传感器

Pressure Transducer 模块对将压力测量转换为电压的通用压力传感器进行建模。使用该模块可测量各种域中的压力。使用 **Fluid port type** 参数指定域类型。

输出电压与压力成线性比例。如果压力小于零，模块输出零伏。如果输入压力等于 **Pressure range** 参数的值，则输出电压等于 **Full-scale deflection** 参数值。对于更高的压力，输出电压保持在此 **Full-scale deflection** 值。

可以选择真空压力、大气压力或密封表压参考压力作为压力测量的参考点。

如果将 **Dynamics** 参数设置为 `Model transducer bandwidth`，模块使用一阶滞后近似传感器动态特性。**Bandwidth** 参数确定滞后。如果选择 `Model transducer bandwidth` 选项，还必须使用 **Measured pressure** 初始目标指定滞后的初始条件。

要使用定步长求解器或为硬件在环测试生成代码，请将 **Dynamics** 参数设置为 `No dynamics — Suitable for HIL`。如果传感器带宽较高，除非将传感器建模为无动态特性，否则需要较小的仿真时间步长。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

**Measured pressure** 初始目标指定传感器的初始输出。
