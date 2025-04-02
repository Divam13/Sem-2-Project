from API import stock_data as stock_api
from API import news_data as news_api
from StockProcessing.data_processor import DataProcessor
from StockProcessing.visualizer import StockVisualizer
import pandas as pd
import os
import json

def ensure_directory_exists(directory_path):
    """Ensure the specified directory exists, create it if it doesn't."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def add_company_details_to_csv():
    """Add company details to a CSV file."""
    with open('companies.json', 'r') as file:
        companies_details = json.load(file)

        for comapany_detail in companies_details:
            # Initialize API objects
            stock = stock_api.StockData(stock_symbol=companies_details['symbol'], company_name=comapany_detail['name'])
            
            # Ensure the output directory exists
            ensure_directory_exists("website/images")

            stock_data = stock.fetch_stock_data()
            
            # Process the stock data
            processor = DataProcessor()
            csv_file = processor.dict_to_csv(stock_data)
            stock_df, ticker = processor.process_csv_data(csv_file)
            
            # Save the processed data
            processed_file = processor.save_processed_data()
            print(f"Processed stock data saved to: {processed_file}")

def main():
    add_company_details_to_csv()
    
    '''# Create visualizations
    visualizer = StockVisualizer()
    chart_path = visualizer.plot_stock_data(stock_df, ticker)
    
    print(f"Processed stock data for {ticker} and created chart at '{chart_path}'")'''

    
    '''# Example of how to fetch additional data and create more visualizations:
    
    # Fetch news data
    news_data = news.fetch_news()
    print(f"Fetched {len(news_data)} news articles")
    
    # Get price change data
    price_changes = stock.get_price_change()
    print(f"Price change: {price_changes}")'''

if __name__ == "__main__":
    main()