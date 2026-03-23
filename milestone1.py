import pandas as pd
import re
import string

# Define a basic set of stopwords
STOPWORDS = {
    "is", "the", "and", "a", "an", "to", "of", "in", "on", "for", "with", "this",
    "that", "it", "was", "are", "as", "at", "be", "by", "from", "or", "but","i","am","feel"
}

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r"http\S+", "", text)
    # Remove numbers
    text = re.sub(r"\d+", "", text)
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    # Remove stopwords
    words = [w for w in text.split() if w not in STOPWORDS]
    return " ".join(words)

def main():
    #  Removed leading space and ensured path matches the CSV generated earlier
    input_file = r"C:\Infosys_springboard\ReviewSense_Customer_Feedback_5000.csv"
    output_file = "Milestone1_Cleaned_Feedback.csv"

    try:
        print(f"Attempting to read: {input_file}")
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print("Input file not found. Checking for existing cleaned file...")
        try:
            df = pd.read_csv(output_file)
            if "clean_feedback" in df.columns:
                print("Cleaned file already exists. Preview:")
                print(df[["feedback", "clean_feedback"]].head())
                return
        except FileNotFoundError:
            print("❌ No data files found. Please run the data generation script first.")
            return

    # Ensure feedback column exists
    if "feedback" not in df.columns:
        print("❌ Error: 'feedback' column not found in the dataset.")
        return

    print("Cleaning feedback text...")
    df["clean_feedback"] = df["feedback"].apply(clean_text)

    # Save the cleaned data
    df.to_csv(output_file, index=False)

    print("✅ Milestone 1 completed successfully!")
    print("\nSample of cleaned data:")
    print(df[["feedback", "clean_feedback"]].head())

if __name__ == "__main__":
    main()