---
type: simulink-block
title: 'Discrete Varying Observer Form'
family: 'linear-parameter-varying'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'discretevaryingobserverform'
documentation_source_path: 'ref/discretevaryingobserverform.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Varying Observer Form

## 端口

### 输入

### **yk** — 测量信号 scalar | vector

测得的被控对象输出信号。

### **A** — 被控对象状态矩阵 matrix

被控对象状态矩阵，维度为 *Nx*×*Nx*，其中 *Nx* 是被控对象状态的数量。

### **B** — 被控对象输入矩阵 matrix

被控对象输入矩阵，维度为 *Nx*×*Nu*，其中 *Nu* 是被控对象输入的数量。

### **C** — 被控对象输出矩阵 matrix

被控对象输出矩阵，维度为 *Ny*×*Nx*，其中 *Ny* 是被控对象输出的数量。

### **D** — 被控对象前馈矩阵 matrix

被控对象前馈矩阵，维度为 *Ny*×*Nu*。

### **K** — 状态反馈矩阵 matrix

状态反馈矩阵，维度为 *Nu*×*Nx*。

### **L** — 状态观测器矩阵 matrix

状态观测器矩阵，维度为 *Nx*×*Ny*。

### 输出

### **uk** — 控制信号 scalar | vector

控制信号（被控对象输入）。

### **xk** — 估计的被控对象状态向量 vector

被控对象状态的估计值向量。

#### 依赖关系

要启用此端口，请选择 **Output states** 参数。

### **xk+1** — 估计的下一状态向量 vector

下一时间步的估计状态值。

#### 依赖关系

要启用此端口，请选择 **Output state updates** 参数。

## 参数

### **Initial conditions** — 系统初始条件 0（默认值）| scalar | vector

初始状态值，指定为标量或向量，其长度等于被控对象状态的数量。

### **Sample time (-1 for inherited)** — 模块采样时间 –1（默认值）| positive scalar

模块采样时间，指定为 –1（继承采样时间）或正标量值。

### **Output states** — 提供状态输出 on（默认值）| off

选中此参数可启用估计状态输出端口 **xe**。

### **Output state derivatives** — 提供状态更新 on（默认值）| off

选中此参数可启用估计状态更新输出端口 **xk+1**。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

矩阵值可变的离散时间观测器形式状态空间模型

使用此模块实现观测器形式的离散时间时变状态空间模型。系统矩阵 *A*、*B*、*C* 和 *D* 描述被控对象的动态特性，矩阵 *K* 和 *L* 分别指定状态反馈增益和状态观测器增益。将这些矩阵的瞬时值提供给相应的输入端口。观测器形式为：

xk+1=Axk+Buk+Lεkuk=−Kxkεk=yk−Cxk−Duk,

其中，*uk* 是被控对象输入（控制信号），*yk* 是被控对象输出，*xk* 是估计状态，*εk* 是新息，即被控对象输出的预测值与测量值之差。观测器形式很适合用于状态空间控制器的增益调度。具体而言，状态 *xk* 跟踪被控对象状态，并且所有控制器均使用相同的状态坐标表示。

使用此模块和 Linear Parameter Varying 库中的其他模块，可实现参数或系数可变的常用控制元素。有关详细信息，请参阅“在 Simulink 中对增益调度控制系统进行建模”。

**注意**

避免使 **K** 矩阵依赖于控制信号 **uk**。如果存在这种依赖关系，则生成的方程 *uk* = –*K*(*uk*)*xk* 会创建代数环，因为计算模块输出值需要已知模块输出值。此代数环容易导致不稳定和发散。相反，请尝试用时间 *t* 和模块输入 **yk** 来表示 **K**。

出于类似原因，避免使 **A**、**B** 或 **L** 依赖于 **uk+1** 输出。
