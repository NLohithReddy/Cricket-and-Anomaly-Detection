# Cricket Anomaly Detection

This repository contains Python code for detecting anomalies in cricket match data using Isolation Forest.

## Overview

The provided Python script uses the Isolation Forest algorithm from scikit-learn to detect anomalies in a cricket match dataset. Anomalies are identified as data points that deviate significantly from the norm, such as unusually high or low runs scored in specific overs.

## Dependencies

- pandas
- scikit-learn
- numpy

## Usage

**Dataset Preparation:**

   Ensure you have a CSV file named `cricket_scores.csv` containing columns 'Overs' and 'Runs_Scored' representing the overs and cumulative runs scored.

## Explanantion

In this specific scenario, the code is conducting a one-sample t-test to evaluate whether the mean of the 'marks_data' significantly differs from the expected mean of 70.

In hypothesis testing, there are typically two hypotheses:

Null Hypothesis (H₀): States there is no significant difference or relationship between variables. In this case, the null hypothesis could be that the mean of 'marks_data' is equal to the expected mean of 70.

Alternate Hypothesis (H₁ or Ha): Contradicts the null hypothesis. It asserts that there is a significant difference or relationship between variables. In this case, the alternate hypothesis would be that the mean of 'marks_data' is different from the expected mean of 70.

The code evaluates the p-value resulting from the t-test. If the p-value is less than the predefined alpha level (0.05 in this case), it rejects the null hypothesis. The printed statement, "Null hypothesis rejected, The mean significantly deviates from the expected value," corresponds to accepting the alternate hypothesis, implying that there's significant evidence to suggest that the mean is different from the expected value of 70.

