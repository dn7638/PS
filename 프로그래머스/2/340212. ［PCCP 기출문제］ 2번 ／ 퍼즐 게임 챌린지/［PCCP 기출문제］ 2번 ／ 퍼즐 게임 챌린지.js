function a(diffs, times, limit, level, limit){
    var time = 0
    
    
    for (let i = 0; i < diffs.length; i++){
        var time_cur = times[i]
        
        if (i == 0){
            time += times[0]
        }
        else{
            var time_prev = times[i-1]
            
            if (diffs[i] <= level){
                time += time_cur
            }
            else if(diffs[i] > level){
                time += (time_cur+time_prev) * (diffs[i] - level) + time_cur
                
            }
            
        }
    }
    // console.log(`time : ${time}, level : ${level}, limit : ${limit}`);
    if (time <= limit){
        return true
    }
    else{
        return false
    }
}

function solution(diffs, times, limit) {
    
    // 실패하면 위, 성공하면 아래
    // 레벨이 100,000보다 큰 답은 없다
    
    var left = 1
    var right = 100000
    var mid = Math.floor((left+right)/2)
    
    while (left < right){
        if(a(diffs, times, limit, mid, limit)){
            right = mid
        }
        else{
            left = mid + 1
        }
        mid = Math.floor((left+right)/2)
        // console.log(`left : ${left}, mid : ${mid}, right : ${right}`);

    }
    return mid
        
}
        
        


