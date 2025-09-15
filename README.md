# 📊 Data Cleaning Automation Toolkit

A beginner-friendly data cleaning and analysis toolkit with both console and web interfaces. Perfect for students, data enthusiasts, and professionals who need quick data processing solutions.

## ✨ Features

### 🖥️ Console Application (`main.py`)
- **Menu-driven interface** with 9 core functionalities
- **Load CSV files** with robust error handling
- **Handle missing values** (drop, fill with mean/median/custom)
- **Remove duplicates** automatically
- **Change data types** (integer, float, string, datetime)
- **Search and filter** data within columns
- **Sort data** by any column (ascending/descending)
- **Create pivot tables** with various aggregations
- **View comprehensive data summaries** and statistics
- **Save cleaned data** with timestamps

### 🌐 Web Interface (`streamlit_app.py`)
Four specialized tools accessible through a clean sidebar:

#### 🏫 Student Marks Analyzer
- Calculates total marks, percentages, and grades
- Determines pass/fail status (minimum 40 per subject)
- Generates student rankings
- Shows class statistics and top performers

#### 💰 Sales Data Summarizer
- Computes revenue from quantity × price
- Analyzes daily sales trends
- Identifies best-selling items by quantity and revenue
- Provides comprehensive sales metrics

#### 🌦️ Weather Data Cleaner
- Automatically handles missing weather data
- Fills temperature gaps with mean values
- Fills humidity gaps with median values
- Sets missing rainfall to zero
- Provides weather statistics (max/min/average)

#### 🧾 Simple Expense Tracker
- Add new expenses through interactive forms
- Categorize spending (Food, Transport, Shopping, etc.)
- View spending patterns by category and time
- Generate monthly expense trends

## 📁 Project Structure

```
data-cleaning-toolkit/
│
├── main.py                 # Console application
├── streamlit_app.py         # Web interface
├── README.md               # Project documentation
│
├── sample_data/            # Sample CSV files
│   ├── student_marks.csv   # 20 students with marks
│   ├── sales_data.csv      # 20 sales transactions
│   ├── weather_data.csv    # 20 days weather data
│   └── expenses.csv        # 20 expense entries
│
└── requirements.txt        # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download** the project files
2. **Install required packages:**
   ```bash
   pip install pandas streamlit
   ```

### Running the Applications

#### Console Version
```bash
python main.py
```
Navigate through the menu using numbers 0-9.

#### Web Version
```bash
streamlit run streamlit_app.py
```
Open your browser to `http://localhost:8501`

## 📋 Expected CSV Formats

### Student Marks Analyzer
```csv
Name,Math,Science,English
John Doe,85,92,78
Jane Smith,67,73,81
```

### Sales Data Summarizer
```csv
Date,Item,Quantity,Price
2024-09-01,Laptop,2,45000
2024-09-01,Mouse,5,800
```

### Weather Data Cleaner
```csv
Date,Temperature,Humidity,Rainfall
2024-09-01,32.5,68,0.0
2024-09-02,31.2,72,2.3
```

### Expense Tracker
```csv
Date,Category,Amount,Note
2024-09-01,Food,450,Lunch at restaurant
2024-09-01,Transport,120,Auto rickshaw
```

## 📊 Sample Data

The project includes realistic sample data files with 20 entries each:

- **`student_marks.csv`** - Mixed performance students with Indian names
- **`sales_data.csv`** - Electronics sales over 10 days
- **`weather_data.csv`** - Weather data with intentional missing values
- **`expenses.csv`** - Personal expenses across different categories

## 💡 Usage Tips

### Console Application
1. Always **load a CSV file first** (option 1)
2. **Handle missing values** before other operations
3. **View data summary** (option 8) to understand your dataset
4. **Save your work** regularly (option 9)

### Web Interface
1. **Select the appropriate tool** from the sidebar
2. **Upload CSV files** in the expected format
3. **Download processed results** using the download buttons
4. **Validate data columns** - the app will show helpful error messages

## 🛠️ Technical Details

### Dependencies
- **pandas**: Data manipulation and analysis
- **streamlit**: Web application framework
- **datetime**: Date and time handling

### Key Features
- **Robust error handling** with user-friendly messages
- **Data validation** to ensure correct CSV formats
- **Automatic data type detection** and conversion
- **Memory-efficient processing** suitable for medium datasets
- **Cross-platform compatibility** (Windows, macOS, Linux)

## 🎯 Use Cases

### Educational
- **Students** learning data analysis concepts
- **Teachers** demonstrating data cleaning techniques
- **Workshops** on data preprocessing

### Professional
- **Quick data cleaning** before analysis
- **Sales report generation** from transaction data
- **Weather data preprocessing** for research
- **Personal expense tracking** and budgeting

### Business
- **Student performance analysis** in educational institutions
- **Sales trend analysis** for small businesses
- **Expense management** for teams and departments

## 🔧 Customization

The toolkit is designed to be easily extensible:

- **Add new tools** by creating functions in `streamlit_app.py`
- **Modify data processing logic** in individual tool functions
- **Change CSV formats** by updating validation logic
- **Add new aggregation methods** in pivot table functionality

## 🐛 Troubleshooting

### Common Issues

**"File not found" error:**
- Check file path spelling and location
- Remove quotes around file paths
- Use forward slashes (/) in paths

**"Missing columns" error:**
- Verify CSV has exact column names as specified
- Check for extra spaces in column headers
- Ensure CSV is properly formatted

**"Cannot convert data type" error:**
- Check for non-numeric data in numeric columns
- Handle missing values before type conversion
- Use string type for mixed data

## 📈 Future Enhancements

Potential improvements for advanced users:
- Support for Excel files (.xlsx)
- Advanced visualization charts
- Data export to multiple formats
- Automated data quality reports
- Integration with databases
- Batch processing capabilities

## 🤝 Contributing

This project is designed for educational purposes. Feel free to:
- **Fork and modify** for your needs
- **Add new features** and tools
- **Improve error handling** and user experience
- **Create additional sample datasets**

## 📝 License

This project is open source and available for educational and personal use.

## 👥 Target Audience

- **Beginners** learning data analysis
- **Students** in data science courses
- **Small business owners** needing quick insights
- **Anyone** who works with CSV data regularly

---

**Happy Data Cleaning!** 🎉

For questions or improvements, feel free to modify and extend this toolkit according to your needs.
