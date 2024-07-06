from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

plt.switch_backend('Agg')

app = Flask(__name__)

def question_5(data):
    # What does the graph of the total annual amount of waste look like in each province from year to year?
    data.plot(kind='line', marker='o', figsize=(6, 3))

    # Title and labels
    plt.title('Total Annual Waste Generation by Year (Line Plot)')
    plt.xlabel('Year')
    plt.ylabel('Total Waste Generation (tons)')
    plt.legend(title='Province', bbox_to_anchor=(1, 1))

    # Save the plot to the static folder
    plot_path = os.path.join('static', 'total_annual_amount_of_waste.png')
    plt.savefig(plot_path, bbox_inches='tight')

    plt.close()

    return plot_path

def question_6(data):
    # Display of categorization and visualization of average incidence annual waste in each province for the entire year with provision:
    # 1. The provincial category is "GREEN" if the average annual waste generation is <= 100,000 tons
    # 2. Th province category “Orange” if 100,000 < average annual waste generation <= 700,000 tons
    # 3. The provincial category is "RED" if the average annual waste generation is > 700,000 tons.
    green_threshold = 100000
    orange_threshold = 700000

    def categorize_province(avg_waste):
        if avg_waste <= green_threshold:
            return 'GREEN'
        elif avg_waste <= orange_threshold:
            return 'ORANGE'
        else:
            return 'RED'

    data['Category'] = data['Timbulan Sampah Tahunan(ton)'].apply(categorize_province)
    category_counts = data['Category'].value_counts().reindex(['GREEN', 'ORANGE', 'RED']).fillna(0)
    plt.bar(category_counts.index, category_counts.values, color=['green', 'orange', 'red'])
    plt.title('Provincial Waste Generation Categorization')
    plt.xlabel('Category')
    plt.ylabel('Number of Provinces')
    plt.grid(axis='y')

    # Save the plot to the static folder
    plot_path = os.path.join('static', 'average_annual_waste_generation.png')
    plt.savefig(plot_path, bbox_inches='tight')

    plt.close()

    return plot_path

@app.route('/')
def index():
    # read data
    data = pd.read_csv("data/concat_data.csv")

    # Question - answers
    # What is the total amount of annual waste generation in each province in each year?
    annual_waste_generation = data.groupby(['Tahun', 'Provinsi'])['Timbulan Sampah Tahunan(ton)'].sum().unstack()

    # What is the average total annual waste generation in each province for all years?
    average_annual_waste_generation = data.groupby('Provinsi')['Timbulan Sampah Tahunan(ton)'].mean().reset_index()


    # Generate plot for question 5
    plot1_path = question_5(annual_waste_generation)
    plot2_path = question_6(average_annual_waste_generation)

    return render_template('index.html', plot1_path=plot1_path, plot2_path=plot2_path)

if __name__ == '__main__':
    app.run(debug=True)
