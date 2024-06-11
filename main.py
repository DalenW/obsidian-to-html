import marko
import os

input_directory = "input"
output_directory = "output"

keep_attributes = False

def main():
    # loop through all the directories and files recursively
    for root, dirs, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".md"):
                # construct full file path
                file_path = os.path.join(root, filename)
                # read the file
                with open(file_path, "r") as file:
                    contents = file.read()
                    
                # remove attributes
                contents = remove_attributes(contents)
                    
                # convert the markdown to html
                html = marko.convert(contents)
                
                # construct output file path
                relative_path = os.path.relpath(root, input_directory)
                output_file_dir = os.path.join(output_directory, relative_path)
                os.makedirs(output_file_dir, exist_ok=True)
                output_file_path = os.path.join(output_file_dir, filename[:-3] + ".html")
                
                # write the html to a file
                with open(output_file_path, "w") as file:
                    file.write(html)
                    
                print(f"Converted {file_path} to {output_file_path}")


def remove_attributes(content):
    
    if keep_attributes:
        return content
    
    # obsidian (well markdown in general) have attributes at the very beginning of a file seperated by two diviedrs, "---". Let's remove them
    # we'll determine if a file has attributes by checking if the first characters are "---"
    if content.startswith("---"):
        # find the second occurance of "---"
        end = content.find("---", 3)
        # remove the attributes
        content = content[end+3:]
        
    return content


main()