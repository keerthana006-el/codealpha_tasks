def main():
    
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 250.75,
        "GOOGL": 145.20,
        "MSFT": 420.15,
        "AMZN": 185.30,
        "NVDA": 895.40
    }
    
    print("=== Stock Portfolio Tracker ===")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    print("-" * 40)
    
    portfolio = {}
    total_investment = 0.0
    
    while True:
        stock_symbol = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()
        
        if stock_symbol.lower() == 'done':
            break
            
        if stock_symbol not in stock_prices:
            print(f"❌ {stock_symbol} not found! Available: {', '.join(stock_prices.keys())}")
            continue
        
        try:
            quantity = float(input(f"Enter quantity for {stock_symbol}: "))
            if quantity <= 0:
                print("❌ Quantity must be positive!")
                continue
                
            portfolio[stock_symbol] = quantity
            value = quantity * stock_prices[stock_symbol]
            total_investment += value
            print(f"✅ Added {quantity} shares of {stock_symbol} @ ${stock_prices[stock_symbol]:.2f} = ${value:.2f}")
            
        except ValueError:
            print("❌ Please enter a valid number for quantity!")
    
    if portfolio:
        print("\n" + "="*50)
        print("YOUR PORTFOLIO SUMMARY")
        print("="*50)
        
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]
            value = qty * price
            print(f"{symbol:>6} | {qty:>8.0f} shares | ${price:>8.2f} | ${value:>10.2f}")
        
        print("-" * 50)
        print(f"TOTAL INVESTMENT VALUE: ${total_investment:>10.2f}")
        print("="*50)
        
        save_file = input("\nSave portfolio to file? (y/n): ").lower().strip()
        if save_file in ['y', 'yes']:
            save_to_file(portfolio, stock_prices, total_investment)
    else:
        print("No stocks added to portfolio.")

def save_to_file(portfolio, stock_prices, total_investment):
    """Save portfolio to both TXT and CSV files"""
    filename_txt = "portfolio_summary.txt"
    filename_csv = "portfolio_summary.csv"
    
    with open(filename_txt, 'w') as f:
        f.write("STOCK PORTFOLIO SUMMARY\n")
        f.write("="*50 + "\n\n")
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]
            value = qty * price
            f.write(f"{symbol:>6} | {qty:>8.0f} shares | ${price:>8.2f} | ${value:>10.2f}\n")
        f.write("-" * 50 + "\n")
        f.write(f"TOTAL INVESTMENT: ${total_investment:>10.2f}\n")
    
    with open(filename_csv, 'w') as f:
        f.write("Symbol,Quantity,Price_per_Share,Total_Value\n")
        for symbol, qty in portfolio.items():
            price = stock_prices[symbol]
            value = qty * price
            f.write(f"{symbol},{qty},{price},{value}\n")
        f.write(f"TOTAL,,,{total_investment}\n")
    
    print(f"✅ Portfolio saved to:")
    print(f"   📄 {filename_txt}")
    print(f"   📊 {filename_csv}")

if __name__ == "__main__":
    main()