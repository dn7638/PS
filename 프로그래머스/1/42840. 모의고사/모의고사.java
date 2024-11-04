import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int a_cnt = 0;
        int b_cnt = 0;
        int c_cnt = 0;
        for (int i = 0; i < answers.length ; i++){
            // System.out.println(i);
            if (answers[i] == a[i % a.length]){
                a_cnt += 1;
            }
            if (answers[i] == b[i % b.length]){
                b_cnt += 1;
            }
            if (answers[i] == c[i % c.length]){
                c_cnt += 1;
            }
            
        }
        
        int[] cnts = {a_cnt, b_cnt, c_cnt};
        int max_cnt = 0;
        for(int i = 0; i < 3; i++){
            if (max_cnt < cnts[i]){
                max_cnt = cnts[i];
            }
        }
        System.out.println(max_cnt);
        int[] answer_cnts = {0,0,0};
        int answer_cnt = 0;
        for(int i = 0; i < 3; i++){
            if (max_cnt == cnts[i]){
                
                answer_cnts[i] = 1;
                System.out.println(answer_cnts[i]);
                answer_cnt += 1;
                    
            }
        }
        int[] answer1 = {0};
        int[] answer2 = {0,0};
        int[] answer3 = {0,0,0};
        
        int idx = 0;
        for(int i = 0; i < 3; i++){
            
            if (answer_cnt == 1){
                if (answer_cnts[i] == 1){
                    answer1[idx]= i+1;
                    idx++;
                }    
            }
            else if (answer_cnt == 2){
                if (answer_cnts[i] == 1){
                    answer2[idx]= i+1;
                    idx++;
                }   
            }
            else if (answer_cnt == 3){
                if (answer_cnts[i] == 1){
                    answer3[idx]= i+1;
                    idx++;
                }   
            }
            
        }
        
        if (answer_cnt == 1){
            return answer1;
        }
        else if (answer_cnt == 2){
            return answer2;
        }
        else if (answer_cnt == 3){
            return answer3;
        }
            
    int[] answer = {};
    return answer;
    }
}