function solution(my_string, index_list) {
    var answer = '';
    var len = index_list.length
    for (let i = 0; i < len; i++){
        answer += my_string[index_list[i]]
    }
    
    return answer;
}