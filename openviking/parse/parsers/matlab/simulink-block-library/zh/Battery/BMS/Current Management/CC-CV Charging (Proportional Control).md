---
type: simulink-block
title: 'CC-CV Charging (Proportional Control)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Current Management'
documentation_page: 'cccvchargingproportionalcontrol'
documentation_source_path: 'ref/cccvchargingproportionalcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# CC-CV Charging (Proportional Control)

## 端口

### 输入

### **ChargingEnabled** — 是否启用电池充电 boolean

是否启用电池充电，指定为 `1`（启用）或 `0`（禁用）。

### **CellVoltage** — 电池单体的电压，V 标量 | 向量

电池单体的电压，对于单个电池单体指定为标量，对于多个电池单体指定为向量。

如果选择 **Specify CellVoltage input as [Min,Max]** 参数，则必须为此端口指定最小值和最大值，例如 `CellVoltage=[CellVoltageMin,CellVoltageMax]`。

### **ChargeCurrentLimit** — 充电电流限值，A 标量

电池用于充电的电流限值，指定为标量。

### **CellVoltageThreshold** — 放电电流，V 标量

最大允许电池单体电压，指定为标量。

### 输出

### **ChargeCurrentRequest** — 充电电流标量

充电电流命令，以标量形式返回。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Specify CellVoltage input as [Min,Max]** — 用于将 CellVoltage 输入指定为最小值和最大值的选项 `off`（默认） | `on`

用于将 **CellVoltage** 输入端口的值指定为最小值和最大值的向量。如果清除此参数，则必须为该输入端口指定单个值。然后模块会在内部计算最小值和最大值。

### **Controller proportional gain** — 控制器的比例增益 `0.02`（默认） | 标量

控制器的比例增益 *Kp*。

### **Sample time (-1 for inherited)** — 模块采样时间 `1`（默认） | `-1` | 正整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。

## 所属库

Simscape / Battery / BMS / Current Management

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

采用比例控制的恒流恒压充电算法

CC-CV Charging (Proportional Control) 模块为电池实现采用比例控制的恒流 (CC)、恒压 (CV) 充电算法。要使用比例积分控制实现 CC-CV 充电算法，请参阅 Battery CC-CV 模块。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，除 **Sample time (-1 for inherited)** 参数外，所有输入和参数的数据类型都必须为 `single`。

要将模块配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正的非零值。要从上游模块继承采样时间，请将 **Sample time (-1 for inherited)** 参数设置为 `-1`。

下图说明了模块的总体结构：

CC-CV Charging (Proportional Control) 模块的内部结构

### 方程

此模块在恒流和恒压模式下实现 CC-CV 算法。下图显示了这些模式的操作：

CC-CV 算法的工作模式。蓝线表示充电电流，红线表示电压，绿线表示充电容量。

此方程定义了模块在离散时间时刻 *k* 输出的电池充电电流：

ichg(k)={
  最大充电电流, 如果电池正在充电且 vmax<vthreshold
  Kp(vthreshold−vmax)+ichg(k−1), 如果电池正在充电且 vmax≥vthreshold
  0, 如果电池未充电
}

其中

- *i*chg*(k)* 是时间时刻 *k* 的充电电流。
- *i*chg*(k-1)* 是上一时间时刻的充电电流。
- *v*max 是最高电池单体的电压。
- *v*threshold 是最大允许电池单体电压。
- *Kp* 是 **Controller proportional gain** 参数的值。
