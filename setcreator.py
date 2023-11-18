import argparse
import random

def generate_dataset(size):
    """Generate a dataset with the specified number of random integers."""
    return [random.randint(1, 1000) for _ in range(size)]

def save_dataset(dataset, file_path):
    """Save the generated dataset to a file."""
    with open(file_path, 'w') as file:
        for number in dataset:
            file.write(f"{number}\n")

def main():
    parser = argparse.ArgumentParser(
        description='Generate a dataset with a specified number of random integers.')
    parser.add_argument('-d', '--data', type=int, required=True, 
                        help='Number of data points to generate')
    parser.add_argument('-o', '--output', type=str, default='dataset.txt',
                        help='Output file name for the generated dataset')
    
    args = parser.parse_args()
    dataset = generate_dataset(args.data)
    save_dataset(dataset, args.output)
    print(f"Dataset with {args.data} data points has been saved to {args.output}")

if __name__ == "__main__":
    main()
