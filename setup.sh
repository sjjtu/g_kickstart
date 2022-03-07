read -p "Year: " year
read -p "Round: " round
read -p "Name of directory: " dirname
mkdir $year/$round/$dirname
cp template.py $year/$round/$dirname/
mv $year/$round/$dirname/template.py $year/$round/$dirname/main.py
touch $year/$round/$dirname/testfile.txt

