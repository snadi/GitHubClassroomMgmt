for dir in */; do
    cd $dir
    for subdir in */; do
        if [[ -d $subdir ]]; then
            cd $subdir
            git pull
            cd ..
        fi
    done
    cd ..
done