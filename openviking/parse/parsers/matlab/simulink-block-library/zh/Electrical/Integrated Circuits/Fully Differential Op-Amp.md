---
type: simulink-block
title: 'Fully Differential Op-Amp'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'fullydifferentialopamp'
documentation_source_path: 'ref/fullydifferentialopamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Fully Differential Op-Amp

## 端口
```yaml
ports:
- name: +
  summary: 同相输入电气端口
  direction: conserving
- name: '-'
  summary: 反相输入电气端口
  direction: conserving
- name: cm
  summary: 共模端口电气端口
  direction: conserving
- name: Vout+
  summary: 同相输出电气端口
  direction: conserving
- name: Vout-
  summary: 反相输出电气端口
  direction: conserving
```

### 守恒端口

### **+** — 同相输入电气端口

与运算放大器同相输入端关联的电气守恒端口。

### **-** — 反相输入电气端口

与运算放大器反相输入端关联的电气守恒端口。

### **cm** — 共模端口电气端口

与运算放大器共模端口关联的电气守恒端口。如果要将此引脚保持开路，请在 `cm` 端口和参考端口之间连接一个电压传感器。

### **Vout+** — 同相输出电气端口

与运算放大器同相输出端关联的电气守恒端口。

### **Vout-** — 反相输出电气端口

与运算放大器反相输出端关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Differential gain
  summary: 差分增益 1e3（默认值）
  group: 增益
- name: Bandwidth
  summary: 带宽 1.5 GHz（默认值）
  group: 增益
- name: Differential input resistance
  summary: 差分输入电阻 1.3 MOhm（默认值）
  group: 输入阻抗
- name: Differential input capacitance
  summary: 差分输入电容 1.8 pF（默认值）
  group: 输入阻抗
- name: Common-mode input resistance
  summary: 共模输入电阻 1.0 MOhm（默认值）
  group: 输入阻抗
- name: Common-mode input capacitance
  summary: 共模输入电容 2.3 pF（默认值）
  group: 输入阻抗
- name: Output resistance
  summary: 输出电阻 1 Ohm（默认值）
  group: 输出限幅
- name: Minimum output voltage low
  summary: 最低输出电压低 -1.4 V（默认值）
  group: 输出限幅
- name: Maximum output voltage low
  summary: 最高输出电压低 1.4 V（默认值）
  group: 输出限幅
- name: Differential maximum slew rate
  summary: 差分最大压摆率 5000 V/us（默认值）
  group: 输出限幅
- name: Common-mode port input resistance
  summary: 共模端口输入电阻 23.0 kOhm（默认值）
  group: 输出偏置
- name: Negative supply voltage
  summary: 负电源电压 -5 V（默认值）
  group: 输出偏置
- name: Positive supply voltage
  summary: 正电源电压 5 V（默认值）
  group: 输出偏置
- name: Initial differential output voltage
  summary: 初始差分输出电压 0 V（默认值）
  group: 初始条件
```

### 增益

### **Differential gain** — 差分增益 `1e3`（默认值）

施加于 + 和 – 输入端之间电压差的增益。

### **Bandwidth** — 带宽 `1.5` `GHz`（默认值）

差分电压增益从其直流值下降 3 dB 时的频率。

### 输入阻抗

### **Differential input resistance** — 差分输入电阻 `1.3` `MOhm`（默认值）

施加在 + 和 – 输入端之间的电压源所看到的输入电阻。默认值为 `1.3` MOhm。

### **Differential input capacitance** — 差分输入电容 `1.8` `pF`（默认值）

施加在 + 和 – 输入端之间的电流源所看到的输入电容。

### **Common-mode input resistance** — 共模输入电阻 `1.0` `MOhm`（默认值）

施加在接地与 + 输入端之间，或接地与 – 输入端之间的电压源所看到的输入电阻。

### **Common-mode input capacitance** — 共模输入电容 `2.3` `pF`（默认值）

施加在接地与 + 输入端之间，或接地与 – 输入端之间的电流源所看到的输入电容。

### 输出限幅

### **Output resistance** — 输出电阻 `1` `Ohm`（默认值）

任一输出端相对于共模电压参考的输出电阻。因此，差分输出电阻是输出电阻 R\_out 值的两倍。

### **Minimum output voltage low** — 最低输出电压低 `-1.4` `V`（默认值）

两个输出引脚中任一引脚相对于接地的最低输出电压。

### **Maximum output voltage low** — 最高输出电压低 `1.4` `V`（默认值）

两个输出引脚中任一引脚相对于接地的最高输出电压。

### **Differential maximum slew rate** — 差分最大压摆率 `5000` `V/us`（默认值）

差分输出电压的最大压摆率。

### 输出偏置

### **Common-mode port input resistance** — 共模端口输入电阻 `23.0` `kOhm`（默认值）

施加在接地与共模端口之间的电压源所看到的输入电阻。

### **Negative supply voltage** — 负电源电压 `-5` `V`（默认值）

连接到共模偏置电阻 R3b 的负电源电压值（见图）。

### **Positive supply voltage** — 正电源电压 `5` `V`（默认值）

连接到共模偏置电阻 R3a 的正电源电压值（见图）。

### 初始条件

### **Initial differential output voltage** — 初始差分输出电压 `0` `V`（默认值）

当输出电流为零时，两个输出端之间的初始差分电压。
## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

具有全差分输出的运算放大器，即不参考接地

Fully Differential Op-Amp 模块对全差分运算放大器进行建模。由于对外部噪声源的敏感度降低，差分信号传输优于单端传输。应用包括输入为差分信号的数据采集，例如 sigma-delta 转换器。

下图显示了放大器的内部表示。

电路元件的参数由您提供的模块参数推导得出。两个压控电压源（VCVS1 和 VCVS2）的增益设置为差分增益值的一半。类似地，每个电压源的压摆率设置为差分最大压摆率值的一半。两个输出端口 `Vout+` 和 `Vout-` 的电压都被限制在您指定的最低和最高输出电压范围内。

零差分输入电压时的输出电压由共模端口 `cm` 控制。如果外部电路未从 `cm` 端口抽取电流，则输出电压由 R3a 和 R3b 组成的电阻梯设置为正负电源电压的平均值。请注意，负电源电压可以为零，这对应于没有分离电源可用时的操作。您提供的最低和最高输出电压值必须与您提供的电源电压值一致。因此，例如，最高输出高电压将小于正电源电压，其差值对应于电路中的 p-n 结电压降数量。
