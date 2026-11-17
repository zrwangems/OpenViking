---
type: simulink-block
title: 'Discrete Varying Observer Form'
family: 'control'
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

### **yk** — 测量信号 标量 | 向量

被测对象输出信号。

### **A** — 对象状态矩阵 矩阵

对象状态矩阵，维度为 *Nx*×*Nx*，其中 *Nx* 是对象状态的数量。

### **B** — 对象输入矩阵 矩阵

对象输入矩阵，维度为 *Nx*×*Nu*，其中 *Nu* 是对象输入的数量。

### **C** — 对象输出矩阵 矩阵

对象输出矩阵，维度为 *Ny*×*Nx*，其中 *Ny* 是对象输出的数量。

### **D** — 对象前馈矩阵 矩阵

对象前馈矩阵，维度为 *Ny*×*Nu*。

### **K** — 状态反馈矩阵 矩阵

状态反馈矩阵，维度为 *Nu*×*Nx*。

### **L** — 状态观测器矩阵 矩阵

状态观测器矩阵，维度为 *Nx*×*Ny*。
### 输出

### **uk** — 控制信号 标量 | 向量

控制信号（对象输入）。

### **xk** — 估计的对象状态向量 向量

估计的对象状态向量。

#### 依赖关系

要启用此端口，请选择 **Output states** 参数。

### **xk+1** — 估计的下一状态向量 向量

下一时间步的估计状态值。

#### 依赖关系

要启用此端口，请选择 **Output state updates** 参数。

## 参数

### **Initial conditions** — 系统初始条件 0（默认）| 标量 | 向量

初始状态值，指定为标量或长度等于对象状态数量的向量。

### **Sample time (-1 for inherited)** — 模块采样时间 –1（默认）| 正标量

模块采样时间，指定为 –1（继承采样时间）或正标量值。

### **Output states** — 提供状态输出 on（默认）| off

选择以启用估计状态输出端口 **xe**。

### **Output state derivatives** — 提供状态更新 on（默认）| off

选择以启用估计状态更新输出端口 **xk+1**。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

具有可变矩阵值的离散时间观测器形式状态空间模型

使用此模块实现观测器形式的离散时间可变状态空间模型。系统矩阵 *A*、*B*、*C* 和 *D* 描述对象动态特性，矩阵 *K* 和 *L* 分别指定状态反馈增益和状态观测器增益。将这些矩阵的瞬时值馈入对应的输入端口。观测器形式由下式给出：

xk+1=Axk+Buk+Lεkuk=−Kxkεk=yk−Cxk−Duk，

其中 *uk* 是对象输入（控制信号），*yk* 是对象输出，*xk* 是估计状态，*εk* 是新息，即预测的对象输出与测量的对象输出之间的差值。观测器形式非常适用于状态空间控制器的增益调度。特别是，状态 *xk* 跟踪对象状态，并且所有控制器都以相同的状态坐标表示。

使用此模块以及 Linear Parameter Varying 库中的其他模块来实现具有可变参数或系数的常见控制元件。有关详细信息，请参阅 Model Gain-Scheduled Control Systems in Simulink。

**注意**

避免使 **K** 矩阵依赖于控制信号 **uk**。如果您有这样的依赖关系，所得方程 *uk* = –*K*(*uk*)*xk* 会创建代数环，因为计算模块输出值需要知道模块输出值。此代数环容易导致不稳定和发散。相反，请尝试将 **K** 表示为时间 *t* 和模块输入 **yk** 的函数。

出于类似原因，避免使 **A**、**B** 或 **L** 依赖于 **uk+1** 输出。
