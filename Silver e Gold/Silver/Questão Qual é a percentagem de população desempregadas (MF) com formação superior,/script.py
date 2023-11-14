import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('C:\Users\Professor\Desktop\Nova pasta\Employment and Time Use.csv')

# Select the worksheet
worksheet = workbook.active

# Create a dictionary to store the names and their row numbers
name_dict = {}

# Loop through each row in the worksheet
for row in worksheet.iter_rows(min_row=2):
    # Get the name from the first cell in the row
    name = row[0].value

    # If the name is already in the dictionary, delete the row
    if name in name_dict:
        worksheet.delete_rows(row[0].row, 1)
    else:
        # If the name is not in the dictionary, add it and its row number to the dictionary
        name_dict[name] = row[0].row

# Save the changes to the workbook
# Save the changes to the workbook with escaped backslashes
workbook.save('C:\\Users\\Professor\\Desktop\\Nova pasta\\Employment and Time Use2.csv')
