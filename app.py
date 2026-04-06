#based on the sales analysis notebook, we will create a web application using Streamlit to display the insights from the sales data analysis. The app will have different sections for each analysis and will allow users to interact with the data through filters and visualizations. 
import streamlit as st
import pandas as pd 


#load the cleaned dataset
from pathlib import Path
import pandas as pd

file_path = Path("Data") / "Cleaned_Sales_data.xlsx"
data = pd.read_excel(file_path)

# CLEAN + DEBUG
#data.columns = data.columns.str.strip()
#st.write("Columns:", data.columns)

# Set the title of the app and cetralize it
st.markdown("<h1 style='text-align: center; color: black;'>Sales Data Analysis Dashboard for CityMart</h1>", unsafe_allow_html=True)

#set the name of the developer and the month and year of the analysis and centralize it
st.markdown("<h3 style='text-align: center; color: black;'>Developed by Tolulope Olalere, April 2026</h3>", unsafe_allow_html=True)



#analysis 1: top 20 high profit products
st.subheader("Top 20 High Profit Products")
high_profit_products = data.groupby('Products')['Profit'].sum().sort_values(ascending=False).head(20)
st.dataframe(high_profit_products)
#plot top 20 products with the highest profit using histogram
st.bar_chart(high_profit_products)
#write professional insights and recommendations for the top 20 high profit products and give statistics on the profit contribution of these products to the overall profit of the company
total_profit = data['Profit'].sum()
high_profit_contribution = high_profit_products.sum()
st.markdown(f"### Insights and Recommendations for Top 20 High Profit Products")
st.markdown(f"The top 20 high profit products contribute {high_profit_contribution/total_profit*100:.2f}% to the overall profit of the company.")   
st.markdown("1. These products are the most profitable for the company and should be prioritized in terms of inventory management, marketing, and sales strategies.")     
st.markdown("2. It is also important to monitor the performance of these products regularly and adjust strategies as needed to maintain their profitability. Consider investing in targeted marketing campaigns and promotions to boost sales of these high profit products, while also ensuring that inventory levels are sufficient to meet demand without overstocking.")
st.markdown("3. It is highly recommended that these top 20 high profit products be given special attention in terms of inventory management, marketing, and sales strategies to maximize their contribution to the company's overall profitability")
st.markdown("4. In conclusion, the top 20 high profit products are critical to the company's success and should be prioritized in strategic planning and decision-making to ensure continued growth and profitability.")



# Analysis 2: top 20 low profit products
st.subheader("Top 20 Low Profit Products")  
low_profit_products = data.groupby('Products')['Profit'].sum().sort_values(ascending=True).head(20)
st.dataframe(low_profit_products)
#plot top 20 products with the lowest profit
st.bar_chart(low_profit_products)
#professional insights and recommendations for the top 20 low profit products and give statistics on the profit contribution of these products to the overall profit of the company
low_profit_contribution = low_profit_products.sum() 
st.markdown(f"### Insights and Recommendations for Top 20 Low Profit Products")
st.markdown(f"The top 20 low profit products contribute {low_profit_contribution/total_profit*100:.2f}% to the overall profit of the company.")
st.markdown("1. These products are the least profitable for the company and may require a strategic review to determine whether they should be discontinued, improved, or marketed differently.")
st.markdown("2. It is important to analyze the reasons behind the low profitability of these products, such as high costs, low sales volume, or poor market fit, and develop targeted strategies to address these issues.")
st.markdown("3. Consider conducting market research to understand customer preferences and identify potential improvements or repositioning opportunities for these low profit products. Additionally, evaluate the cost structure and pricing strategy to enhance profitability.")
st.markdown("4. In conclusion, the top 20 low profit products require careful analysis and strategic action to either improve their performance or make informed decisions about their future in the product portfolio, with the goal of optimizing overall profitability for the company.")    



# Analysis 3: low performing products based on quantity sold
st.subheader("Low Performing Products Based on Quantity Sold")
low_quantity_products = data.groupby('Products')['Quantity'].sum().sort_values(ascending=True).head(20)
st.dataframe(low_quantity_products)
#plot low performing products based on quantity sold using histogram
st.bar_chart(low_quantity_products)
#professional insights and recommendations for the low performing products based on quantity sold and give statistics on the quantity contribution of these products to the overall quantity sold by the company
total_quantity = data['Quantity'].sum() 
low_quantity_contribution = low_quantity_products.sum()
st.markdown(f"### Insights and Recommendations for Low Performing Products Based on Quantity Sold") 
st.markdown(f"The low performing products based on quantity sold contribute {low_quantity_contribution/total_quantity*100:.2f}% to the overall quantity sold by the company.")
st.markdown("1. These products have low sales volume and may require a strategic review to determine whether they should be discontinued, improved, or marketed differently.")
st.markdown("2. It is important to analyze the reasons behind the low sales volume of these products, such as lack of customer awareness, poor market fit, or high competition, and develop targeted strategies to address these issues.")
st.markdown("3. Consider conducting market research to understand customer preferences and identify potential improvements or repositioning opportunities for these low performing products. Additionally, evaluate the marketing and promotional strategies to boost sales and increase customer awareness.")
st.markdown("4. In conclusion, the low performing products based on quantity sold require careful analysis and strategic action to either improve their performance or make informed decisions about their future in the product portfolio, with the goal of optimizing overall sales volume for the company.") 



# Analysis 4: best return per unit sold
st.subheader("Best Return Per Unit Sold")   
best_return_products = data.groupby('Products').apply(lambda x: x['Profit'].sum() / x['Quantity'].sum() if x['Quantity'].sum() != 0 else 0).sort_values(ascending=False).head(20)
st.dataframe(best_return_products)
#plot best return per unit sold using bar chart
st.bar_chart(best_return_products)
#professional insights and recommendations for the best return per unit sold products and give statistics on the return contribution of these products to the overall profit of the company
best_return_contribution = best_return_products.sum()   
st.markdown(f"### Insights and Recommendations for Best Return Per Unit Sold Products")
st.markdown(f"The best return per unit sold products contribute {best_return_contribution/total_profit*100:.2f}% to the overall profit of the company.")
st.markdown("1. These products have the highest return on investment per unit sold and should be prioritized in terms of inventory management, marketing, and sales strategies to maximize profitability.")
st.markdown("2. It is important to monitor the performance of these products regularly and adjust strategies as needed to maintain their high return per unit sold. Consider investing in targeted marketing campaigns and promotions to boost sales of these high return products, while also ensuring that inventory levels are sufficient to meet demand without overstocking.")
st.markdown("3. It is highly recommended that these best return per unit sold products be given special attention in terms of inventory management, marketing, and sales strategies to maximize their contribution to the company's overall profitability.")
st.markdown("4. In conclusion, the best return per unit sold products are critical to the company's success and should be prioritized in strategic planning and decision-making to ensure continued growth and profitability.") 



# Analysis 5: best gross contributing products
st.subheader("Best Gross Contributing Products")    
best_gross_products = data.groupby('Products')['Gross'].sum().sort_values(ascending=False).head(20)
st.dataframe(best_gross_products)
#plot best gross contributing products using bar chart
st.bar_chart(best_gross_products)
#professional insights and recommendations for the best gross contributing products and give statistics on the gross contribution of these products to the overall revenue of the company
total_gross = data['Gross'].sum()
best_gross_contribution = best_gross_products.sum()
st.markdown(f"### Insights and Recommendations for Best Gross Contributing Products")   
st.markdown(f"The best gross contributing products contribute {best_gross_contribution/total_gross*100:.2f}% to the overall revenue of the company.")
st.markdown("1. These products have the highest gross revenue contribution and should be prioritized in terms of inventory management, marketing, and sales strategies to maximize revenue generation.")
st.markdown("2. It is important to monitor the performance of these products regularly and adjust strategies as needed to maintain their high gross contribution. Consider investing in targeted marketing campaigns and promotions to boost sales of these high gross products, while also ensuring that inventory levels are sufficient to meet demand without overstocking.")
st.markdown("3. It is highly recommended that these best gross contributing products be given special attention in terms of inventory management, marketing, and sales strategies to maximize their contribution to the company's overall revenue.")
st.markdown("4. In conclusion, the best gross contributing products are critical to the company's success and should be prioritized in strategic planning and decision-making to ensure continued growth and profitability.")




# Analysis 6: best profit contributing products
st.subheader("Best Profit Contributing Products")
best_profit_products = data.groupby('Products')['Profit'].sum().sort_values(ascending=False).head(20)
st.dataframe(best_profit_products)
#plot best profit contributing products
st.bar_chart(best_profit_products)
#professional insights and recommendations for the best profit contributing products and give statistics on the profit contribution of these products to the overall profit of the company
best_profit_contribution = best_profit_products.sum()   
st.markdown(f"### Insights and Recommendations for Best Profit Contributing Products")
st.markdown(f"The best profit contributing products contribute {best_profit_contribution/total_profit*100:.2f}% to the overall profit of the company.")
st.markdown("1. These products have the highest profit contribution and should be prioritized in terms of inventory management, marketing, and sales strategies to maximize profitability.")
st.markdown("2. It is important to monitor the performance of these products regularly and adjust strategies as needed to maintain their high profit contribution. Consider investing in targeted marketing campaigns and promotions to boost sales of these high profit products, while also ensuring that inventory levels are sufficient to meet demand without overstocking.")
st.markdown("3. It is highly recommended that these best profit contributing products be given special attention in terms of inventory management, marketing, and sales strategies to maximize their contribution to the company's overall profitability.")
st.markdown("4. In conclusion, the best profit contributing products are critical to the company's success and should be prioritized in strategic planning and decision-making to ensure continued growth and profitability.")  


# Analysis 7: best quantity sold products
st.subheader("Best Quantity Sold Products")     
best_quantity_products = data.groupby('Products')['Quantity'].sum().sort_values(ascending=False).head(20)
st.dataframe(best_quantity_products)
#plot best quantity sold products using bar chart
st.bar_chart(best_quantity_products)
#professional insights and recommendations for the best quantity sold products and give statistics on the quantity contribution of these products to the overall quantity sold by the company
best_quantity_contribution = best_quantity_products.sum()   
st.markdown(f"### Insights and Recommendations for Best Quantity Sold Products")
st.markdown(f"The best quantity sold products contribute {best_quantity_contribution/total_quantity*100:.2f}% to the overall quantity sold by the company.")
st.markdown("1. These products have the highest sales volume and should be prioritized in terms of inventory management, marketing, and sales strategies to maximize sales volume.")
st.markdown("2. It is important to monitor the performance of these products regularly and adjust strategies as needed to maintain their high sales volume. Consider investing in targeted marketing campaigns and promotions to boost sales of these high quantity products, while also ensuring that inventory levels are sufficient to meet demand without overstocking.")
st.markdown("3. It is highly recommended that these best quantity sold products be given special attention in terms of inventory management, marketing, and sales strategies to maximize their contribution to the company's overall sales volume.")
st.markdown("4. In conclusion, the best quantity sold products are critical to the company's success and should be prioritized in strategic planning and decision-making to ensure continued growth and profitability.")
