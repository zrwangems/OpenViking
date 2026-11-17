---
type: simulink-block
title: 'S-Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'sfunction'
documentation_source_path: 'slref/sfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Function

## 端口
```yaml
ports:
- name: In
  summary: S-Function 模块的信号输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Out
  summary: S-Function 模块的信号输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **In** — S-Function 模块的信号输入 标量 | 向量 | 矩阵

您可以使用 `mdlInitializeSizes` 回调函数配置输入端口。使用 `mdlInitializeSizes` 函数指定输入端口数量、输入信号维度、每个端口的采样时间，以及端口是否为直接馈通。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Out** — S-Function 模块的信号输出 标量 | 向量 | 矩阵

您可以使用 `mdlInitializeSizes` 回调函数配置输出端口。使用 `mdlInitializeSizes` 函数指定输出端口数量、输出信号维度，以及每个端口的采样时间。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: S-function name
  summary: S-Function 的名称 system（默认）| S-Function 名称
  group: ''
  block_parameter: FunctionName
  values: '''system''（默认）| 带引号的 S-Function 名称'
- name: S-function parameters
  summary: 附加的 S-Function 参数 MATLAB 表达式 | 逗号分隔的变量
  group: ''
  block_parameter: Parameters
  values: '''''（默认）| 带引号的 S-Function 参数'
- name: S-function modules
  summary: 用于代码生成的附加文件 ''（默认）| 文件名
  group: ''
  block_parameter: SFunctionModules
  values: '''''（默认）| 带引号的文件名'
```

### **S-function name** — S-Function 的名称 `system`（默认）| S-Function 名称

使用此参数指定 S-Function 的名称。

#### 编程方式使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `FunctionName` |
| **值：** | `'system'`（默认）| 带引号的 S-Function 名称 |

### **S-function parameters** — 附加的 S-Function 参数 MATLAB 表达式 | 逗号分隔的变量

指定附加的 S-Function 参数。

函数参数可以指定为 MATLAB 表达式或以逗号分隔的变量。例如：

```
A, B, C, D, [eye(2,2);zeros(2,2)]
```

虽然各个参数可以用方括号括起来，但参数列表本身不能用方括号括起来。

#### 编程方式使用

|  |  |
| --- | --- |
| **参数：** | `Parameters` |
| **值：** | `''`（默认）| 带引号的 S-Function 参数 |

### **S-function modules** — 用于代码生成的附加文件 `''`（默认）| 文件名

此参数仅当此模块表示 C MEX S-Function 且您打算使用 Simulink Coder™ 软件从包含该模块的模型生成代码时适用。如果使用此参数，当您准备生成代码时，必须强制代码生成器重新构建顶层模型，如 Control Regeneration of Top Model Code (Simulink Coder) 中所述。

有关使用此参数的详细信息，请参阅 Specify Additional Source Files for an S-Function (Simulink Coder)。

#### 编程方式使用

|  |  |
| --- | --- |
| **参数：** | `SFunctionModules` |
| **值：** | `''`（默认）| 带引号的文件名 |
## 所属库

Simulink / User-Defined Functions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `yesa` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **过零检测** | `yesa` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 实际代码生成支持取决于模块实现。
- 调用 MATLAB 的 S-Function 不支持代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

- 实际数据类型支持取决于模块实现。
- 有关在 S-Function 中使用定点数据类型的详细信息，请参阅 Integrate External Code (Fixed-Point Designer)。

## 版本历史

**在 R2006a 之前引入**

## 描述

在模型中包含 S-Function

S-Function 模块允许您将用 C、C++ 或 Fortran® 编写的 S-Function 或系统函数算法（称为 C MEX S-Function）集成到 Simulink 模型中。您可以使用该模块实现 Level-1 或 Level-2 C MEX S-Function。要将 S-Function 合并到模型中，在编译 C MEX S-Function 之后：

1. 从 **Simulink Library Browser** 中将 S-Function 模块拖到您的模型中。
2. 打开 **Block Parameters** 对话框，在 **S-function name** 字段中指定 S-Function 名称，为 S-Function 模块提供功能。例如，键入 `timestwo` 并选择 **Apply**。

*S-Function* 是用 MATLAB®、C、C++ 或 Fortran 编写的 Simulink® 模块的计算机语言描述。如果您有 C、C++ 或 Fortran S-Function，则需要使用 `mex` 实用程序将其编译为 MEX 文件（请参阅 Build C MEX Function）。S-Function 定义了模块在仿真的不同阶段（如初始化、更新、导数、输出和终止）的工作方式。S-Function 使用一种称为 S-Function API 的特殊调用语法，使您能够与 Simulink 引擎交互。这种交互与引擎和内置 Simulink 模块之间发生的交互非常相似。在仿真的每一步中，仿真引擎都会调用一个方法来执行特定任务。

例如，下面是一个名为 `timestwo.c` 的简单 C MEX S-Function 示例，它输出其输入的两倍。

```
#define S_FUNCTION_NAME timestwo /* Specifies the name of the S-function (timestwo) */
#define S_FUNCTION_LEVEL 2 /* Specifies that the S-function is in the Level 2 format */

#include "simstruc.h" /* Defines the data structure */
static void mdlInitializeSizes(SimStruct *S) /* Initialize the input and output ports and their size */
{
    ssSetNumSFcnParams(S, 0);
    if (ssGetNumSFcnParams(S) != ssGetSFcnParamsCount(S)) {
        return; /* Parameter mismatch reported by the Simulink engine*/
    }

    if (!ssSetNumInputPorts(S, 1)) return;
    ssSetInputPortWidth(S, 0, DYNAMICALLY_SIZED);
    ssSetInputPortDirectFeedThrough(S, 0, 1);

    if (!ssSetNumOutputPorts(S,1)) return;
    ssSetOutputPortWidth(S, 0, DYNAMICALLY_SIZED);

    ssSetNumSampleTimes(S, 1);

    /* Take care when specifying exception free code - see sfuntmpl.doc */
    ssSetOptions(S, SS_OPTION_EXCEPTION_FREE_CODE);
    }
static void mdlInitializeSampleTimes(SimStruct *S) /* Set the sample time of the S-function as inherited */
{
    ssSetSampleTime(S, 0, INHERITED_SAMPLE_TIME);
    ssSetOffsetTime(S, 0, 0.0);
}
static void mdlOutputs(SimStruct *S, int_T tid) /* Calculate the block output for each time step */
{
    int_T i;
    InputRealPtrsType uPtrs = ssGetInputPortRealSignalPtrs(S,0);
    real_T *y = ssGetOutputPortRealSignal(S,0);
    int_T width = ssGetOutputPortWidth(S,0);

    for (i=0; i<width; i++) {
        *y++ = 2.0 *(*uPtrs[i]);
    }
}
static void mdlTerminate(SimStruct *S){} /* Perform tasks at the end of the simulation */

#ifdef MATLAB_MEX_FILE /* Is this file being compiled as a MEX-file? */
#include "simulink.c" /* MEX-file interface mechanism */
#else
#include "cg_sfun.h" /* Code generation registration function */
#endif
```

S-Function 遵循通用形式，可以适应连续、离散和混合系统。您可以在 S-Function 中实现算法，并使用 S-Function 模块将其添加到 Simulink 模型中。在编写 S-Function 并将其名称放入 S-Function 模块（可在 User-Defined Functions 模块库中找到）后，您可以使用封装来自定义用户界面。在此示例中，`timestwo.c` 函数使用 `mex timestwo.c` 编译，并使用 S-Function 模块实现。

Timestwo S-Function 使用 S-Function 模块实现。模块的输入是正弦波，模块的输出连接到 Scope 模块。

S-Function 模块显示指定的 S-Function 名称以及 S-Function 指定的输入和输出端口数量。连接到输入的信号必须具有 S-Function 为输入指定的维度。

**注意**

使用 Level-2 MATLAB S-Function 模块将 Level-2 MATLAB S-Function 包含在框图中。
