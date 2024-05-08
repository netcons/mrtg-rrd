#!/usr/bin/perl

do 'mrtg-rrd-lib.pl';

&ui_print_header($text{'title_desc'} , $text{'title'}, "", undef, 0, 1, 1,
        "<script type='text/javascript' src='mrtg-rrd.js'></script>");

print "<div>";
print "<iframe src='mrtg-rrd.cgi' marginheight='0' marginwidth='0' scrolling='no' noresize frameborder='0' id='iframe0' onLoad='resizeIframe(iframe0);'></iframe>";
print "<div>";

&ui_print_footer("/", $text{'index'});
