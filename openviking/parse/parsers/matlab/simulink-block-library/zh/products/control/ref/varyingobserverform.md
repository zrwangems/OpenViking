---
type: simulink-block
title: 'Varying Observer Form'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Control System Design and Tuning / Gain Scheduling / Continuous Time'
documentation_page: 'varyingobserverform'
documentation_source_path: '../control/ref/varyingobserverform.html'
language: zh-CN
chinese_source: worker-translation
---

# Varying Observer Form

## 端口

### 输入

### **y** — 测量信号 标量 | 向量

测得的被控对象输出信号。

### **A** — 被控对象状态矩阵 矩阵

被控对象状态矩阵，维度为 *Nx*-by-*Nx*，其中 *Nx* 是被控对象状态的数量。

### **B** — 被控对象输入矩阵 矩阵

被控对象输入矩阵，维度为 *Nx*-by-*Nu*，其中 *Nu* 是被控对象输入的数量。

### **C** — 被控对象输出矩阵 矩阵

被控对象输出矩阵 *Ny*-by-*Nx*，其中 *Ny* 是被控对象输出的数量。

### **D** — 被控对象前馈矩阵 矩阵

被控对象前馈矩阵，维度为 *Ny*-by-*Nu*。

### **K** — 状态反馈矩阵 矩阵

状态反馈矩阵，维度为 *Nu*-by-*Nx*。

### **L** — 状态观测器矩阵 矩阵

状态观测器矩阵，维度为 *Nx*-by-*Ny*。

### 输出

### **u** — 控制信号 标量 | 向量

控制信号（被控对象输入）。

### **xe** — 估计的被控对象状态向量 向量

估计的被控对象状态组成的向量。

#### 依赖关系

要启用此端口，请选择 **Output states** 参数。

### **dxe** — 估计的状态导数 向量

**xe** 中相应估计状态的导数。

#### 依赖关系

要启用此端口，请选择 **Output state updates** 参数。

## 参数

### **Initial conditions** — 系统初始条件 0（默认）| 标量 | 向量

初始状态值，指定为标量或向量，其长度为被控对象状态的数量。

### **State names (e.g., 'position')** — 被控对象状态名称 `''`（默认）| character vector | cell array

要标识被控对象状态，请将状态名称指定为：

- character vector，用于单状态被控对象。
- Cell array of character vectors，用于多状态
  被控对象。

### **Output states** — 提供状态输出 on（默认）| off

选择以启用估计状态输出端口 **xe**。

### **Output state derivatives** — 提供状态导数 on（默认）| off

选择以启用估计状态导数输出端口 **dxe**。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

矩阵值可变的观测器形式状态空间模型

使用此模块实现观测器形式的连续时间变化状态空间模型。系统矩阵 *A*、*B*、*C* 和 *D* 描述被控对象动态，矩阵 *K* 和 *L* 分别指定状态反馈增益和状态观测器增益。将这些矩阵的瞬时值馈送到对应的输入端口。观测器形式由下式给出：

dxe=Axe+Bu+Lεu=−Kxeε=y−Cxe−Du,

其中 *u* 是被控对象输入（控制信号），*y* 是被控对象输出，*xe* 是估计状态，*ε* 是新息，即预测的被控对象输出与测得的被控对象输出之间的差。观测器形式非常适用于状态空间控制器的增益调度。特别地，状态 *xe* 跟踪被控对象状态，并且所有控制器都用相同的状态坐标表示。

使用此模块以及 Linear Parameter Varying 库中的其他模块来实现具有可变参数或系数的常见控制元件。有关详细信息，请参阅 Model Gain-Scheduled Control Systems in Simulink。

**注意**

避免使 **K** 矩阵依赖于控制信号 **u**。如果存在这种依赖关系，则所得方程 *u* = –*K*(*u*)*xe* 会创建一个代数环，因为计算模块输出值需要知道模块输出值。此代数环容易导致不稳定和发散。相反，请尝试用时间 *t* 和模块输入 **y** 来表示 **K**。

出于类似原因，避免使 **A** 和 **B** 依赖于 **dxe** 输出。
