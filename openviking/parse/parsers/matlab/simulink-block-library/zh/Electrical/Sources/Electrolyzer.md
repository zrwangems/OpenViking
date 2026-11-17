---
type: simulink-block
title: 'Electrolyzer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'electrolyzer'
documentation_source_path: 'ref/electrolyzer.html'
language: zh-CN
chinese_source: worker-translation
---

# Electrolyzer

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: purge
  summary: 吹扫逻辑输入，无量纲物理信号
  direction: input
- name: vol
  summary: 水体积，m^3 物理信号
  direction: input
- name: T
  summary: 水温，K 物理信号
  direction: input
- name: volPurging
  summary: 吹扫水体积，m^3 物理信号
  direction: output
- name: pH
  summary: 水 pH，无量纲物理信号
  direction: output
- name: mdotH2
  summary: 氢气质量流量，g/s 物理信号
  direction: output
- name: mdotH2O
  summary: 消耗水质量流量，g/s 物理信号
  direction: output
```

### 守恒端口

### **+** — 正极端子电气

与电解槽罐阳极关联的电气守恒端口。

### **-** — 负极端子电气

与电解槽罐阴极关联的电气守恒端口。

### 输入

### **purge** — 吹扫逻辑输入，无量纲物理信号

吹扫逻辑输入，指定为物理信号。该信号启用罐中水的替换。

### **vol** — 水体积，m^3 物理信号

电解槽罐中的水体积，以 m3 为单位，指定为物理信号。

### **T** — 水温，K 物理信号

水温，以 K 为单位，指定为物理信号。

### 输出

### **volPurging** — 吹扫水体积，m^3 物理信号

用于吹扫的消耗水体积，以 m3 为单位，指定为物理信号。

### **pH** — 水 pH，无量纲物理信号

电解槽罐中的水 pH，指定为物理信号。

### **mdotH2** — 氢气质量流量，g/s 物理信号

氢气的质量流量，以 g/s 为单位，指定为物理信号。

### **mdotH2O** — 消耗水质量流量，g/s 物理信号

消耗水的质量流量，以 g/s 为单位，指定为物理信号。
## 参数
```yaml
parameters:
- name: Assumption pH
  summary: 恒定或动态 pH Constant（默认）| Dynamic
  group: ''
- name: Resistance
  summary: 外部电阻 10 Ohm（默认）| 非负标量
  group: ''
- name: Cross-sectional transport area
  summary: 横截面积传输区域 0.04 m^2（默认）| 正标量
  group: ''
- name: Distance anode-cathode
  summary: 阳极与阴极之间的距离 0.01 m（默认）| 正标量
  group: ''
- name: Number of cells
  summary: 电池数量 50（默认）| 正标量
  group: ''
- name: Initial pH
  summary: 初始 pH 0（默认）| 标量
  group: ''
- name: Constant pH
  summary: 恒定 pH 6（默认）| 标量
  group: ''
- name: pH vector, pH_vec
  summary: pH 向量 [5, 5.5, 6, 6.5, 7]（默认）| 正标量行向量
  group: ''
- name: Electrical resistivity vector, rho_vec
  summary: 电阻率向量 [.2, .75, 2.5, 8, 18.2] MOhm*cm（默认）| 标量向量
  group: ''
- name: Temperature vector for efficiency, T_vec
  summary: 效率温度向量 [273, 298, 323, 348, 373] K（默认）| 标量向量
  group: ''
- name: Electrolysis efficiency vector, efficiency(T)
  summary: 电解效率向量 ones(5, 1)（默认）| 标量向量
  group: ''
```

### **Assumption pH** — 恒定或动态 pH `Constant`（默认）| `Dynamic`

假设电解槽罐中的 pH 是恒定还是动态。

### **Resistance** — 外部电阻 `10` `Ohm`（默认）| 非负标量

外部电阻的量值。

### **Cross-sectional transport area** — 横截面积传输区域 `0.04` `m^2`（默认）| 正标量

垂直于连接阳极和阴极的向量的法向面积。带正电的离子从阳极穿过该区域到达阴极，在阴极被还原并产生氢气。

### **Distance anode-cathode** — 阳极与阴极之间的距离 `0.01` `m`（默认）| 正标量

浸没在电解液中的阳极与阴极之间的距离。

### **Number of cells** — 电池数量 `50`（默认）| 正标量

电解槽中的电池数量。

### **Initial pH** — 初始 pH `0`（默认）| 标量

罐中水的初始 pH 值。

### **Constant pH** — 恒定 pH `6`（默认）| 标量

罐中水的恒定 pH 值。

#### 依赖关系

要启用此参数，请将 **Assumption pH** 设置为 `Constant`。

### **pH vector, pH\_vec** — pH 向量 `[5, 5.5, 6, 6.5, 7]`（默认）| 正标量行向量

pH 值向量。此参数必须与 **Electrical resistivity vector, rho\_vec** 参数具有相同数量的元素。

#### 依赖关系

要启用此参数，请将 **Assumption pH** 设置为 `Dynamic`

### **Electrical resistivity vector, rho\_vec** — 电阻率向量 `[.2, .75, 2.5, 8, 18.2]` `MOhm*cm`（默认）| 标量向量

电阻率值向量。此参数必须与 **pH vector, pH\_vec** 参数具有相同数量的元素。

#### 依赖关系

要启用此参数，请将 **Assumption pH** 设置为 `Dynamic`

### **Temperature vector for efficiency, T\_vec** — 效率温度向量 `[273, 298, 323, 348, 373]` `K`（默认）| 标量向量

用于效率的温度向量。此参数必须与 **Electrolysis efficiency vector, efficiency(T)** 参数具有相同数量的元素。

### **Electrolysis efficiency vector, efficiency(T)** — 电解效率向量 `ones(5, 1)`（默认）| 标量向量

电解效率值向量。此参数必须与 **Temperature vector for efficiency, T\_vec** 参数具有相同数量的元素。
## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2024a：**Number of electrode pairs** 参数已移除

**Number of electrode pairs** 参数已移除。

## 描述

电解槽的电力负载

Electrolyzer 模块表示与电解槽相关的电力负载。电解槽由一个阳极和一个阴极组成，二者由电解质隔开。该模块根据所提供的电能以及水箱中的水温计算产生的氢气量。

在聚合物电解质膜（PEM）电解槽中，这些化学反应定义了阳极和阴极转化过程：

2H2O→O2+4H++4e−

4H++4e−→2H2

电解堆由多个串联的单个电解槽单元组成。指定 **Assumption pH** 参数，可将此模块建模为 pH 相关状态或具有恒定 pH 的理想状态。

### 方程

Electrolyzer 模块使用以下公式计算电功率

PE=v2RT，

其中 *v* 是电压，*RT* 是总电阻。总电阻 *RT* 定义为

1RT=1Rel+1R，

其中：

- *R* 是外部电阻。
- Rel=ρ(pH)xA。该值是由横截传输面积 *A*、阳极-阴极距离 *x* 以及溶液的电阻率 *ρ(pH)* 得到的电阻项。

储存在电力负载两端的摩尔能量使水电解过程得以进行，并由以下方程计算：

GE=PE1 mol/s。

为完成电解，电解槽需要最低能量

Gmin=ΔH−TT0TΔS，

其中：

- *ΔH* 是水的焓。
- *TΔS* 是反应熵。
- *T* 是水温。
- *T0* 是参考温度。

如果电能不足以解离水，则电解槽不产生氢气。因此，Electrolyzer 模块计算电子摩尔速率 *mole* 和氢气摩尔速率 *molH2*

mole={μ(GE−Gmin)eVNAGE>Gmin0GE≤Gmin

molH2={Ncmole2,GE>Gmin0,GE≤Gmin

其中：

- *NA* 是阿伏伽德罗常数。
- *eV* 是每个电子的能量。
- *Nc* 是单元数量。
- *μ* 是电解的温度相关效率。

随后，流过电解槽水箱的电流由下式得到

i=moleF，

其中 *F* 是法拉第常数。

Electrolyzer 模块使用以下方程计算消耗水的质量速率和生成氢气的质量速率：

m˙H2 O=molH2MH2 Om˙H2=molH2MH2

其中 *MH2O* 是水的摩尔质量，*MH2* 是氢气的摩尔质量。

为计算水箱中水的 pH，该模块使用

pH=−ln(xhpmolH2\_acc)，

其中：

- xhp={∫mole,pH assumed constant∫(1−purge)mole,pH assumed dynamic 表示溶液中游离的氢离子（H+）。
- molH2\_acc=VρH2 O(T)MH2 O 是水的摩尔数。
- *V* 是体积。
- *ρH2O(T)* 是水箱中水的密度。

电解槽内溶液中的残余质子会随时间自然增加水箱中水的 pH 和电导率。电导率的增加会导致失控现象。为防止失控，必须通过取出水箱体积的水并用清水填充来对水箱中的水进行吹扫。
