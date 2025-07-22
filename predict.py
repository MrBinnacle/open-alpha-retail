import argparse
from models.baseline_model import BaselineETHModel

def main():
    parser = argparse.ArgumentParser(description='Predict ETH price based on stETH supply.')
    parser.add_argument('supply', type=float, help='stETH supply value')
    parser.add_argument('--model', type=str, default='models/baseline_model.pkl', help='Path to trained model file')

    args = parser.parse_args()

    model = BaselineETHModel()
    model.load(args.model)

    prediction = model.predict(args.supply)
    print(f"Predicted ETH price: ${prediction:,.2f}")

if __name__ == '__main__':
    main()
