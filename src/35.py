def calculate_interest_rate(principal_amount, interest_rate, time_in_years):
    # Calculate monthly interest rate using compound interest formula
    monthly_interest = principal_amount * (interest_rate / 12)
    
    # Calculate final amount after taking into account the compounding effect of monthly interest rates
    final_amount = principal_amount + (principal_amount * monthly_interest * time_in_years)
    
    return final_amount

# Example usage
if __name__ == "__main__":
    principal_amount = 5000
    interest_rate = 2.0
    time_in_years = 3
    
    print("Final amount:", calculate_interest_rate(principal_amount, interest_rate, time_in_years))
