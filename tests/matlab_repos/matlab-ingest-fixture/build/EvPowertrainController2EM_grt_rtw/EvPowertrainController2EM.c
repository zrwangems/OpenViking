/*
 * EvPowertrainController2EM.c
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

#include "EvPowertrainController2EM.h"
#include "rtwtypes.h"
#include <math.h>
#include "EvPowertrainController2EM_private.h"
#include <string.h>
#include "rt_nonfinite.h"
#define EvPowertrainController2E_period (0.01)

/* Block signals (default storage) */
B_EvPowertrainController2EM_T EvPowertrainController2EM_B;

/* Block states (default storage) */
DW_EvPowertrainController2EM_T EvPowertrainController2EM_DW;

/* External inputs (root inport signals with default storage) */
ExtU_EvPowertrainController2E_T EvPowertrainController2EM_U;

/* External outputs (root outports fed by signals with default storage) */
ExtY_EvPowertrainController2E_T EvPowertrainController2EM_Y;

/* Real-time model */
static RT_MODEL_EvPowertrainControll_T EvPowertrainController2EM_M_;
RT_MODEL_EvPowertrainControll_T *const EvPowertrainController2EM_M =
  &EvPowertrainController2EM_M_;

/* Forward declaration for local functions */
static void EvPowertrainController2_minimum(const real_T x[201], real_T *ex,
  int32_T *idx);
real_T look1_binlcapw(real_T u0, const real_T bp0[], const real_T table[],
                      uint32_T maxIndex)
{
  real_T frac;
  real_T y;
  uint32_T iLeft;

  /* Column-major Lookup 1-D
     Search method: 'binary'
     Use previous index: 'off'
     Interpolation method: 'Linear point-slope'
     Extrapolation method: 'Clip'
     Use last breakpoint for index at or above upper limit: 'on'
     Remove protection against out-of-range input in generated code: 'off'
   */
  /* Prelookup - Index and Fraction
     Index Search method: 'binary'
     Extrapolation method: 'Clip'
     Use previous index: 'off'
     Use last breakpoint for index at or above upper limit: 'on'
     Remove protection against out-of-range input in generated code: 'off'
   */
  if (u0 <= bp0[0U]) {
    iLeft = 0U;
    frac = 0.0;
  } else if (u0 < bp0[maxIndex]) {
    uint32_T bpIdx;
    uint32_T iRght;

    /* Binary Search */
    bpIdx = maxIndex >> 1U;
    iLeft = 0U;
    iRght = maxIndex;
    while (iRght - iLeft > 1U) {
      if (u0 < bp0[bpIdx]) {
        iRght = bpIdx;
      } else {
        iLeft = bpIdx;
      }

      bpIdx = (iRght + iLeft) >> 1U;
    }

    frac = (u0 - bp0[iLeft]) / (bp0[iLeft + 1U] - bp0[iLeft]);
  } else {
    iLeft = maxIndex;
    frac = 0.0;
  }

  /* Column-major Interpolation 1-D
     Interpolation method: 'Linear point-slope'
     Use last breakpoint for index at or above upper limit: 'on'
     Overflow mode: 'portable wrapping'
   */
  if (iLeft == maxIndex) {
    y = table[iLeft];
  } else {
    real_T yL_0d0;
    yL_0d0 = table[iLeft];
    y = (table[iLeft + 1U] - yL_0d0) * frac + yL_0d0;
  }

  return y;
}

real_T look1_pbinlcapw(real_T u0, const real_T bp0[], const real_T table[],
  uint32_T prevIndex[], uint32_T maxIndex)
{
  real_T frac;
  real_T y;
  uint32_T bpIdx;

  /* Column-major Lookup 1-D
     Search method: 'binary'
     Use previous index: 'on'
     Interpolation method: 'Linear point-slope'
     Extrapolation method: 'Clip'
     Use last breakpoint for index at or above upper limit: 'on'
     Remove protection against out-of-range input in generated code: 'off'
   */
  /* Prelookup - Index and Fraction
     Index Search method: 'binary'
     Extrapolation method: 'Clip'
     Use previous index: 'on'
     Use last breakpoint for index at or above upper limit: 'on'
     Remove protection against out-of-range input in generated code: 'off'
   */
  if (u0 <= bp0[0U]) {
    bpIdx = 0U;
    frac = 0.0;
  } else if (u0 < bp0[maxIndex]) {
    uint32_T found;
    uint32_T iLeft;
    uint32_T iRght;

    /* Binary Search using Previous Index */
    bpIdx = prevIndex[0U];
    iLeft = 0U;
    iRght = maxIndex;
    found = 0U;
    while (found == 0U) {
      if (u0 < bp0[bpIdx]) {
        iRght = bpIdx - 1U;
        bpIdx = ((bpIdx + iLeft) - 1U) >> 1U;
      } else if (u0 < bp0[bpIdx + 1U]) {
        found = 1U;
      } else {
        iLeft = bpIdx + 1U;
        bpIdx = ((bpIdx + iRght) + 1U) >> 1U;
      }
    }

    frac = (u0 - bp0[bpIdx]) / (bp0[bpIdx + 1U] - bp0[bpIdx]);
  } else {
    bpIdx = maxIndex;
    frac = 0.0;
  }

  prevIndex[0U] = bpIdx;

  /* Column-major Interpolation 1-D
     Interpolation method: 'Linear point-slope'
     Use last breakpoint for index at or above upper limit: 'on'
     Overflow mode: 'portable wrapping'
   */
  if (bpIdx == maxIndex) {
    y = table[bpIdx];
  } else {
    real_T yL_0d0;
    yL_0d0 = table[bpIdx];
    y = (table[bpIdx + 1U] - yL_0d0) * frac + yL_0d0;
  }

  return y;
}

uint32_T plook_bincpa(real_T u, const real_T bp[], uint32_T maxIndex, real_T
                      *fraction, uint32_T *prevIndex)
{
  uint32_T bpIndex;

  /* Prelookup - Index and Fraction
     Index Search method: 'binary'
     Extrapolation method: 'Clip'
     Use previous index: 'on'
     Use last breakpoint for index at or above upper limit: 'on'
     Remove protection against out-of-range input in generated code: 'off'
   */
  if (u <= bp[0U]) {
    bpIndex = 0U;
    *fraction = 0.0;
  } else if (u < bp[maxIndex]) {
    bpIndex = binsearch_u32d_prevIdx(u, bp, *prevIndex, maxIndex);
    *fraction = (u - bp[bpIndex]) / (bp[bpIndex + 1U] - bp[bpIndex]);
  } else {
    bpIndex = maxIndex;
    *fraction = 0.0;
  }

  *prevIndex = bpIndex;
  return bpIndex;
}

real_T intrp2d_la_pw(const uint32_T bpIndex[], const real_T frac[], const real_T
                     table[], const uint32_T stride, const uint32_T maxIndex[])
{
  real_T y;
  real_T yL_0d0;
  uint32_T offset_1d;

  /* Column-major Interpolation 2-D
     Interpolation method: 'Linear point-slope'
     Use last breakpoint for index at or above upper limit: 'on'
     Overflow mode: 'portable wrapping'
   */
  offset_1d = bpIndex[1U] * stride + bpIndex[0U];
  if (bpIndex[0U] == maxIndex[0U]) {
    y = table[offset_1d];
  } else {
    yL_0d0 = table[offset_1d];
    y = (table[offset_1d + 1U] - yL_0d0) * frac[0U] + yL_0d0;
  }

  if (bpIndex[1U] == maxIndex[1U]) {
  } else {
    offset_1d += stride;
    if (bpIndex[0U] == maxIndex[0U]) {
      yL_0d0 = table[offset_1d];
    } else {
      yL_0d0 = table[offset_1d];
      yL_0d0 += (table[offset_1d + 1U] - yL_0d0) * frac[0U];
    }

    y += (yL_0d0 - y) * frac[1U];
  }

  return y;
}

uint32_T binsearch_u32d_prevIdx(real_T u, const real_T bp[], uint32_T startIndex,
  uint32_T maxIndex)
{
  uint32_T bpIndex;
  uint32_T found;
  uint32_T iLeft;
  uint32_T iRght;

  /* Binary Search using Previous Index */
  bpIndex = startIndex;
  iLeft = 0U;
  iRght = maxIndex;
  found = 0U;
  while (found == 0U) {
    if (u < bp[bpIndex]) {
      iRght = bpIndex - 1U;
      bpIndex = ((bpIndex + iLeft) - 1U) >> 1U;
    } else if (u < bp[bpIndex + 1U]) {
      found = 1U;
    } else {
      iLeft = bpIndex + 1U;
      bpIndex = ((bpIndex + iRght) + 1U) >> 1U;
    }
  }

  return bpIndex;
}

real_T rt_powd_snf(real_T u0, real_T u1)
{
  real_T y;
  if (rtIsNaN(u0) || rtIsNaN(u1)) {
    y = (rtNaN);
  } else {
    real_T tmp;
    real_T tmp_0;
    tmp = fabs(u0);
    tmp_0 = fabs(u1);
    if (rtIsInf(u1)) {
      if (tmp == 1.0) {
        y = 1.0;
      } else if (tmp > 1.0) {
        if (u1 > 0.0) {
          y = (rtInf);
        } else {
          y = 0.0;
        }
      } else if (u1 > 0.0) {
        y = 0.0;
      } else {
        y = (rtInf);
      }
    } else if (tmp_0 == 0.0) {
      y = 1.0;
    } else if (tmp_0 == 1.0) {
      if (u1 > 0.0) {
        y = u0;
      } else {
        y = 1.0 / u0;
      }
    } else if (u1 == 2.0) {
      y = u0 * u0;
    } else if ((u1 == 0.5) && (u0 >= 0.0)) {
      y = sqrt(u0);
    } else if ((u0 < 0.0) && (u1 > floor(u1))) {
      y = (rtNaN);
    } else {
      y = pow(u0, u1);
    }
  }

  return y;
}

/* Function for MATLAB Function: '<S23>/MATLAB Function' */
static void EvPowertrainController2_minimum(const real_T x[201], real_T *ex,
  int32_T *idx)
{
  int32_T b_idx;
  int32_T k;
  if (!rtIsNaN(x[0])) {
    b_idx = 1;
  } else {
    boolean_T exitg1;
    b_idx = 0;
    k = 2;
    exitg1 = false;
    while ((!exitg1) && (k < 202)) {
      if (!rtIsNaN(x[k - 1])) {
        b_idx = k;
        exitg1 = true;
      } else {
        k++;
      }
    }
  }

  if (b_idx == 0) {
    *ex = x[0];
    *idx = 1;
  } else {
    *ex = x[b_idx - 1];
    *idx = b_idx;
    for (k = b_idx + 1; k < 202; k++) {
      real_T x_0;
      x_0 = x[k - 1];
      if (*ex > x_0) {
        *ex = x_0;
        *idx = k;
      }
    }
  }
}

/* Model step function */
void EvPowertrainController2EM_step(void)
{
  real_T rtb_Divide[201];
  real_T rtb_Divide2_ir[201];
  real_T rtb_Divide2_p[201];
  real_T rtb_Product4[201];
  real_T rtb_Sqrt1[201];
  real_T rtb_Switch2[201];
  real_T rtb_Switch2_l[201];
  real_T rtb_VectorConcatenate1[201];
  real_T rtb_VectorConcatenate_i[201];
  real_T fractions[2];
  real_T rtb_VectorConcatenate1_l[2];
  real_T EMSpd;
  real_T rtb_BrkTrqReqTotal;
  real_T rtb_BrkTrqReqTotal_tmp;
  real_T rtb_Gain1_n;
  real_T rtb_Product;
  real_T rtb_Product1;
  real_T rtb_RateLimiter_idx_0;
  real_T rtb_RateLimiter_idx_0_tmp;
  real_T rtb_RateLimiter_idx_1;
  real_T rtb_RateLimiter_idx_1_tmp;
  real_T rtb_RegenFactor;
  real_T rtb_UnitDelay2;
  real_T rtb_VectorConcatenate_j;
  real_T rtb_WhlEMTrqMax_tmp;
  real_T rtb_WhlEMTrqMax_tmp_0;
  real_T rtb_whlpureelectrictraction;
  int32_T i;
  int32_T tmp;
  int32_T tmp_0;
  uint32_T bpIndices[2];
  uint32_T bpIndices_0[2];
  uint32_T tmp_1;
  boolean_T rtb_LogicalOperator_c[201];
  boolean_T rtb_LogicalOperator_f[201];
  boolean_T rtb_LogicalOperator_he[201];
  boolean_T rtb_Switch2_g_tmp[201];
  boolean_T exitg1;
  boolean_T rtb_Compare_n;
  boolean_T rtb_LogicalOperator_l;
  boolean_T rtb_Switch2_g_tmp_0;

  /* Outport: '<Root>/EngTrqCmd' incorporates:
   *  Constant: '<Root>/Constant1'
   */
  EvPowertrainController2EM_Y.EngTrqCmd =
    EvPowertrainController2EM_P.Constant1_Value_gn;

  /* Product: '<S4>/Product' incorporates:
   *  Gain: '<S4>/Gain1'
   *  Inport: '<Root>/BMSDischrgCurrLmt'
   *  Inport: '<Root>/BattPackVolt'
   */
  rtb_Product = EvPowertrainController2EM_P.Gain1_Gain_i *
    EvPowertrainController2EM_U.BMSDischrgCurrLmt *
    EvPowertrainController2EM_U.BattPackVolt;

  /* Product: '<S4>/Product1' incorporates:
   *  Gain: '<S4>/Gain'
   *  Inport: '<Root>/BMSChrgCurrLmt'
   *  Inport: '<Root>/BattPackVolt'
   */
  rtb_Product1 = EvPowertrainController2EM_P.Gain_Gain_e *
    EvPowertrainController2EM_U.BMSChrgCurrLmt *
    EvPowertrainController2EM_U.BattPackVolt;

  /* Outputs for Atomic SubSystem: '<Root>/Energy Management' */
  /* Lookup_n-D: '<S28>/MaxEMTrqVsSpd' incorporates:
   *  Inport: '<Root>/EMSpd'
   */
  rtb_Gain1_n = look1_binlcapw(EvPowertrainController2EM_U.EMSpd[0],
    EvPowertrainController2EM_P.PlntEM1Spd,
    EvPowertrainController2EM_P.PlntEM1Trq, 13U);

  /* Switch: '<S31>/Switch2' incorporates:
   *  Constant: '<S31>/Constant1'
   *  Constant: '<S31>/Constant2'
   *  Inport: '<Root>/EMSpd'
   *  Product: '<S31>/Product1'
   */
  if (rtb_Gain1_n * EvPowertrainController2EM_U.EMSpd[0] >=
      EvPowertrainController2EM_P.Switch2_Threshold_g) {
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Constant1_Value;
  } else {
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Constant2_Value;
  }

  /* End of Switch: '<S31>/Switch2' */

  /* Math: '<S31>/Math Function1' incorporates:
   *  Constant: '<S16>/Constant'
   *  Constant: '<S31>/Constant'
   *  Constant: '<S38>/Constant'
   *  Constant: '<S43>/Constant'
   *  Math: '<S16>/Math Function1'
   *  Math: '<S38>/Math Function1'
   *  Math: '<S43>/Math Function1'
   *  Switch: '<S21>/Accel Decel Switch'
   */
  rtb_WhlEMTrqMax_tmp = EvPowertrainController2EM_P.PlntDiffrntlEff *
    EvPowertrainController2EM_P.PlntEM1TransEff;
  if ((rtb_WhlEMTrqMax_tmp < 0.0) && (rtb_UnitDelay2 > floor(rtb_UnitDelay2))) {
    rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp, rtb_UnitDelay2);
  } else {
    rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp, rtb_UnitDelay2);
  }

  /* Gain: '<S30>/Gain3' incorporates:
   *  Gain: '<S15>/Gain3'
   *  Gain: '<S19>/Gain1'
   *  Gain: '<S37>/Gain3'
   *  Gain: '<S69>/Gain3'
   *  Switch: '<S21>/Accel Decel Switch'
   */
  rtb_RateLimiter_idx_0_tmp = EvPowertrainController2EM_P.PlntDiffrntlRatio *
    EvPowertrainController2EM_P.PlntEM1TransGearRatio;

  /* Product: '<S30>/Divide2' incorporates:
   *  Gain: '<S30>/Gain3'
   *  Math: '<S31>/Math Function1'
   */
  rtb_RateLimiter_idx_0 = rtb_RateLimiter_idx_0_tmp * rtb_Gain1_n *
    rtb_BrkTrqReqTotal_tmp;

  /* Lookup_n-D: '<S29>/MaxEMTrqVsSpd' incorporates:
   *  Inport: '<Root>/EMSpd'
   */
  rtb_UnitDelay2 = look1_binlcapw(EvPowertrainController2EM_U.EMSpd[1],
    EvPowertrainController2EM_P.PlntEM2Spd,
    EvPowertrainController2EM_P.PlntEM2Trq, 13U);

  /* Switch: '<S33>/Switch2' incorporates:
   *  Constant: '<S33>/Constant1'
   *  Constant: '<S33>/Constant2'
   *  Inport: '<Root>/EMSpd'
   *  Product: '<S33>/Product1'
   */
  if (rtb_UnitDelay2 * EvPowertrainController2EM_U.EMSpd[1] >=
      EvPowertrainController2EM_P.Switch2_Threshold_h) {
    rtb_Gain1_n = EvPowertrainController2EM_P.Constant1_Value_g;
  } else {
    rtb_Gain1_n = EvPowertrainController2EM_P.Constant2_Value_j;
  }

  /* End of Switch: '<S33>/Switch2' */

  /* Math: '<S33>/Math Function1' incorporates:
   *  Constant: '<S33>/Constant'
   *  Constant: '<S40>/Constant'
   *  Constant: '<S44>/Constant'
   *  Constant: '<S83>/Constant'
   *  Math: '<S40>/Math Function1'
   *  Math: '<S44>/Math Function1'
   *  Math: '<S83>/Math Function1'
   */
  rtb_WhlEMTrqMax_tmp_0 = EvPowertrainController2EM_P.PlntDiffrntl2Eff *
    EvPowertrainController2EM_P.PlntEM2TransEff;
  if ((rtb_WhlEMTrqMax_tmp_0 < 0.0) && (rtb_Gain1_n > floor(rtb_Gain1_n))) {
    rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp_0, rtb_Gain1_n);
  } else {
    rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp_0, rtb_Gain1_n);
  }

  /* Gain: '<S32>/Gain3' incorporates:
   *  Gain: '<S17>/Gain3'
   *  Gain: '<S19>/Gain2'
   *  Gain: '<S39>/Gain3'
   *  Gain: '<S82>/Gain3'
   *  Switch: '<S21>/Accel Decel Switch'
   */
  rtb_RateLimiter_idx_1_tmp = EvPowertrainController2EM_P.PlntDiffrntl2Ratio *
    EvPowertrainController2EM_P.PlntEM2TransGearRatio;

  /* Product: '<S32>/Divide2' incorporates:
   *  Gain: '<S32>/Gain3'
   *  Math: '<S33>/Math Function1'
   */
  rtb_RateLimiter_idx_1 = rtb_RateLimiter_idx_1_tmp * rtb_UnitDelay2 *
    rtb_BrkTrqReqTotal_tmp;

  /* Product: '<S41>/Product5' incorporates:
   *  Constant: '<S41>/Front Brakes'
   *  Product: '<S41>/Product2'
   */
  rtb_BrkTrqReqTotal = EvPowertrainController2EM_P.PlntBrkKinFricCffFrnt *
    3.1415926535897931 * 0.0025000000000000005 *
    EvPowertrainController2EM_P.PlntBrkPadMeanRadiusFrnt *
    EvPowertrainController2EM_P.PlntBrkNumPadsFrnt / 4.0;

  /* Product: '<S41>/Product3' incorporates:
   *  Constant: '<S41>/Rear Brakes'
   *  Product: '<S41>/Product1'
   */
  rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.PlntBrkKinFricCffRear *
    3.1415926535897931 * 0.0025000000000000005 *
    EvPowertrainController2EM_P.PlntBrkPadMeanRadiusRear *
    EvPowertrainController2EM_P.PlntBrkNumPadsRear / 4.0;

  /* Sum: '<S41>/Add' incorporates:
   *  Constant: '<S2>/Front Bias'
   *  Constant: '<S2>/Rear Bias'
   *  Constant: '<S41>/Front Brakes'
   *  Constant: '<S41>/Rear Brakes'
   *  Gain: '<S2>/Gain4'
   *  Inport: '<Root>/BcuBrkPrsCmd'
   *  Product: '<S2>/Product'
   *  Product: '<S41>/Product1'
   *  Product: '<S41>/Product2'
   *  Product: '<S41>/Product3'
   *  Product: '<S41>/Product5'
   */
  rtb_BrkTrqReqTotal = ((EvPowertrainController2EM_P.PlntBrkFrntBias *
    EvPowertrainController2EM_U.BcuBrkPrsCmd[0] *
    EvPowertrainController2EM_P.PlntBrkPrsFctr * rtb_BrkTrqReqTotal +
    EvPowertrainController2EM_P.PlntBrkFrntBias *
    EvPowertrainController2EM_U.BcuBrkPrsCmd[1] *
    EvPowertrainController2EM_P.PlntBrkPrsFctr * rtb_BrkTrqReqTotal) +
                        EvPowertrainController2EM_P.PlntBrkRearBias *
                        EvPowertrainController2EM_U.BcuBrkPrsCmd[2] *
                        EvPowertrainController2EM_P.PlntBrkPrsFctr *
                        rtb_BrkTrqReqTotal_tmp) +
    EvPowertrainController2EM_P.PlntBrkRearBias *
    EvPowertrainController2EM_U.BcuBrkPrsCmd[3] *
    EvPowertrainController2EM_P.PlntBrkPrsFctr * rtb_BrkTrqReqTotal_tmp;

  /* Switch: '<S21>/Accel Decel Switch' incorporates:
   *  Gain: '<S15>/Gain3'
   *  Gain: '<S36>/Gain1'
   *  Gain: '<S5>/convert2percent'
   *  Inport: '<Root>/AccelPdl'
   *  Inport: '<Root>/BMSSOC'
   *  Inport: '<Root>/VehSpdFdbk'
   *  Lookup_n-D: '<S36>/ChrgLmt'
   *  Lookup_n-D: '<S36>/RegenBrakingCutoff'
   *  Math: '<S16>/Math Function1'
   *  MinMax: '<S36>/MinMax'
   *  Product: '<S15>/Divide2'
   *  Product: '<S17>/Divide2'
   *  Product: '<S1>/Product1'
   *  Product: '<S36>/Product1'
   *  Product: '<S36>/Product3'
   *  Sum: '<S36>/Sum of Elements'
   *  Sum: '<S9>/Add'
   */
  if (EvPowertrainController2EM_U.AccelPdl >
      EvPowertrainController2EM_P.AccelDecelSwitch_Threshold) {
    /* Gain: '<S19>/Gain2' incorporates:
     *  Gain: '<S19>/Gain4'
     *  Inport: '<Root>/VehSpdFdbk'
     */
    rtb_RegenFactor = 1.0 / EvPowertrainController2EM_P.PlntWhlLdRadiusRear *
      EvPowertrainController2EM_U.VehSpdFdbk * rtb_RateLimiter_idx_1_tmp;

    /* Lookup_n-D: '<S13>/MaxEMTrqVsSpd' incorporates:
     *  Lookup_n-D: '<S12>/MaxEMTrqVsSpd'
     */
    rtb_Gain1_n = look1_binlcapw(rtb_RegenFactor,
      EvPowertrainController2EM_P.PlntEM2Spd,
      EvPowertrainController2EM_P.PlntEM2Trq, 13U);

    /* Gain: '<S17>/Gain3' */
    rtb_whlpureelectrictraction = rtb_RateLimiter_idx_1_tmp * rtb_Gain1_n;

    /* Switch: '<S18>/Switch2' incorporates:
     *  Constant: '<S18>/Constant1'
     *  Constant: '<S18>/Constant2'
     *  Product: '<S18>/Product1'
     */
    if (rtb_Gain1_n * rtb_RegenFactor >=
        EvPowertrainController2EM_P.Switch2_Threshold) {
      rtb_Gain1_n = EvPowertrainController2EM_P.Constant1_Value_kl;
    } else {
      rtb_Gain1_n = EvPowertrainController2EM_P.Constant2_Value_b;
    }

    /* End of Switch: '<S18>/Switch2' */

    /* Math: '<S18>/Math Function1' incorporates:
     *  Constant: '<S33>/Constant'
     *  Math: '<S33>/Math Function1'
     */
    if ((rtb_WhlEMTrqMax_tmp_0 < 0.0) && (rtb_Gain1_n > floor(rtb_Gain1_n))) {
      rtb_UnitDelay2 = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp_0, rtb_Gain1_n);
    } else {
      rtb_UnitDelay2 = rt_powd_snf(rtb_WhlEMTrqMax_tmp_0, rtb_Gain1_n);
    }

    /* End of Math: '<S18>/Math Function1' */

    /* Gain: '<S19>/Gain1' incorporates:
     *  Gain: '<S19>/Gain3'
     *  Inport: '<Root>/VehSpdFdbk'
     */
    rtb_Gain1_n = 1.0 / EvPowertrainController2EM_P.PlntWhlLdRadiusFrnt *
      EvPowertrainController2EM_U.VehSpdFdbk * rtb_RateLimiter_idx_0_tmp;

    /* Lookup_n-D: '<S12>/MaxEMTrqVsSpd' incorporates:
     *  Math: '<S16>/Math Function1'
     */
    rtb_RegenFactor = look1_binlcapw(rtb_Gain1_n,
      EvPowertrainController2EM_P.PlntEM1Spd,
      EvPowertrainController2EM_P.PlntEM1Trq, 13U);

    /* Switch: '<S16>/Switch2' incorporates:
     *  Constant: '<S16>/Constant1'
     *  Constant: '<S16>/Constant2'
     *  Product: '<S16>/Product1'
     */
    if (rtb_RegenFactor * rtb_Gain1_n >=
        EvPowertrainController2EM_P.Switch2_Threshold_l) {
      rtb_Gain1_n = EvPowertrainController2EM_P.Constant1_Value_k;
    } else {
      rtb_Gain1_n = EvPowertrainController2EM_P.Constant2_Value_jm;
    }

    /* End of Switch: '<S16>/Switch2' */

    /* Math: '<S16>/Math Function1' */
    if ((rtb_WhlEMTrqMax_tmp < 0.0) && (rtb_Gain1_n > floor(rtb_Gain1_n))) {
      rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp, rtb_Gain1_n);
    } else {
      rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp, rtb_Gain1_n);
    }

    rtb_whlpureelectrictraction = (rtb_RateLimiter_idx_0_tmp * rtb_RegenFactor *
      rtb_BrkTrqReqTotal_tmp + rtb_UnitDelay2 * rtb_whlpureelectrictraction) *
      EvPowertrainController2EM_U.AccelPdl;
  } else {
    rtb_whlpureelectrictraction = look1_binlcapw
      (EvPowertrainController2EM_P.convert2percent_Gain *
       EvPowertrainController2EM_U.BMSSOC,
       EvPowertrainController2EM_P.CtrlVcuEvSocBpt,
       EvPowertrainController2EM_P.CtrlVcuEvChrgLmtBpt, 10U) * look1_binlcapw
      (EvPowertrainController2EM_U.VehSpdFdbk,
       EvPowertrainController2EM_P.CtrlVcuEvRegenBrkSpdBpt,
       EvPowertrainController2EM_P.CtrlVcuEvRegenBrkCutOff, 1U) * fmin
      (rtb_BrkTrqReqTotal, rtb_RateLimiter_idx_0 + rtb_RateLimiter_idx_1) *
      EvPowertrainController2EM_P.Gain1_Gain;
  }

  for (i = 0; i < 200; i++) {
    /* Switch: '<S21>/Accel Decel Switch1' incorporates:
     *  Constant: '<S39>/EMTrq Control Vector Traction'
     *  Gain: '<S39>/Gain'
     *  Gain: '<S39>/Gain3'
     *  Inport: '<Root>/AccelPdl'
     *  Math: '<S40>/Math Function1'
     *  Product: '<S39>/Divide2'
     */
    if (EvPowertrainController2EM_U.AccelPdl >
        EvPowertrainController2EM_P.AccelDecelSwitch1_Threshold) {
      /* Product: '<S40>/Product1' incorporates:
       *  Constant: '<S39>/EMTrq Control Vector Traction'
       */
      rtb_RegenFactor =
        EvPowertrainController2EM_P.EMTrqControlVectorTraction_Valu[i];

      /* Switch: '<S40>/Switch2' incorporates:
       *  Constant: '<S39>/EMTrq Control Vector Traction'
       *  Constant: '<S40>/Constant1'
       *  Constant: '<S40>/Constant2'
       *  Inport: '<Root>/EMSpd'
       *  Product: '<S40>/Product1'
       *  SignalConversion generated from: '<S25>/Vector Concatenate1'
       */
      if (rtb_RegenFactor * EvPowertrainController2EM_U.EMSpd[1] >=
          EvPowertrainController2EM_P.Switch2_Threshold_k) {
        rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant1_Value_ky;
      } else {
        rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant2_Value_bd;
      }

      /* Math: '<S40>/Math Function1' */
      if ((rtb_WhlEMTrqMax_tmp_0 < 0.0) && (rtb_BrkTrqReqTotal_tmp > floor
           (rtb_BrkTrqReqTotal_tmp))) {
        rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp_0,
          rtb_BrkTrqReqTotal_tmp);
      } else {
        rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp_0,
          rtb_BrkTrqReqTotal_tmp);
      }

      rtb_VectorConcatenate_i[i + 1] = rtb_RateLimiter_idx_1_tmp *
        rtb_RegenFactor * rtb_BrkTrqReqTotal_tmp;
    } else {
      /* Product: '<S40>/Product1' incorporates:
       *  Constant: '<S39>/EMTrq Control Vector Traction'
       */
      rtb_RegenFactor =
        EvPowertrainController2EM_P.EMTrqControlVectorTraction_Valu[i];

      /* Switch: '<S40>/Switch2' incorporates:
       *  Constant: '<S39>/EMTrq Control Vector Traction'
       *  Constant: '<S40>/Constant1'
       *  Constant: '<S40>/Constant2'
       *  Inport: '<Root>/EMSpd'
       *  Product: '<S40>/Product1'
       *  SignalConversion generated from: '<S25>/Vector Concatenate1'
       */
      if (rtb_RegenFactor * EvPowertrainController2EM_U.EMSpd[1] >=
          EvPowertrainController2EM_P.Switch2_Threshold_k) {
        rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant1_Value_ky;
      } else {
        rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant2_Value_bd;
      }

      /* Math: '<S40>/Math Function1' */
      if ((rtb_WhlEMTrqMax_tmp_0 < 0.0) && (rtb_BrkTrqReqTotal_tmp > floor
           (rtb_BrkTrqReqTotal_tmp))) {
        rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp_0,
          rtb_BrkTrqReqTotal_tmp);
      } else {
        rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp_0,
          rtb_BrkTrqReqTotal_tmp);
      }

      rtb_VectorConcatenate_i[i + 1] = rtb_RateLimiter_idx_1_tmp *
        rtb_RegenFactor * rtb_BrkTrqReqTotal_tmp *
        EvPowertrainController2EM_P.Gain_Gain;
    }

    /* End of Switch: '<S21>/Accel Decel Switch1' */

    /* Switch: '<S21>/Accel Decel Switch2' incorporates:
     *  Constant: '<S37>/EMTrq Control Vector Traction'
     *  Gain: '<S37>/Gain'
     *  Gain: '<S37>/Gain3'
     *  Inport: '<Root>/AccelPdl'
     *  Math: '<S38>/Math Function1'
     *  Product: '<S37>/Divide2'
     */
    if (EvPowertrainController2EM_U.AccelPdl >
        EvPowertrainController2EM_P.AccelDecelSwitch2_Threshold) {
      /* Product: '<S38>/Product1' incorporates:
       *  Constant: '<S37>/EMTrq Control Vector Traction'
       */
      rtb_RegenFactor =
        EvPowertrainController2EM_P.EMTrqControlVectorTraction_Va_j[i];

      /* Switch: '<S38>/Switch2' incorporates:
       *  Constant: '<S37>/EMTrq Control Vector Traction'
       *  Constant: '<S38>/Constant1'
       *  Constant: '<S38>/Constant2'
       *  Inport: '<Root>/EMSpd'
       *  Product: '<S38>/Product1'
       *  SignalConversion generated from: '<S25>/Vector Concatenate1'
       */
      if (rtb_RegenFactor * EvPowertrainController2EM_U.EMSpd[0] >=
          EvPowertrainController2EM_P.Switch2_Threshold_j) {
        rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant1_Value_n;
      } else {
        rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant2_Value_jmm;
      }

      /* Math: '<S38>/Math Function1' */
      if ((rtb_WhlEMTrqMax_tmp < 0.0) && (rtb_BrkTrqReqTotal_tmp > floor
           (rtb_BrkTrqReqTotal_tmp))) {
        rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp,
          rtb_BrkTrqReqTotal_tmp);
      } else {
        rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp,
          rtb_BrkTrqReqTotal_tmp);
      }

      rtb_VectorConcatenate1[i + 1] = rtb_RateLimiter_idx_0_tmp *
        rtb_RegenFactor * rtb_BrkTrqReqTotal_tmp;
    } else {
      /* Product: '<S38>/Product1' incorporates:
       *  Constant: '<S37>/EMTrq Control Vector Traction'
       */
      rtb_RegenFactor =
        EvPowertrainController2EM_P.EMTrqControlVectorTraction_Va_j[i];

      /* Switch: '<S38>/Switch2' incorporates:
       *  Constant: '<S37>/EMTrq Control Vector Traction'
       *  Constant: '<S38>/Constant1'
       *  Constant: '<S38>/Constant2'
       *  Inport: '<Root>/EMSpd'
       *  Product: '<S38>/Product1'
       *  SignalConversion generated from: '<S25>/Vector Concatenate1'
       */
      if (rtb_RegenFactor * EvPowertrainController2EM_U.EMSpd[0] >=
          EvPowertrainController2EM_P.Switch2_Threshold_j) {
        rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant1_Value_n;
      } else {
        rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant2_Value_jmm;
      }

      /* Math: '<S38>/Math Function1' */
      if ((rtb_WhlEMTrqMax_tmp < 0.0) && (rtb_BrkTrqReqTotal_tmp > floor
           (rtb_BrkTrqReqTotal_tmp))) {
        rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp,
          rtb_BrkTrqReqTotal_tmp);
      } else {
        rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp,
          rtb_BrkTrqReqTotal_tmp);
      }

      rtb_VectorConcatenate1[i + 1] = rtb_RateLimiter_idx_0_tmp *
        rtb_RegenFactor * rtb_BrkTrqReqTotal_tmp *
        EvPowertrainController2EM_P.Gain_Gain_d;
    }

    /* End of Switch: '<S21>/Accel Decel Switch2' */
  }

  /* SignalConversion generated from: '<S21>/Vector Concatenate1' */
  rtb_VectorConcatenate1[0] = rtb_whlpureelectrictraction;

  /* SignalConversion generated from: '<S21>/Vector Concatenate' */
  rtb_VectorConcatenate_i[0] = rtb_whlpureelectrictraction;

  /* Switch: '<S57>/Switch' incorporates:
   *  Constant: '<S60>/Constant'
   *  Constant: '<S61>/Constant'
   *  Fcn: '<S57>/Fcn'
   *  Inport: '<Root>/BattPackVolt'
   *  Logic: '<S57>/Logical Operator'
   *  Product: '<S57>/Product'
   *  RelationalOperator: '<S60>/Compare'
   *  RelationalOperator: '<S61>/Compare'
   *  Switch: '<S57>/Switch1'
   */
  if ((EvPowertrainController2EM_U.BattPackVolt >=
       -EvPowertrainController2EM_P.div0protectpoly1_thresh) &&
      (EvPowertrainController2EM_U.BattPackVolt <=
       EvPowertrainController2EM_P.div0protectpoly1_thresh)) {
    /* Switch: '<S57>/Switch1' incorporates:
     *  Constant: '<S57>/Constant'
     *  UnaryMinus: '<S57>/Unary Minus'
     */
    if (EvPowertrainController2EM_U.BattPackVolt >=
        EvPowertrainController2EM_P.Switch1_Threshold_p) {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant_Value_i;
    } else {
      rtb_BrkTrqReqTotal_tmp = -EvPowertrainController2EM_P.Constant_Value_i;
    }

    rtb_RegenFactor = 0.02 / (3.0 - rt_powd_snf
      (EvPowertrainController2EM_U.BattPackVolt / 0.01, 2.0)) *
      rtb_BrkTrqReqTotal_tmp;
  } else {
    rtb_RegenFactor = EvPowertrainController2EM_U.BattPackVolt;
  }

  /* End of Switch: '<S57>/Switch' */

  /* Product: '<S52>/Divide' */
  rtb_RegenFactor = rtb_Product / rtb_RegenFactor;

  /* Switch: '<S64>/Switch' incorporates:
   *  Constant: '<S64>/Constant'
   *  Constant: '<S72>/Constant7'
   *  Constant: '<S73>/Constant2'
   *  Constant: '<S73>/Constant20'
   *  Constant: '<S73>/Constant4'
   *  Constant: '<S73>/Constant5'
   *  Constant: '<S73>/Constant6'
   *  Constant: '<S73>/Constant7'
   *  Constant: '<S73>/Constant9'
   *  Gain: '<S64>/Road mu'
   *  Gain: '<S64>/Safety Factor'
   *  Gain: '<S73>/TireRadius'
   *  Product: '<S73>/Divide'
   *  Product: '<S73>/Product'
   *  Product: '<S73>/Product1'
   *  Sum: '<S73>/Add2'
   *  Sum: '<S73>/Add3'
   *  Sum: '<S73>/Add4'
   */
  if (rtb_whlpureelectrictraction > EvPowertrainController2EM_P.Switch_Threshold)
  {
    rtb_Gain1_n = (EvPowertrainController2EM_P.PlntVehDstCGRearAxl *
                   EvPowertrainController2EM_P.PlntVehMass *
                   EvPowertrainController2EM_P.EnvGrvty -
                   EvPowertrainController2EM_P.EnvGrvty *
                   EvPowertrainController2EM_P.PlntVehMass *
                   (EvPowertrainController2EM_P.PlntVehCGHgtAxl +
                    EvPowertrainController2EM_P.PlntWhlLdRadiusFrnt) *
                   EvPowertrainController2EM_P.CtrlVcuMaxAccelG) /
      (EvPowertrainController2EM_P.PlntVehDstCGFrntAxl +
       EvPowertrainController2EM_P.PlntVehDstCGRearAxl) *
      EvPowertrainController2EM_P.PlntWhlLdRadiusFrnt *
      EvPowertrainController2EM_P.CtrlVcuRoadMuEst *
      EvPowertrainController2EM_P.CtrlVcuSftyFctr;
  } else {
    rtb_Gain1_n = EvPowertrainController2EM_P.Constant_Value_p;
  }

  /* End of Switch: '<S64>/Switch' */

  /* Outputs for IfAction SubSystem: '<S50>/Regen' incorporates:
   *  ActionPort: '<S88>/Action Port'
   */
  for (i = 0; i < 201; i++) {
    /* If: '<S50>/If' */
    if (rtb_whlpureelectrictraction >= 0.0) {
      /* Outputs for IfAction SubSystem: '<S50>/Traction' incorporates:
       *  ActionPort: '<S89>/Action Port'
       */
      /* Switch: '<S89>/Switch1' incorporates:
       *  RelationalOperator: '<S89>/Relational Operator'
       *  SignalConversion generated from: '<S89>/WhlEMTrqSplitVecRear'
       *  Sum: '<S89>/Add3'
       *  UnitDelay: '<S24>/Unit Delay'
       */
      if (rtb_whlpureelectrictraction <= rtb_VectorConcatenate_i[i]) {
        rtb_VectorConcatenate1[i] = rtb_whlpureelectrictraction -
          EvPowertrainController2EM_DW.UnitDelay_DSTATE_p[i];
      }

      /* End of Switch: '<S89>/Switch1' */
      /* End of Outputs for SubSystem: '<S50>/Traction' */
    } else {
      /* Switch: '<S88>/Switch1' incorporates:
       *  SignalConversion generated from: '<S88>/WhlEMTrqSplitVecFrnt'
       */
      rtb_VectorConcatenate_j = rtb_VectorConcatenate_i[i];

      /* SignalConversion generated from: '<S88>/WhlEMTrqSplitVecFrnt' */
      rtb_BrkTrqReqTotal_tmp = rtb_VectorConcatenate1[i];

      /* Switch: '<S88>/Switch1' incorporates:
       *  RelationalOperator: '<S88>/Relational Operator'
       *  SignalConversion generated from: '<S88>/WhlEMTrqSplitVecFrnt'
       *  Sum: '<S88>/Add3'
       *  UnitDelay: '<S24>/Unit Delay1'
       */
      if (rtb_whlpureelectrictraction >= rtb_BrkTrqReqTotal_tmp) {
        rtb_VectorConcatenate_j = rtb_whlpureelectrictraction -
          EvPowertrainController2EM_DW.UnitDelay1_DSTATE[i];
      }

      /* Switch: '<S90>/Switch2' incorporates:
       *  Constant: '<S88>/Constant1'
       *  RelationalOperator: '<S90>/LowerRelop1'
       *  RelationalOperator: '<S90>/UpperRelop'
       *  SignalConversion generated from: '<S88>/WhlEMTrqSplitVecFrnt'
       *  Switch: '<S90>/Switch'
       */
      if (rtb_VectorConcatenate_j >
          EvPowertrainController2EM_P.Constant1_Value_h5) {
        /* SignalConversion generated from: '<S88>/WhlEMTrqSplitVecRear1' */
        rtb_VectorConcatenate_j = EvPowertrainController2EM_P.Constant1_Value_h5;
      } else if (rtb_VectorConcatenate_j < rtb_BrkTrqReqTotal_tmp) {
        /* Switch: '<S90>/Switch' incorporates:
         *  SignalConversion generated from: '<S88>/WhlEMTrqSplitVecRear1'
         *  SignalConversion generated from: '<S88>/WhlEMTrqSplitVecFrnt'
         */
        rtb_VectorConcatenate_j = rtb_BrkTrqReqTotal_tmp;
      }

      /* End of Switch: '<S90>/Switch2' */

      /* SignalConversion generated from: '<S88>/WhlEMTrqSplitVecRear1' incorporates:
       *  RelationalOperator: '<S90>/LowerRelop1'
       */
      rtb_VectorConcatenate_i[i] = rtb_VectorConcatenate_j;
    }

    /* End of If: '<S50>/If' */
  }

  /* End of Outputs for SubSystem: '<S50>/Regen' */

  /* Switch: '<S64>/Switch1' incorporates:
   *  Constant: '<S64>/Constant'
   *  Constant: '<S72>/Constant6'
   *  Constant: '<S74>/Constant2'
   *  Constant: '<S74>/Constant20'
   *  Constant: '<S74>/Constant4'
   *  Constant: '<S74>/Constant5'
   *  Constant: '<S74>/Constant6'
   *  Constant: '<S74>/Constant7'
   *  Constant: '<S74>/Constant9'
   *  Gain: '<S64>/Road mu1'
   *  Gain: '<S64>/Safety Factor1'
   *  Gain: '<S72>/Gain'
   *  Gain: '<S74>/TireRadius'
   *  Product: '<S74>/Divide'
   *  Product: '<S74>/Product'
   *  Product: '<S74>/Product1'
   *  Sum: '<S74>/Add2'
   *  Sum: '<S74>/Add3'
   *  Sum: '<S74>/Add4'
   */
  if (rtb_whlpureelectrictraction >
      EvPowertrainController2EM_P.Switch1_Threshold_h) {
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Constant_Value_p;
  } else {
    rtb_UnitDelay2 = (EvPowertrainController2EM_P.PlntVehDstCGRearAxl *
                      EvPowertrainController2EM_P.PlntVehMass *
                      EvPowertrainController2EM_P.EnvGrvty -
                      EvPowertrainController2EM_P.EnvGrvty *
                      EvPowertrainController2EM_P.PlntVehMass *
                      (EvPowertrainController2EM_P.PlntVehCGHgtAxl +
                       EvPowertrainController2EM_P.PlntWhlLdRadiusFrnt) *
                      EvPowertrainController2EM_P.CtrlVcuMaxDecelG) /
      (EvPowertrainController2EM_P.PlntVehDstCGFrntAxl +
       EvPowertrainController2EM_P.PlntVehDstCGRearAxl) *
      EvPowertrainController2EM_P.PlntWhlLdRadiusFrnt *
      EvPowertrainController2EM_P.Gain_Gain_o *
      EvPowertrainController2EM_P.CtrlVcuRoadMuEst *
      EvPowertrainController2EM_P.CtrlVcuSftyFctr;
  }

  /* End of Switch: '<S64>/Switch1' */

  /* Switch: '<S71>/Switch2' incorporates:
   *  RelationalOperator: '<S71>/LowerRelop1'
   *  RelationalOperator: '<S71>/UpperRelop'
   *  Switch: '<S71>/Switch'
   */
  for (i = 0; i < 201; i++) {
    /* RelationalOperator: '<S71>/LowerRelop1' */
    rtb_BrkTrqReqTotal_tmp = rtb_VectorConcatenate1[i];
    if (rtb_BrkTrqReqTotal_tmp > rtb_Gain1_n) {
      rtb_VectorConcatenate1[i] = rtb_Gain1_n;
    } else if (rtb_BrkTrqReqTotal_tmp < rtb_UnitDelay2) {
      /* Switch: '<S71>/Switch' */
      rtb_VectorConcatenate1[i] = rtb_UnitDelay2;
    }
  }

  /* End of Switch: '<S71>/Switch2' */

  /* Gain: '<S62>/Gain' */
  rtb_Gain1_n = EvPowertrainController2EM_P.Gain_Gain_h * rtb_RateLimiter_idx_0;

  /* Gain: '<S69>/Gain3' incorporates:
   *  Gain: '<S42>/Gain3'
   */
  rtb_RateLimiter_idx_0_tmp = 1.0 / rtb_RateLimiter_idx_0_tmp;

  /* SignalConversion generated from: '<S25>/Vector Concatenate1' incorporates:
   *  Inport: '<Root>/EMSpd'
   */
  EMSpd = EvPowertrainController2EM_U.EMSpd[0];
  for (i = 0; i < 201; i++) {
    /* RelationalOperator: '<S67>/UpperRelop' incorporates:
     *  RelationalOperator: '<S62>/Relational Operator1'
     */
    rtb_BrkTrqReqTotal_tmp = rtb_VectorConcatenate1[i];
    rtb_Compare_n = (rtb_BrkTrqReqTotal_tmp < rtb_Gain1_n);
    rtb_LogicalOperator_he[i] = rtb_Compare_n;

    /* Switch: '<S67>/Switch2' incorporates:
     *  RelationalOperator: '<S67>/LowerRelop1'
     *  RelationalOperator: '<S67>/UpperRelop'
     *  Switch: '<S67>/Switch'
     */
    if (rtb_BrkTrqReqTotal_tmp > rtb_RateLimiter_idx_0) {
      rtb_Switch2[i] = rtb_RateLimiter_idx_0;
    } else if (rtb_Compare_n) {
      /* Switch: '<S67>/Switch' */
      rtb_Switch2[i] = rtb_Gain1_n;
    } else {
      rtb_Switch2[i] = rtb_BrkTrqReqTotal_tmp;
    }

    /* End of Switch: '<S67>/Switch2' */

    /* Switch: '<S70>/Switch2' incorporates:
     *  Constant: '<S70>/Constant1'
     *  Constant: '<S70>/Constant2'
     *  Product: '<S70>/Product1'
     *  SignalConversion generated from: '<S25>/Vector Concatenate1'
     *  UnitDelay: '<S69>/Unit Delay'
     */
    if (EvPowertrainController2EM_DW.UnitDelay_DSTATE[i] * EMSpd >=
        EvPowertrainController2EM_P.Switch2_Threshold_m) {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant1_Value_o;
    } else {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant2_Value_d;
    }

    /* End of Switch: '<S70>/Switch2' */

    /* Math: '<S70>/Math Function1' */
    if ((rtb_WhlEMTrqMax_tmp < 0.0) && (rtb_BrkTrqReqTotal_tmp > floor
         (rtb_BrkTrqReqTotal_tmp))) {
      rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp,
        rtb_BrkTrqReqTotal_tmp);
    } else {
      rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp,
        rtb_BrkTrqReqTotal_tmp);
    }

    /* Product: '<S69>/Divide2' incorporates:
     *  Gain: '<S69>/Gain3'
     *  Math: '<S70>/Math Function1'
     */
    rtb_BrkTrqReqTotal_tmp = 1.0 / rtb_BrkTrqReqTotal_tmp *
      (rtb_RateLimiter_idx_0_tmp * rtb_Switch2[i]);
    rtb_Divide2_p[i] = rtb_BrkTrqReqTotal_tmp;

    /* Product: '<S68>/Product1' incorporates:
     *  SignalConversion generated from: '<S25>/Vector Concatenate1'
     */
    rtb_Divide[i] = EMSpd * rtb_BrkTrqReqTotal_tmp;

    /* Abs: '<S68>/Abs1' */
    rtb_Switch2_l[i] = fabs(rtb_BrkTrqReqTotal_tmp);
  }

  /* Lookup_n-D: '<S68>/Eff Map' incorporates:
   *  Abs: '<S68>/Abs'
   *  Inport: '<Root>/EMSpd'
   *  SignalConversion generated from: '<S25>/Vector Concatenate1'
   */
  bpIndices[0U] = plook_bincpa(fabs(EvPowertrainController2EM_U.EMSpd[0]),
    EvPowertrainController2EM_P.PlntEM1SpdEff, 13U, &rtb_Gain1_n,
    &EvPowertrainController2EM_DW.m_Cache01);
  rtb_VectorConcatenate1_l[0U] = rtb_Gain1_n;
  for (i = 0; i < 201; i++) {
    bpIndices[1U] = plook_bincpa(rtb_Switch2_l[i],
      EvPowertrainController2EM_P.PlntEM1TrqEff, 10U, &rtb_Gain1_n,
      &EvPowertrainController2EM_DW.m_Cache02[i]);
    rtb_VectorConcatenate1_l[1U] = rtb_Gain1_n;
    rtb_Switch2_l[i] = intrp2d_la_pw(bpIndices, rtb_VectorConcatenate1_l,
      EvPowertrainController2EM_P.PlntEM1EffTbl, 14U,
      EvPowertrainController2EM_P.EffMap_maxIndex);
  }

  /* End of Lookup_n-D: '<S68>/Eff Map' */

  /* Product: '<S68>/Product4' incorporates:
   *  Math: '<S68>/Math Function1'
   */
  for (i = 0; i < 201; i++) {
    rtb_VectorConcatenate_j = rtb_Divide[i];

    /* Switch: '<S68>/Switch2' incorporates:
     *  Constant: '<S68>/Constant1'
     *  Constant: '<S68>/Constant2'
     */
    if (rtb_VectorConcatenate_j >=
        EvPowertrainController2EM_P.Switch2_Threshold_p) {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant1_Value_n0;
    } else {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant2_Value_i;
    }

    /* End of Switch: '<S68>/Switch2' */

    /* Gain: '<S68>/Gain2' */
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Gain2_Gain * rtb_Switch2_l[i];

    /* Math: '<S68>/Math Function1' */
    if ((rtb_UnitDelay2 < 0.0) && (rtb_BrkTrqReqTotal_tmp > floor
         (rtb_BrkTrqReqTotal_tmp))) {
      rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_UnitDelay2,
        rtb_BrkTrqReqTotal_tmp);
    } else {
      rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_UnitDelay2,
        rtb_BrkTrqReqTotal_tmp);
    }

    rtb_Product4[i] = rtb_VectorConcatenate_j * rtb_BrkTrqReqTotal_tmp;
  }

  /* End of Product: '<S68>/Product4' */

  /* Switch: '<S77>/Switch' incorporates:
   *  Constant: '<S77>/Constant'
   *  Constant: '<S85>/Constant7'
   *  Constant: '<S86>/Constant1'
   *  Constant: '<S86>/Constant11'
   *  Constant: '<S86>/Constant12'
   *  Constant: '<S86>/Constant13'
   *  Constant: '<S86>/Constant14'
   *  Constant: '<S86>/Constant3'
   *  Constant: '<S86>/Constant8'
   *  Gain: '<S77>/Road mu'
   *  Gain: '<S77>/Safety Factor'
   *  Gain: '<S86>/TireRadius1'
   *  Product: '<S86>/Divide1'
   *  Product: '<S86>/Product2'
   *  Product: '<S86>/Product3'
   *  Sum: '<S86>/Add1'
   *  Sum: '<S86>/Add5'
   *  Sum: '<S86>/Add6'
   */
  if (rtb_whlpureelectrictraction >
      EvPowertrainController2EM_P.Switch_Threshold_c) {
    rtb_UnitDelay2 = (EvPowertrainController2EM_P.EnvGrvty *
                      EvPowertrainController2EM_P.PlntVehMass *
                      (EvPowertrainController2EM_P.PlntVehCGHgtAxl +
                       EvPowertrainController2EM_P.PlntWhlLdRadiusRear) *
                      EvPowertrainController2EM_P.CtrlVcuMaxAccelG +
                      EvPowertrainController2EM_P.PlntVehDstCGFrntAxl *
                      EvPowertrainController2EM_P.PlntVehMass *
                      EvPowertrainController2EM_P.EnvGrvty) /
      (EvPowertrainController2EM_P.PlntVehDstCGFrntAxl +
       EvPowertrainController2EM_P.PlntVehDstCGRearAxl) *
      EvPowertrainController2EM_P.PlntWhlLdRadiusRear *
      EvPowertrainController2EM_P.CtrlVcuRoadMuEst *
      EvPowertrainController2EM_P.CtrlVcuSftyFctr;
  } else {
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Constant_Value_a;
  }

  /* End of Switch: '<S77>/Switch' */

  /* Switch: '<S77>/Switch1' incorporates:
   *  Constant: '<S77>/Constant'
   *  Constant: '<S85>/Constant6'
   *  Constant: '<S87>/Constant1'
   *  Constant: '<S87>/Constant11'
   *  Constant: '<S87>/Constant12'
   *  Constant: '<S87>/Constant13'
   *  Constant: '<S87>/Constant14'
   *  Constant: '<S87>/Constant3'
   *  Constant: '<S87>/Constant8'
   *  Gain: '<S77>/Road mu1'
   *  Gain: '<S77>/Safety Factor1'
   *  Gain: '<S85>/Gain'
   *  Gain: '<S87>/TireRadius1'
   *  Product: '<S87>/Divide1'
   *  Product: '<S87>/Product2'
   *  Product: '<S87>/Product3'
   *  Sum: '<S87>/Add1'
   *  Sum: '<S87>/Add5'
   *  Sum: '<S87>/Add6'
   */
  if (rtb_whlpureelectrictraction >
      EvPowertrainController2EM_P.Switch1_Threshold_m) {
    rtb_Gain1_n = EvPowertrainController2EM_P.Constant_Value_a;
  } else {
    rtb_Gain1_n = (EvPowertrainController2EM_P.EnvGrvty *
                   EvPowertrainController2EM_P.PlntVehMass *
                   (EvPowertrainController2EM_P.PlntVehCGHgtAxl +
                    EvPowertrainController2EM_P.PlntWhlLdRadiusRear) *
                   EvPowertrainController2EM_P.CtrlVcuMaxDecelG +
                   EvPowertrainController2EM_P.PlntVehDstCGFrntAxl *
                   EvPowertrainController2EM_P.PlntVehMass *
                   EvPowertrainController2EM_P.EnvGrvty) /
      (EvPowertrainController2EM_P.PlntVehDstCGFrntAxl +
       EvPowertrainController2EM_P.PlntVehDstCGRearAxl) *
      EvPowertrainController2EM_P.PlntWhlLdRadiusRear *
      EvPowertrainController2EM_P.Gain_Gain_l *
      EvPowertrainController2EM_P.CtrlVcuRoadMuEst *
      EvPowertrainController2EM_P.CtrlVcuSftyFctr;
  }

  /* End of Switch: '<S77>/Switch1' */

  /* Switch: '<S84>/Switch2' incorporates:
   *  RelationalOperator: '<S84>/LowerRelop1'
   *  RelationalOperator: '<S84>/UpperRelop'
   *  Switch: '<S84>/Switch'
   */
  for (i = 0; i < 201; i++) {
    /* RelationalOperator: '<S84>/LowerRelop1' */
    rtb_VectorConcatenate_j = rtb_VectorConcatenate_i[i];
    if (rtb_VectorConcatenate_j > rtb_UnitDelay2) {
      rtb_VectorConcatenate_i[i] = rtb_UnitDelay2;
    } else if (rtb_VectorConcatenate_j < rtb_Gain1_n) {
      /* Switch: '<S84>/Switch' */
      rtb_VectorConcatenate_i[i] = rtb_Gain1_n;
    }
  }

  /* End of Switch: '<S84>/Switch2' */

  /* Gain: '<S75>/Gain' */
  rtb_UnitDelay2 = EvPowertrainController2EM_P.Gain_Gain_dl *
    rtb_RateLimiter_idx_1;

  /* Gain: '<S82>/Gain3' incorporates:
   *  Gain: '<S42>/Gain1'
   */
  rtb_RateLimiter_idx_1_tmp = 1.0 / rtb_RateLimiter_idx_1_tmp;

  /* SignalConversion generated from: '<S25>/Vector Concatenate1' incorporates:
   *  Inport: '<Root>/EMSpd'
   */
  EMSpd = EvPowertrainController2EM_U.EMSpd[1];
  for (i = 0; i < 201; i++) {
    /* RelationalOperator: '<S80>/UpperRelop' incorporates:
     *  RelationalOperator: '<S75>/Relational Operator1'
     */
    rtb_VectorConcatenate_j = rtb_VectorConcatenate_i[i];
    rtb_Compare_n = (rtb_VectorConcatenate_j < rtb_UnitDelay2);
    rtb_LogicalOperator_c[i] = rtb_Compare_n;

    /* Switch: '<S80>/Switch2' incorporates:
     *  RelationalOperator: '<S80>/LowerRelop1'
     *  RelationalOperator: '<S80>/UpperRelop'
     *  Switch: '<S80>/Switch'
     */
    if (rtb_VectorConcatenate_j > rtb_RateLimiter_idx_1) {
      rtb_VectorConcatenate_j = rtb_RateLimiter_idx_1;
    } else if (rtb_Compare_n) {
      /* Switch: '<S80>/Switch' */
      rtb_VectorConcatenate_j = rtb_UnitDelay2;
    }

    rtb_Switch2_l[i] = rtb_VectorConcatenate_j;

    /* End of Switch: '<S80>/Switch2' */

    /* Switch: '<S83>/Switch2' incorporates:
     *  Constant: '<S83>/Constant1'
     *  Constant: '<S83>/Constant2'
     *  Product: '<S83>/Product1'
     *  SignalConversion generated from: '<S25>/Vector Concatenate1'
     *  UnitDelay: '<S82>/Unit Delay'
     */
    if (EvPowertrainController2EM_DW.UnitDelay_DSTATE_n[i] * EMSpd >=
        EvPowertrainController2EM_P.Switch2_Threshold_c) {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant1_Value_gm;
    } else {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant2_Value_iu;
    }

    /* End of Switch: '<S83>/Switch2' */

    /* Math: '<S83>/Math Function1' */
    if ((rtb_WhlEMTrqMax_tmp_0 < 0.0) && (rtb_BrkTrqReqTotal_tmp > floor
         (rtb_BrkTrqReqTotal_tmp))) {
      rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp_0,
        rtb_BrkTrqReqTotal_tmp);
    } else {
      rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp_0,
        rtb_BrkTrqReqTotal_tmp);
    }

    /* Product: '<S82>/Divide2' incorporates:
     *  Gain: '<S82>/Gain3'
     *  Math: '<S83>/Math Function1'
     */
    rtb_BrkTrqReqTotal_tmp = 1.0 / rtb_BrkTrqReqTotal_tmp *
      (rtb_RateLimiter_idx_1_tmp * rtb_VectorConcatenate_j);
    rtb_Divide2_ir[i] = rtb_BrkTrqReqTotal_tmp;

    /* Product: '<S81>/Product1' incorporates:
     *  SignalConversion generated from: '<S25>/Vector Concatenate1'
     */
    rtb_Sqrt1[i] = EMSpd * rtb_BrkTrqReqTotal_tmp;

    /* Abs: '<S81>/Abs1' */
    rtb_Divide[i] = fabs(rtb_BrkTrqReqTotal_tmp);
  }

  /* Lookup_n-D: '<S81>/Eff Map' incorporates:
   *  Abs: '<S81>/Abs'
   *  Inport: '<Root>/EMSpd'
   *  SignalConversion generated from: '<S25>/Vector Concatenate1'
   */
  bpIndices_0[0U] = plook_bincpa(fabs(EvPowertrainController2EM_U.EMSpd[1]),
    EvPowertrainController2EM_P.PlntEM2SpdEff, 13U, &rtb_Gain1_n,
    &EvPowertrainController2EM_DW.m_Cache01_a);
  fractions[0U] = rtb_Gain1_n;
  for (i = 0; i < 201; i++) {
    bpIndices_0[1U] = plook_bincpa(rtb_Divide[i],
      EvPowertrainController2EM_P.PlntEM2TrqEff, 10U, &rtb_Gain1_n,
      &EvPowertrainController2EM_DW.m_Cache02_g[i]);
    fractions[1U] = rtb_Gain1_n;
    rtb_Divide[i] = intrp2d_la_pw(bpIndices_0, fractions,
      EvPowertrainController2EM_P.PlntEM2EffTbl, 14U,
      EvPowertrainController2EM_P.EffMap_maxIndex_l);
  }

  /* End of Lookup_n-D: '<S81>/Eff Map' */

  /* Saturate: '<S51>/Saturation' incorporates:
   *  Inport: '<Root>/BattPackVolt'
   */
  if (EvPowertrainController2EM_U.BattPackVolt >
      EvPowertrainController2EM_P.Saturation_UpperSat) {
    rtb_Gain1_n = EvPowertrainController2EM_P.Saturation_UpperSat;
  } else if (EvPowertrainController2EM_U.BattPackVolt <
             EvPowertrainController2EM_P.Saturation_LowerSat) {
    rtb_Gain1_n = EvPowertrainController2EM_P.Saturation_LowerSat;
  } else {
    rtb_Gain1_n = EvPowertrainController2EM_U.BattPackVolt;
  }

  /* End of Saturate: '<S51>/Saturation' */
  for (i = 0; i < 201; i++) {
    /* Product: '<S81>/Product4' incorporates:
     *  Sum: '<S24>/Add2'
     */
    rtb_VectorConcatenate_j = rtb_Sqrt1[i];

    /* Math: '<S81>/Math Function1' incorporates:
     *  Constant: '<S81>/Constant1'
     *  Constant: '<S81>/Constant2'
     *  Gain: '<S81>/Gain2'
     *  Sum: '<S24>/Add2'
     *  Switch: '<S81>/Switch2'
     */
    if (rtb_VectorConcatenate_j >=
        EvPowertrainController2EM_P.Switch2_Threshold_i) {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant1_Value_m;
    } else {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant2_Value_m;
    }

    rtb_UnitDelay2 = EvPowertrainController2EM_P.Gain2_Gain_j * rtb_Divide[i];
    if ((rtb_UnitDelay2 < 0.0) && (rtb_BrkTrqReqTotal_tmp > floor
         (rtb_BrkTrqReqTotal_tmp))) {
      rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_UnitDelay2,
        rtb_BrkTrqReqTotal_tmp);
    } else {
      rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_UnitDelay2,
        rtb_BrkTrqReqTotal_tmp);
    }

    /* Sum: '<S24>/Add2' incorporates:
     *  Math: '<S81>/Math Function1'
     *  Product: '<S81>/Product4'
     */
    rtb_VectorConcatenate_j = rtb_VectorConcatenate_j * rtb_BrkTrqReqTotal_tmp +
      rtb_Product4[i];
    rtb_Sqrt1[i] = rtb_VectorConcatenate_j;

    /* Product: '<S51>/Divide' */
    rtb_Divide[i] = rtb_VectorConcatenate_j / rtb_Gain1_n;
  }

  /* Switch: '<S56>/Switch' incorporates:
   *  Constant: '<S58>/Constant'
   *  Constant: '<S59>/Constant'
   *  Fcn: '<S56>/Fcn'
   *  Inport: '<Root>/BattPackVolt'
   *  Logic: '<S56>/Logical Operator'
   *  Product: '<S56>/Product'
   *  RelationalOperator: '<S58>/Compare'
   *  RelationalOperator: '<S59>/Compare'
   *  Switch: '<S56>/Switch1'
   */
  if ((EvPowertrainController2EM_U.BattPackVolt >=
       -EvPowertrainController2EM_P.div0protectpoly_thresh) &&
      (EvPowertrainController2EM_U.BattPackVolt <=
       EvPowertrainController2EM_P.div0protectpoly_thresh)) {
    /* Switch: '<S56>/Switch1' incorporates:
     *  Constant: '<S56>/Constant'
     *  UnaryMinus: '<S56>/Unary Minus'
     */
    if (EvPowertrainController2EM_U.BattPackVolt >=
        EvPowertrainController2EM_P.Switch1_Threshold) {
      rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.Constant_Value_ag;
    } else {
      rtb_BrkTrqReqTotal_tmp = -EvPowertrainController2EM_P.Constant_Value_ag;
    }

    rtb_Gain1_n = 0.02 / (3.0 - rt_powd_snf
                          (EvPowertrainController2EM_U.BattPackVolt / 0.01, 2.0))
      * rtb_BrkTrqReqTotal_tmp;
  } else {
    rtb_Gain1_n = EvPowertrainController2EM_U.BattPackVolt;
  }

  /* End of Switch: '<S56>/Switch' */

  /* Product: '<S52>/Divide1' */
  rtb_Gain1_n = 1.0 / rtb_Gain1_n * rtb_Product1;

  /* RelationalOperator: '<S66>/Compare' incorporates:
   *  Constant: '<S66>/Constant'
   */
  rtb_Compare_n = (rtb_whlpureelectrictraction >=
                   EvPowertrainController2EM_P.Constant_Value_c);
  for (i = 0; i < 201; i++) {
    /* RelationalOperator: '<S53>/LowerRelop1' incorporates:
     *  RelationalOperator: '<S47>/Relational Operator'
     */
    rtb_VectorConcatenate_j = rtb_Divide[i];
    rtb_LogicalOperator_l = (rtb_VectorConcatenate_j > rtb_RegenFactor);
    rtb_LogicalOperator_f[i] = rtb_LogicalOperator_l;

    /* RelationalOperator: '<S53>/UpperRelop' incorporates:
     *  RelationalOperator: '<S47>/Relational Operator3'
     */
    rtb_Switch2_g_tmp_0 = (rtb_VectorConcatenate_j < rtb_Gain1_n);
    rtb_Switch2_g_tmp[i] = rtb_Switch2_g_tmp_0;

    /* Switch: '<S53>/Switch2' incorporates:
     *  RelationalOperator: '<S53>/LowerRelop1'
     *  RelationalOperator: '<S53>/UpperRelop'
     *  Switch: '<S53>/Switch'
     */
    if (rtb_LogicalOperator_l) {
      rtb_VectorConcatenate_j = rtb_RegenFactor;
    } else if (rtb_Switch2_g_tmp_0) {
      /* Switch: '<S53>/Switch' */
      rtb_VectorConcatenate_j = rtb_Gain1_n;
    }

    rtb_Divide[i] = rtb_VectorConcatenate_j;

    /* End of Switch: '<S53>/Switch2' */

    /* RelationalOperator: '<S62>/Relational Operator' */
    rtb_BrkTrqReqTotal_tmp = rtb_VectorConcatenate1[i];

    /* Logic: '<S62>/Logical Operator' incorporates:
     *  Constant: '<S65>/Constant'
     *  Logic: '<S62>/Logical Operator1'
     *  RelationalOperator: '<S62>/Relational Operator'
     *  RelationalOperator: '<S62>/Relational Operator1'
     *  RelationalOperator: '<S65>/Compare'
     */
    rtb_LogicalOperator_he[i] = ((rtb_RateLimiter_idx_0 < rtb_BrkTrqReqTotal_tmp)
      || rtb_LogicalOperator_he[i] || ((rtb_BrkTrqReqTotal_tmp <
      EvPowertrainController2EM_P.Constant_Value) && rtb_Compare_n));
  }

  /* RelationalOperator: '<S79>/Compare' incorporates:
   *  Constant: '<S79>/Constant'
   */
  rtb_Compare_n = (rtb_whlpureelectrictraction >=
                   EvPowertrainController2EM_P.Constant_Value_l);

  /* Gain: '<S24>/Veh2WhlSpd' incorporates:
   *  Gain: '<S23>/Veh2WhlSpd'
   *  Inport: '<Root>/VehSpdFdbk'
   */
  rtb_RateLimiter_idx_0 = 1.0 /
    ((EvPowertrainController2EM_P.PlntWhlLdRadiusFrnt +
      EvPowertrainController2EM_P.PlntWhlLdRadiusRear) / 2.0);
  rtb_RegenFactor = rtb_RateLimiter_idx_0 *
    EvPowertrainController2EM_U.VehSpdFdbk;

  /* Saturate: '<S24>/Saturation1' */
  if (rtb_RegenFactor > EvPowertrainController2EM_P.Saturation1_UpperSat) {
    rtb_RegenFactor = EvPowertrainController2EM_P.Saturation1_UpperSat;
  } else if (rtb_RegenFactor < EvPowertrainController2EM_P.Saturation1_LowerSat)
  {
    rtb_RegenFactor = EvPowertrainController2EM_P.Saturation1_LowerSat;
  }

  /* End of Saturate: '<S24>/Saturation1' */
  for (i = 0; i < 201; i++) {
    /* RelationalOperator: '<S75>/Relational Operator' */
    rtb_VectorConcatenate_j = rtb_VectorConcatenate_i[i];

    /* Logic: '<S75>/Logical Operator' incorporates:
     *  Constant: '<S78>/Constant'
     *  Logic: '<S75>/Logical Operator1'
     *  RelationalOperator: '<S75>/Relational Operator'
     *  RelationalOperator: '<S75>/Relational Operator1'
     *  RelationalOperator: '<S78>/Compare'
     */
    rtb_LogicalOperator_c[i] = ((rtb_RateLimiter_idx_1 < rtb_VectorConcatenate_j)
      || rtb_LogicalOperator_c[i] || ((rtb_VectorConcatenate_j <
      EvPowertrainController2EM_P.Constant_Value_h) && rtb_Compare_n));

    /* RelationalOperator: '<S47>/Relational Operator1' incorporates:
     *  RelationalOperator: '<S47>/Relational Operator'
     */
    rtb_VectorConcatenate_j = rtb_Sqrt1[i];

    /* Logic: '<S47>/Logical Operator' incorporates:
     *  RelationalOperator: '<S47>/Relational Operator'
     *  RelationalOperator: '<S47>/Relational Operator1'
     *  RelationalOperator: '<S47>/Relational Operator2'
     *  RelationalOperator: '<S47>/Relational Operator3'
     */
    rtb_LogicalOperator_f[i] = (rtb_LogicalOperator_f[i] || rtb_Switch2_g_tmp[i]
      || (rtb_VectorConcatenate_j > rtb_Product) || (rtb_VectorConcatenate_j <
      rtb_Product1));

    /* Abs: '<S24>/Abs' incorporates:
     *  Product: '<S24>/Product'
     *  Sum: '<S24>/Add'
     *  Sum: '<S24>/Add1'
     */
    rtb_VectorConcatenate_i[i] = fabs((rtb_whlpureelectrictraction -
      (rtb_Switch2[i] + rtb_Switch2_l[i])) * rtb_RegenFactor);
  }

  /* DeadZone: '<S23>/Dead Zone' incorporates:
   *  Inport: '<Root>/VehSpdFdbk'
   */
  if (EvPowertrainController2EM_U.VehSpdFdbk >
      EvPowertrainController2EM_P.DeadZone_End) {
    rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_U.VehSpdFdbk -
      EvPowertrainController2EM_P.DeadZone_End;
  } else if (EvPowertrainController2EM_U.VehSpdFdbk >=
             EvPowertrainController2EM_P.DeadZone_Start) {
    rtb_BrkTrqReqTotal_tmp = 0.0;
  } else {
    rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_U.VehSpdFdbk -
      EvPowertrainController2EM_P.DeadZone_Start;
  }

  /* Gain: '<S23>/Veh2WhlSpd' incorporates:
   *  DeadZone: '<S23>/Dead Zone'
   */
  rtb_RegenFactor = rtb_RateLimiter_idx_0 * rtb_BrkTrqReqTotal_tmp;

  /* Switch: '<S23>/Switch1' incorporates:
   *  UnitDelay: '<S23>/Unit Delay1'
   *  UnitDelay: '<S23>/Unit Delay2'
   */
  if (rtb_whlpureelectrictraction >=
      EvPowertrainController2EM_P.Switch1_Threshold_o) {
    rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_DW.UnitDelay1_DSTATE_p;
  } else {
    rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_DW.UnitDelay2_DSTATE;
  }

  /* Product: '<S46>/Product1' incorporates:
   *  Switch: '<S23>/Switch1'
   */
  rtb_Product = rtb_RegenFactor * rtb_BrkTrqReqTotal_tmp;
  for (i = 0; i < 201; i++) {
    /* Switch: '<S23>/Switch' */
    if (rtb_whlpureelectrictraction >=
        EvPowertrainController2EM_P.Switch_Threshold_k) {
      rtb_BrkTrqReqTotal_tmp = rtb_Switch2[i];
    } else {
      rtb_BrkTrqReqTotal_tmp = rtb_Switch2_l[i];
    }

    /* Sum: '<S46>/Subtract' incorporates:
     *  Product: '<S46>/Product6'
     *  Switch: '<S23>/Switch'
     */
    rtb_VectorConcatenate_j = rtb_BrkTrqReqTotal_tmp * rtb_RegenFactor -
      rtb_Product;

    /* Sqrt: '<S46>/Sqrt1' incorporates:
     *  Product: '<S46>/Product7'
     */
    rtb_Sqrt1[i] = sqrt(rtb_VectorConcatenate_j * rtb_VectorConcatenate_j);
  }

  /* Lookup_n-D: '<S46>/1-D Lookup Table' incorporates:
   *  Inport: '<Root>/AccelPdl'
   */
  rtb_RegenFactor = look1_pbinlcapw(EvPowertrainController2EM_U.AccelPdl,
    EvPowertrainController2EM_P.CtrlVcuAccelPdlBpts,
    EvPowertrainController2EM_P.CtrlVcuPwrRatePnlty,
    &EvPowertrainController2EM_DW.m_bpIndex_b, 2U);

  /* MATLAB Function: '<S23>/MATLAB Function' */
  rtb_Compare_n = true;
  i = 0;
  exitg1 = false;
  while ((!exitg1) && (i < 201)) {
    if ((!rtb_LogicalOperator_he[i]) || (!rtb_LogicalOperator_c[i]) ||
        (!rtb_LogicalOperator_f[i])) {
      rtb_Compare_n = false;
      exitg1 = true;
    } else {
      i++;
    }
  }

  if (rtb_Compare_n) {
    /* Sum: '<S23>/Add' incorporates:
     *  DataTypeConversion: '<S23>/Data Type Conversion1'
     *  Gain: '<S23>/TracPwrErr Penalty'
     *  Gain: '<S23>/W2kW '
     *  Gain: '<S23>/W2kW 1'
     *  Gain: '<S24>/Constraint Penalty Factor'
     *  Gain: '<S24>/Constraint Penalty Factor1'
     *  Gain: '<S24>/Constraint Penalty Factor2'
     *  Gain: '<S46>/W2kW'
     *  Inport: '<Root>/BattPackVolt'
     *  Product: '<S23>/Product3'
     *  Product: '<S46>/Product'
     *  Sum: '<S24>/Add4'
     */
    for (i = 0; i < 201; i++) {
      /* Gain: '<S24>/Constraint Penalty Factor2' incorporates:
       *  Product: '<S23>/Product3'
       */
      if (rtb_LogicalOperator_he[i]) {
        tmp = EvPowertrainController2EM_P.CtrlVcuEMPnlty;
      } else {
        tmp = 0;
      }

      /* Gain: '<S24>/Constraint Penalty Factor1' incorporates:
       *  Product: '<S23>/Product3'
       */
      if (rtb_LogicalOperator_c[i]) {
        tmp_0 = EvPowertrainController2EM_P.CtrlVcuEMPnlty;
      } else {
        tmp_0 = 0;
      }

      /* Gain: '<S24>/Constraint Penalty Factor' incorporates:
       *  Product: '<S23>/Product3'
       */
      if (rtb_LogicalOperator_f[i]) {
        tmp_1 = EvPowertrainController2EM_P.CtrlVcuBattPnlty;
      } else {
        tmp_1 = 0U;
      }

      rtb_VectorConcatenate1[i] = (((real_T)((((uint32_T)tmp << 7) + ((uint32_T)
        tmp_0 << 7)) + tmp_1) * 0.00390625 +
        EvPowertrainController2EM_U.BattPackVolt * rtb_Divide[i] *
        EvPowertrainController2EM_P.W2kW_Gain) +
        EvPowertrainController2EM_P.W2kW1_Gain * rtb_VectorConcatenate_i[i] *
        EvPowertrainController2EM_P.CtrlVcuTracPwrErrPnlty) +
        EvPowertrainController2EM_P.W2kW_Gain_a * rtb_Sqrt1[i] * rtb_RegenFactor;
    }

    EvPowertrainController2_minimum(rtb_VectorConcatenate1, &rtb_Product, &i);
    rtb_Product = i;
  } else {
    /* Sum: '<S23>/Add' incorporates:
     *  DataTypeConversion: '<S23>/Data Type Conversion1'
     *  Gain: '<S23>/TracPwrErr Penalty'
     *  Gain: '<S23>/W2kW '
     *  Gain: '<S23>/W2kW 1'
     *  Gain: '<S24>/Constraint Penalty Factor'
     *  Gain: '<S24>/Constraint Penalty Factor1'
     *  Gain: '<S24>/Constraint Penalty Factor2'
     *  Gain: '<S46>/W2kW'
     *  Inport: '<Root>/BattPackVolt'
     *  Product: '<S23>/Product3'
     *  Product: '<S46>/Product'
     *  Sum: '<S24>/Add4'
     */
    for (i = 0; i < 201; i++) {
      /* Gain: '<S24>/Constraint Penalty Factor2' incorporates:
       *  Product: '<S23>/Product3'
       */
      if (rtb_LogicalOperator_he[i]) {
        tmp = EvPowertrainController2EM_P.CtrlVcuEMPnlty;
      } else {
        tmp = 0;
      }

      /* Gain: '<S24>/Constraint Penalty Factor1' incorporates:
       *  Product: '<S23>/Product3'
       */
      if (rtb_LogicalOperator_c[i]) {
        tmp_0 = EvPowertrainController2EM_P.CtrlVcuEMPnlty;
      } else {
        tmp_0 = 0;
      }

      /* Gain: '<S24>/Constraint Penalty Factor' incorporates:
       *  Product: '<S23>/Product3'
       */
      if (rtb_LogicalOperator_f[i]) {
        tmp_1 = EvPowertrainController2EM_P.CtrlVcuBattPnlty;
      } else {
        tmp_1 = 0U;
      }

      rtb_VectorConcatenate1[i] = (((real_T)((((uint32_T)tmp << 7) + ((uint32_T)
        tmp_0 << 7)) + tmp_1) * 0.00390625 +
        EvPowertrainController2EM_U.BattPackVolt * rtb_Divide[i] *
        EvPowertrainController2EM_P.W2kW_Gain) +
        EvPowertrainController2EM_P.W2kW1_Gain * rtb_VectorConcatenate_i[i] *
        EvPowertrainController2EM_P.CtrlVcuTracPwrErrPnlty) +
        EvPowertrainController2EM_P.W2kW_Gain_a * rtb_Sqrt1[i] * rtb_RegenFactor;
    }

    EvPowertrainController2_minimum(rtb_VectorConcatenate1, &rtb_Product, &i);
    rtb_Product = i;
  }

  /* End of MATLAB Function: '<S23>/MATLAB Function' */

  /* MultiPortSwitch: '<S23>/Index Vector' incorporates:
   *  MultiPortSwitch: '<S23>/Index Vector1'
   */
  i = (int32_T)rtb_Product - 1;
  rtb_RateLimiter_idx_0 = rtb_Switch2[i];

  /* MultiPortSwitch: '<S23>/Index Vector1' */
  rtb_Product = rtb_Switch2_l[i];

  /* Sum: '<S36>/Add1' incorporates:
   *  MultiPortSwitch: '<S23>/Index Vector'
   *  MultiPortSwitch: '<S23>/Index Vector1'
   */
  rtb_UnitDelay2 = rtb_RateLimiter_idx_0 + rtb_Product;

  /* Saturate: '<S36>/Negative 1' */
  if (rtb_UnitDelay2 > EvPowertrainController2EM_P.Negative1_UpperSat) {
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Negative1_UpperSat;
  } else if (rtb_UnitDelay2 < EvPowertrainController2EM_P.Negative1_LowerSat) {
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Negative1_LowerSat;
  }

  /* Sum: '<S36>/Subtract' incorporates:
   *  Saturate: '<S36>/Negative 1'
   */
  rtb_UnitDelay2 += rtb_BrkTrqReqTotal;

  /* Saturate: '<S36>/Negative 5' */
  if (rtb_UnitDelay2 > EvPowertrainController2EM_P.Negative5_UpperSat) {
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Negative5_UpperSat;
  } else if (rtb_UnitDelay2 < EvPowertrainController2EM_P.Negative5_LowerSat) {
    rtb_UnitDelay2 = EvPowertrainController2EM_P.Negative5_LowerSat;
  }

  /* Gain: '<S36>/Gain6' incorporates:
   *  Constant: '<S36>/Constant1'
   *  Product: '<S36>/Product4'
   *  Saturate: '<S36>/Negative 5'
   */
  rtb_BrkTrqReqTotal = rtb_UnitDelay2 /
    ((EvPowertrainController2EM_P.PlntBrkFrntBias *
      EvPowertrainController2EM_P.PlntBrkKinFricCffFrnt * 3.1415926535897931 *
      0.0025000000000000005 *
      EvPowertrainController2EM_P.PlntBrkPadMeanRadiusFrnt *
      EvPowertrainController2EM_P.PlntBrkNumPadsFrnt / 4.0 +
      EvPowertrainController2EM_P.PlntBrkRearBias *
      EvPowertrainController2EM_P.PlntBrkKinFricCffRear * 3.1415926535897931 *
      0.0025000000000000005 *
      EvPowertrainController2EM_P.PlntBrkPadMeanRadiusRear *
      EvPowertrainController2EM_P.PlntBrkNumPadsRear / 4.0) * 2.0) * (1.0 /
    EvPowertrainController2EM_P.PlntBrkPrsFctr);

  /* Saturate: '<S36>/Saturation' */
  if (rtb_BrkTrqReqTotal > EvPowertrainController2EM_P.Saturation_UpperSat_n) {
    rtb_BrkTrqReqTotal = EvPowertrainController2EM_P.Saturation_UpperSat_n;
  } else if (rtb_BrkTrqReqTotal <
             EvPowertrainController2EM_P.Saturation_LowerSat_j) {
    rtb_BrkTrqReqTotal = EvPowertrainController2EM_P.Saturation_LowerSat_j;
  }

  /* End of Saturate: '<S36>/Saturation' */

  /* Switch: '<S43>/Switch2' incorporates:
   *  Constant: '<S43>/Constant1'
   *  Constant: '<S43>/Constant2'
   *  Inport: '<Root>/EMSpd'
   *  Product: '<S43>/Product1'
   *  SignalConversion generated from: '<S25>/Vector Concatenate1'
   *  UnitDelay: '<S42>/Unit Delay'
   */
  if (EvPowertrainController2EM_DW.UnitDelay_DSTATE_l *
      EvPowertrainController2EM_U.EMSpd[0] >=
      EvPowertrainController2EM_P.Switch2_Threshold_py) {
    rtb_RegenFactor = EvPowertrainController2EM_P.Constant1_Value_h;
  } else {
    rtb_RegenFactor = EvPowertrainController2EM_P.Constant2_Value_o;
  }

  /* End of Switch: '<S43>/Switch2' */

  /* Math: '<S43>/Math Function1' */
  if ((rtb_WhlEMTrqMax_tmp < 0.0) && (rtb_RegenFactor > floor(rtb_RegenFactor)))
  {
    rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp, rtb_RegenFactor);
  } else {
    rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp, rtb_RegenFactor);
  }

  /* Product: '<S42>/Divide2' incorporates:
   *  Gain: '<S42>/Gain3'
   *  Math: '<S43>/Math Function1'
   */
  rtb_Product1 = rtb_RateLimiter_idx_0_tmp * rtb_RateLimiter_idx_0 * (1.0 /
    rtb_BrkTrqReqTotal_tmp);

  /* Switch: '<S44>/Switch2' incorporates:
   *  Constant: '<S44>/Constant1'
   *  Constant: '<S44>/Constant2'
   *  Inport: '<Root>/EMSpd'
   *  Product: '<S44>/Product1'
   *  SignalConversion generated from: '<S25>/Vector Concatenate1'
   *  UnitDelay: '<S42>/Unit Delay1'
   */
  if (EvPowertrainController2EM_DW.UnitDelay1_DSTATE_o *
      EvPowertrainController2EM_U.EMSpd[1] >=
      EvPowertrainController2EM_P.Switch2_Threshold_o) {
    rtb_RegenFactor = EvPowertrainController2EM_P.Constant1_Value_j;
  } else {
    rtb_RegenFactor = EvPowertrainController2EM_P.Constant2_Value_h;
  }

  /* End of Switch: '<S44>/Switch2' */

  /* Math: '<S44>/Math Function1' */
  if ((rtb_WhlEMTrqMax_tmp_0 < 0.0) && (rtb_RegenFactor > floor(rtb_RegenFactor)))
  {
    rtb_BrkTrqReqTotal_tmp = -rt_powd_snf(-rtb_WhlEMTrqMax_tmp_0,
      rtb_RegenFactor);
  } else {
    rtb_BrkTrqReqTotal_tmp = rt_powd_snf(rtb_WhlEMTrqMax_tmp_0, rtb_RegenFactor);
  }

  /* Product: '<S42>/Divide1' incorporates:
   *  Gain: '<S42>/Gain1'
   *  Math: '<S44>/Math Function1'
   */
  rtb_Gain1_n = rtb_RateLimiter_idx_1_tmp * rtb_Product * (1.0 /
    rtb_BrkTrqReqTotal_tmp);

  /* Update for UnitDelay: '<S69>/Unit Delay' */
  memcpy(&EvPowertrainController2EM_DW.UnitDelay_DSTATE[0], &rtb_Divide2_p[0],
         201U * sizeof(real_T));

  /* Update for UnitDelay: '<S24>/Unit Delay' */
  memcpy(&EvPowertrainController2EM_DW.UnitDelay_DSTATE_p[0], &rtb_Switch2_l[0],
         201U * sizeof(real_T));

  /* Update for UnitDelay: '<S24>/Unit Delay1' */
  memcpy(&EvPowertrainController2EM_DW.UnitDelay1_DSTATE[0], &rtb_Switch2[0],
         201U * sizeof(real_T));

  /* Update for UnitDelay: '<S82>/Unit Delay' */
  memcpy(&EvPowertrainController2EM_DW.UnitDelay_DSTATE_n[0], &rtb_Divide2_ir[0],
         201U * sizeof(real_T));

  /* Update for UnitDelay: '<S23>/Unit Delay1' */
  EvPowertrainController2EM_DW.UnitDelay1_DSTATE_p = rtb_RateLimiter_idx_0;

  /* Update for UnitDelay: '<S23>/Unit Delay2' */
  EvPowertrainController2EM_DW.UnitDelay2_DSTATE = rtb_Product;

  /* Update for UnitDelay: '<S42>/Unit Delay' */
  EvPowertrainController2EM_DW.UnitDelay_DSTATE_l = rtb_Product1;

  /* Update for UnitDelay: '<S42>/Unit Delay1' */
  EvPowertrainController2EM_DW.UnitDelay1_DSTATE_o = rtb_Gain1_n;

  /* End of Outputs for SubSystem: '<Root>/Energy Management' */

  /* RateLimiter: '<Root>/Rate Limiter' incorporates:
   *  SignalConversion generated from: '<S42>/Vector Concatenate1'
   */
  rtb_BrkTrqReqTotal_tmp = EvPowertrainController2EM_P.CtrlVcuRiseRate *
    EvPowertrainController2E_period;
  rtb_WhlEMTrqMax_tmp = EvPowertrainController2EM_P.CtrlVcuFallRate *
    EvPowertrainController2E_period;

  /* Outputs for Atomic SubSystem: '<Root>/Energy Management' */
  rtb_WhlEMTrqMax_tmp_0 = rtb_Product1 - EvPowertrainController2EM_DW.PrevY[0];

  /* End of Outputs for SubSystem: '<Root>/Energy Management' */
  if (rtb_WhlEMTrqMax_tmp_0 > rtb_BrkTrqReqTotal_tmp) {
    rtb_WhlEMTrqMax_tmp_0 = EvPowertrainController2EM_DW.PrevY[0] +
      rtb_BrkTrqReqTotal_tmp;
  } else if (rtb_WhlEMTrqMax_tmp_0 < rtb_WhlEMTrqMax_tmp) {
    rtb_WhlEMTrqMax_tmp_0 = EvPowertrainController2EM_DW.PrevY[0] +
      rtb_WhlEMTrqMax_tmp;
  } else {
    /* Outputs for Atomic SubSystem: '<Root>/Energy Management' */
    rtb_WhlEMTrqMax_tmp_0 = rtb_Product1;

    /* End of Outputs for SubSystem: '<Root>/Energy Management' */
  }

  EvPowertrainController2EM_DW.PrevY[0] = rtb_WhlEMTrqMax_tmp_0;

  /* Outport: '<Root>/EMTrqCmd' */
  EvPowertrainController2EM_Y.EMTrqCmd[0] = rtb_WhlEMTrqMax_tmp_0;

  /* Outputs for Atomic SubSystem: '<Root>/Energy Management' */
  /* RateLimiter: '<Root>/Rate Limiter' incorporates:
   *  SignalConversion generated from: '<S42>/Vector Concatenate1'
   */
  rtb_WhlEMTrqMax_tmp_0 = rtb_Gain1_n - EvPowertrainController2EM_DW.PrevY[1];

  /* End of Outputs for SubSystem: '<Root>/Energy Management' */
  if (rtb_WhlEMTrqMax_tmp_0 > rtb_BrkTrqReqTotal_tmp) {
    rtb_WhlEMTrqMax_tmp_0 = EvPowertrainController2EM_DW.PrevY[1] +
      rtb_BrkTrqReqTotal_tmp;
  } else if (rtb_WhlEMTrqMax_tmp_0 < rtb_WhlEMTrqMax_tmp) {
    rtb_WhlEMTrqMax_tmp_0 = EvPowertrainController2EM_DW.PrevY[1] +
      rtb_WhlEMTrqMax_tmp;
  } else {
    /* Outputs for Atomic SubSystem: '<Root>/Energy Management' */
    rtb_WhlEMTrqMax_tmp_0 = rtb_Gain1_n;

    /* End of Outputs for SubSystem: '<Root>/Energy Management' */
  }

  EvPowertrainController2EM_DW.PrevY[1] = rtb_WhlEMTrqMax_tmp_0;

  /* Outport: '<Root>/EMTrqCmd' */
  EvPowertrainController2EM_Y.EMTrqCmd[1] = rtb_WhlEMTrqMax_tmp_0;

  /* Outport: '<Root>/VcuBrkPrsCmd' */
  EvPowertrainController2EM_Y.VcuBrkPrsCmd[0] = rtb_BrkTrqReqTotal;
  EvPowertrainController2EM_Y.VcuBrkPrsCmd[1] = rtb_BrkTrqReqTotal;
  EvPowertrainController2EM_Y.VcuBrkPrsCmd[2] = rtb_BrkTrqReqTotal;
  EvPowertrainController2EM_Y.VcuBrkPrsCmd[3] = rtb_BrkTrqReqTotal;

  /* Gain: '<S7>/Gain1' incorporates:
   *  Product: '<S7>/Product'
   *  Sum: '<S7>/Sum'
   */
  rtb_Gain1_n = (((rtb_BrkTrqReqTotal + rtb_BrkTrqReqTotal) + rtb_BrkTrqReqTotal)
                 + rtb_BrkTrqReqTotal) / EvPowertrainController2EM_B.Probe *
    EvPowertrainController2EM_P.CtrlBcuTrlrBrkGain;

  /* Outport: '<Root>/VcuTrlrBrkPrsCmd' */
  EvPowertrainController2EM_Y.VcuTrlrBrkPrsCmd[0] = rtb_Gain1_n;
  EvPowertrainController2EM_Y.VcuTrlrBrkPrsCmd[1] = rtb_Gain1_n;
  EvPowertrainController2EM_Y.VcuTrlrBrkPrsCmd[2] = rtb_Gain1_n;
  EvPowertrainController2EM_Y.VcuTrlrBrkPrsCmd[3] = rtb_Gain1_n;
  EvPowertrainController2EM_Y.VcuTrlrBrkPrsCmd[4] = rtb_Gain1_n;
  EvPowertrainController2EM_Y.VcuTrlrBrkPrsCmd[5] = rtb_Gain1_n;

  /* Outport: '<Root>/Cltch1Cmd' incorporates:
   *  Constant: '<Root>/Constant2'
   */
  EvPowertrainController2EM_Y.Cltch1Cmd =
    EvPowertrainController2EM_P.Constant2_Value_f;

  /* Outport: '<Root>/Neutral' incorporates:
   *  Constant: '<Root>/Constant3'
   */
  EvPowertrainController2EM_Y.Neutral =
    EvPowertrainController2EM_P.Constant3_Value;

  /* Outport: '<Root>/FuelCellCurrCmd' incorporates:
   *  Constant: '<Root>/Constant4'
   */
  EvPowertrainController2EM_Y.FuelCellCurrCmd =
    EvPowertrainController2EM_P.Constant4_Value;

  /* Outport: '<Root>/FuelCellTempCmd' incorporates:
   *  Constant: '<Root>/Constant5'
   */
  EvPowertrainController2EM_Y.FuelCellTempCmd =
    EvPowertrainController2EM_P.Constant5_Value;

  /* Matfile logging */
  rt_UpdateTXYLogVars(EvPowertrainController2EM_M->rtwLogInfo,
                      (&EvPowertrainController2EM_M->Timing.taskTime0));

  /* signal main to stop simulation */
  {                                    /* Sample time: [0.01s, 0.0s] */
    if ((rtmGetTFinal(EvPowertrainController2EM_M)!=-1) &&
        !((rtmGetTFinal(EvPowertrainController2EM_M)-
           EvPowertrainController2EM_M->Timing.taskTime0) >
          EvPowertrainController2EM_M->Timing.taskTime0 * (DBL_EPSILON))) {
      rtmSetErrorStatus(EvPowertrainController2EM_M, "Simulation finished");
    }
  }

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   * Timer of this task consists of two 32 bit unsigned integers.
   * The two integers represent the low bits Timing.clockTick0 and the high bits
   * Timing.clockTickH0. When the low bit overflows to 0, the high bits increment.
   */
  if (!(++EvPowertrainController2EM_M->Timing.clockTick0)) {
    ++EvPowertrainController2EM_M->Timing.clockTickH0;
  }

  EvPowertrainController2EM_M->Timing.taskTime0 =
    EvPowertrainController2EM_M->Timing.clockTick0 *
    EvPowertrainController2EM_M->Timing.stepSize0 +
    EvPowertrainController2EM_M->Timing.clockTickH0 *
    EvPowertrainController2EM_M->Timing.stepSize0 * 4294967296.0;
}

/* Model initialize function */
void EvPowertrainController2EM_initialize(void)
{
  /* Registration code */

  /* initialize real-time model */
  (void) memset((void *)EvPowertrainController2EM_M, 0,
                sizeof(RT_MODEL_EvPowertrainControll_T));
  rtmSetTFinal(EvPowertrainController2EM_M, 10.0);
  EvPowertrainController2EM_M->Timing.stepSize0 = 0.01;

  /* Setup for data logging */
  {
    static RTWLogInfo rt_DataLoggingInfo;
    rt_DataLoggingInfo.loggingInterval = (NULL);
    EvPowertrainController2EM_M->rtwLogInfo = &rt_DataLoggingInfo;
  }

  /* Setup for data logging */
  {
    rtliSetLogXSignalInfo(EvPowertrainController2EM_M->rtwLogInfo, (NULL));
    rtliSetLogXSignalPtrs(EvPowertrainController2EM_M->rtwLogInfo, (NULL));
    rtliSetLogT(EvPowertrainController2EM_M->rtwLogInfo, "tout");
    rtliSetLogX(EvPowertrainController2EM_M->rtwLogInfo, "");
    rtliSetLogXFinal(EvPowertrainController2EM_M->rtwLogInfo, "");
    rtliSetLogVarNameModifier(EvPowertrainController2EM_M->rtwLogInfo, "rt_");
    rtliSetLogFormat(EvPowertrainController2EM_M->rtwLogInfo, 4);
    rtliSetLogMaxRows(EvPowertrainController2EM_M->rtwLogInfo, 0);
    rtliSetLogDecimation(EvPowertrainController2EM_M->rtwLogInfo, 1);
    rtliSetLogY(EvPowertrainController2EM_M->rtwLogInfo, "");
    rtliSetLogYSignalInfo(EvPowertrainController2EM_M->rtwLogInfo, (NULL));
    rtliSetLogYSignalPtrs(EvPowertrainController2EM_M->rtwLogInfo, (NULL));
  }

  /* block I/O */
  (void) memset(((void *) &EvPowertrainController2EM_B), 0,
                sizeof(B_EvPowertrainController2EM_T));

  /* states (dwork) */
  (void) memset((void *)&EvPowertrainController2EM_DW, 0,
                sizeof(DW_EvPowertrainController2EM_T));

  /* external inputs */
  (void)memset(&EvPowertrainController2EM_U, 0, sizeof
               (ExtU_EvPowertrainController2E_T));

  /* external outputs */
  (void)memset(&EvPowertrainController2EM_Y, 0, sizeof
               (ExtY_EvPowertrainController2E_T));

  /* Matfile logging */
  rt_StartDataLoggingWithStartTime(EvPowertrainController2EM_M->rtwLogInfo, 0.0,
    rtmGetTFinal(EvPowertrainController2EM_M),
    EvPowertrainController2EM_M->Timing.stepSize0, (&rtmGetErrorStatus
    (EvPowertrainController2EM_M)));

  /* Start for Probe: '<S7>/Probe' */
  EvPowertrainController2EM_B.Probe = 4.0;

  {
    int32_T i;

    /* InitializeConditions for RateLimiter: '<Root>/Rate Limiter' */
    EvPowertrainController2EM_DW.PrevY[0] =
      EvPowertrainController2EM_P.RateLimiter_IC;
    EvPowertrainController2EM_DW.PrevY[1] =
      EvPowertrainController2EM_P.RateLimiter_IC;

    /* SystemInitialize for Atomic SubSystem: '<Root>/Energy Management' */
    for (i = 0; i < 201; i++) {
      /* InitializeConditions for UnitDelay: '<S69>/Unit Delay' */
      EvPowertrainController2EM_DW.UnitDelay_DSTATE[i] =
        EvPowertrainController2EM_P.UnitDelay_InitialCondition;

      /* InitializeConditions for UnitDelay: '<S24>/Unit Delay' */
      EvPowertrainController2EM_DW.UnitDelay_DSTATE_p[i] =
        EvPowertrainController2EM_P.UnitDelay_InitialCondition_o;

      /* InitializeConditions for UnitDelay: '<S24>/Unit Delay1' */
      EvPowertrainController2EM_DW.UnitDelay1_DSTATE[i] =
        EvPowertrainController2EM_P.UnitDelay1_InitialCondition;

      /* InitializeConditions for UnitDelay: '<S82>/Unit Delay' */
      EvPowertrainController2EM_DW.UnitDelay_DSTATE_n[i] =
        EvPowertrainController2EM_P.UnitDelay_InitialCondition_a;
    }

    /* InitializeConditions for UnitDelay: '<S23>/Unit Delay1' */
    EvPowertrainController2EM_DW.UnitDelay1_DSTATE_p =
      EvPowertrainController2EM_P.UnitDelay1_InitialCondition_m;

    /* InitializeConditions for UnitDelay: '<S23>/Unit Delay2' */
    EvPowertrainController2EM_DW.UnitDelay2_DSTATE =
      EvPowertrainController2EM_P.UnitDelay2_InitialCondition;

    /* InitializeConditions for UnitDelay: '<S42>/Unit Delay' */
    EvPowertrainController2EM_DW.UnitDelay_DSTATE_l =
      EvPowertrainController2EM_P.UnitDelay_InitialCondition_p;

    /* InitializeConditions for UnitDelay: '<S42>/Unit Delay1' */
    EvPowertrainController2EM_DW.UnitDelay1_DSTATE_o =
      EvPowertrainController2EM_P.UnitDelay1_InitialCondition_a;

    /* End of SystemInitialize for SubSystem: '<Root>/Energy Management' */
  }
}

/* Model terminate function */
void EvPowertrainController2EM_terminate(void)
{
  /* (no terminate code required) */
}
