---
type: simulink-block
title: 'SPICE-Imported MOSFET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'spiceimportedmosfet'
documentation_source_path: 'ref/spiceimportedmosfet.html'
language: zh-CN
chinese_source: worker-translation
---

# SPICE-Imported MOSFET

## 端口

### 守恒端口

### **g** — 栅极端子电气端口

与所选预参数化 MOSFET 的栅极端子相关联的电气守恒端口。

### **d** — 漏极端子电气端口

与所选预参数化 MOSFET 的漏极端子相关联的电气守恒端口。

### **tj** — 结温电气端口

与所选预参数化 MOSFET 的结温相关联的电气守恒端口。

该端口测得的电压对应结温。例如，如果该端口的值等于 25V，则结温等于 25 摄氏度。

**Tj** 通常是一个监测节点，不进行连接。

### **tc** — 壳温电气端口

与所选预参数化 MOSFET 的壳温相关联的电气守恒端口。

该端口测得的电压对应壳温。例如，如果该端口的值等于 25V，则壳温等于 25 摄氏度。

**Tc** 连接到表示环境温度的电压源，或连接到由电阻和电容表示的散热器热网络。

### **s** — 源极端子电气端口

与所选预参数化 MOSFET 的源极端子相关联的电气守恒端口。

## 参数

### **Series** — MOSFET 系列 `Infineon OptiMOS6 40V`（默认）| `Infineon OptiMOS5 80V` | `Infineon OptiMOS4 60V` | `Infineon OptiMOST 120V`

预参数化 MOSFET 的系列，指定为 `Infineon OptiMOS6 40V`、`Infineon OptiMOS5 80V`、`Infineon OptiMOS4 60V` 或 `Infineon OptiMOST 120V`。

### **Device** — 器件名称 `IPB015N08N5` | `IAUC120N04S6N009` | `IAUC120N04S6N010` | `IAUC120N04S6N013` | `IAUC100N04S6N015` | ...

器件名称，指定为可用参数化表中列出的选项之一。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

由外部 SPICE 子电路参数化的预定义 MOSFET

SPICE-Imported MOSFET 模块对使用外部 SPICE 子电路参数化的金属氧化物半导体场效应晶体管（MOSFET）进行建模。

您可以使用此模块对表中列出的 MOSFET 器件进行建模。这些参数化已使用 `subcircuit2ssc` 函数导入到 Simscape 中，并且已针对使用 SPICE 仿真工具生成的结果进行了数值验证。

**可用参数化**

| 系列 | 器件 |
| --- | --- |
| **Infineon OptiMOS6 40V** | `IAUC120N04S6N009` |
| `IAUC120N04S6N010` |
| `IAUC120N04S6N013` |
| `IAUC100N04S6N015` |
| `IAUC100N04S6N022` |
| `IAUC100N04S6N028` |
| `IAUC80N04S6N036` |
| `IAUC60N04S6N036` |
| `IAUC120N04S6L008` |
| `IAUC120N04S6L009` |
| `IAUC120N04S6L012` |
| `IAUC100N04S6L014` |
| `IAUC100N04S6L020` |
| `IAUC100N04S6L025` |
| `IAUC80N04S6L032` |
| `IAUC60N04S6L039` |
| **Infineon OptiMOS5 80V** | `IPB015N08N5` |
| `IPB017N08N5` |
| `IPP020N08N5` |
| `IPT012N08N5` |
| `IPB020N08N5` |
| `IPP023N08N5` |
| `IPB024N08N5` |
| `IPP027N08N5` |
| `IPB031N08N5` |
| `IPP034N08N5` |
| `IPB049N08N5` |
| `IPP052N08N5` |
| `IAUT300N08S5N012` |
| `IAUT165N08S5N029` |
| `IAUT300N08S5N014` |
| `IAUT240N08S5N019` |
| `IAUT200N08S5N023` |
| `IAUS300N08S5N013T` |
| `IAUS300N08S5N015T` |
| `IAUC100N08S5N031` |
| `IAUC100N08S5N043` |
| `IAUC70N08S5N074` |
| **Infineon OptiMOS4 60V** | `IPB180N06S4_H1` |
| `IPB120N06S4_H1` |
| `IPI120N06S4_H1` |
| `IPP120N06S4_H1` |
| `IPB120N06S4_02` |
| `IPI120N06S4_02` |
| `IPP120N06S4_02` |
| `IPB120N06S4_03` |
| `IPI120N06S4_03` |
| `IPP120N06S4_03` |
| `IPB90N06S4_04` |
| `IPD90N06S4_04` |
| `IPD100N06S4_03` |
| `IPI90N06S4_04` |
| `IPP90N06S4_04` |
| `IPB80N06S4_05` |
| `IPD90N06S4_05` |
| `IPI80N06S4_05` |
| `IPP80N06S4_05` |
| `IPB80N06S4_07` |
| `IPD90N06S4_07` |
| `IPI80N06S4_07` |
| `IPP80N06S4_07` |
| `IPB45N06S4_09` |
| `IPD50N06S4_09` |
| `IPI45N06S4_09` |
| `IPP45N06S4_09` |
| `IPG20N06S4_15` |
| `IPB90N06S4L_04` |
| `IPD90N06S4L_03` |
| `IPI90N06S4L_04` |
| `IPP90N06S4L_04` |
| `IPB80N06S4L_05` |
| `IPD90N06S4L_05` |
| `IPI80N06S4L_05` |
| `IPP80N06S4L_05` |
| `IPB80N06S4L_07` |
| `IPD90N06S4L_06` |
| `IPI80N06S4L_07` |
| `IPP80N06S4L_07` |
| `IPB45N06S4L_08` |
| `IPD50N06S4L_08` |
| `IPI45N06S4L_08` |
| `IPP45N06S4L_08` |
| `IPD50N06S4L_12` |
| `IPD30N06S4L_23` |
| `IPD25N06S4L_30` |
| `IPG20N06S4L_11` |
| `IPG20N06S4L_14` |
| `IPG20N06S4L_26` |
| **Infineon OptiMOST 120V** | `IPB100N12S3_05` |
| `IPI100N12S3_05` |
| `IPP100N12S3_05` |
| `IPB70N12S3_11` |
| `IPI70N12S3_11` |
| `IPP70N12S3_11` |
| `IPD70N12S3_11` |
| `IPD70N12S3L_12` |
| `IPB70N12S3L_12` |
| `IPI70N12S3L_12` |
| `IPP70N12S3L_12` |
| `IPB50N12S3L_15` |
| `IPD50N12S3L_15` |
| `IPI50N12S3L_15` |
| `IPP50N12S3L_15` |
| `IPB35N12S3L_26` |
| `IPD35N12S3L_24` |
| `IPD30N12S3L_31` |
