#!/usr/bin/perl
# Chris Heiner
# Lab 8 - Sockets
# CS 3030 - Scripting Languages
use strict;
use warnings;
use IO::Socket;

#Check for correct number of args and exit with rc 1 if wrong
if(@ARGV !=2)
{
	print STDERR "Usage: ./socket.pl HOSTNAME SOCKETNUMBER\n";
	exit(1);
}

#Create connection utilizing given port number using tcp or quit and print error if unable to
my $remote = IO::Socket::INET->new(
	Proto => "tcp",
	PeerAddr => "$ARGV[0]",
	PeerPort => "socket($ARGV[1])", )
	or die print STDERR "Error: Unable to connect to port ($ARGV[1]) at ($ARGV[0]).";

#Read and print first line sent back from server/host
my $line = <$remote>;
print $line;
exit(0);
