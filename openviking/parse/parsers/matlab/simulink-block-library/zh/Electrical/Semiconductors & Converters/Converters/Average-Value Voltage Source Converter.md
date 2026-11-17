---
type: simulink-block
title: 'Average-Value Voltage Source Converter'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluevoltagesourceconverter'
documentation_source_path: 'ref/averagevaluevoltagesourceconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Average-Value Voltage Source Converter

## 端口

### 输入

### **ModWave** — 调制波向量

与归一化调制波关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **输入类型** 设置为
`Modulation wave`。

### **Vt** — RMS 电压标量

与 RMS 电压关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **输入类型** 设置为
`Sinusoidal magnitude and phase shift`。

### **ph** — 相移标量

与相移关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **输入类型** 设置为
`Sinusoidal magnitude and phase shift`。
### 守恒

### **A** — 交流侧端子 A 电气

与交流侧端子关联的电气守恒端口。

### **B** — 交流侧端子 B 电气

与交流侧端子关联的电气守恒端口。

### **+** — 直流侧正极端子电气

与直流侧正极端子关联的电气守恒端口。

### **-** — 直流侧负极端子电气

与直流侧负极端子关联的电气守恒端口。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **输入类型** — 用于指定模块输入的选项 `Modulation wave`（默认） | `Sinusoidal magnitude and phase shift`

用于将模块输入指定为调制波或通过正弦幅值和相移指定的选项。

### **额定电气频率** — 额定电气频率 `60` `Hz` | 标量

额定电气频率。如果模型中存在其他正弦源，则此参数的值必须等于这些源的额定电气频率值。

### **直流侧初始电流** — 直流侧初始电流 `0` `A` | 标量

变换器直流侧的初始电流。

### **直流侧初始电流保持时间** — 直流侧初始电流保持时间 `1/60` `s` | 标量

保持变换器直流侧初始电流的时间。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

单相平均值双向 AC/DC 电压源变换器

Average-Value Voltage Source Converter 模块根据输入的单相调制波将电能从交流转换为直流电压，或从直流转换为交流电压。您可以直接指定调制波，也可以通过相量（例如幅值和相移）指定。相应的输入功率等于输出功率。

此模块可在时域仿真模式和频率和时间仿真模式下工作。有关详细信息，请参阅频率和时间仿真模式。
