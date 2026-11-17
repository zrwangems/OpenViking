---
type: simulink-block
title: 'Induction Machine Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'inductionmachinemeasurement'
documentation_source_path: 'ref/inductionmachinemeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Measurement

## 端口
```yaml
ports:
- name: pu
  summary: 输入端口物理量
  direction: input
- name: o
  summary: 标幺值测量输出物理量
  direction: output
```

### 输入

### **pu** — 输入端口物理量

与来自所连接感应电机的标幺值测量值相关联的物理信号向量。向量元素为：

- *pu\_torque*
- *pu\_velocity*
- *pu\_vds*
- *pu\_vqs*
- *pu\_v0s*
- *pu\_ids*
- *pu\_iqs*
- *pu\_i0s*
### 输出

### **o** — 标幺值测量输出物理量

与标幺值测量输出相关联的物理信号。
## 参数
```yaml
parameters:
- name: Output
  summary: 来自感应电机的标幺值测量值 Electrical torque（默认）| Rotor velocity | Stator d-axis voltage | Stator q-axis voltage | Stator zero-sequence
    voltage | Stator d-axis current | Stator q-axis current | Stator zero-sequence current | Slip | Apparent power | Real
    power | Reactive power | Terminal voltage | Power factor angle | Power factor angle
  group: ''
```

### **Output** — 来自感应电机的标幺值测量值 `Electrical torque`（默认）| `Rotor velocity` | `Stator d-axis voltage` | `Stator q-axis voltage` | `Stator zero-sequence voltage` | `Stator d-axis current` | `Stator q-axis current` | `Stator zero-sequence current` | `Slip` | `Apparent power` | `Real power` | `Reactive power` | `Terminal voltage` | `Power factor angle` | `Power factor angle`

来自感应电机的标幺值测量值。选项包括：

- `Electrical torque`
- `Rotor velocity`
- `Stator d-axis voltage`
- `Stator q-axis voltage`
- `Stator zero-sequence voltage`
- `Stator d-axis current`
- `Stator q-axis current`
- `Stator zero-sequence current`
- `Slip`
- `Apparent power`
- `Real power`
- `Reactive power`
- `Terminal voltage`
- `Power factor angle`
- `Power factor angle`
## 所属库

Simscape / Electrical / Electromechanical / Asynchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

来自感应电机的标幺值测量

Induction Machine Measurement 模块输出与所连接的 Induction Machine Squirrel Cage 或 Induction Machine Wound Rotor 模块相关联的标幺值测量值。Induction Machine Measurement 模块的输入连接到感应电机模块的 `pu` 输出端口。

您将 **Output** 参数设置为与感应电机相关联的标幺值测量值。根据您选择的值，Induction Machine Measurement 模块会：

- 直接输出输入信号向量中某个元素的值
- 通过在数学表达式中使用输入信号向量中元素的值来计算标幺值测量值

Induction Machine Measurement 模块根据表中的输出值表达式输出感应电机的标幺值测量值。例如，当您将 **Output** 设置为 *Stator d-axis voltage* 时，模块直接输出输入信号向量中 *pu\_vds* 元素的值。然而，当您将 **Output** 设置为 *Slip* 时，模块通过从 1 中减去 *pu\_velocity* 元素的值来计算转差率值。

| 输出参数设置 | 输出值表达式 |
| --- | --- |
| Electrical torque | pu\_torque |
| Rotor velocity | pu\_velocity |
| Stator d-axis voltage | pu\_vds |
| Stator q-axis voltage | pu\_vqs |
| Stator zero-sequence voltage | pu\_v0s |
| Stator d-axis current | pu\_ids |
| Stator q-axis current | pu\_iqs |
| Stator zero-sequence current | pu\_i0s |
| Slip | 1-pu\_velocity |
| Apparent power | pu\_Pt2+pu\_Qt2 |
| Real power | pu\_Pt = (pu\_vds\*pu\_ids) + (pu\_vqs\*pu\_iqs) + 2(pu\_v0s\*pu\_i0s) |
| Reactive power | pu\_Qt = (pu\_vqs\*pu\_ids) – (pu\_vds\*pu\_iqs) |
| Terminal voltage | pu\_vds2+pu\_vqs2 |
| Terminal current | pu\_ids2+pu\_iqs2 |
| Power factor angle (rad) | power\_factor\_angle = atan2(pu\_Qt, pu\_Pt) |
| Power factor | cos(power\_factor\_angle) |
