func shipWithinDays(weights []int, days int) int {
    left, right := 0, 0
    for _, v := range weights{
        left = GetMax(left, v)
        right = right + v
    }
    for left < right {
        mid := (right + left) / 2
        if MidCheck(weights, days, mid){
            right = mid
        }else{
            left = mid + 1
        }
    }
    return left
}

func GetMax (m, n int) int{
    if m > n{
        return m
    }else{
        return n
    }
}

func MidCheck(weights []int, days int, mid int) bool{
    x, num := 0, 1
    for _, v := range weights {
        if x + v > mid {
            x = 0
            num ++
        }
        x = x + v
    }
    return num <= days
}