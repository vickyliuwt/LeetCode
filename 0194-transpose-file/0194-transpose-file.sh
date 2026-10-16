# Read from the file file.txt and print its transposed content to stdout.
arr=()

while read l; do
    i=0
    for w in $l; do
        if [ "${arr[i]}" ]; then
            arr[$i]+=' '
        fi
        arr[$i]+=$w
        i=$((i + 1))
    done
done < file.txt

for r in "${arr[@]}"; do
    echo "$r";
done