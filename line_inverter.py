# inverts file line(s) and writes to a new file
def line_inverter(import_file_name, export_file_name, prefix_string):
    
    # tries to open import file in reading mode
    f1 = open(import_file_name, "r")
    
    # tries to create export file in append mode
    f2 = open(export_file_name, "a")
    
    
    # creates a list with each line in a separate index
    line_list = f1.readlines()
    
    # reverses line order
    line_list.reverse()
    
    # closes import file, since all data is stored in line_list
    f1.close()
    
    
    # loops through line_list to modify individual indices
    for line in line_list:
        
        # strips the "\n" from the string
        line = line.strip("\n")
        
        # concatenates prefix_string and a character from the line_list
        x = prefix_string + line
        
        # appends the line to the new file
        f2.write(x)
        
    # once the loop is finished, close the new file
    f2.close()
