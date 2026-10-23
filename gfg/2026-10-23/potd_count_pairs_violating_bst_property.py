class Solution:
    def pairsViolatingBST(self, root):
        # inorder traversal, then count pairs i<j with a[i] > a[j]
        a = []
        st = []
        cur = root
        while cur or st:
            while cur:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            a.append(cur.data)
            cur = cur.right
        vals = sorted(set(a))
        rank = {v: i + 1 for i, v in enumerate(vals)}
        n = len(vals)
        bit = [0] * (n + 2)
        res = 0
        seen = 0
        for x in a:
            r = rank[x]
            i = r
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            res += seen - s
            i = r
            while i <= n:
                bit[i] += 1
                i += i & -i
            seen += 1
        return res
