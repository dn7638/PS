function solution(my_string, is_suffix) {
    var set = new Set();  // 집합 생성
    const len = my_string.length;  // 문자열 길이

    for (let i = 0; i < len; i++) {  // 반복문 세미콜론 수정
        set.add(my_string.slice(i, len));  // 부분 문자열 집합에 추가
    }

    if (set.has(is_suffix)) {  // 집합에 존재 여부 확인
        return 1;
    }
    return 0;
}
