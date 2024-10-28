import os

# Paths to the label directories in the old dataset
label_dirs = ["C:/Users/Pawel Sloboda/Desktop/rustHax/train/labels", 
              "C:/Users/Pawel Sloboda/Desktop/rustHax/valid/labels", 
              "C:/Users/Pawel Sloboda/Desktop/rustHax/test/labels"]

for label_dir in label_dirs:
    for label_file in os.listdir(label_dir):
        file_path = os.path.join(label_dir, label_file)
        
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace label '1' with '0' if present
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if parts[0] == '1':
                parts[0] = '0'
            new_lines.append(" ".join(parts) + "\n")

        # Save the modified label file
        with open(file_path, 'w') as file:
            file.writelines(new_lines)

print("Label files updated successfully.")
