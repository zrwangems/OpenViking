---
type: simulink-block
title: 'Average-Value Voltage Source Converter'
family: 'sps'
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

与归一化调制波相关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为
`Modulation wave`。

### **Vt** — RMS 电压标量

与 RMS 电压相关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为
`Sinusoidal magnitude and phase shift`。

### **ph** — 相移标量

与相移相关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请将 **Input type** 设置为
`Sinusoidal magnitude and phase shift`。
### 守恒

### **A** — 交流侧端子 A 电气

与交流侧端子相关联的电气守恒端口。

### **B** — 交流侧端子 B 电气

与交流侧端子相关联的电气守恒端口。

### **+** — 直流侧正极端子 电气

与直流侧正极端子相关联的电气守恒端口。

### **-** — 直流侧负极端子 电气

与直流侧负极端子相关联的电气守恒端口。

## 参数

要以交互方式编辑模块参数，请使用
属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### **Input type** — 用于指定模块输入的选项 `Modulation wave`（默认）| `Sinusoidal magnitude and phase shift`

用于将模块的输入指定为调制波或通过正弦
幅值和相移指定的选项。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz` | 标量

额定电气频率。如果模型中存在其他正弦源，此参数的值必须等于
这些源的额定电气频率的值。

### **Initial current at DC side** — 直流侧初始电流 `0` `A` | 标量

变换器直流侧的初始电流。

### **Time for holding initial current at DC side** — 保持直流侧初始电流的时间 `1/60` `s` | 标量

保持变换器直流侧初始电流的时间。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

单相平均値双向 AC/DC 电压源变换器

Average-Value Voltage Source Converter 模块根据输入
单相调制波将电能从 AC 转换为 DC 电压，或从 DC 转换为 AC 电压。您可以直接指定调制波，或通过相量
量（如幅值和相移）指定。相应的输入功率等于
输出功率。

此模块可在时域和频率-时间仿真模式下工作。有关更多
信息，请参阅 Frequency and Time Simulation Mode。
