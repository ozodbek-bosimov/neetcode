func lengthOfLastWord(s string) int {
    i := len(s) - 1
    for i >= 0 && s[i] == ' ' {
        i--
    }

    end_i := i
    for i >= 0 && s[i] != ' ' {
        i--
    }
    return end_i - i 

}