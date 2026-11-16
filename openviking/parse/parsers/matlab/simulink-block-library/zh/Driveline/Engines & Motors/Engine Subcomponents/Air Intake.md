---
type: simulink-block
title: 'Air Intake'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors / Engine Subcomponents'
documentation_page: 'airintake'
documentation_source_path: 'ref/airintake.html'
language: zh-CN
chinese_source: worker-translation
---

# Air Intake

## 端口

### 输入

### **Thr** — 节气门指令输入，无量纲物理信号

与归一化节气门指令关联的物理信号输入，其中 `0` 表示节气门完全关闭，`1` 表示节气门完全打开。该模块将此输入映射为 `0` 到 `90` 度之间的节气门打开角度。

### **EngSpd** — 发动机转速，rad/s 物理信号

与转速关联的物理信号输入，单位为 rad/s。

### 输出

### **Pim** — 进气歧管压力输入，kPa 物理信号

与进气歧管关联的物理信号输入，单位为 kPa。

## 参数

### **干空气比气体常数** — 干空气比气体常数 `287.058` `J/(K*kg)` (默认) | 正标量

干空气的比气体常数。

### **干空气比热比** — 干空气比热比 `1.4` (默认) | 正标量

干空气的比热比。

### **环境压力** — 参考空气压力 `101.325` `kPa` (默认) | 正标量

进入进气口的空气压力。

### **环境温度** — 参考温度 `298.15` `K` (默认) | 正标量

进入进气口的空气温度。

### **节气门静止角度** — 释放的节气门位置 `3` `deg` (默认) | 正标量

从节气门静止位置到 `0` 度的径向距离。

### **节气门板直径** — 节气门板直径 `5` `cm` (默认) | 正标量

节气门体中蝶阀盘的直径。

### **节气门泄漏面积** — 节气门泄漏面积 `1` `cm^2` (默认) | 非负标量

节气门泄漏的累计面积。

### **进气歧管体积** — 进气歧管体积 `1000` `cm^3` (默认) | 正标量

进气歧管的容积。

### **发动机排量** — 发动机排量 `1500` `cm^3` (默认) | 正标量

所有发动机活塞的总排量。

### **节气门响应时间常数** — 节气门响应时间常数 `0.1` `s` (默认) | 正标量

与发动机对节气门指令的响应速率关联的时间常数。

## 所属库

Simscape / Driveline / Engines & Motors / Engine Subcomponents

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

燃烧气缸空气供给进气

Air Intake 模块表示一个抽象进气系统，用于计算集总参数空气流动力学。该模块适用于内燃机。该模块根据节气门和发动机转速计算进气歧管压力。

### 方程

Air Intake 模块按以下公式计算进气歧管压力

ddtPim=RairTambVim(m˙thr−m˙cyl),

其中

- *Rair* 是 **干空气比气体常数** 参数。
- *Tamb* 是 **环境温度** 参数。
- *Vim* 是 **进气歧管体积** 参数。

该模块按以下公式计算燃烧气缸质量流量 *ṁcyl*：

m˙cyl=ωVdPim2RairTamb,

这是理想气体定律的时间导数形式。*ω* 是模块从端口 **EngSpd** 接收的发动机转速，*Vd* 是 **发动机排量** 参数。

该模块按以下公式计算节气门质量流量 *ṁthr*：

m˙thr={SthrTambc1(Pamb−Pim)                            LaminarSthrTambPambc2[(PambPim)cb−(PambPim)ca]  SubsonicSthrTambc3Pamb                                        Choked

具体取决于流动条件。在此方程中，*Sthr* 是节气门开口面积，*Pamb* 是环境压力。该模块将方程常数定义为

ca=κ+1κcb=2κc1=c2(Πlamcb−Πlamca)1−Πlamc2=2κRair(κ−1)c3=κRairΠcrca

其中

- *κ* 是 **干空气比热比** 参数。
- *Πlam* 是层流阈值常数。
- *Πcr* 是临界压力比。

该模块按以下公式求取 *Πcr*：

Πcr=(2κ+1)κκ−1.

**节气门打开面积**

该模块将节气门打开面积 *Sthr* 视为关于节气门角度 *θ* 的三阶多项式函数。此方法简化了模块计算以提高性能。该模块按以下公式计算节气门打开面积：

Sthr(θ)=k0+k1θ+k2θ2+k3θ3,

其中，该模块使用以下量推导系数 *ki*：

- *Dplate* — **节气门板直径** 参数
- *Arest* — **节气门静止角度** 参数
- *Apeak* — 85°
- *Sleak* — **节气门泄漏面积** 参数

节气门打开面积使用以下约束：

Sthr(0)=Seng(0)Sthr(π2)=Seng(Apeak)ddθSthr(Arest)=ddθSeng(Arest)ddθthrSthr(Apeak)=0

其中 *Seng* 是节气门打开面积的工程公式，即

Seng(θ)=π(Dplate2)2(1−cos(θ)cos(Arest))+Sleak.

此图显示了多项式结果与工程结果的比较。

节气门打开面积随节气门角度的变化。多项式近似与工程方程的形状不同，但它们的趋势彼此接近。
