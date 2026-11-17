---
type: simulink-block
title: 'Band-Limited Op-Amp'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'bandlimitedopamp'
documentation_source_path: 'ref/bandlimitedopamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Band-Limited Op-Amp

## 端口

### 守恒端口

### **+** — 同相输入电气端口

与运放同相输入端关联的电气守恒端口

### **-** — 反相输入电气端口

与运放反相输入端关联的电气守恒端口

### **OUT** — 输出电压电气端口

与运放输出电压关联的电气守恒端口

## 参数

### **Gain, A** — 开环增益 `1000`（默认值）

运算放大器的开环增益。

### **Input resistance, Rin** — 输入电阻 `1e6` `Ohm`（默认值）

运算放大器输入端的电阻，模块使用该电阻计算输入电流。

### **Output resistance, Rout** — 输出电阻 `100` `Ohm`（默认值）

运算放大器输出端的电阻，模块使用该电阻计算由输出电流引起的输出电压降。

### **Minimum output, Vmin** — 最小输出电压 `-15` `V`（默认值）

运算放大器空载输出电压的下限。

### **Maximum output, Vmax** — 最大输出电压 `15` `V`（默认值）

运算放大器空载输出电压的上限。

### **Maximum slew rate, Vdot** — 最大压摆率 `1000` `V/s`（默认值）

输出电压幅值的最大正向或负向变化率。

### **Bandwidth, f** — 开环带宽 `1e5` `Hz`（默认值）

开环带宽，即增益相对于低频增益 *A* 下降 3 dB 时的频率。

### **Initial output voltage, V0** — 初始输出电压 `0` `V`（默认值）

输出电流为零时仿真开始时的输出电压。

**注意**

此参数值未考虑输出电阻上的电压降。

## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

对带宽受限运算放大器进行建模

Band-Limited Op-Amp 模块对带宽受限运算放大器进行建模。如果正端口和负端口的电压分别为 *Vp* 和 *Vm*，则输出电压为：

Vout = A(Vp-Vm)s2πf+1−Iout\*Rout

其中：

- *A* 是增益。
- *Rout* 是输出电阻。
- *Iout* 是输出电流。
- *s* 是拉普拉斯算子。
- *f* 是 3-dB 带宽。

输入电流为：

Vp-VmRin

其中 *Rin* 是输入电阻。

如果在 Simscape™ Solver Configuration 模块中选中 **Start simulation from steady state** 复选框，则模块不使用通过 **Initial output voltage, V0** 参数指定的初始条件。
