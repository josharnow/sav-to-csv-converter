# SOURCE - https://www.reddit.com/r/learnpython/comments/1jj5t2s/comment/mjktp8d/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
import pandas as pd 
import pyreadstat

def main():
    def convert_sav_to_csv(input_path: str = "input.sav", output_path: str = "output.csv"):
        """
        Convert a .sav file to .csv format.
        """

        df, meta = pyreadstat.read_sav(input_path) # Read the .sav file
        df.to_csv(output_path, index=False) # Save to .csv

        return df, meta
    def save_metadata(meta, output_path: str):
        """
        Save metadata to a text file.
        """
        with open(output_path.replace('.csv', '_metadata.txt'), 'w', encoding="utf-8") as f:
        #     f.write(str(meta))
            f.write("Variable Names and Labels:\n") 
            for var in meta.column_names_to_labels:
                f.write(f"{var}: {meta.column_names_to_labels[var]}\n")

    input_path = input("Enter the path to the .sav file (default: input.sav): ")
    output_path = input("Enter the path to save the .csv file (default: output.csv): ")

    df, meta = convert_sav_to_csv(input_path, output_path)

    save_metadata(meta, output_path)

    print("Conversion complete! CSV and metadata saved.")

if __name__ == "__main__":
    main()