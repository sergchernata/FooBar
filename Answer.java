//package com.google.challenges;

public class Answer {
    public static int answer(int start, int length) {

        int count = start;
        int checksum = -1;

        for(int y=length; y>1; y--){
            int line = y + 1;

            for(int x = 0; x<length+1; x++){
                if(line > 0){
                    if(checksum > -1){
                        checksum ^= count;
                    }else{
                        checksum = start;
                    }

                    line--;
                    count++;
                }else{
                    count += length - x;
                    break;
                }
            }
        }

        return checksum;
    }
}