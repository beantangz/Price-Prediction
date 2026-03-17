import csv
import json

def load_data(filename):
    mileage = []
    price = []

    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            mileage.append(float(row["km"]))
            price.append(float(row["price"]))

    return mileage, price


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def mean_std(values):
    m = len(values)
    mean = sum(values)/m
    std = (sum((v - mean)**2 for v in values)/m)**0.5
    return mean, std

def train(mileage, price, learning_rate=0.1, iterations=10000):
    theta0 = 0
    theta1 = 0

    m = len(mileage)

    # normalisation avant la boucle
    mean_m, std_m = mean_std(mileage)
    x = [(v - mean_m)/std_m for v in mileage]
    y = price[:]

    for _ in range(iterations):
        tmp_theta0 = 0
        tmp_theta1 = 0

        for i in range(m):
            prediction = theta0 + theta1 * x[i]
            error = prediction - y[i]

            tmp_theta0 += error
            tmp_theta1 += error * x[i]

        tmp_theta0 = learning_rate * tmp_theta0 / m
        tmp_theta1 = learning_rate * tmp_theta1 / m

        # mise à jour simultanée
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    # renormalisation finale
    theta1 = theta1 / std_m
    theta0 = theta0 - theta1 * mean_m

    return theta0, theta1

def save_theta(theta0, theta1):
    with open("theta.json", "w") as f:
        json.dump({"theta0": theta0, "theta1": theta1}, f)

def main():
    mileage, price = load_data("data.csv")
    theta0, theta1 = train(mileage, price, learning_rate=0.01, iterations=50000)
    save_theta(theta0, theta1)
    print("Training finished")
    print("theta0 =", theta0)
    print("theta1 =", theta1)

if __name__ == "__main__":
    main()