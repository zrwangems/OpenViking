---
type: simulink-block
title: 'Varying Observer Form'
family: 'linear-parameter-varying'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyingobserverform'
documentation_source_path: 'ref/varyingobserverform.html'
language: zh-CN
chinese_source: worker-translation
---

# Varying Observer Form

## 端口

### 输入

### **y** — 测量信号 scalar | vector

测得的被控对象输出信号。

### **A** — 被控对象状态矩阵 matrix

被控对象状态矩阵，维度为 *Nx*-by-*Nx*，其中 *Nx* 为被控对象状态数。

### **B** — 被控对象输入矩阵 matrix

被控对象输入矩阵，维度为 *Nx*-by-*Nu*，其中 *Nu* 为被控对象输入数。

### **C** — 被控对象输出矩阵 matrix

被控对象输出矩阵，维度为 *Ny*-by-*Nx*，其中 *Ny* 为被控对象输出数。

### **D** — 被控对象前馈矩阵 matrix

被控对象前馈矩阵，维度为 *Ny*-by-*Nu*。

### **K** — 状态反馈矩阵 matrix

状态反馈矩阵，维度为 *Nu*-by-*Nx*。

### **L** — 状态观测器矩阵 matrix

状态观测器矩阵，维度为 *Nx*-by-*Ny*。
### 输出

### **u** — 控制信号 scalar | vector

控制信号（被控对象输入）。

### **xe** — 被控对象状态估计向量 vector

被控对象状态估计值向量。

#### 依赖关系

要启用此端口，请选择 **输出状态** 参数。

### **dxe** — 估计状态导数 vector

**xe** 中对应估计状态的导数。

#### 依赖关系

要启用此端口，请选择 **输出状态更新** 参数。

## 参数

### **初始条件** — 系统初始条件 0 (默认) | scalar | vector

初始状态值，指定为 scalar 或 vector；如果使用 vector，其长度必须等于被控对象状态数。

### **状态名称（例如 'position'）** — 被控对象状态名称 `''` (默认) | character vector | cell array

要标识被控对象状态，请按以下方式指定状态名称：

- character vector，适用于单状态被控对象。
- 由 character vector 组成的 cell array，适用于多状态
  被控对象。

### **输出状态** — 提供状态输出 on (默认) | off

选择此参数可启用估计状态输出端口 **xe**。

### **输出状态导数** — 提供状态导数 on (默认) | off

选择此参数可启用估计状态导数输出端口 **dxe**。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

矩阵值可变的观测器形式状态空间模型

使用此模块可实现观测器形式的连续时间时变状态空间模型。系统矩阵 *A*、*B*、*C* 和 *D* 描述被控对象的动态特性，矩阵 *K* 和 *L* 分别指定状态反馈增益和状态观测器增益。将这些矩阵的瞬时值输入到相应的输入端口。观测器形式为：

dxe=Axe+Bu+Lεu=−Kxeε=y−Cxe−Du,

其中，*u* 为被控对象输入（控制信号），*y* 为被控对象输出，*xe* 为估计状态，*ε* 为新息，即被控对象输出的预测值与测量值之差。观测器形式非常适用于状态空间控制器的增益调度。具体而言，状态 *xe* 会跟踪被控对象状态，并且所有控制器均使用相同的状态坐标表示。

使用此模块以及 Linear Parameter Varying 库中的其他模块，可实现具有可变参数或系数的常用控制元素。有关详细信息，请参阅“在 Simulink 中对增益调度控制系统建模”。

**注意**

避免使 **K** 矩阵依赖于控制信号 **u**。如果存在这种依赖关系，则生成的方程 *u* = –*K*(*u*)*xe* 会创建代数环，因为计算模块输出值需要知道模块输出值本身。此代数环容易导致不稳定和发散。相反，请尝试用时间 *t* 和模块输入 **y** 来表示 **K**。

出于类似原因，避免使 **A** 和 **B** 依赖于 **dxe** 输出。
