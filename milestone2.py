import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

def get_sentiment(text):
    # Polarity ranges from -1 (Negative) to +1 (Positive)
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0:
        return "positive", polarity
    elif polarity < 0:
        return "negative", polarity
    else:
        return "neutral", polarity

if __name__ == "__main__":
    # Ensure the filename matches Milestone 1 exactly
    try:
        df = pd.read_csv("Milestone1_Cleaned_Feedback.csv")
    except FileNotFoundError:
        print("❌ Could not find Milestone1_Cleaned_Feedback.csv. Please run Milestone 1 first.")
        exit()

    print("Analyzing sentiment...")
    # Creating sentiment and confidence_score columns
    df[["sentiment", "confidence_score"]] = df["clean_feedback"].apply(
        lambda x: pd.Series(get_sentiment(x))
    )

    # Save the new dataset
    output_csv = "Milestone2_Sentiment_Results_new.csv"
    df.to_csv(output_csv, index=False)
    print(f"✅ Milestone 2 completed successfully! Saved to {output_csv}")

    # --- Visualization ---
    sentiment_counts = df['sentiment'].value_counts()
    
    # Map colors specifically to the categories present
    color_map = {'positive': 'green', 'negative': 'red', 'neutral': 'gray'}
    current_colors = [color_map.get(label, 'blue') for label in sentiment_counts.index]

    plt.figure(figsize=(8, 5))
    sentiment_counts.plot(kind='bar', color=current_colors)
    
    plt.title('How Customers Feel - Sentiment Summary', fontsize=14)
    plt.xlabel('Sentiment Category', fontsize=12)
    plt.ylabel('Number of Reviews', fontsize=12)
    plt.xticks(rotation=0)

    # Add count labels on top of bars
    for i, count in enumerate(sentiment_counts):
        plt.text(i, count + 20, str(count), ha='center', fontsize=11, fontweight='bold')

    plt.savefig('sentiment_bar_chart.png', dpi=100, bbox_inches='tight')
    print("📈 Bar chart saved as: sentiment_bar_chart.png")
    
    # Display preview
    print("\nPreview of Results:")
    print(df[["clean_feedback", "sentiment", "confidence_score"]].head())
    plt.show()