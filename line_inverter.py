# inverts file line(s) and writes to a new file
def line_inverter(import_file_name, export_file_name, prefix_string):
    
    # tries to opens import file in reading mode
    try:
        f1 = open(import_file_name, "r")
    
    # if it can't, asks for user to pass a proper string to reference
    except TypeError:
        print("Input the file name as a string, please.")
    
    # tries to create a new file with the name of export_file_name var. in
    # append mode
    try:
        f2 = open(export_file_name, "a")
    
    # if it can't, asks for user to pass a proper string to reference
    except TypeError:
        print("Input the file name as a string, please.")
    
    
    # creates a list with each line in a separate index
    line_list = f1.readlines()
    
    # closes import file, since all data is stored in line_list
    f1.close()
    
    
    # loops through line_list to modify individual indices
    for i in line_list:
        
        # strips the "\n" from the string
        line = i.strip("\n")
        
        # inverts line string and overwrites to line var.
        line = line[::-1]
        
        # splits line var. into individual characters and assigns to char_list
        char_list = line.split()
        
        # loops through char_list
        for i, char in enumerate(char_list):
            
            # concatenates prefix_string and a character from the list
            x = prefix_string + char
            
            # assigns new variable (x) to the corresponding index the character
            # came from
            char_list[i] = x
     
        # joins char_list into a single string for export
        line = (" ").join(char_list)
        
        # appends the line to the new file
        f2.write(line)
        
    # once the loop is finished, close the new file
    f2.close()
