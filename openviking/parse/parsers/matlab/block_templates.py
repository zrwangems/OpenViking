# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Per-block description templates for Simulink system JSON.

Every template is a deterministic string with named placeholders.  The values
come from the block's own XML/MDL parameters, so generating a description does
not call a language model, a network service or any other non-reproducible
component.  Types without a dedicated entry use ``GENERIC``; therefore every
block gets a description even when a model uses a toolbox block that is not
listed here.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BlockTemplate:
    """One bilingual block description template."""

    zh: str
    en: str


def _t(zh: str, en: str) -> BlockTemplate:
    return BlockTemplate(zh=zh, en=en)


# Templates are keyed by Simulink BlockType.  Keep placeholders aligned with the
# parameter names written by Simulink in the SLX/MDL file; the renderer falls
# back to a language-specific "not set" marker when an optional parameter is
# absent.  ``source_block``, ``config`` and ``param_count`` are computed.
TEMPLATES: dict[str, BlockTemplate] = {
    "Inport": _t(
        "输入端口，端口序号 {Port}，输出数据类型 {OutDataTypeStr}。",
        "Input port {Port}; output data type {OutDataTypeStr}.",
    ),
    "InportShadow": _t(
        "Inport Shadow 模块，对应端口 {Port} 的输入影子。",
        "Inport Shadow for port {Port}.",
    ),
    "Outport": _t(
        "输出端口，端口序号 {Port}，初始输出 {InitialOutput}，输出数据类型 {OutDataTypeStr}。",
        "Output port {Port}; initial output {InitialOutput}; output data type {OutDataTypeStr}.",
    ),
    "PMIOPort": _t(
        "物理建模端口，端口序号 {Port}，位于 {Side} 侧。",
        "Physical modeling port {Port} on the {Side} side.",
    ),
    "ConnectionPort": _t(
        "Simscape 连接端口，端口序号 {Port}，位于 {Side} 侧，定义域 {Domain}。",
        "Simscape connection port {Port} on the {Side} side; domain {Domain}.",
    ),
    "EnablePort": _t(
        "使能端口，使能时状态 {StatesWhenEnabling}。",
        "Enable port; states when enabling: {StatesWhenEnabling}.",
    ),
    "TriggerPort": _t(
        "触发端口，触发类型 {TriggerType}，使能时状态 {StatesWhenEnabling}。",
        "Trigger port; trigger type {TriggerType}; states when enabling {StatesWhenEnabling}.",
    ),
    "ActionPort": _t(
        "动作端口，标记动作子系统的执行入口。",
        "Action port marking the execution entry of an action subsystem.",
    ),
    "ResetPort": _t(
        "复位端口，复位时把子系统状态恢复到初始值。",
        "Reset port restoring subsystem states to their initial values.",
    ),
    "ForEach": _t(
        "For Each 控制块，按模型的迭代维度重复执行子系统。",
        "For Each control block repeating the subsystem over the configured dimensions.",
    ),
    "ForIterator": _t(
        "For Iterator 控制块，按迭代变量和范围重复执行子系统。",
        "For Iterator control block repeating the subsystem over an iteration range.",
    ),
    "WhileIterator": _t(
        "While Iterator 控制块，在条件成立时重复执行子系统。",
        "While Iterator control block repeating the subsystem while its condition holds.",
    ),
    "MessageTrigger": _t(
        "消息触发端口，收到消息时触发子系统。",
        "Message trigger port firing the subsystem when a message arrives.",
    ),
    "SubSystem": _t(
        "子系统模块，内部块和连线展开到子页面。配置：{config}。",
        "Subsystem; its blocks and connections are expanded on a child page. Configuration: {config}.",
    ),
    "VariantAssemblySubSystem": _t(
        "变体装配子系统，按变体配置选择内部装配方案。",
        "Variant assembly subsystem selecting an internal assembly by variant configuration.",
    ),
    "VariantSource": _t(
        "变体源模块，变体控制模式 {VariantControlMode}。",
        "Variant source; variant control mode {VariantControlMode}.",
    ),
    "VariantSink": _t(
        "变体汇模块，把选中的变体分支汇合到输出。",
        "Variant sink merging the selected variant branch into its output.",
    ),
    "ModelReference": _t(
        "模型引用模块，引用模型 {ModelNameDialog}，仿真模式 {SimulationMode}。",
        "Model reference to {ModelNameDialog}; simulation mode {SimulationMode}.",
    ),
    "Reference": _t(
        "库引用模块，引用 {source_block}，实例类型 {SourceType}，参数化方式 {param_by}；共 {param_count} 项实例参数按模板写入被引用模块。",
        "Library reference to {source_block}; instance type {SourceType}; parameterization {param_by}; {param_count} instance parameters are written by the template.",
    ),
    "Constant": _t(
        "常量模块，输出常量值 {Value}，采样时间 {SampleTime}。",
        "Constant block outputting {Value}; sample time {SampleTime}.",
    ),
    "Ground": _t(
        "接地模块，输出零值参考信号。",
        "Ground block outputting a zero reference signal.",
    ),
    "From": _t(
        "From 信号接收模块，接收 Goto 标签 {GotoTag}，标签可见性 {TagVisibility}。",
        "From block receiving Goto tag {GotoTag}; tag visibility {TagVisibility}.",
    ),
    "Goto": _t(
        "Goto 信号发送模块，发送标签 {GotoTag}，标签可见性 {TagVisibility}。",
        "Goto block sending tag {GotoTag}; tag visibility {TagVisibility}.",
    ),
    "ConnectionLabel": _t(
        "物理连接标签 {Label}，用于标识守恒网络中的连接点。",
        "Physical connection label {Label} identifying a connection point in a conserving network.",
    ),
    "TwoWayConnection": _t(
        "双向物理连接块，连接两个守恒端口。",
        "Two-way physical connection joining two conserving ports.",
    ),
    "Gain": _t(
        "增益模块，输出 = 输入 × {Gain}，乘法方式 {Multiplication}。",
        "Gain block: output = input × {Gain}; multiplication {Multiplication}.",
    ),
    "Sum": _t(
        "求和模块，输入符号 {Inputs}，图标形状 {IconShape}。",
        "Sum block with input signs {Inputs}; icon shape {IconShape}.",
    ),
    "Product": _t(
        "乘法模块，输入个数 {Inputs}，乘法方式 {Multiplication}。",
        "Product block with {Inputs} inputs; multiplication {Multiplication}.",
    ),
    "UnaryMinus": _t(
        "一元取反模块，输出为输入的相反数。",
        "Unary minus block negating its input.",
    ),
    "Math": _t(
        "数学运算模块，算子 {Operator}，输出信号类型 {OutputSignalType}。",
        "Math operation {Operator}; output signal type {OutputSignalType}.",
    ),
    "Trigonometry": _t(
        "三角函数模块，算子 {Operator}。",
        "Trigonometric function {Operator}.",
    ),
    "Sqrt": _t(
        "平方根模块，输出输入的平方根。",
        "Square root block.",
    ),
    "Abs": _t(
        "绝对值模块，输出输入信号的绝对值。",
        "Absolute value block.",
    ),
    "Signum": _t(
        "符号函数模块，输出输入的符号。",
        "Signum block outputting the sign of its input.",
    ),
    "Rounding": _t(
        "取整模块，算子 {Operator}。",
        "Rounding function {Operator}.",
    ),
    "Bias": _t(
        "偏置模块，输出 = 输入 + {Bias}。",
        "Bias block: output = input + {Bias}.",
    ),
    "MinMax": _t(
        "最值模块，函数 {Function}，输入个数 {Inputs}。",
        "Min/max block using {Function} over {Inputs} inputs.",
    ),
    "DotProduct": _t(
        "点积模块，计算输入向量的点积。",
        "Dot product block.",
    ),
    "UnitConversion": _t(
        "单位转换模块，按模型配置转换输入输出的物理单位。",
        "Unit conversion block applying the configured physical unit conversion.",
    ),
    "Saturate": _t(
        "饱和模块，输出限制在 [{LowerLimit}, {UpperLimit}]。",
        "Saturation block limiting the output to [{LowerLimit}, {UpperLimit}].",
    ),
    "DeadZone": _t(
        "死区模块，死区范围 [{LowerValue}, {UpperValue}]。",
        "Dead zone between {LowerValue} and {UpperValue}.",
    ),
    "Relay": _t(
        "继电器模块，开启阈值 {OnSwitchValue}，关闭阈值 {OffSwitchValue}，开启输出 {OnOutputValue}，关闭输出 {OffOutputValue}。",
        "Relay switching on at {OnSwitchValue} and off at {OffSwitchValue}; on output {OnOutputValue}; off output {OffOutputValue}.",
    ),
    "Quantizer": _t(
        "量化器模块，量化间隔 {QuantizationInterval}。",
        "Quantizer with interval {QuantizationInterval}.",
    ),
    "WrapToZero": _t(
        "回绕到零模块，输入超过阈值 {Threshold} 时输出零。",
        "Wrap-to-zero block outputting zero above threshold {Threshold}.",
    ),
    "HitCrossing": _t(
        "过零检测模块，检测信号穿过偏置 {Offset} 的时刻。",
        "Hit crossing detection around offset {Offset}.",
    ),
    "Backlash": _t(
        "齿隙模块，死区宽度 {DeadbandWidth}。",
        "Backlash with deadband width {DeadbandWidth}.",
    ),
    "SaturationDynamic": _t(
        "动态饱和模块，上下限由输入端口给定。",
        "Dynamic saturation with upper and lower limits supplied by input ports.",
    ),
    "DeadZoneDynamic": _t(
        "动态死区模块，死区上下限由输入端口给定。",
        "Dynamic dead zone with limits supplied by input ports.",
    ),
    "RateLimiter": _t(
        "速率限制模块，上升斜率 {RisingSlewLimit}，下降斜率 {FallingSlewLimit}。",
        "Rate limiter with rising slew {RisingSlewLimit} and falling slew {FallingSlewLimit}.",
    ),
    "RateLimiterDynamic": _t(
        "动态速率限制模块，升降斜率由输入端口给定。",
        "Dynamic rate limiter with slews supplied by input ports.",
    ),
    "Switch": _t(
        "开关模块，按判据 {Criteria} 与阈值 {Threshold} 选择输入。",
        "Switch selecting an input by {Criteria} at threshold {Threshold}.",
    ),
    "MultiPortSwitch": _t(
        "多端口开关，数据端口顺序 {DataPortOrder}，索引 {DataPortIndices}。",
        "Multiport switch with data port order {DataPortOrder} and indices {DataPortIndices}.",
    ),
    "ManualSwitch": _t(
        "手动开关，当前设置 {CurrentSetting}。",
        "Manual switch currently set to {CurrentSetting}.",
    ),
    "Merge": _t(
        "信号合并模块，合并 {Inputs} 路条件执行分支。",
        "Merge block combining {Inputs} conditionally executed branches.",
    ),
    "Selector": _t(
        "选择器模块，按索引 {Indices} 选择输入元素，索引选项 {IndexOptions}。",
        "Selector using indices {Indices}; index option {IndexOptions}.",
    ),
    "BusSelector": _t(
        "总线选择器，从总线中选出 {OutputSignals}。",
        "Bus selector extracting {OutputSignals}.",
    ),
    "BusCreator": _t(
        "总线创建模块，把 {Inputs} 路信号组合成总线。",
        "Bus creator combining {Inputs} signals into a bus.",
    ),
    "BusAssignment": _t(
        "总线赋值模块，替换总线中的 {AssignedSignals} 信号。",
        "Bus assignment replacing {AssignedSignals}.",
    ),
    "BusToVector": _t(
        "总线转向量模块，把总线信号转换为向量。",
        "Bus to vector conversion.",
    ),
    "SignalConversion": _t(
        "信号转换模块，转换输出为 {ConversionOutput}。",
        "Signal conversion to {ConversionOutput}.",
    ),
    "SignalSpecification": _t(
        "信号属性模块，声明维度 {Dimensions}、数据类型 {OutDataTypeStr}、单位 {Unit}。",
        "Signal specification with dimensions {Dimensions}, data type {OutDataTypeStr} and unit {Unit}.",
    ),
    "DataTypeConversion": _t(
        "数据类型转换模块，输出数据类型 {OutDataTypeStr}，舍入方式 {RndMeth}。",
        "Data type conversion to {OutDataTypeStr}; rounding {RndMeth}.",
    ),
    "Reshape": _t(
        "维度变换模块，输出维度 {OutputDimensions}，输出维度模式 {OutputDimensionality}。",
        "Reshape block with output dimensions {OutputDimensions}; mode {OutputDimensionality}.",
    ),
    "PermuteDimensions": _t(
        "维度重排模块，按模型配置重排输入维度。",
        "Permute dimensions block reordering input dimensions.",
    ),
    "Concatenate": _t(
        "拼接模块，把 {NumInputs} 路输入沿维度 {ConcatenateDimension} 拼接，模式 {Mode}。",
        "Concatenate {NumInputs} inputs along dimension {ConcatenateDimension}; mode {Mode}.",
    ),
    "Demux": _t(
        "解复用模块，把输入拆成 {Outputs} 路输出。",
        "Demux splitting the input into {Outputs} outputs.",
    ),
    "Mux": _t(
        "复用模块，把 {Inputs} 路输入合成一路。",
        "Mux combining {Inputs} inputs into one signal.",
    ),
    "Width": _t(
        "宽度模块，输出输入信号的宽度。",
        "Width block outputting the input signal width.",
    ),
    "Lookup": _t(
        "查表模块，输入值 {InputValues}，表数据 {Table}，插值方法 {LookUpMeth}。",
        "Lookup using input values {InputValues}, table {Table} and method {LookUpMeth}.",
    ),
    "Lookup_n-D": _t(
        "N 维查表模块，表数据 {Table}，第一维断点 {BreakpointsForDimension1}，越界诊断 {DiagnosticForOutOfRangeInput}。",
        "N-D lookup with table {Table}, first breakpoint set {BreakpointsForDimension1} and out-of-range diagnostic {DiagnosticForOutOfRangeInput}.",
    ),
    "LookupNDDirect": _t(
        "直接 N 维查表模块，维度数 {NumberOfTableDimensions}，表数据 {Table}。",
        "Direct N-D lookup with {NumberOfTableDimensions} dimensions and table {Table}.",
    ),
    "PreLookup": _t(
        "预查表模块，为后续插值计算断点区间和索引。",
        "Pre-lookup computing breakpoint intervals and indices for interpolation.",
    ),
    "Interpolation_n-D": _t(
        "N 维插值模块，按预查表结果和表数据计算插值输出。",
        "N-D interpolation using pre-lookup results and table data.",
    ),
    "TransferFcn": _t(
        "连续传递函数模块，分子 {Numerator}，分母 {Denominator}。",
        "Continuous transfer function with numerator {Numerator} and denominator {Denominator}.",
    ),
    "DiscreteTransferFcn": _t(
        "离散传递函数模块，分子 {Numerator}，分母 {Denominator}，初始状态 {InitialStates}。",
        "Discrete transfer function with numerator {Numerator}, denominator {Denominator} and initial states {InitialStates}.",
    ),
    "StateSpace": _t(
        "状态空间模块，A={A}，B={B}，C={C}，D={D}。",
        "State-space block with A={A}, B={B}, C={C}, D={D}.",
    ),
    "ZeroPole": _t(
        "零极点模块，零点 {Zeros}，极点 {Poles}，增益 {Gain}。",
        "Zero-pole block with zeros {Zeros}, poles {Poles} and gain {Gain}.",
    ),
    "DiscreteFilter": _t(
        "离散滤波器，分子 {Numerator}，分母 {Denominator}，初始状态 {InitialStates}。",
        "Discrete filter with numerator {Numerator}, denominator {Denominator} and initial states {InitialStates}.",
    ),
    "PIDController": _t(
        "PID 控制器，比例 {P}，积分 {I}，微分 {D}。",
        "PID controller with P={P}, I={I} and D={D}.",
    ),
    "Integrator": _t(
        "积分器模块，初始条件 {InitialCondition}，输出限幅 [{LowerSaturationLimit}, {UpperSaturationLimit}]。",
        "Integrator with initial condition {InitialCondition} and output limits [{LowerSaturationLimit}, {UpperSaturationLimit}].",
    ),
    "DiscreteIntegrator": _t(
        "离散积分器，积分方法 {IntegratorMethod}，初始条件 {InitialCondition}，采样时间 {SampleTime}。",
        "Discrete integrator using {IntegratorMethod}; initial condition {InitialCondition}; sample time {SampleTime}.",
    ),
    "SecondOrderIntegrator": _t(
        "二阶积分器，初始 X={ICX}，初始 dX/dt={ICDXDT}，X 限幅 [{LowerLimitX}, {UpperLimitX}]。",
        "Second-order integrator with initial X={ICX}, initial dX/dt={ICDXDT} and X limits [{LowerLimitX}, {UpperLimitX}].",
    ),
    "Derivative": _t(
        "微分模块，输出输入信号的时间导数。",
        "Derivative block outputting the time derivative of its input.",
    ),
    "FirstOrderHold": _t(
        "一阶保持器，初始输出 {InitialOutput}，输出算法 {OutputAlgorithm}。",
        "First-order hold with initial output {InitialOutput} and algorithm {OutputAlgorithm}.",
    ),
    "ZeroOrderHold": _t(
        "零阶保持器，采样时间 {SampleTime}。",
        "Zero-order hold with sample time {SampleTime}.",
    ),
    "UnitDelay": _t(
        "单位延迟模块，初始条件 {InitialCondition}，采样时间 {SampleTime}。",
        "Unit delay with initial condition {InitialCondition} and sample time {SampleTime}.",
    ),
    "Delay": _t(
        "延迟模块，延迟 {DelayLength} 个采样步，初始条件 {InitialCondition}。",
        "Delay of {DelayLength} samples with initial condition {InitialCondition}.",
    ),
    "TappedDelay": _t(
        "抽头延迟线，抽头数 {NumDelays}，初始条件 {InitialCondition}。",
        "Tapped delay line with {NumDelays} taps and initial condition {InitialCondition}.",
    ),
    "TransportDelay": _t(
        "传输延迟模块，延迟时间 {DelayTime}。",
        "Transport delay of {DelayTime}.",
    ),
    "VariableTransportDelay": _t(
        "可变传输延迟模块，延迟时间由输入端口给定。",
        "Variable transport delay with delay time supplied by an input port.",
    ),
    "Memory": _t(
        "记忆模块，输出上一采样步的输入，初始条件 {InitialCondition}。",
        "Memory block holding the previous input; initial condition {InitialCondition}.",
    ),
    "RateTransition": _t(
        "速率转换模块，输出采样时间 {OutPortSampleTime}，数据完整性 {Integrity}。",
        "Rate transition with output sample time {OutPortSampleTime}; integrity {Integrity}.",
    ),
    "DataStoreRead": _t(
        "数据存储读取模块，读取数据存储 {DataStoreName}。",
        "Data store read from {DataStoreName}.",
    ),
    "DataStoreWrite": _t(
        "数据存储写入模块，写入数据存储 {DataStoreName}。",
        "Data store write to {DataStoreName}.",
    ),
    "DataStoreMemory": _t(
        "数据存储内存模块，定义数据存储 {DataStoreName}。",
        "Data store memory defining {DataStoreName}.",
    ),
    "Logic": _t(
        "逻辑运算模块，算子 {Operator}，输入个数 {Inputs}。",
        "Logical operation {Operator} over {Inputs} inputs.",
    ),
    "RelationalOperator": _t(
        "关系运算模块，算子 {Operator}。",
        "Relational operator {Operator}.",
    ),
    "If": _t(
        "If 条件子系统控制块，条件表达式 {IfExpression}。",
        "If control block with expression {IfExpression}.",
    ),
    "Fcn": _t(
        "Fcn 模块，按表达式 {Expr} 计算输出。",
        "Fcn block evaluating {Expr}.",
    ),
    "S-Function": _t(
        "S-Function 模块，函数名 {FunctionName}，参数 {Parameters}。",
        "S-Function {FunctionName} with parameters {Parameters}.",
    ),
    "MATLABFunction": _t(
        "MATLAB Function 模块，执行内嵌的 MATLAB 代码。",
        "MATLAB Function block executing embedded MATLAB code.",
    ),
    "MATLABSystem": _t(
        "MATLAB System 模块，执行 System object 实现。",
        "MATLAB System block backed by a System object.",
    ),
    "Stateflow": _t(
        "Stateflow 图表，状态与转移在 stateflow 子页展开。",
        "Stateflow chart; states and transitions are expanded under stateflow.",
    ),
    "Probe": _t(
        "探针模块，测量信号的维度、采样时间或数据类型等属性。",
        "Probe block measuring signal dimensions, sample time or data type.",
    ),
    "Assertion": _t(
        "断言模块，检查信号是否满足模型断言条件。",
        "Assertion block checking a model assertion condition.",
    ),
    "Terminator": _t(
        "终止模块，吸收未连接的信号。",
        "Terminator absorbing an unconnected signal.",
    ),
    "Stop": _t(
        "Stop 模块，仿真到达该块时停止。",
        "Stop block halting the simulation when reached.",
    ),
    "Scope": _t(
        "示波器模块，显示 {NumInputPorts} 路信号，采样时间 {SampleTime}。",
        "Scope displaying {NumInputPorts} signals; sample time {SampleTime}.",
    ),
    "Display": _t(
        "显示模块，显示输入信号的数值。",
        "Display block showing the input value.",
    ),
    "ToWorkspace": _t(
        "To Workspace 模块，把信号写入工作区变量 {VariableName}。",
        "To Workspace block writing to variable {VariableName}.",
    ),
    "FromWorkspace": _t(
        "From Workspace 模块，从工作区变量 {VariableName} 读取信号，采样时间 {SampleTime}。",
        "From Workspace block reading variable {VariableName}; sample time {SampleTime}.",
    ),
    "Clock": _t(
        "时钟模块，输出仿真时间，采样时间 {SampleTime}。",
        "Clock block outputting simulation time; sample time {SampleTime}.",
    ),
    "DigitalClock": _t(
        "数字时钟模块，采样时间 {SampleTime}。",
        "Digital clock with sample time {SampleTime}.",
    ),
    "Step": _t(
        "阶跃模块，在 {Time} 时刻从 {Before} 跳到 {After}。",
        "Step changing from {Before} to {After} at time {Time}.",
    ),
    "InitialCondition": _t(
        "初始条件模块，输出初始值 {Value}。",
        "Initial condition block outputting {Value}.",
    ),
    "LampBlock": _t(
        "指示灯模块，按绑定信号显示状态。",
        "Lamp block displaying the state of its bound signal.",
    ),
    "SliderBlock": _t(
        "滑块控件模块，范围 [{ScaleMin}, {ScaleMax}]，刻度 {TickInterval}。",
        "Slider control with range [{ScaleMin}, {ScaleMax}] and tick interval {TickInterval}.",
    ),
    "KnobBlock": _t(
        "旋钮控件模块，范围 [{ScaleMin}, {ScaleMax}]，刻度 {TickInterval}。",
        "Knob control with range [{ScaleMin}, {ScaleMax}] and tick interval {TickInterval}.",
    ),
    "RotarySwitchBlock": _t(
        "旋转开关控件模块，按绑定信号选择档位。",
        "Rotary switch control selecting a position from its bound signal.",
    ),
    "PushButtonBlock": _t(
        "按钮控件模块，按钮文本 {ButtonText}，按钮类型 {ButtonType}。",
        "Push button control labelled {ButtonText}; button type {ButtonType}.",
    ),
    "ComboBox": _t(
        "下拉框控件模块，当前选项 {SelectedLabel}。",
        "Combo box control currently showing {SelectedLabel}.",
    ),
    "SimscapeBus": _t(
        "Simscape 总线模块，按 {HierarchyStrings} 组织物理网络连接。",
        "Simscape bus organizing physical connections as {HierarchyStrings}.",
    ),
    "SimscapeProbe": _t(
        "Simscape 探针模块，测量 {Variables}。",
        "Simscape probe measuring {Variables}.",
    ),
    "SimscapeComponentBlock": _t(
        "Simscape 组件模块，类名 {ClassName}，组件路径 {ComponentPath}。",
        "Simscape component {ClassName} at {ComponentPath}.",
    ),
    "FMU": _t(
        "FMU 导入模块，按 FMI 模型描述执行外部功能。",
        "FMU import block executing an external model through FMI.",
    ),
    "SHGravity": _t(
        "球谐重力模块，重力模型 {ephemerisModel}，阶数 {degree}，数据文件 {datafile}。",
        "Spherical harmonic gravity using {ephemerisModel}, degree {degree} and data file {datafile}.",
    ),
    "PlanetaryEphem": _t(
        "行星星历模块，目标 {target}，星历模型 {ephemerisModel}，输出速度 {outputVelocity}。",
        "Planetary ephemeris for {target} using {ephemerisModel}; output velocity {outputVelocity}.",
    ),
    "ECEF2LLA": _t(
        "ECEF 转 LLA 坐标模块，把地心地固坐标转换为经纬高。",
        "ECEF to LLA conversion.",
    ),
    "SpacecraftDynamics": _t(
        "航天器动力学模块，质量 {mass}，惯性 {inertia}，姿态 {attitude}，加速度输入 {accelIn}。",
        "Spacecraft dynamics with mass {mass}, inertia {inertia}, attitude {attitude} and acceleration input {accelIn}.",
    ),
    "FunctionCallGenerator": _t(
        "函数调用生成器，采样时间 {SampleTime}。",
        "Function-call generator with sample time {SampleTime}.",
    ),
    "FunctionCaller": _t(
        "函数调用模块，按函数原型调用模型中的函数。",
        "Function caller invoking a model function through its prototype.",
    ),
    "FunctionCallFeedbackLatch": _t(
        "函数调用反馈锁存模块，保存函数调用子系统的反馈状态。",
        "Function-call feedback latch holding feedback state for a function-call subsystem.",
    ),
}


GENERIC = _t(
    "{block_type} 模块（库来源 {source_block}）。按原模块类型套用通用描述模板；实例配置：{config}。",
    "{block_type} block from {source_block}. Generic description template; instance configuration: {config}.",
)
