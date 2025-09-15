import pandas as pd
import os
from datetime import datetime

# Global variables
df = None
filename = ""

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("      📊 DATA CLEANING AUTOMATION TOOL")
    print("="*50)
    print("1. 📂 Load CSV File")
    print("2. 🧹 Handle Missing Values")
    print("3. 🔄 Remove Duplicates")
    print("4. 🔧 Change Data Type")
    print("5. 🔍 Search Data")
    print("6. 📈 Sort Data")
    print("7. 📊 Create Pivot Table")
    print("8. 📋 View Data Summary")
    print("9. 💾 Save Cleaned Data")
    print("0. 🚪 Exit")
    print("="*50)

def load_csv():
    """Load CSV file"""
    global df, filename
    
    print("\n--- Load CSV File ---")
    file_path = input("Enter CSV file path: ").strip()
    
    # Remove quotes if present
    if file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]
    
    try:
        df = pd.read_csv(file_path)
        filename = file_path
        print(f"\n✅ File loaded successfully!")
        print(f"📊 Data shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print(f"📋 Columns: {list(df.columns)}")
        return True
    except FileNotFoundError:
        print("\n❌ File not found! Please check the file path.")
        return False
    except Exception as e:
        print(f"\n❌ Error loading file: {e}")
        return False

def handle_missing():
    """Handle missing values"""
    global df
    
    print("\n--- Handle Missing Values ---")
    print(f"Missing values per column:")
    missing_data = df.isnull().sum()
    print(missing_data[missing_data > 0])
    
    if missing_data.sum() == 0:
        print("✅ No missing values found!")
        return
    
    print("\nOptions:")
    print("1. Drop rows with missing values")
    print("2. Fill with mean (numeric columns)")
    print("3. Fill with median (numeric columns)")
    print("4. Fill with custom value")
    
    choice = input("Choose option (1-4): ").strip()
    
    if choice == "1":
        df = df.dropna()
        print("✅ Rows with missing values removed!")
    elif choice == "2":
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        print("✅ Missing values filled with mean!")
    elif choice == "3":
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        print("✅ Missing values filled with median!")
    elif choice == "4":
        value = input("Enter value to fill missing data: ")
        df = df.fillna(value)
        print("✅ Missing values filled with custom value!")

def remove_duplicates():
    """Remove duplicate rows"""
    global df
    
    print("\n--- Remove Duplicates ---")
    initial_rows = len(df)
    df = df.drop_duplicates()
    final_rows = len(df)
    removed = initial_rows - final_rows
    
    print(f"✅ Removed {removed} duplicate rows!")
    print(f"📊 Remaining rows: {final_rows}")

def change_data_type():
    """Change column data type"""
    global df
    
    print("\n--- Change Data Type ---")
    print("Available columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col} ({df[col].dtype})")
    
    try:
        col_choice = int(input("\nEnter column number: ")) - 1
        column = df.columns[col_choice]
        
        print("\nData type options:")
        print("1. Integer (int)")
        print("2. Float (float)")
        print("3. String (str)")
        print("4. DateTime")
        
        type_choice = input("Choose data type (1-4): ").strip()
        
        if type_choice == "1":
            df[column] = pd.to_numeric(df[column], errors='coerce').astype('Int64')
        elif type_choice == "2":
            df[column] = pd.to_numeric(df[column], errors='coerce')
        elif type_choice == "3":
            df[column] = df[column].astype(str)
        elif type_choice == "4":
            df[column] = pd.to_datetime(df[column], errors='coerce')
        
        print(f"✅ Column '{column}' converted successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def search_data():
    """Search for specific data"""
    global df
    
    print("\n--- Search Data ---")
    print("Available columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    
    try:
        col_choice = int(input("\nEnter column number to search: ")) - 1
        column = df.columns[col_choice]
        search_value = input(f"Enter value to search in '{column}': ")
        
        # Convert column to string for searching
        results = df[df[column].astype(str).str.contains(search_value, case=False, na=False)]
        
        print(f"\n🔍 Found {len(results)} matching records:")
        if len(results) > 0:
            print(results.to_string())
        else:
            print("No matching records found.")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def sort_data():
    """Sort data by column"""
    global df
    
    print("\n--- Sort Data ---")
    print("Available columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    
    try:
        col_choice = int(input("\nEnter column number to sort by: ")) - 1
        column = df.columns[col_choice]
        
        order = input("Sort ascending? (y/n): ").strip().lower()
        ascending = order == 'y'
        
        df = df.sort_values(by=column, ascending=ascending)
        print(f"✅ Data sorted by '{column}' ({'ascending' if ascending else 'descending'})")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def create_pivot():
    """Create pivot table"""
    global df
    
    print("\n--- Create Pivot Table ---")
    print("Available columns:")
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    
    try:
        index_choice = int(input("\nEnter column number for rows (index): ")) - 1
        index_col = df.columns[index_choice]
        
        value_choice = int(input("Enter column number for values: ")) - 1
        value_col = df.columns[value_choice]
        
        print("\nAggregation options:")
        print("1. Sum")
        print("2. Mean")
        print("3. Count")
        print("4. Max")
        print("5. Min")
        
        agg_choice = input("Choose aggregation (1-5): ").strip()
        agg_map = {'1': 'sum', '2': 'mean', '3': 'count', '4': 'max', '5': 'min'}
        agg_func = agg_map.get(agg_choice, 'sum')
        
        pivot = pd.pivot_table(df, index=index_col, values=value_col, aggfunc=agg_func)
        
        print(f"\n📊 Pivot Table ({agg_func} of {value_col} by {index_col}):")
        print(pivot.to_string())
        
    except Exception as e:
        print(f"❌ Error: {e}")

def view_summary():
    """Display data summary"""
    global df
    
    print("\n--- Data Summary ---")
    print(f"📊 Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\n📋 Column Information:")
    print(df.info())
    
    print(f"\n📈 Statistical Summary:")
    print(df.describe())
    
    print(f"\n🔍 Missing Values:")
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values")

def save_data():
    """Save cleaned data"""
    global df, filename
    
    print("\n--- Save Cleaned Data ---")
    
    # Generate new filename
    base_name = os.path.splitext(os.path.basename(filename))[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{base_name}_cleaned_{timestamp}.csv"
    
    try:
        df.to_csv(new_filename, index=False)
        print(f"✅ Data saved successfully as: {new_filename}")
        print(f"📊 Saved {len(df)} rows and {len(df.columns)} columns")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

def main():
    """Main program loop"""
    global df
    
    print("Welcome to the Data Cleaning Automation Tool!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-9): ").strip()
        
        if choice == "0":
            print("\n👋 Thank you for using the Data Cleaning Tool!")
            break
        elif choice == "1":
            load_csv()
        elif df is None:
            print("\n⚠️  Please load a CSV file first (option 1)")
        elif choice == "2":
            handle_missing()
        elif choice == "3":
            remove_duplicates()
        elif choice == "4":
            change_data_type()
        elif choice == "5":
            search_data()
        elif choice == "6":
            sort_data()
        elif choice == "7":
            create_pivot()
        elif choice == "8":
            view_summary()
        elif choice == "9":
            save_data()
        else:
            print("\n❌ Invalid choice! Please enter 0-9.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()