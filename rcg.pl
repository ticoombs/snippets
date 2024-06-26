#!/usr/bin/perl -w
#
#       regexp coloured glasses - from Linux Server Hacks from O'Reilly
#
#       eg ./rcg "fatal" "BOLD . YELLOW . ON_WHITE"  /var/adm/messages
#
use strict;
use Term::ANSIColor qw(:constants);
 
my %target = ( );
 
while (my $arg = shift) {
        my $clr = shift;
 
        if (($arg =~ /^-/) | !$clr) {
                print "Usage: rcg [regex] [color] [regex] [color] ...\n";
                exit(2);
        }
 
        #
        # Ugly, lazy, pathetic hack here. [Unquote]
        #
        $target{$arg} = eval($clr);
 
}
 
my $rst = RESET;
 
while(<>) {
        foreach my $x (keys(%target)) {
                s/($x)/$target{$x}$1$rst/g;
        }
        print
}
