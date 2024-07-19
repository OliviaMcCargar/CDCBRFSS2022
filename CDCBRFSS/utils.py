import os

project_dir = os.path.join(os.path.dirname( __file__ ), os.path.pardir)
raw_data_2022_dir = os.path.join(project_dir, 'data', 'raw', '2022')

def main():
    print(raw_data_2022_dir)

if __name__ == "__main__":
    main()