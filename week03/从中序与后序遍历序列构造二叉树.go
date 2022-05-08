/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 
 func buildTree(inorder []int, postorder []int) *TreeNode {
    if len(inorder) == 0{
        return nil
    }
    inmap := map[int]int{}
    for k, v := range inorder{
        inmap[v] = k
    }
    var result func(int, int) *TreeNode
    result = func(inleft, inright int) *TreeNode{
        if inleft > inright{
            return nil
        }
        root := &TreeNode{
            Val: (postorder[len(postorder) - 1]),
        }
        postorder = postorder[:len(postorder) - 1]
        inRootIndex := inmap[root.Val]
        root.Right = result(inRootIndex + 1, inright)
        root.Left = result(inleft, inRootIndex - 1)
        return root
    }
    return result(0, len(inorder) - 1)
}