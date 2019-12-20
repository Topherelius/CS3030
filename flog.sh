#!/bin/bash
# Chris Heiner
# Lab 3 - Failed Login Report
# CS 3030 - Scripting Languages

# If the file (argument) is not passed in, print the statement and exit with return code 1

if [ -z $1 ]; then
  
    echo "Usage: flog LOGFILE"
    exit 1
fi

#Search for "Failed password for " in passed in file/directory and save output into file s1out
grep 'Failed password for ' $1 > s1out

#Substring extraction of zero or more chars of the group(parens) and output only the matches of () 
sed -n 's/.*Failed password for \([a-z0-9A-Z_]*\) .*/\1/p' s1out > s2out

#sort user names
sort <s2out >s3out

#combine and count input (will only work if data is in alphabetical ascending sequence)
uniq -c <s3out >s4out

#Sort input's 1st field in (n)numeric (r)descending order and the 2nd field ascending order
sort -k1,1nr -k2,2 s4out >s5out

#Change invalid user name to <UNKNOWN>
sed 's/invalid/\&lt;UNKNOWN\&gt;/' <s5out >s6out

#Print opening html tags and header
echo "<html>"
echo "<body><h1>Failed Login Attempts Report as of $(date)</h1>"

#Print break html, counts (with commas), and userids as a string on a new line with a while loop
cat s6out| while read mycount myuserid; do
	printf "<br /> %'d %s\n" "$mycount" "$myuserid"
done

#Print closing html tags
printf "</body> </html>"

exit 0
