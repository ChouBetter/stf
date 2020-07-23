for i in $(seq 24720 24729)
do
appium -p $i > /dev/null 2>&1 &
done
