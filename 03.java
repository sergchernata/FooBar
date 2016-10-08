package com.google.challenges;

public class Answer {
    public static int answer(int start, int length) {

        // Your code goes here.
        count = start
        checksum = -1
        x_axis = range(length + 1)

        for y in y_axis:
            line = y + 1
            for x in x_axis:
                if line > 0:
                    if checksum > -1:
                        checksum ^= count
                    else:
                        checksum = start
                    line -= 1
                    count += 1
                else:
                    count += length - x
                    break

        return checksum
    }
}