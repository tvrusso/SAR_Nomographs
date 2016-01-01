# SAR_Nomographs

This is a collection of hacks I created using [PyNomo](http://www.pynomo.org/).

The purpose is to provide a simple, usable set of nomographs that
search planners and debriefers can use to estimate POD or the effort
required to achieve a given POD, without having to pull out a computer
and spreadsheet program to do so.

You must first install PyNomo and all of its dependencies according to
the directions on its web site.  Once PyNomo is installed properly,
you can just run these scripts to produce the nomographs.  The scripts
produce PDFs of the nomographs for viewing in any PDF viewer or
incorporation into other documents.

The two nomographs that are intended to be used are
POD_from_W_v_t_simplified.py and POD_from_W_L_N.py.  The others are
all just toys I created while learning PyNomo and building these two.

POD_from_W_v_t_simplified.py is intended for planning purposes, and
instructions for using it are in "PlanningNomograph_Instructions.odt",
a LibreOffice document.  It can be used to estimate the searcher
effort (in "searcher-hours") required to achieve a given POD, knowing
either the effective sweep width or the measured average range of
detection, the searcher speed and region area and desired POD.
Alternatively, it can be used to determine the attainable POD using a
given level of effort (in searcher-hours).

Conversion between range of detection and sweep width makes use of the
approximate relations described in [Use of the Visual Range of
Detection to Estimate Effective Sweep Widths for Land Search and
Rescue Based on 10 Detection Experiments in North
America](http://www.wemjournal.org/article/S1080-6032%2813%2900266-4/abstract).

The second nomograph, POD_from_W_L_N.py, is for debriefing purposes.
It allows the debriefer to compute the POD of a completed search using
the measured average range of detection (or alternatively the
tabulated effective sweep width), the total track length of one
searcher in the team (as measured by GPS), the number of searchers on
the team, and the area searched.  Instructions for using it are in
"DebriefNomograph_Instructions.odt" (also a LibreOffice document).
 


PDF versions of both instruction sheets are also present in the
repository, for those who cannot read LibreOffice documents.