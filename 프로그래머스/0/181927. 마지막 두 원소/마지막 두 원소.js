function solution(num_list) {
    var idx = num_list.length
    if (num_list[idx-1] > num_list[idx-2]){
        num_list.push(num_list[idx-1] - num_list[idx-2])
        return num_list
    }
    else{
        num_list.push(2 * num_list[idx-1])
        return num_list
    }
}