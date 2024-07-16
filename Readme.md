# EDA in one click
### "EDA-In-One-Click" is a Streamlit application that simplifies Exploratory Data Analysis (EDA) by allowing users to perform various EDA tasks with just one click.
### [Streamlit App Link](https://eda-in-one-click-8gqlw8te5tn6zbyuf5n8qn.streamlit.app)

---

### Repository Structure
```
EDA-In-One-Click
├── __pycache__
├── pages
├── .gitignore
├── Readme.md
├── requirements.txt
├── 😊Welcome.py
```

### Steps to Run the Project

1. **Clone the Repository**
   ```sh
   git clone https://github.com/iamdebasishdas123/EDA-In-One-Click.git
   cd EDA-In-One-Click
   ```

2. **Set Up a Virtual Environment**
   It's a good practice to use a virtual environment to manage your project's dependencies.
   
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Required Dependencies**
   Install the required Python packages listed in `requirements.txt`.

   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Main Script**
    `😊Welcome.py` is the main entry point of the project.

   ```sh
   Streamlit run 😊Welcome.py
   ```
---
### **Brief Description About Plot**

here are introductions and descriptions for the various plots, including when to use each plot and the observations you can get from them:

### 1. Pair Plot

**Introduction**: A pair plot is a matrix of scatter plots that shows the relationships between pairs of variables in a dataset.

**When to Use**: Use a pair plot to visually explore the relationships between multiple variables and to identify patterns, trends, or correlations.

**Observations**: You can observe the linear or non-linear relationships between pairs of variables, identify clusters or outliers, and understand the distribution of individual variables.

### 2. Correlation Heatmap

**Introduction**: A correlation heatmap is a visual representation of the correlation matrix that shows the pairwise correlation coefficients between variables.

**When to Use**: Use a correlation heatmap to understand the strength and direction of relationships between multiple variables.

**Observations**: You can observe positive or negative correlations, the magnitude of the correlations, and identify highly correlated variables.

### 3. Histplot

**Introduction**: A histplot (histogram plot) displays the distribution of a single variable by counting the number of observations that fall within each of a set of bins.

**When to Use**: Use a histplot to understand the distribution of a variable, identify the central tendency, spread, and skewness of the data.

**Observations**: You can observe the shape of the distribution (e.g., normal, skewed), identify outliers, and understand the frequency of data points within specific ranges.

### 4. Rug Plot

**Introduction**: A rug plot adds small vertical lines (or "rugs") along the x-axis of a plot to indicate the positions of individual data points.

**When to Use**: Use a rug plot to add more detail to a distribution plot or scatter plot, highlighting the exact positions of data points.

**Observations**: You can observe the density of data points along the axis, identify clusters, and better understand the distribution of data points.

### 5. ECDF Plot

**Introduction**: An Empirical Cumulative Distribution Function (ECDF) plot shows the cumulative frequency distribution of a variable.

**When to Use**: Use an ECDF plot to visualize the proportion of observations below each value in a dataset.

**Observations**: You can observe the cumulative probability, identify medians, percentiles, and compare distributions between different groups.

### 6. KDE Plot

**Introduction**: A Kernel Density Estimate (KDE) plot is a smoothed version of a histogram that estimates the probability density function of a variable.

**When to Use**: Use a KDE plot to visualize the distribution of a variable and understand its density without the granularity of a histogram.

**Observations**: You can observe the underlying distribution shape, identify modes, and compare distributions between groups.

### 7. Box Plot

**Introduction**: A box plot (or box-and-whisker plot) summarizes the distribution of a variable by displaying its quartiles, median, and potential outliers.

**When to Use**: Use a box plot to compare the distributions of a variable across different categories or groups.

**Observations**: You can observe the central tendency, spread, and presence of outliers, and compare the distribution shapes across different groups.

### 8. Violin Plot

**Introduction**: A violin plot combines aspects of a box plot and a KDE plot to show the distribution of a variable along with its probability density.

**When to Use**: Use a violin plot to compare the distribution and density of a variable across different categories or groups.

**Observations**: You can observe the distribution shape, density, and compare distributions across groups, along with central tendency and spread.

### 9. QQ Plot

**Introduction**: A Quantile-Quantile (QQ) plot compares the quantiles of a variable's distribution to the quantiles of a theoretical distribution (e.g., normal distribution).

**When to Use**: Use a QQ plot to assess whether a variable follows a specific theoretical distribution.

**Observations**: You can observe deviations from the theoretical distribution, identify skewness, and detect outliers.

### 10. Clustermap (Creamer Heat Map)

**Introduction**: A clustermap is a heatmap that includes hierarchical clustering to group similar variables or observations together.

**When to Use**: Use a clustermap to visualize the correlation between variables and identify clusters or patterns in the data.

**Observations**: You can observe clusters of similar variables, identify patterns or trends, and understand the relationships between variables.

### 11. Scatter Plot

**Introduction**: A scatter plot displays individual data points plotted on two axes to show the relationship between two variables.

**When to Use**: Use a scatter plot to explore the relationship between two continuous variables and identify trends, patterns, or correlations.

**Observations**: You can observe correlations (positive or negative), identify clusters or outliers, and understand the nature of the relationship between variables.

### 12. Colorbar

**Introduction**: A colorbar is an additional visual element in a plot that represents the range of values mapped to colors in the plot.

**When to Use**: Use a colorbar to provide a reference for interpreting the color coding in a plot, such as a heatmap or scatter plot with color-coded points.

**Observations**: You can observe the range of values represented by colors, understand the gradient, and interpret the color-coded data points.

### 13. Pie Chart

**Introduction**: A pie chart displays the proportions of a whole, divided into slices representing different categories.

**When to Use**: Use a pie chart to visualize the relative proportions or percentages of different categories in a dataset.

**Observations**: You can observe the distribution of categories, identify the largest or smallest categories, and understand the composition of the whole.

### 14. Bar Plot

**Introduction**: A bar plot displays categorical data with rectangular bars representing the frequency or value of each category.

**When to Use**: Use a bar plot to compare the frequency or value of different categories.

**Observations**: You can observe the relative sizes of categories, identify trends or patterns, and compare the values of different categories.

### 15. Word Cloud

**Introduction**: A word cloud is a visual representation of text data, where the size of each word indicates its frequency or importance.

**When to Use**: Use a word cloud to highlight the most frequent or important words in a text dataset.

**Observations**: You can observe the most prominent words, identify key themes or topics, and understand the relative importance of words.

### 16. Cross Tab

**Introduction**: A cross tabulation (cross tab) is a table that displays the frequency distribution of variables and shows the relationship between them.

**When to Use**: Use a cross tab to analyze the relationship between two or more categorical variables.

**Observations**: You can observe the frequency distribution, identify patterns or associations between variables, and understand the joint distribution of variables.

---

Each plot provides unique insights and helps in understanding different aspects of the data, facilitating better decision-making and analysis.
