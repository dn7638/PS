def solution(phone_book):
    
    phone = set()
    for num in phone_book:
        for i in range(1, len(num)):
            phone.add(num[0:i])
            
    for num in phone_book:
        if num in phone:
            return False
        
    
    answer = True
    return answer