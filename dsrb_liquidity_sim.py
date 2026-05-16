# Hi guys, this is a simple Monte Carlo script for an academic project for a multi-currency defense bank model!

import numpy as np
import pandas as pd

def run_simulation():
    # load the basic csv data file
    try:
        df = pd.read_csv('mock_balance_sheet.csv')
    except:
        print("Missing the csv data file!")
        return

    print("--- Running Student Liquidity Simulation Model ---")
    
    # settings for the simulation loops
    sim_runs = 2000 
    lcr_results = []
    
    # random seed so the numbers stay consistent when running
    np.random.seed(42)
    
    for run in range(sim_runs):
        current_hqla = 0.0
        current_outflow = 0.0
        
        for idx, row in df.iterrows():
            base_hqla = row['HQLA_Baseline']
            inflow = row['Projected_Inflow']
            outflow = row['Committed_Outflow']
            vol = row['Shock_Factor_Pct']
            
            # Currency shock model using basic random normal distribution
            # Simulating currency dropping value against CAD during a crisis
            random_draw = np.random.normal(0, 1)
            currency_drop = np.exp((-0.02 - 0.5 * (vol**2)) + vol * random_draw)
            
            shocked_hqla_pool = base_hqla * currency_drop
            
            # Bernoulli trial for a country delaying cash payments
            # Set to a casual 10% chance of a delay happening
            delay_chance = 0.10
            is_delayed = np.random.binomial(1, delay_chance)
            
            if is_delayed == 1:
                # if delayed, we only get 50% of incoming cash and outflows spike by 10%
                actual_inflow = inflow * 0.50
                actual_outflow = outflow * 1.10
            else:
                actual_inflow = inflow
                actual_outflow = outflow
                
            current_hqla += shocked_hqla_pool + actual_inflow
            current_outflow += actual_outflow
            
        # simple calculation for the Liquidity Coverage Ratio (LCR)
        final_lcr = (current_hqla / current_outflow) * 100
        lcr_results.append(final_lcr)
        
    # convert list to numpy array to calculate averages and boundaries
    lcr_results = np.array(lcr_results)
    
    average_lcr = np.mean(lcr_results)
    worst_5_percent_lcr = np.percentile(lcr_results, 5) # lower 5% threshold

    # printing out the basic metrics
    print(f"Average Simulated LCR: {average_lcr:.2f}%")
    print(f"Worst-case 5th Percentile LCR: {worst_5_percent_lcr:.2f}%")
    print("-------------------------------------------------")
    
    if worst_5_percent_lcr < 100.0:
        print("Result: Cash reserves fall below safe limits under bad conditions.")
    else:
        print("Result: Cash buffers remain okay.")

if __name__ == "__main__":
    run_simulation()
