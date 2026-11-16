---
type: simulink-block
title: 'Battery CC-CV'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Management System / Current Management\u200b'
documentation_page: 'batterycccv'
documentation_source_path: 'ref/batterycccv.html'
language: zh-CN
chinese_source: worker-translation
---

# Battery CC-CV

## 端口

### 输入

### **ChargingEnabled** — 是否启用电池充电 boolean

是否启用电池充电，指定为 `1`（启用）或 `0`（禁用）。

### **CellVoltage** — 电芯电压，V 标量 | 向量

电芯的电压，指定为单电芯的标量或多电芯的向量。

如果选择 **将 CellVoltage 输入指定为 [Min,Max]** 参数，则必须为此端口指定最小值和最大值，例如 `CellVoltage=[CellVoltageMin,CellVoltageMax]`。*（自 R2025a 起）*

### **CurrentWhenCharging** — 充电电流，A 标量

电池用于充电的电流值，指定为标量。

### **CurrentWhenDischarging** — 放电电流，A 标量

电池用于放电的电流值，指定为标量。

### 输出

### **Current** — 计算得到的参考电流，A 标量

电池包的参考电流，以标量形式返回。

## 参数

### **将 CellVoltage 输入指定为 [Min,Max]** — 用于将 CellVoltage 输入指定为最小值和最大值的选项 `off`（默认） | `on`

*自 R2025a 起*

用于将 **CellVoltage** 输入端口处的值指定为最小值和最大值的向量的选项。如果清除此参数，则必须为输入端口指定单个值。然后，模块会在内部计算最小值和最大值。

### **电芯电压阈值 (V)** — 最大允许电芯电压 `4.5`（默认） | 标量

最大允许电芯电压，单位为 V。

### **控制器比例增益** — PI 控制器的比例增益 `100`（默认） | 标量

PI 控制器的比例增益 *Kp*。

### **控制器积分增益** — PI 控制器的积分增益 `10`（默认） | 标量

PI 控制器的积分增益 *Ki*。

### **控制器抗积分饱和增益** — PI 控制器的抗积分饱和增益 `1`（默认） | 标量

PI 控制器的抗积分饱和增益。

### **信号跟踪反馈环路增益** — PI 控制器的跟踪系数 `1`（默认） | 标量

PI 控制器的跟踪系数 *Kt*。

模块将跟踪信号与控制器输出之间的差值以增益值 *Kt* 反馈到积分器输入。使用此参数指定该反馈环路中的增益。

信号跟踪有多种应用，包括无扰控制切换以及避免多回路控制结构中的积分饱和。

### **采样时间（-1 表示继承）** — 模块采样时间 `1`（默认） | `0` | `-1` | 正整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，将此参数指定为 `-1`。对于离散时间操作，将此参数指定为正整数。对于连续时间操作，将此参数指定为 `0`。

如果此模块位于允许在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅提升掩码上的模块参数。

## 所属库

Simscape / Battery / BMS / Current Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：为 **CellVoltage** 输入端口指定最小值和最大值

可以为 **CellVoltage** 输入端口指定最小值和最大值。要将此输入指定为最小值和最大值的向量，请选择 **将 CellVoltage 输入指定为 [Min,Max]** 参数。

## 描述

恒流恒压充电算法

Battery CC-CV 模块为电池实现恒流 (CC)、恒压 (CV) 充电算法。对于正在放电的电池，模块使用 **CurrentWhenDischarging** 输入端口的值。要实现使用比例控制的更简单版 CC-CV 充电算法，请参阅 CC-CV Charging (Proportional Control) 模块。

此模块支持 single 精度和 double 精度浮点仿真。

**注意**

要启用继承的 single 精度浮点仿真，除 **采样时间（-1 表示继承）** 参数外，所有输入和参数的数据类型都必须为 `single`。

通过使用 **采样时间（-1 表示继承）** 参数，可以在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **采样时间（-1 表示继承）** 参数设置为 `0`。要将模块配置为离散时间，请将 **采样时间（-1 表示继承）** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

**注意**

此模块的连续时间实现仅在 double 精度浮点仿真中工作。如果提供 single 精度浮点参数和输入，此模块会将其转换为 double 精度浮点值以防止错误。

此图说明了模块的整体结构：

### 方程

此模块在恒流模式和恒压模式下实现 CC-CV 算法。此图显示了这些模式的操作：

此方程定义了模块输出的电池参考电流：

Current={最大充电电流,如果电池正在充电且 vmeas<vmax(Kp+Ki1s)(vmax−vmeas),如果电池正在充电且 vmeas≥vmax最大放电电流,如果电池正在放电

其中

- *vmax* 是 **电芯电压阈值 (V)** 参数的值。
- *vmeas* 是电压最高的电芯的电压。
- *Kp* 和 *Ki* 是 **控制器比例增益** 和 **控制器积分增益** 参数的值。
