func findOrder(numCourses int, prerequisites [][]int) []int {
    var (
        edg = make([][]int, numCourses)
        dis = make([]int, numCourses)
        result []int
    )
    for _, key := range prerequisites {
        edg[key[1]] = append(edg[key[1]], key[0])
        dis[key[0]]++
    }
    x := []int{}
    for i := 0; i < numCourses; i++{
        if dis[i] == 0{
            x = append(x, i)
        }
    }
    for len(x) > 0{
        m := x[0]
        x = x[1:]
        result = append(result, m)
        for _, v := range edg[m]{
            dis[v]--
            if dis[v] == 0{
                x = append(x,v)
            }
        }
    }
    if len(result) != numCourses{return []int{}}
    return result
}