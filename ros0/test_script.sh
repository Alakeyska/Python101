User='Alakey'
echo "Hello! My name is $User!"

math_score="5 5 5 5"
english_score="5 5 5 5"
russian_score="3 2 2 2"

for subject in 'math' 'english' 'russian' 'biology'
do
    mkdir $subject
    cd $subject
    touch $subject.txt
    cd ..
    echo "Here is $subject"
done 

touch master.txt
echo "Hello! My name is $User!" >> master.txt
date >> master.txt

