import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Data Toolkit", 
    page_icon="📊", 
    layout="wide"
)

# Initialize session state
if 'df' not in st.session_state:
    st.session_state.df = None

# Sidebar
st.sidebar.title("📊 Data Toolkit")
st.sidebar.markdown("---")

tool = st.sidebar.radio(
    "Select Tool:",
    [
        "🏫 Student Marks Analyzer",
        "💰 Sales Data Summarizer", 
        "🌦️ Weather Data Cleaner",
        "🧾 Expense Tracker"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Instructions")
st.sidebar.markdown("1. Select a tool from above")
st.sidebar.markdown("2. Upload your CSV file")
st.sidebar.markdown("3. View results and download")

# Helper function to display dataframe with formatting
def display_dataframe(df, title="Data"):
    st.subheader(f"📋 {title}")
    st.dataframe(df, use_container_width=True)

# Helper function to create download button
def download_button(df, filename, label="📥 Download Results"):
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=label,
        data=csv,
        file_name=filename,
        mime='text/csv'
    )

# =============== STUDENT MARKS ANALYZER ===============
def student_marks_analyzer():
    st.title("🏫 Student Marks Analyzer")
    st.markdown("Upload a CSV file with columns: **Name, Math, Science, English**")
    
    uploaded_file = st.file_uploader(
        "Choose your student marks CSV file",
        type=['csv'],
        key="student_file"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Validate required columns
            required_cols = ['Name', 'Math', 'Science', 'English']
            if not all(col in df.columns for col in required_cols):
                st.error(f"❌ Missing required columns! Expected: {required_cols}")
                st.info("Your file columns: " + str(list(df.columns)))
                return
            
            # Calculate results
            df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
            df['Percentage'] = df['Total'] / 3
            
            # Determine pass/fail (minimum 40 marks in each subject)
            df['Result'] = df.apply(lambda row: "Pass" if (
                row['Math'] >= 40 and 
                row['Science'] >= 40 and 
                row['English'] >= 40
            ) else "Fail", axis=1)
            
            # Calculate ranks
            df['Rank'] = df['Percentage'].rank(ascending=False, method='dense').astype(int)
            
            # Sort by rank
            df_sorted = df.sort_values('Percentage', ascending=False)
            
            # Display results
            display_dataframe(
                df_sorted[['Rank', 'Name', 'Math', 'Science', 'English', 'Total', 'Percentage', 'Result']],
                "Student Results with Rankings"
            )
            
            # Statistics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("👥 Total Students", len(df))
            with col2:
                st.metric("✅ Passed", len(df[df['Result'] == 'Pass']))
            with col3:
                st.metric("❌ Failed", len(df[df['Result'] == 'Fail']))
            with col4:
                st.metric("📊 Average %", f"{df['Percentage'].mean():.1f}")
            
            # Top performer
            top_student = df_sorted.iloc[0]
            st.success(f"🏆 Top Performer: **{top_student['Name']}** with {top_student['Percentage']:.1f}%")
            
            download_button(df_sorted, "student_results.csv")
            
        except Exception as e:
            st.error(f"❌ Error processing file: {e}")

# =============== SALES DATA SUMMARIZER ===============
def sales_data_summarizer():
    st.title("💰 Sales Data Summarizer")
    st.markdown("Upload a CSV file with columns: **Date, Item, Quantity, Price**")
    
    uploaded_file = st.file_uploader(
        "Choose your sales CSV file",
        type=['csv'],
        key="sales_file"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Validate required columns
            required_cols = ['Date', 'Item', 'Quantity', 'Price']
            if not all(col in df.columns for col in required_cols):
                st.error(f"❌ Missing required columns! Expected: {required_cols}")
                st.info("Your file columns: " + str(list(df.columns)))
                return
            
            # Calculate revenue
            df['Revenue'] = df['Quantity'] * df['Price']
            
            # Summary metrics
            total_revenue = df['Revenue'].sum()
            total_quantity = df['Quantity'].sum()
            avg_price = df['Price'].mean()
            
            # Display metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("💵 Total Revenue", f"₹{total_revenue:,.2f}")
            with col2:
                st.metric("📦 Items Sold", f"{total_quantity:,}")
            with col3:
                st.metric("💰 Avg Price", f"₹{avg_price:.2f}")
            
            # Analysis
            st.subheader("📈 Sales Analysis")
            
            # Daily sales
            daily_sales = df.groupby('Date')['Revenue'].sum().reset_index()
            daily_sales = daily_sales.sort_values('Revenue', ascending=False)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**📅 Daily Sales**")
                st.dataframe(daily_sales, use_container_width=True)
            
            # Top items by quantity
            top_items_qty = df.groupby('Item')['Quantity'].sum().reset_index()
            top_items_qty = top_items_qty.sort_values('Quantity', ascending=False)
            
            with col2:
                st.markdown("**🏆 Best Selling Items (Quantity)**")
                st.dataframe(top_items_qty, use_container_width=True)
            
            # Top revenue items
            top_revenue = df.groupby('Item')['Revenue'].sum().reset_index()
            top_revenue = top_revenue.sort_values('Revenue', ascending=False)
            
            st.markdown("**💰 Top Revenue Items**")
            st.dataframe(top_revenue, use_container_width=True)
            
            # Best performing item
            best_item = top_revenue.iloc[0]['Item']
            best_revenue = top_revenue.iloc[0]['Revenue']
            st.success(f"🌟 Top Revenue Item: **{best_item}** (₹{best_revenue:,.2f})")
            
            download_button(df, "sales_analysis.csv")
            
        except Exception as e:
            st.error(f"❌ Error processing file: {e}")

# =============== WEATHER DATA CLEANER ===============
def weather_data_cleaner():
    st.title("🌦️ Weather Data Cleaner")
    st.markdown("Upload a CSV file with columns: **Date, Temperature, Humidity, Rainfall**")
    
    uploaded_file = st.file_uploader(
        "Choose your weather CSV file",
        type=['csv'],
        key="weather_file"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            st.subheader("📊 Raw Data")
            st.dataframe(df, use_container_width=True)
            
            # Show missing data info
            missing_data = df.isnull().sum()
            if missing_data.sum() > 0:
                st.warning(f"⚠️ Found {missing_data.sum()} missing values")
                st.write("Missing values per column:", missing_data[missing_data > 0])
            
            # Clean the data
            df_cleaned = df.copy()
            
            # Handle missing values
            if 'Temperature' in df_cleaned.columns:
                df_cleaned['Temperature'].fillna(df_cleaned['Temperature'].mean(), inplace=True)
            if 'Humidity' in df_cleaned.columns:
                df_cleaned['Humidity'].fillna(df_cleaned['Humidity'].median(), inplace=True)
            if 'Rainfall' in df_cleaned.columns:
                df_cleaned['Rainfall'].fillna(0, inplace=True)
            
            # Convert date column
            if 'Date' in df_cleaned.columns:
                df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'], errors='coerce')
            
            st.subheader("🧹 Cleaned Data")
            st.dataframe(df_cleaned, use_container_width=True)
            
            # Weather statistics
            if 'Temperature' in df_cleaned.columns:
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    max_temp = df_cleaned['Temperature'].max()
                    st.metric("🔥 Max Temperature", f"{max_temp:.1f}°C")
                
                with col2:
                    min_temp = df_cleaned['Temperature'].min()
                    st.metric("❄️ Min Temperature", f"{min_temp:.1f}°C")
                
                with col3:
                    avg_temp = df_cleaned['Temperature'].mean()
                    st.metric("🌡️ Average Temperature", f"{avg_temp:.1f}°C")
            
            # Rainfall statistics
            if 'Rainfall' in df_cleaned.columns:
                col1, col2 = st.columns(2)
                
                with col1:
                    total_rainfall = df_cleaned['Rainfall'].sum()
                    st.metric("🌧️ Total Rainfall", f"{total_rainfall:.1f} mm")
                
                with col2:
                    avg_rainfall = df_cleaned['Rainfall'].mean()
                    st.metric("☔ Average Rainfall", f"{avg_rainfall:.1f} mm")
            
            # Humidity statistics
            if 'Humidity' in df_cleaned.columns:
                avg_humidity = df_cleaned['Humidity'].mean()
                st.metric("💧 Average Humidity", f"{avg_humidity:.1f}%")
            
            download_button(df_cleaned, "weather_cleaned.csv")
            
        except Exception as e:
            st.error(f"❌ Error processing file: {e}")

# =============== EXPENSE TRACKER ===============
def expense_tracker():
    st.title("🧾 Simple Expense Tracker")
    st.markdown("Upload a CSV file with columns: **Date, Category, Amount, Note** (or start with empty file)")
    
    uploaded_file = st.file_uploader(
        "Choose your expense CSV file (optional)",
        type=['csv'],
        key="expense_file"
    )
    
    # Initialize or load data
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            # Validate columns
            if not all(col in df.columns for col in ['Date', 'Category', 'Amount']):
                st.error("❌ CSV should have columns: Date, Category, Amount, Note")
                return
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
            return
    else:
        # Create empty dataframe
        df = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Note'])
    
    st.subheader("➕ Add New Expense")
    
    # Add new expense form
    with st.form("expense_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            date = st.date_input("Date", datetime.today())
            category = st.selectbox(
                "Category", 
                ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]
            )
        
        with col2:
            amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0)
            note = st.text_input("Note (optional)")
        
        submitted = st.form_submit_button("Add Expense")
        
        if submitted and amount > 0:
            new_expense = pd.DataFrame({
                'Date': [date],
                'Category': [category],
                'Amount': [amount],
                'Note': [note]
            })
            df = pd.concat([df, new_expense], ignore_index=True)
            st.success("✅ Expense added successfully!")
    
    # Display expenses if any
    if not df.empty:
        st.subheader("📊 Expense Summary")
        
        # Convert date column
        df['Date'] = pd.to_datetime(df['Date'])
        
        # Summary metrics
        total_expenses = df['Amount'].sum()
        expense_count = len(df)
        avg_expense = df['Amount'].mean()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("💰 Total Spent", f"₹{total_expenses:,.2f}")
        with col2:
            st.metric("📋 Total Expenses", expense_count)
        with col3:
            st.metric("📊 Average Expense", f"₹{avg_expense:.2f}")
        
        # Category-wise expenses
        category_expenses = df.groupby('Category')['Amount'].sum().reset_index()
        category_expenses = category_expenses.sort_values('Amount', ascending=False)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📈 Category-wise Spending**")
            st.dataframe(category_expenses, width='stretch')
        
        with col2:
            st.markdown("**📅 Recent Expenses**")
            recent_expenses = df.sort_values('Date', ascending=False).head(10)
            st.dataframe(recent_expenses[['Date', 'Category', 'Amount', 'Note']], width='stretch')
        
        # Monthly trend
        df['Month'] = df['Date'].dt.to_period('M').astype(str)
        monthly_expenses = df.groupby('Month')['Amount'].sum().reset_index()
        
        st.markdown("**📊 Monthly Spending Trend**")
        st.dataframe(monthly_expenses, width='stretch')
        
        download_button(df, "expenses.csv", "💾 Download Expense Data")

# =============== MAIN APP ===============
def main():
    # Main content based on selected tool
    if tool == "🏫 Student Marks Analyzer":
        student_marks_analyzer()
    elif tool == "💰 Sales Data Summarizer":
        sales_data_summarizer()
    elif tool == "🌦️ Weather Data Cleaner":
        weather_data_cleaner()
    elif tool == "🧾 Expense Tracker":
        expense_tracker()

if __name__ == "__main__":
    main()