from datasets import load_dataset, get_dataset_split_names

if __name__ == "__main__":
    #ds_split_name = get_dataset_split_names("imdb")
    dataset = load_dataset("rotten_tomatoes", split="train")
    print(dataset)
