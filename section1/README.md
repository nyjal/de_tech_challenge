# Section 1: Data Pipelines

Pipeline consist of 3 steps:
0. Files get transferred or generated in landing folder (landing_dir)
1. Check for data file do exist in landing_dir, script will then process it and export into output_dir
2. Backup the original data files that was sent to us(zip, append date, and move to a backup_folder)
3. Delete the original data files in the landing folder (To mark as job completed, and to anticipate next file)

All of the above is run by a single python script, section1.py

To create cron schedule to run the script daily, set at 1:15AM daily.

### Open crontab editor
crontabs -e

### Set with the below values, job to be run at 1:15AM everyday, having 15minute buffer
#### to include path of python location and full path to where the application is resided in.
15 1 * * * usr/local/bin/python3 full/path/to/application/section1/section1.py