#!/usr/bin/perl
#Chris Heiner
#Lab 7 Perl Filter
#CS 3030 - Scripting
use strict;
use warnings;

#Checking for correct number of arguments and exiting with rc 1 if wrong
if (@ARGV !=2)
{
	print STDERR "Usage: ./filter.pl 'FROMSTRING' 'TOSTRING'";
	exit(1);
}

#Substitute all instances of From and To and print all lines
while(<STDIN>)
{
	s/$ARGV[0]/eval qq("$ARGV[1]")/ge;
	print "$_";
}
exit(0);
