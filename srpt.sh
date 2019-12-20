#!/bin/bash
# Chris Heiner
# Lab 2 - Search and Report
# CS 3030 - Scripting Languages

mkdir /tmp/$USER/ #creates my uniqueID temp folder

#If path is empty, print Usage statement and exit with status code 1

if [ -z "$1" ]; then

    echo Usage: srpt PATH

    exit 1

#Otherwise, continue through the script
else

    #Finds requested files/subdirectories and saves each to my unique tmp folder for count/manipulation
    
    find $1 -mindepth 1 \( -type f -fprintf /tmp/$USER/files.txt "%s\n" \) , \( -type d -fprintf /tmp/$USER/subdir.txt "\n" \) , \( -type l -fprintf /tmp/$USER/links.txt "\n" \) , \( -type f -mtime +365 -fprintf /tmp/$USER/old.txt "\n" \) , \( -type f -size +500000c -fprintf /tmp/$USER/large.txt "\n" \) , \( -type f \( -name "*.jpg" -o -name "*.gif" -o -name "*.bmp" \) -fprintf /tmp/$USER/pics.txt "\n" \) , \( -type f -name "*.o" -fprintf /tmp/$USER/temp.txt "\n" \) , \( -type f -executable -fprintf /tmp/$USER/exe.txt "\n" \)  
    
    #Variable creation and assignment of counts
    files=$(wc -l /tmp/$USER/files.txt | cut -d" " -f1)
    dir=$(wc -l /tmp/$USER/subdir.txt | cut -d" " -f1)
    symlink=$(wc -l /tmp/$USER/links.txt | cut -d" " -f1)
    oldfile=$(wc -l /tmp/$USER/old.txt | cut -d" " -f1)
    bigfile=$(wc -l /tmp/$USER/large.txt | cut -d" " -f1)
    graphics=$(wc -l /tmp/$USER/pics.txt | cut -d" " -f1)
    tempfile=$(wc -l /tmp/$USER/temp.txt | cut -d" " -f1)
    exefile=$(wc -l /tmp/$USER/exe.txt | cut -d" " -f1)
    totalsize=$(awk '{ sum+=$1} END {print sum}' /tmp/$USER/files.txt) 

    #Beginning of report with formatting, execution time, and counted directories, files, and size
    echo -e "SearchReport $HOSTNAME $1 $(date)\n"
    echo Execution time $SECONDS
    printf "Directories %'d\n" $dir
    printf "Files %'d\n" $files
    printf "Sym links %'d\n" $symlink
    printf "Old files %'d\n" $oldfile
    printf "Large files %'d\n" $bigfile
    printf "Graphics files %'d\n" $graphics
    printf "Temporary files %'d\n" $tempfile
    printf "Executable files %'d\n" $exefile
    printf "TotalFileSize %'d\n" $totalsize

fi

rm -r /tmp/$USER  #deletes my tmp folder and every file in it like a good computer citizen =)

exit 0
