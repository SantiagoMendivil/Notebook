#!/usr/bin/bash 

# In this script we will se how to save outputs in different ways 

# ########################################################
# Save outputs to a specific file
echo "Hello World" > output.txt

# Save multiple outputs to a specific file. 
# ctrl + d to exit
cat > output.txt 

# Instead of replacing the content of the file, we can append the output to the file
cat >> output.txt

# Pass something to cat to show an output
cat << newText 
Hello World
This is the the text
that will be saved to the file
newText