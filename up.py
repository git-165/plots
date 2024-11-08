import os

# Define paths
plotly_folder = 'plotly'
template_file = 'index.template.html'
output_file = 'index.html'

# Get all .html files in the plotly folder
plot_files = [f for f in os.listdir(plotly_folder) if f.endswith('.html')]

# Format the file names into JavaScript array syntax
file_list = ",\n      ".join([f"'{file}'" for file in plot_files])

# Read the template file
with open(template_file, 'r') as file:
    html_content = file.read()

# Replace the placeholder with the dynamic file list
updated_html = html_content.replace("{{plot_files_placeholder}}", file_list)

# Write the updated content to index.html
with open(output_file, 'w') as file:
    file.write(updated_html)

print("index.html has been updated with the current plot files.")
