import json

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def load_theta():
    try:
        with open("theta.json", "r") as f:
            data = json.load(f)
            return data["theta0"], data["theta1"]
    except:
        return 0, 0


def main():
    theta0, theta1 = load_theta()

    mileage = float(input("Enter mileage: "))

    price = estimate_price(mileage, theta0, theta1)

    print(f"Estimated price: {price}")


if __name__ == "__main__":
    main()