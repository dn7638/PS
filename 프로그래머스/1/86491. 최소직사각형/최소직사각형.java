import java.util.*;

class Solution {
    public int solution(int[][] sizes) {
        
        int max_val = 0;
        int pair_val = 0;
        
        for (int[] size : sizes){
            int a = size[0];
            int b = size[1];
            int temp = 0;
            if (a<b){
                temp = a;
                a = b;
                b = temp;
            }
            if (max_val < a){
                max_val = a;
                pair_val = b;
            }
        }
            
        for (int[] size : sizes){
            int a = size[0];
            int b = size[1];
            int temp = 0;
            if (a<b){
                temp = a;
                a = b;
                b = temp;
            }
            
            if (pair_val < b){
                pair_val = b;
            }   
        }
        
        
        int answer = 0;
        answer = pair_val * max_val;
        return answer;
    }
}