for i in $(seq 34720 34729)
do
appium -p $i > /dev/null 2>&1 &
done
