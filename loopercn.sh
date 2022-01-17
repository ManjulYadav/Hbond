#!/bin/bash

f_pre="box_01_step_"	#FILENAME PREFIX
f_suf=".pdb"		#FILENAME SUFFIX 

strt=199000		#START
stp=200000		#STOP
incr=20			#INCREMENT

out="cn_box_01.txt"

rm -rf $out		#Delete previous ouput

tot=0
num=0

for f in $(seq -f "%014g" $strt $incr $stp)
do
	fn="$f_pre$f$f_suf"
	cn=$(./cn.py $fn)
	one= $1
	num="$num + $one"
	echo "num = 'bc <<< $num'" 
	tot= "$tot + $cn"
	echo "tot = 'bc <<< $tot'" 
	printf "%f-10d%f\n" $num $cn >> $out
done
avg= "$tot/$num"
echo "avg = 'bc <<< $avg'" 

printf "TOT   : %.3f\n" $tot >> $out
printf "NUM   : %.3f\n" $num >> $out
printf "AVG   : %.3f\n" $avg >> $out
