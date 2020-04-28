initial_base="d826e674004f"
head=$(flask db current)


if [ "$head" ==  "$initial_base" ] || [ "$head" == "" ]
then
    flask db stamp "$initial_base"
fi

flask db upgrade
