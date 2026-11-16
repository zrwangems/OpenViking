---
type: simulink-block
title: 'Motorcycle Chain'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Motion'
documentation_page: 'motorcyclechain'
documentation_source_path: 'ref/motorcyclechain.html'
language: zh-CN
chinese_source: worker-translation
---

# Motorcycle Chain

## 端口

### 输入

### **MDshft** — 前链轮上的驱动轴力矩 `scalar`

前链轮上绕 *ym* 的驱动轴力矩，单位为 N·m。

### **FCpR** — 后轮接地点处的纵向力和垂向力 `vector`

后轮接地点 *OCpR* 处沿 *iCpR* 和 *kCpR* 的纵向力和垂向力，单位为 N。信号向量维度为 `[1x2]` 或 `[2x1]`。

### **ThetaFrm** — 主车架俯仰角 `scalar`

主车架俯仰角 *ϴfrm*，单位为 rad。

### **ThetaArmR** — 后摇臂俯仰角 `scalar`

后摇臂俯仰角 *ϴra*，单位为 rad。

### **MBrkR** — 后轮处的制动力矩 `scalar`

后轮 *GWhlRr* 处绕 *jWhlRr* 的制动力矩，单位为 N·m。

### **AngAWhlR** — 后轮角加速度 `scalar`

后轮角加速度，单位为 rad/s2。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `FChn` | 施加到后摇臂的链条力 | N |
| `AngVSprtR` | 后链轮角速度 | rad/s |
| `MDrvSprtR` | 施加到后链轮的车轮减振器力矩 | N·m |
| `WhlDmpAng` | 后链轮与后轮之间的角度 | rad |

### **MDrvSprtR** — 后链轮处的车轮减振器力矩 `scalar`

施加到后链轮的车轮减振器力矩，单位为 N·m。

### **MDrvArmR** — 后摇臂处的驱动链条力矩 `scalar`

后摇臂 *OArmRr* 处绕 *jArmRr* 的驱动链条力矩，单位为 N·m。

### **MDrvFrm** — 车架处的驱动链条力矩 `scalar`

车架 *OFrm* 处绕 *jFrm* 的驱动链条力矩，单位为 N·m。

## 参数

此图显示链条与摩托车车架、后摇臂和后轮之间的几何关系。

摩托车链条示意图

#### 前链轮

### **坐标, SprktFrPxz** — 前链轮位置 `[0.05 -0.05]` (默认) | `vector`

前链轮位置 *SprktFrPxz*，分别沿 *xm* 和 *zm*，单位为 m。

### **质量转动惯量, SprktFrIyy** — 前链轮转动惯量 `0.005` (默认) | `scalar`

前链轮质量转动惯量 *SprktFrIyy*，单位为 kg·m2。

### **半径, SprktFrR** — 前链轮半径 `0.04` (默认) | `scalar`

前链轮半径 *SprktFrR*，单位为 m。

#### 后链轮

### **质量转动惯量, SprktRrIyy** — 后链轮转动惯量 `0.01` (默认) | `scalar`

后链轮质量转动惯量 *SprktRrIyy*，单位为 kg·m2。

### **半径, SprktRrR** — 后链轮半径 `0.12` (默认) | `scalar`

后链轮半径 *SprktRrR*，单位为 m。

#### 后轮

### **质量转动惯量, WhlRrIyy** — 后轮转动惯量 `0.66` (默认) | `scalar`

后轮质量转动惯量 *WhlRrIyy*，单位为 kg·m2。

### **半径, WhlRrR** — 后轮半径 `0.33` (默认) | `scalar`

后轮半径 *WhlRrR*，单位为 m。

#### 后摇臂

### **摇臂长度, ArmRrLen** — 后摇臂长度 `0.535` (默认) | `scalar`

摇臂长度 *ArmRrLen*，单位为 m。

#### 车轮减振器

### **刚度, WhlDmpK** — 车轮减振器刚度 `1e4` (默认) | `scalar`

车轮减振器刚度 *WhlDmpK*，单位为 N/rad。

### **阻尼, WhlDmpC** — 车轮阻尼 `1e2` (默认) | `scalar`

车轮减振器阻尼 *WhlDmpC*，单位为 N·s/rad。

### **平衡角** — 车轮减振器平衡角 `-15e-3` (默认) | `scalar`

平衡角 *WhlDmpAng0*，单位为 rad。

#### 初始条件

### **后链轮角速度, SprktRrAngV0** — 角速度 `0` (默认) | `scalar`

后链轮角速度 *SprktRrAngV0*，单位为 rad/s。

### **后轮角速度, WhlRrAngV0** — 角速度 `0` (默认) | `scalar`

后轮角速度 *WhlRrAngV0*，单位为 rad/s。

## 所属库

Powertrain Blockset / Drivetrain / Couplings Vehicle Dynamics Blockset / Powertrain / Drivetrain / Couplings

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

实现摩托车链条

Motorcycle Chain 模块实现摩托车链条对 Motorcycle Body Longitudinal In-Plane 模块的动态影响，包括动态张力和力矩驱动耦合。

此图显示链条与摩托车车架、后摇臂和后轮之间的几何关系。

摩托车链条示意图

| 坐标系 | 图中变量 | 描述 |
| --- | --- | --- |
| 摩托车主车架  - *xm* – 沿指向前叉的向量向前 - *zm* – 向下 - *ym* – 与摩托车平面正交 | *Om* | 主车架原点 |
