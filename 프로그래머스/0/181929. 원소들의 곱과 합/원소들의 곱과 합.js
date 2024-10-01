function solution(num_list) {
    var 곱 = 1
    var 합의제곱 = 0
    
    for (let i = 0; i < num_list.length; i++){
        곱 *= num_list[i]
    }
    
    for (let i = 0; i < num_list.length; i++){
        합의제곱 += num_list[i]
    }
    
    합의제곱 = 합의제곱 ** 2
    
    if (곱 < 합의제곱){
        return 1
    }
    else{
        return 0
    }
}

