import base64
import os


def constant_head_tail_substitute(input_file, output_file, head_pattern, tail_pattern, new_head, new_tail, var_callback):
    global count
    head_len = len(head_pattern)
    tail_len = len(tail_pattern)

    with open(input_file, 'r') as fin, open(output_file, 'w') as fout:
        for line in fin:
            # Strip newline for processing, but keep track of it
            line = line.rstrip('\n')
            
            # Check if the line matches your criteria
            if line.startswith(head_pattern) and line.endswith(tail_pattern): # Extract the middle part without copying the whole string into a new regex object
                # variable_content = line[start_index : end_index]
                variable_content = line[head_len : -tail_len]

                new_variable_content = var_callback(variable_content)
                count += 1
                
                # Write the new parts directly to the output stream
                fout.write(new_head + new_variable_content + new_tail + '\n')
            else:
                # If it doesn't match, just write the original line
                fout.write(line + '\n')

count = 0

def store_image(f64_string):
    global count
    # 1. Decode the Base64 string to bytes
    image_bytes = base64.b64decode(f64_string)

    image_path = f"img_composed_note_{count}.png"
    # 2. Write the bytes to a .png file
    with open(image_path, "wb") as f:
        f.write(image_bytes)

    return image_path


def _pass(s):
    return s

constant_head_tail_substitute(
    '_index.md', 
    '_index1.md', 
    head_pattern='AAA', 
    tail_pattern='AAA', 
    new_head='<center><i>', 
    new_tail='</i></center>',
    var_callback=_pass
)
