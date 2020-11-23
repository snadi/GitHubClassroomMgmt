for dir in */; do
    if [[ -d $dir ]]; then
        cd $dir
        git pull
        cd ..
    fi
done