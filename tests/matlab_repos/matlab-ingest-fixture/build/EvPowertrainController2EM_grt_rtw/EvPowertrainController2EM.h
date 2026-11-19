/*
 * EvPowertrainController2EM.h
 *
 * Code generation for model "EvPowertrainController2EM".
 *
 * Model version              : 11.0
 * Simulink Coder version : 25.2 (R2025b) 28-Jul-2025
 * C source code generated on : Thu Nov 19 10:59:43 2026
 *
 * Target selection: grt.tlc
 * Note: GRT includes extra infrastructure and instrumentation for prototyping
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef EvPowertrainController2EM_h_
#define EvPowertrainController2EM_h_
#ifndef EvPowertrainController2EM_COMMON_INCLUDES_
#define EvPowertrainController2EM_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "rtw_continuous.h"
#include "rtw_solver.h"
#include "rt_logging.h"
#include "rt_nonfinite.h"
#include "math.h"
#endif                          /* EvPowertrainController2EM_COMMON_INCLUDES_ */

#include "EvPowertrainController2EM_types.h"
#include "rtGetInf.h"
#include "rtGetNaN.h"
#include <float.h>
#include <string.h>
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetFinalTime
#define rtmGetFinalTime(rtm)           ((rtm)->Timing.tFinal)
#endif

#ifndef rtmGetRTWLogInfo
#define rtmGetRTWLogInfo(rtm)          ((rtm)->rtwLogInfo)
#endif

#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

#ifndef rtmGetStopRequested
#define rtmGetStopRequested(rtm)       ((rtm)->Timing.stopRequestedFlag)
#endif

#ifndef rtmSetStopRequested
#define rtmSetStopRequested(rtm, val)  ((rtm)->Timing.stopRequestedFlag = (val))
#endif

#ifndef rtmGetStopRequestedPtr
#define rtmGetStopRequestedPtr(rtm)    (&((rtm)->Timing.stopRequestedFlag))
#endif

#ifndef rtmGetT
#define rtmGetT(rtm)                   ((rtm)->Timing.taskTime0)
#endif

#ifndef rtmGetTFinal
#define rtmGetTFinal(rtm)              ((rtm)->Timing.tFinal)
#endif

#ifndef rtmGetTPtr
#define rtmGetTPtr(rtm)                (&(rtm)->Timing.taskTime0)
#endif

/* Block signals (default storage) */
typedef struct {
  real_T Probe;                        /* '<S7>/Probe' */
} B_EvPowertrainController2EM_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  real_T UnitDelay_DSTATE[201];        /* '<S69>/Unit Delay' */
  real_T UnitDelay_DSTATE_p[201];      /* '<S24>/Unit Delay' */
  real_T UnitDelay1_DSTATE[201];       /* '<S24>/Unit Delay1' */
  real_T UnitDelay_DSTATE_n[201];      /* '<S82>/Unit Delay' */
  real_T UnitDelay1_DSTATE_p;          /* '<S23>/Unit Delay1' */
  real_T UnitDelay2_DSTATE;            /* '<S23>/Unit Delay2' */
  real_T UnitDelay_DSTATE_l;           /* '<S42>/Unit Delay' */
  real_T UnitDelay1_DSTATE_o;          /* '<S42>/Unit Delay1' */
  real_T PrevY[2];                     /* '<Root>/Rate Limiter' */
  uint32_T m_bpIndex[202];             /* '<S68>/Eff Map' */
  uint32_T m_Cache01;                  /* '<S68>/Eff Map' */
  uint32_T m_Cache02[201];             /* '<S68>/Eff Map' */
  uint32_T m_bpIndex_e[202];           /* '<S81>/Eff Map' */
  uint32_T m_Cache01_a;                /* '<S81>/Eff Map' */
  uint32_T m_Cache02_g[201];           /* '<S81>/Eff Map' */
  uint32_T m_bpIndex_b;                /* '<S46>/1-D Lookup Table' */
} DW_EvPowertrainController2EM_T;

/* External inputs (root inport signals with default storage) */
typedef struct {
  real_T AccelPdl;                     /* '<Root>/AccelPdl' */
  real_T BcuBrkPrsCmd[4];              /* '<Root>/BcuBrkPrsCmd' */
  real_T VehSpdFdbk;                   /* '<Root>/VehSpdFdbk' */
  real_T EMSpd[2];                     /* '<Root>/EMSpd' */
  real_T TransGear;                    /* '<Root>/TransGear' */
  real_T BMSSOC;                       /* '<Root>/BMSSOC' */
  real_T BattPackVolt;                 /* '<Root>/BattPackVolt' */
  real_T BMSDischrgCurrLmt;            /* '<Root>/BMSDischrgCurrLmt' */
  real_T BMSChrgCurrLmt;               /* '<Root>/BMSChrgCurrLmt' */
  real_T pqr[3];                       /* '<Root>/pqr' */
  real_T SteerWhlAng[4];               /* '<Root>/SteerWhlAng' */
  real_T SteerCmd;                     /* '<Root>/SteerCmd' */
} ExtU_EvPowertrainController2E_T;

/* External outputs (root outports fed by signals with default storage) */
typedef struct {
  real_T EngTrqCmd;                    /* '<Root>/EngTrqCmd' */
  real_T EMTrqCmd[2];                  /* '<Root>/EMTrqCmd' */
  real_T VcuBrkPrsCmd[4];              /* '<Root>/VcuBrkPrsCmd' */
  real_T Cltch1Cmd;                    /* '<Root>/Cltch1Cmd' */
  real_T Neutral;                      /* '<Root>/Neutral' */
  real_T FuelCellCurrCmd;              /* '<Root>/FuelCellCurrCmd' */
  real_T FuelCellTempCmd;              /* '<Root>/FuelCellTempCmd' */
  real_T VcuTrlrBrkPrsCmd[6];          /* '<Root>/VcuTrlrBrkPrsCmd' */
} ExtY_EvPowertrainController2E_T;

/* Parameters (default storage) */
struct P_EvPowertrainController2EM_T_ {
  real_T CtrlBcuTrlrBrkGain;           /* Variable: CtrlBcuTrlrBrkGain
                                        * Referenced by: '<S7>/Gain1'
                                        */
  real_T CtrlVcuAccelPdlBpts[3];       /* Variable: CtrlVcuAccelPdlBpts
                                        * Referenced by: '<S46>/1-D Lookup Table'
                                        */
  real_T CtrlVcuEvChrgLmtBpt[11];      /* Variable: CtrlVcuEvChrgLmtBpt
                                        * Referenced by: '<S36>/ChrgLmt'
                                        */
  real_T CtrlVcuEvRegenBrkCutOff[2];   /* Variable: CtrlVcuEvRegenBrkCutOff
                                        * Referenced by: '<S36>/RegenBrakingCutoff'
                                        */
  real_T CtrlVcuEvRegenBrkSpdBpt[2];   /* Variable: CtrlVcuEvRegenBrkSpdBpt
                                        * Referenced by: '<S36>/RegenBrakingCutoff'
                                        */
  real_T CtrlVcuEvSocBpt[11];          /* Variable: CtrlVcuEvSocBpt
                                        * Referenced by: '<S36>/ChrgLmt'
                                        */
  real_T CtrlVcuFallRate;              /* Variable: CtrlVcuFallRate
                                        * Referenced by: '<Root>/Rate Limiter'
                                        */
  real_T CtrlVcuMaxAccelG;             /* Variable: CtrlVcuMaxAccelG
                                        * Referenced by:
                                        *   '<S72>/Constant7'
                                        *   '<S85>/Constant7'
                                        */
  real_T CtrlVcuMaxDecelG;             /* Variable: CtrlVcuMaxDecelG
                                        * Referenced by:
                                        *   '<S72>/Constant6'
                                        *   '<S85>/Constant6'
                                        */
  real_T CtrlVcuPwrRatePnlty[3];       /* Variable: CtrlVcuPwrRatePnlty
                                        * Referenced by: '<S46>/1-D Lookup Table'
                                        */
  real_T CtrlVcuRiseRate;              /* Variable: CtrlVcuRiseRate
                                        * Referenced by: '<Root>/Rate Limiter'
                                        */
  real_T CtrlVcuRoadMuEst;             /* Variable: CtrlVcuRoadMuEst
                                        * Referenced by:
                                        *   '<S64>/Road mu'
                                        *   '<S64>/Road mu1'
                                        *   '<S77>/Road mu'
                                        *   '<S77>/Road mu1'
                                        */
  real_T CtrlVcuSftyFctr;              /* Variable: CtrlVcuSftyFctr
                                        * Referenced by:
                                        *   '<S64>/Safety Factor'
                                        *   '<S64>/Safety Factor1'
                                        *   '<S77>/Safety Factor'
                                        *   '<S77>/Safety Factor1'
                                        */
  real_T CtrlVcuTracPwrErrPnlty;       /* Variable: CtrlVcuTracPwrErrPnlty
                                        * Referenced by: '<S23>/TracPwrErr Penalty'
                                        */
  real_T EnvGrvty;                     /* Variable: EnvGrvty
                                        * Referenced by:
                                        *   '<S73>/Constant20'
                                        *   '<S74>/Constant20'
                                        *   '<S74>/Constant3'
                                        *   '<S86>/Constant3'
                                        *   '<S87>/Constant20'
                                        *   '<S87>/Constant3'
                                        */
  real_T PlntBrkFrntBias;              /* Variable: PlntBrkFrntBias
                                        * Referenced by:
                                        *   '<S2>/Front Bias'
                                        *   '<S36>/Constant1'
                                        */
  real_T PlntBrkKinFricCffFrnt;        /* Variable: PlntBrkKinFricCffFrnt
                                        * Referenced by:
                                        *   '<S36>/Constant1'
                                        *   '<S41>/Front Brakes'
                                        */
  real_T PlntBrkKinFricCffRear;        /* Variable: PlntBrkKinFricCffRear
                                        * Referenced by:
                                        *   '<S36>/Constant1'
                                        *   '<S41>/Rear Brakes'
                                        */
  real_T PlntBrkNumPadsFrnt;           /* Variable: PlntBrkNumPadsFrnt
                                        * Referenced by:
                                        *   '<S36>/Constant1'
                                        *   '<S41>/Front Brakes'
                                        */
  real_T PlntBrkNumPadsRear;           /* Variable: PlntBrkNumPadsRear
                                        * Referenced by:
                                        *   '<S36>/Constant1'
                                        *   '<S41>/Rear Brakes'
                                        */
  real_T PlntBrkPadMeanRadiusFrnt;     /* Variable: PlntBrkPadMeanRadiusFrnt
                                        * Referenced by:
                                        *   '<S36>/Constant1'
                                        *   '<S41>/Front Brakes'
                                        */
  real_T PlntBrkPadMeanRadiusRear;     /* Variable: PlntBrkPadMeanRadiusRear
                                        * Referenced by:
                                        *   '<S36>/Constant1'
                                        *   '<S41>/Rear Brakes'
                                        */
  real_T PlntBrkPrsFctr;               /* Variable: PlntBrkPrsFctr
                                        * Referenced by:
                                        *   '<S2>/Gain4'
                                        *   '<S36>/Gain6'
                                        */
  real_T PlntBrkRearBias;              /* Variable: PlntBrkRearBias
                                        * Referenced by:
                                        *   '<S2>/Rear Bias'
                                        *   '<S36>/Constant1'
                                        */
  real_T PlntDiffrntl2Eff;             /* Variable: PlntDiffrntl2Eff
                                        * Referenced by:
                                        *   '<S44>/Constant'
                                        *   '<S40>/Constant'
                                        *   '<S18>/Constant'
                                        *   '<S33>/Constant'
                                        *   '<S83>/Constant'
                                        */
  real_T PlntDiffrntl2Ratio;           /* Variable: PlntDiffrntl2Ratio
                                        * Referenced by:
                                        *   '<S42>/Gain1'
                                        *   '<S39>/Gain3'
                                        *   '<S17>/Gain3'
                                        *   '<S19>/Gain2'
                                        *   '<S32>/Gain3'
                                        *   '<S82>/Gain3'
                                        */
  real_T PlntDiffrntlEff;              /* Variable: PlntDiffrntlEff
                                        * Referenced by:
                                        *   '<S43>/Constant'
                                        *   '<S38>/Constant'
                                        *   '<S16>/Constant'
                                        *   '<S31>/Constant'
                                        *   '<S70>/Constant'
                                        */
  real_T PlntDiffrntlRatio;            /* Variable: PlntDiffrntlRatio
                                        * Referenced by:
                                        *   '<S42>/Gain3'
                                        *   '<S37>/Gain3'
                                        *   '<S15>/Gain3'
                                        *   '<S19>/Gain1'
                                        *   '<S30>/Gain3'
                                        *   '<S69>/Gain3'
                                        */
  real_T PlntEM1EffTbl[154];           /* Variable: PlntEM1EffTbl
                                        * Referenced by: '<S68>/Eff Map'
                                        */
  real_T PlntEM1Spd[14];               /* Variable: PlntEM1Spd
                                        * Referenced by:
                                        *   '<S12>/MaxEMTrqVsSpd'
                                        *   '<S28>/MaxEMTrqVsSpd'
                                        */
  real_T PlntEM1SpdEff[14];            /* Variable: PlntEM1SpdEff
                                        * Referenced by: '<S68>/Eff Map'
                                        */
  real_T PlntEM1TransEff;              /* Variable: PlntEM1TransEff
                                        * Referenced by:
                                        *   '<S43>/Constant'
                                        *   '<S38>/Constant'
                                        *   '<S16>/Constant'
                                        *   '<S31>/Constant'
                                        *   '<S70>/Constant'
                                        */
  real_T PlntEM1TransGearRatio;        /* Variable: PlntEM1TransGearRatio
                                        * Referenced by:
                                        *   '<S42>/Gain3'
                                        *   '<S37>/Gain3'
                                        *   '<S15>/Gain3'
                                        *   '<S19>/Gain1'
                                        *   '<S30>/Gain3'
                                        *   '<S69>/Gain3'
                                        */
  real_T PlntEM1Trq[14];               /* Variable: PlntEM1Trq
                                        * Referenced by:
                                        *   '<S12>/MaxEMTrqVsSpd'
                                        *   '<S28>/MaxEMTrqVsSpd'
                                        */
  real_T PlntEM1TrqEff[11];            /* Variable: PlntEM1TrqEff
                                        * Referenced by: '<S68>/Eff Map'
                                        */
  real_T PlntEM2EffTbl[154];           /* Variable: PlntEM2EffTbl
                                        * Referenced by: '<S81>/Eff Map'
                                        */
  real_T PlntEM2Spd[14];               /* Variable: PlntEM2Spd
                                        * Referenced by:
                                        *   '<S13>/MaxEMTrqVsSpd'
                                        *   '<S29>/MaxEMTrqVsSpd'
                                        */
  real_T PlntEM2SpdEff[14];            /* Variable: PlntEM2SpdEff
                                        * Referenced by: '<S81>/Eff Map'
                                        */
  real_T PlntEM2TransEff;              /* Variable: PlntEM2TransEff
                                        * Referenced by:
                                        *   '<S44>/Constant'
                                        *   '<S40>/Constant'
                                        *   '<S18>/Constant'
                                        *   '<S33>/Constant'
                                        *   '<S83>/Constant'
                                        */
  real_T PlntEM2TransGearRatio;        /* Variable: PlntEM2TransGearRatio
                                        * Referenced by:
                                        *   '<S42>/Gain1'
                                        *   '<S39>/Gain3'
                                        *   '<S17>/Gain3'
                                        *   '<S19>/Gain2'
                                        *   '<S32>/Gain3'
                                        *   '<S82>/Gain3'
                                        */
  real_T PlntEM2Trq[14];               /* Variable: PlntEM2Trq
                                        * Referenced by:
                                        *   '<S13>/MaxEMTrqVsSpd'
                                        *   '<S29>/MaxEMTrqVsSpd'
                                        */
  real_T PlntEM2TrqEff[11];            /* Variable: PlntEM2TrqEff
                                        * Referenced by: '<S81>/Eff Map'
                                        */
  real_T PlntVehCGHgtAxl;              /* Variable: PlntVehCGHgtAxl
                                        * Referenced by:
                                        *   '<S73>/Constant7'
                                        *   '<S74>/Constant13'
                                        *   '<S74>/Constant7'
                                        *   '<S86>/Constant13'
                                        *   '<S87>/Constant13'
                                        *   '<S87>/Constant7'
                                        */
  real_T PlntVehDstCGFrntAxl;          /* Variable: PlntVehDstCGFrntAxl
                                        * Referenced by:
                                        *   '<S73>/Constant5'
                                        *   '<S74>/Constant1'
                                        *   '<S74>/Constant11'
                                        *   '<S74>/Constant5'
                                        *   '<S86>/Constant1'
                                        *   '<S86>/Constant11'
                                        *   '<S87>/Constant1'
                                        *   '<S87>/Constant11'
                                        *   '<S87>/Constant5'
                                        */
  real_T PlntVehDstCGRearAxl;          /* Variable: PlntVehDstCGRearAxl
                                        * Referenced by:
                                        *   '<S73>/Constant2'
                                        *   '<S73>/Constant6'
                                        *   '<S74>/Constant12'
                                        *   '<S74>/Constant2'
                                        *   '<S74>/Constant6'
                                        *   '<S86>/Constant12'
                                        *   '<S87>/Constant12'
                                        *   '<S87>/Constant2'
                                        *   '<S87>/Constant6'
                                        */
  real_T PlntVehMass;                  /* Variable: PlntVehMass
                                        * Referenced by:
                                        *   '<S73>/Constant4'
                                        *   '<S74>/Constant4'
                                        *   '<S74>/Constant8'
                                        *   '<S86>/Constant8'
                                        *   '<S87>/Constant4'
                                        *   '<S87>/Constant8'
                                        */
  real_T PlntWhlLdRadiusFrnt;          /* Variable: PlntWhlLdRadiusFrnt
                                        * Referenced by:
                                        *   '<S23>/Veh2WhlSpd'
                                        *   '<S24>/Veh2WhlSpd'
                                        *   '<S19>/Gain3'
                                        *   '<S73>/Constant9'
                                        *   '<S73>/TireRadius'
                                        *   '<S74>/Constant9'
                                        *   '<S74>/TireRadius'
                                        *   '<S87>/Constant9'
                                        *   '<S87>/TireRadius'
                                        */
  real_T PlntWhlLdRadiusRear;          /* Variable: PlntWhlLdRadiusRear
                                        * Referenced by:
                                        *   '<S23>/Veh2WhlSpd'
                                        *   '<S24>/Veh2WhlSpd'
                                        *   '<S19>/Gain4'
                                        *   '<S74>/Constant14'
                                        *   '<S74>/TireRadius1'
                                        *   '<S86>/Constant14'
                                        *   '<S86>/TireRadius1'
                                        *   '<S87>/Constant14'
                                        *   '<S87>/TireRadius1'
                                        */
  uint32_T CtrlVcuBattPnlty;           /* Variable: CtrlVcuBattPnlty
                                        * Referenced by: '<S24>/Constraint Penalty Factor'
                                        */
  uint8_T CtrlVcuEMPnlty;              /* Variable: CtrlVcuEMPnlty
                                        * Referenced by:
                                        *   '<S24>/Constraint Penalty Factor1'
                                        *   '<S24>/Constraint Penalty Factor2'
                                        */
  real_T div0protectpoly1_thresh;     /* Mask Parameter: div0protectpoly1_thresh
                                       * Referenced by:
                                       *   '<S60>/Constant'
                                       *   '<S61>/Constant'
                                       */
  real_T div0protectpoly_thresh;       /* Mask Parameter: div0protectpoly_thresh
                                        * Referenced by:
                                        *   '<S58>/Constant'
                                        *   '<S59>/Constant'
                                        */
  real_T Constant1_Value;              /* Expression: 1
                                        * Referenced by: '<S31>/Constant1'
                                        */
  real_T Constant2_Value;              /* Expression: -1
                                        * Referenced by: '<S31>/Constant2'
                                        */
  real_T Constant1_Value_g;            /* Expression: 1
                                        * Referenced by: '<S33>/Constant1'
                                        */
  real_T Constant2_Value_j;            /* Expression: -1
                                        * Referenced by: '<S33>/Constant2'
                                        */
  real_T Gain_Gain;                    /* Expression: -1
                                        * Referenced by: '<S39>/Gain'
                                        */
  real_T Gain_Gain_d;                  /* Expression: -1
                                        * Referenced by: '<S37>/Gain'
                                        */
  real_T Constant1_Value_k;            /* Expression: 1
                                        * Referenced by: '<S16>/Constant1'
                                        */
  real_T Constant1_Value_kl;           /* Expression: 1
                                        * Referenced by: '<S18>/Constant1'
                                        */
  real_T Constant2_Value_jm;           /* Expression: -1
                                        * Referenced by: '<S16>/Constant2'
                                        */
  real_T Constant2_Value_b;            /* Expression: -1
                                        * Referenced by: '<S18>/Constant2'
                                        */
  real_T Switch2_Threshold;            /* Expression: 0
                                        * Referenced by: '<S18>/Switch2'
                                        */
  real_T Switch2_Threshold_l;          /* Expression: 0
                                        * Referenced by: '<S16>/Switch2'
                                        */
  real_T convert2percent_Gain;         /* Expression: 100
                                        * Referenced by: '<S5>/convert2percent'
                                        */
  real_T Gain1_Gain;                   /* Expression: -1
                                        * Referenced by: '<S36>/Gain1'
                                        */
  real_T Constant1_Value_h;            /* Expression: 1
                                        * Referenced by: '<S43>/Constant1'
                                        */
  real_T Constant2_Value_o;            /* Expression: -1
                                        * Referenced by: '<S43>/Constant2'
                                        */
  real_T Constant1_Value_j;            /* Expression: 1
                                        * Referenced by: '<S44>/Constant1'
                                        */
  real_T Constant2_Value_h;            /* Expression: -1
                                        * Referenced by: '<S44>/Constant2'
                                        */
  real_T Switch1_Threshold;            /* Expression: 0
                                        * Referenced by: '<S56>/Switch1'
                                        */
  real_T Switch1_Threshold_p;          /* Expression: 0
                                        * Referenced by: '<S57>/Switch1'
                                        */
  real_T Gain_Gain_o;                  /* Expression: -1
                                        * Referenced by: '<S72>/Gain'
                                        */
  real_T Gain_Gain_l;                  /* Expression: -1
                                        * Referenced by: '<S85>/Gain'
                                        */
  real_T Constant1_Value_h5;           /* Expression: 0
                                        * Referenced by: '<S88>/Constant1'
                                        */
  real_T Constant_Value;               /* Expression: 0
                                        * Referenced by: '<S65>/Constant'
                                        */
  real_T Constant_Value_c;             /* Expression: 0
                                        * Referenced by: '<S66>/Constant'
                                        */
  real_T Constant_Value_h;             /* Expression: 0
                                        * Referenced by: '<S78>/Constant'
                                        */
  real_T Constant_Value_l;             /* Expression: 0
                                        * Referenced by: '<S79>/Constant'
                                        */
  real_T Switch2_Threshold_g;          /* Expression: 0
                                        * Referenced by: '<S31>/Switch2'
                                        */
  real_T Switch2_Threshold_h;          /* Expression: 0
                                        * Referenced by: '<S33>/Switch2'
                                        */
  real_T AccelDecelSwitch_Threshold;   /* Expression: 0
                                        * Referenced by: '<S21>/Accel Decel Switch'
                                        */
  real_T Constant1_Value_ky;           /* Expression: 1
                                        * Referenced by: '<S40>/Constant1'
                                        */
  real_T EMTrqControlVectorTraction_Valu[200];
              /* Expression: linspace(0, max(PlntEM2Trq), CtrlVcuEMTrqSplitGrid)
               * Referenced by: '<S39>/EMTrq Control Vector Traction'
               */
  real_T Constant2_Value_bd;           /* Expression: -1
                                        * Referenced by: '<S40>/Constant2'
                                        */
  real_T Switch2_Threshold_k;          /* Expression: 0
                                        * Referenced by: '<S40>/Switch2'
                                        */
  real_T AccelDecelSwitch1_Threshold;  /* Expression: 0
                                        * Referenced by: '<S21>/Accel Decel Switch1'
                                        */
  real_T Constant1_Value_n;            /* Expression: 1
                                        * Referenced by: '<S38>/Constant1'
                                        */
  real_T EMTrqControlVectorTraction_Va_j[200];
              /* Expression: linspace(0, max(PlntEM1Trq), CtrlVcuEMTrqSplitGrid)
               * Referenced by: '<S37>/EMTrq Control Vector Traction'
               */
  real_T Constant2_Value_jmm;          /* Expression: -1
                                        * Referenced by: '<S38>/Constant2'
                                        */
  real_T Switch2_Threshold_j;          /* Expression: 0
                                        * Referenced by: '<S38>/Switch2'
                                        */
  real_T AccelDecelSwitch2_Threshold;  /* Expression: 0
                                        * Referenced by: '<S21>/Accel Decel Switch2'
                                        */
  real_T Constant_Value_i;             /* Expression: 1
                                        * Referenced by: '<S57>/Constant'
                                        */
  real_T Constant1_Value_o;            /* Expression: 1
                                        * Referenced by: '<S70>/Constant1'
                                        */
  real_T UnitDelay_InitialCondition;   /* Expression: 0
                                        * Referenced by: '<S69>/Unit Delay'
                                        */
  real_T Constant2_Value_d;            /* Expression: -1
                                        * Referenced by: '<S70>/Constant2'
                                        */
  real_T Switch2_Threshold_m;          /* Expression: 0
                                        * Referenced by: '<S70>/Switch2'
                                        */
  real_T Constant_Value_p;             /* Expression: 0
                                        * Referenced by: '<S64>/Constant'
                                        */
  real_T Switch_Threshold;             /* Expression: 0
                                        * Referenced by: '<S64>/Switch'
                                        */
  real_T UnitDelay_InitialCondition_o; /* Expression: 0
                                        * Referenced by: '<S24>/Unit Delay'
                                        */
  real_T UnitDelay1_InitialCondition;  /* Expression: 0
                                        * Referenced by: '<S24>/Unit Delay1'
                                        */
  real_T Switch1_Threshold_h;          /* Expression: 0
                                        * Referenced by: '<S64>/Switch1'
                                        */
  real_T Gain_Gain_h;                  /* Expression: -1
                                        * Referenced by: '<S62>/Gain'
                                        */
  real_T Gain2_Gain;                   /* Expression: 1/100
                                        * Referenced by: '<S68>/Gain2'
                                        */
  real_T Constant1_Value_n0;           /* Expression: -1
                                        * Referenced by: '<S68>/Constant1'
                                        */
  real_T Constant2_Value_i;            /* Expression: 1
                                        * Referenced by: '<S68>/Constant2'
                                        */
  real_T Switch2_Threshold_p;          /* Expression: 0
                                        * Referenced by: '<S68>/Switch2'
                                        */
  real_T Constant1_Value_gm;           /* Expression: 1
                                        * Referenced by: '<S83>/Constant1'
                                        */
  real_T UnitDelay_InitialCondition_a; /* Expression: 0
                                        * Referenced by: '<S82>/Unit Delay'
                                        */
  real_T Constant2_Value_iu;           /* Expression: -1
                                        * Referenced by: '<S83>/Constant2'
                                        */
  real_T Switch2_Threshold_c;          /* Expression: 0
                                        * Referenced by: '<S83>/Switch2'
                                        */
  real_T Constant_Value_a;             /* Expression: 0
                                        * Referenced by: '<S77>/Constant'
                                        */
  real_T Switch_Threshold_c;           /* Expression: 0
                                        * Referenced by: '<S77>/Switch'
                                        */
  real_T Switch1_Threshold_m;          /* Expression: 0
                                        * Referenced by: '<S77>/Switch1'
                                        */
  real_T Gain_Gain_dl;                 /* Expression: -1
                                        * Referenced by: '<S75>/Gain'
                                        */
  real_T Gain2_Gain_j;                 /* Expression: 1/100
                                        * Referenced by: '<S81>/Gain2'
                                        */
  real_T Constant1_Value_m;            /* Expression: -1
                                        * Referenced by: '<S81>/Constant1'
                                        */
  real_T Constant2_Value_m;            /* Expression: 1
                                        * Referenced by: '<S81>/Constant2'
                                        */
  real_T Switch2_Threshold_i;          /* Expression: 0
                                        * Referenced by: '<S81>/Switch2'
                                        */
  real_T Saturation_UpperSat;          /* Expression: Inf
                                        * Referenced by: '<S51>/Saturation'
                                        */
  real_T Saturation_LowerSat;          /* Expression: 0.0001
                                        * Referenced by: '<S51>/Saturation'
                                        */
  real_T Constant_Value_ag;            /* Expression: 1
                                        * Referenced by: '<S56>/Constant'
                                        */
  real_T W2kW_Gain;                    /* Expression: 1/1000
                                        * Referenced by: '<S23>/W2kW '
                                        */
  real_T Saturation1_UpperSat;         /* Expression: inf
                                        * Referenced by: '<S24>/Saturation1'
                                        */
  real_T Saturation1_LowerSat;         /* Expression: 0.001
                                        * Referenced by: '<S24>/Saturation1'
                                        */
  real_T W2kW1_Gain;                   /* Expression: 1/1000
                                        * Referenced by: '<S23>/W2kW 1'
                                        */
  real_T Switch_Threshold_k;           /* Expression: 0
                                        * Referenced by: '<S23>/Switch'
                                        */
  real_T DeadZone_Start;               /* Expression: -0.1
                                        * Referenced by: '<S23>/Dead Zone'
                                        */
  real_T DeadZone_End;                 /* Expression: 0.1
                                        * Referenced by: '<S23>/Dead Zone'
                                        */
  real_T UnitDelay1_InitialCondition_m;/* Expression: 0
                                        * Referenced by: '<S23>/Unit Delay1'
                                        */
  real_T UnitDelay2_InitialCondition;  /* Expression: 0
                                        * Referenced by: '<S23>/Unit Delay2'
                                        */
  real_T Switch1_Threshold_o;          /* Expression: 0
                                        * Referenced by: '<S23>/Switch1'
                                        */
  real_T W2kW_Gain_a;                  /* Expression: 1/1000
                                        * Referenced by: '<S46>/W2kW'
                                        */
  real_T Negative1_UpperSat;           /* Expression: 0
                                        * Referenced by: '<S36>/Negative 1'
                                        */
  real_T Negative1_LowerSat;           /* Expression: -inf
                                        * Referenced by: '<S36>/Negative 1'
                                        */
  real_T Negative5_UpperSat;           /* Expression: inf
                                        * Referenced by: '<S36>/Negative 5'
                                        */
  real_T Negative5_LowerSat;           /* Expression: 0
                                        * Referenced by: '<S36>/Negative 5'
                                        */
  real_T Saturation_UpperSat_n;        /* Expression: 1
                                        * Referenced by: '<S36>/Saturation'
                                        */
  real_T Saturation_LowerSat_j;        /* Expression: 0
                                        * Referenced by: '<S36>/Saturation'
                                        */
  real_T UnitDelay_InitialCondition_p; /* Expression: 0
                                        * Referenced by: '<S42>/Unit Delay'
                                        */
  real_T Switch2_Threshold_py;         /* Expression: 0
                                        * Referenced by: '<S43>/Switch2'
                                        */
  real_T UnitDelay1_InitialCondition_a;/* Expression: 0
                                        * Referenced by: '<S42>/Unit Delay1'
                                        */
  real_T Switch2_Threshold_o;          /* Expression: 0
                                        * Referenced by: '<S44>/Switch2'
                                        */
  real_T Constant1_Value_gn;           /* Expression: 0
                                        * Referenced by: '<Root>/Constant1'
                                        */
  real_T Gain1_Gain_i;                 /* Expression: -1
                                        * Referenced by: '<S4>/Gain1'
                                        */
  real_T Gain_Gain_e;                  /* Expression: -1
                                        * Referenced by: '<S4>/Gain'
                                        */
  real_T RateLimiter_IC;               /* Expression: 0
                                        * Referenced by: '<Root>/Rate Limiter'
                                        */
  real_T Constant2_Value_f;            /* Expression: 0
                                        * Referenced by: '<Root>/Constant2'
                                        */
  real_T Constant3_Value;              /* Expression: 0
                                        * Referenced by: '<Root>/Constant3'
                                        */
  real_T Constant4_Value;              /* Expression: 0
                                        * Referenced by: '<Root>/Constant4'
                                        */
  real_T Constant5_Value;              /* Expression: 0
                                        * Referenced by: '<Root>/Constant5'
                                        */
  uint32_T EffMap_maxIndex[2];         /* Computed Parameter: EffMap_maxIndex
                                        * Referenced by: '<S68>/Eff Map'
                                        */
  uint32_T EffMap_maxIndex_l[2];       /* Computed Parameter: EffMap_maxIndex_l
                                        * Referenced by: '<S81>/Eff Map'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_EvPowertrainControlle_T {
  const char_T *errorStatus;
  RTWLogInfo *rtwLogInfo;

  /*
   * Timing:
   * The following substructure contains information regarding
   * the timing information for the model.
   */
  struct {
    time_T taskTime0;
    uint32_T clockTick0;
    uint32_T clockTickH0;
    time_T stepSize0;
    time_T tFinal;
    boolean_T stopRequestedFlag;
  } Timing;
};

/* Block parameters (default storage) */
extern P_EvPowertrainController2EM_T EvPowertrainController2EM_P;

/* Block signals (default storage) */
extern B_EvPowertrainController2EM_T EvPowertrainController2EM_B;

/* Block states (default storage) */
extern DW_EvPowertrainController2EM_T EvPowertrainController2EM_DW;

/* External inputs (root inport signals with default storage) */
extern ExtU_EvPowertrainController2E_T EvPowertrainController2EM_U;

/* External outputs (root outports fed by signals with default storage) */
extern ExtY_EvPowertrainController2E_T EvPowertrainController2EM_Y;

/* Model entry point functions */
extern void EvPowertrainController2EM_initialize(void);
extern void EvPowertrainController2EM_step(void);
extern void EvPowertrainController2EM_terminate(void);

/* Real-time Model object */
extern RT_MODEL_EvPowertrainControll_T *const EvPowertrainController2EM_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'EvPowertrainController2EM'
 * '<S1>'   : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request'
 * '<S2>'   : 'EvPowertrainController2EM/Brake Pedal to Total Braking Pressure Request'
 * '<S3>'   : 'EvPowertrainController2EM/Energy Management'
 * '<S4>'   : 'EvPowertrainController2EM/Power Limit Calculations'
 * '<S5>'   : 'EvPowertrainController2EM/SOC Calculation'
 * '<S6>'   : 'EvPowertrainController2EM/Torque Vectoring'
 * '<S7>'   : 'EvPowertrainController2EM/Trailer Brake Pressure Command'
 * '<S8>'   : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq'
 * '<S9>'   : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM'
 * '<S10>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/EMTrq2WhlTrqFrnt'
 * '<S11>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/EMTrq2WhlTrqRear'
 * '<S12>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/Maximum Torque Front Axle'
 * '<S13>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/Maximum Torque Rear Axle'
 * '<S14>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/VehSpd2EMSpd'
 * '<S15>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/EMTrq2WhlTrqFrnt/Single Speed Transmission'
 * '<S16>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/EMTrq2WhlTrqFrnt/Single Speed Transmission/Diff Eta'
 * '<S17>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/EMTrq2WhlTrqRear/Single Speed Transmission'
 * '<S18>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/EMTrq2WhlTrqRear/Single Speed Transmission/Diff Eta'
 * '<S19>'  : 'EvPowertrainController2EM/Accel Pedal to Traction Wheel Torque Request/EM2WhlTrq/2EM/VehSpd2EMSpd/Single Speed Transmission'
 * '<S20>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles'
 * '<S21>'  : 'EvPowertrainController2EM/Energy Management/Control Domain '
 * '<S22>'  : 'EvPowertrainController2EM/Energy Management/Convert Whl to EMTrq Vector'
 * '<S23>'  : 'EvPowertrainController2EM/Energy Management/Hamiltonian computation  and minimization'
 * '<S24>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints '
 * '<S25>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM'
 * '<S26>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM/EMTrq2WhlTrqFrnt'
 * '<S27>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM/EMTrq2WhlTrqRear'
 * '<S28>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM/Maximum Torque Front Axle'
 * '<S29>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM/Maximum Torque Rear Axle'
 * '<S30>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM/EMTrq2WhlTrqFrnt/Single Speed Transmission'
 * '<S31>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM/EMTrq2WhlTrqFrnt/Single Speed Transmission/Diff Eta'
 * '<S32>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM/EMTrq2WhlTrqRear/Single Speed Transmission'
 * '<S33>'  : 'EvPowertrainController2EM/Energy Management/Calculate Average EMSpd and Wheel Torque Curves for Front and Rear Axles/2EM/EMTrq2WhlTrqRear/Single Speed Transmission/Diff Eta'
 * '<S34>'  : 'EvPowertrainController2EM/Energy Management/Control Domain /Front Axle EM Torque Vector'
 * '<S35>'  : 'EvPowertrainController2EM/Energy Management/Control Domain /Rear Axle EM Torque Vector'
 * '<S36>'  : 'EvPowertrainController2EM/Energy Management/Control Domain /Series Regen Braking'
 * '<S37>'  : 'EvPowertrainController2EM/Energy Management/Control Domain /Front Axle EM Torque Vector/2EM or 3EM Dual Rear'
 * '<S38>'  : 'EvPowertrainController2EM/Energy Management/Control Domain /Front Axle EM Torque Vector/2EM or 3EM Dual Rear/Diff Eta'
 * '<S39>'  : 'EvPowertrainController2EM/Energy Management/Control Domain /Rear Axle EM Torque Vector/2EM'
 * '<S40>'  : 'EvPowertrainController2EM/Energy Management/Control Domain /Rear Axle EM Torque Vector/2EM/Diff Eta'
 * '<S41>'  : 'EvPowertrainController2EM/Energy Management/Control Domain /Series Regen Braking/BrkTrqEstimate'
 * '<S42>'  : 'EvPowertrainController2EM/Energy Management/Convert Whl to EMTrq Vector/2EM'
 * '<S43>'  : 'EvPowertrainController2EM/Energy Management/Convert Whl to EMTrq Vector/2EM/Diff Eta'
 * '<S44>'  : 'EvPowertrainController2EM/Energy Management/Convert Whl to EMTrq Vector/2EM/Diff Eta1'
 * '<S45>'  : 'EvPowertrainController2EM/Energy Management/Hamiltonian computation  and minimization/MATLAB Function'
 * '<S46>'  : 'EvPowertrainController2EM/Energy Management/Hamiltonian computation  and minimization/Pwr Rate Limit'
 * '<S47>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint'
 * '<S48>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front'
 * '<S49>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear'
 * '<S50>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Wheel Torque Vector Logic'
 * '<S51>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Electrical Current'
 * '<S52>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Power Limit Calculations'
 * '<S53>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Saturation Dynamic'
 * '<S54>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Electrical Current/DC-DC Eta'
 * '<S55>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Electrical Current/DC-DC Eta/No DC-DC'
 * '<S56>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Power Limit Calculations/div0protect - poly'
 * '<S57>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Power Limit Calculations/div0protect - poly1'
 * '<S58>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Power Limit Calculations/div0protect - poly/Compare To Constant'
 * '<S59>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Power Limit Calculations/div0protect - poly/Compare To Constant1'
 * '<S60>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Power Limit Calculations/div0protect - poly1/Compare To Constant'
 * '<S61>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Battery Constraint/Power Limit Calculations/div0protect - poly1/Compare To Constant1'
 * '<S62>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Maximum Torque'
 * '<S63>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Tabular Power Loss Data'
 * '<S64>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Wheel Torque Saturation for Max g Rates'
 * '<S65>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Maximum Torque/Compare To Zero'
 * '<S66>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Maximum Torque/Compare To Zero1'
 * '<S67>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Maximum Torque/Saturation Dynamic'
 * '<S68>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Tabular Power Loss Data/2EM or 3EM Dual Rear'
 * '<S69>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Tabular Power Loss Data/2EM or 3EM Dual Rear/WhlTrq2EMTrq'
 * '<S70>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Tabular Power Loss Data/2EM or 3EM Dual Rear/WhlTrq2EMTrq/Diff Eta'
 * '<S71>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Wheel Torque Saturation for Max g Rates/Saturation Dynamic3'
 * '<S72>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Wheel Torque Saturation for Max g Rates/Wheel Torque Limit at Max g Rates'
 * '<S73>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Wheel Torque Saturation for Max g Rates/Wheel Torque Limit at Max g Rates/Wheel Torque at Max Acceleration Rate'
 * '<S74>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Front/Wheel Torque Saturation for Max g Rates/Wheel Torque Limit at Max g Rates/Wheel Torque at Max Deceleration Rate'
 * '<S75>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Maximum Torque'
 * '<S76>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Tabular Power Loss Data'
 * '<S77>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Wheel Torque Saturation for Max g Rates'
 * '<S78>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Maximum Torque/Compare To Zero'
 * '<S79>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Maximum Torque/Compare To Zero1'
 * '<S80>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Maximum Torque/Saturation Dynamic'
 * '<S81>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Tabular Power Loss Data/2EM'
 * '<S82>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Tabular Power Loss Data/2EM/WhlTrq2EMTrq'
 * '<S83>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Tabular Power Loss Data/2EM/WhlTrq2EMTrq/Diff Eta'
 * '<S84>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Wheel Torque Saturation for Max g Rates/Saturation Dynamic3'
 * '<S85>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Wheel Torque Saturation for Max g Rates/Wheel Torque Limit at Max g Rates'
 * '<S86>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Wheel Torque Saturation for Max g Rates/Wheel Torque Limit at Max g Rates/Wheel Torque at Max Acceleration Rate'
 * '<S87>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /EM Constraint Rear/Wheel Torque Saturation for Max g Rates/Wheel Torque Limit at Max g Rates/Wheel Torque at Max Deceleration Rate'
 * '<S88>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Wheel Torque Vector Logic/Regen'
 * '<S89>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Wheel Torque Vector Logic/Traction'
 * '<S90>'  : 'EvPowertrainController2EM/Energy Management/Powertrain Constraints /Wheel Torque Vector Logic/Regen/Saturation Dynamic'
 * '<S91>'  : 'EvPowertrainController2EM/Torque Vectoring/No Torque Vectoring'
 */
#endif                                 /* EvPowertrainController2EM_h_ */
