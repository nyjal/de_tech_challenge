import pandas as pd
import numpy as np
import os
import shutil

#Function for one of the requirements, removing appended zero
def remove_append_zero(number):
    if float(number) > 0:
        number = str(number)
        number = number.lstrip("0.")
    return float(number)

#Setting directory information, so application can be run anywhere
curr_dir = os.path.dirname(os.path.realpath(__file__))
landing_dir = os.path.join(curr_dir, 'landing_dir')
backup_dir = os.path.join(curr_dir, 'backup_dir')
output_dir = os.path.join(curr_dir, 'output_dir')
processdate=pd.Timestamp('today').strftime("%Y%m%d")

#Search landing_dir for csv files to be used, and append full directory name
#/full/directory/to/data1.csv
filepaths = [os.path.join(landing_dir, f) for f in os.listdir(landing_dir) if f.endswith('.csv')]

#If-Else clause, proceed only if files are found in the landing_dir
if len(filepaths) > 0:
    print('Landing file exist, cleaning data...')
    #Concat/append the 2 data files together and drop rows with empty names
    df = pd.concat(map(pd.read_csv, filepaths))
    df = df.dropna()

    #Remove any zeros prepended to the price field
    df['price'] = df.apply(lambda row : remove_append_zero(row['price']), axis = 1)


    pattern=r'(\,|\.|Mrs.|Miss|Dr.|Mr.|Ms.|DDS|PhD|DVM|MD)'
    #Split name into first last name and title
    df['clean_name'] = df['name'].replace(pattern,'',regex=True)
    df[['first_name', 'last_name', 'titles']] = df.clean_name.str.split(expand=True,)
    df['first_name'] = np.where(df['titles'].isnull(), df['first_name'], df['first_name'].astype(str) + ' ' + df['titles'] )

    #Create a new filed call above_100
    df['above_100'] = df.price.astype(float) > 100
    
    #Drop column not in used, and rearrange column
    df = df.drop('titles', 1)
    df = df.drop('clean_name', 1)
    df = df.drop('name', 1)
    df = df[['first_name', 'last_name', 'price', 'above_100']] 

    #Prepare for data output
    file_name = 'processed_data_' + processdate + '.csv'
    location_file_name = os.path.join(output_dir, file_name)

    df.to_csv(location_file_name, index=False)
    print('Data outputted at', location_file_name)


    #Zip & Backup data from landing dir to backup dir
    filename = shutil.make_archive('backup_' + processdate , 'zip', landing_dir)
    dir_info = shutil.move(filename, backup_dir)
    print('Data have been backup at:', dir_info)
    #delete files
    for files in filepaths:
        os.remove(files)
    print('Files removed from landing_dir')
    print('End of script')

else: 
    print("Landing directory is empty")
    outputpath = [f for f in os.listdir(output_dir) if f.endswith(processdate + '.csv')]
    if len(outputpath) > 0:
        print('Job has ran earlier, an output file has been exist')
    else:
        print('File have not been sent from source system.')