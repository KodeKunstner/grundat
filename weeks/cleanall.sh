for x in week*
do
    cd $x
    ../../clean.sh
    cd ..
done
rm -rf upload
