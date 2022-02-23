#!/usr/bin/perl
use warnings;
use strict;

my $filename =  $ARGV[0];
#my $filename = 'c:\temp\test.txt';

open(FH, '<', $filename) or die $!;

while(<FH>){
}

close(FH);
