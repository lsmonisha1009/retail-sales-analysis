import pandas as pd

def compute_total_revenue(df):
    """Calculates gross revenue generated across all transactions."""
    return df['Total_Amount'].sum()

def get_top_performing_categories(df, top_n=3):
    """Identifies product categories generating the highest sales revenue."""
    category_summary = df.groupby('Product_Category')['Total_Amount'].sum()
    return category_summary.sort_values(ascending=False).head(top_n)

if __name__ == "__main__":
    # Test dataset to verify logic execution
    sample_data = {
        'Transaction_ID':,
        'Date': ['2026-11-01', '2026-11-02', '2026-11-02', '2026-11-03'],
        'Product_Category': ['Electronics', 'Clothing', 'Electronics', 'Home'],
        'Quantity':,
        'Price_Per_Unit': [500.00, 45.00, 120.00, 30.00],
        'Total_Amount': [500.00, 90.00, 120.00, 90.00]
    }
    df = pd.DataFrame(sample_data)
    print("--- Calculated Retail Analytics ---")
    print(f"Total Gross Revenue: ${compute_total_revenue(df):,.2f}")