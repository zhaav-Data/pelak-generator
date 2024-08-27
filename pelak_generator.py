import os
import random
import csv
import json
from tqdm import tqdm
from persian_names import *

os.makedirs('./output/',exist_ok=True)


with open('config.json', 'r') as file:
    data = json.load(file)

chars = data['chars']
models = data['car_model']


def generate_plate_texts(total_count, chunk_size):
    with tqdm(total=total_count, desc="Generating persian car plate number") as pbar:
        chunk = []  # Temporary storage for current chunk of plate texts
        file_index = 1  # Index to keep track of file numbering

        for _ in range(total_count):
            # Make random choices
            chap = str(random.randint(0,99))
            random_char = random.choice(chars)
            rast = str(random.randint(100,990))
            car_model_ = str(random.choice(models))

            plate_text = (chap + ',' + random_char['en'] + ',' + random_char['fa'] + ',' + rast + ',' + car_model_ + ','  + str(random.randint(18,80)) + ',' + firstname_fa('r') + ',' + lastname_fa()) + ',' + str(random.randint(80,130))

            chunk.append([plate_text])

            # Check if current chunk has reached the chunk size
            if len(chunk) >= chunk_size:
                # Write the current chunk to a CSV file
                with open(f'./output/plates_{file_index}.csv', 'w', newline='', encoding='utf-8') as file:
                    # writer = csv.writer(file)
                    # writer.writerows(chunk)
                    writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')  # Set QUOTE_NONE and define an escape character
                    
                    try:
                        writer.writerows(chunk)  # Write the chunk of data
                    except csv.Error as e:
                        print(f'Error writing CSV: {e}')
                        
                chunk = []  # Reset chunk
                file_index += 1  # Increment file index
                pbar.update(chunk_size)  # Update progress bar

        # Write any remaining data in the chunk after the loop
        if chunk:
            with open(f'./output/plates_{file_index}.csv', 'w', newline='', encoding='utf-8') as file:
                # writer = csv.writer(file)
                # writer.writerows(chunk)
                writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')  # Set QUOTE_NONE and define an escape character
                    
                try:
                    writer.writerows(chunk)  # Write the chunk of data
                except csv.Error as e:
                    print(f'Error writing CSV: {e}')
            pbar.update(len(chunk))

# generate_plate_texts(1000000000, 10000000)

generate_plate_texts(2_000_000_000, 50_000_000)