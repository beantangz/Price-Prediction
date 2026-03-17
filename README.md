# Price Prediction
## Description

This project consists of implementing a **simple linear regression** to predict the price of a car based on its mileage.

The model used is:

    estimate_price(mileage) = theta0 + theta1 * mileage

---

## How it works

The project contains two programs:

### 1. train.py

- Reads the dataset from `data.csv`
- Trains the model using **gradient descent**
- Computes `theta0` and `theta1`
- Saves the results in `theta.json`

### 2. predict.py

- Prompts the user for a mileage
- Uses `theta0` and `theta1`
- Returns the estimated price

---

## Method

### Cost function

    J(theta0, theta1) = (1/m) * Σ (prediction - price)^2

### Parameters update

    theta0 -= learning_rate * (1/m) * Σ (prediction - price)
    theta1 -= learning_rate * (1/m) * Σ (prediction - price) * mileage

---

## Normalization

To improve convergence:

    x_norm = (x - mean) / std

After training, we convert back to the original scale:

    theta1 = theta1 / std
    theta0 = theta0 - theta1 * mean

---

## Usage

### Train the model

    python train.py

### Predict a price

    python predict.py

---

## Dataset format

    km,price
    240000,3650
    139800,3800
    ...

---

## Important notes

- Always normalize the data
- Update theta0 and theta1 simultaneously
- Use a proper learning rate (e.g. 0.01)
- Avoid NaN (usually caused by bad normalization)

---

## Objectives

- Understand linear regression
- Implement gradient descent
- Work with CSV data
